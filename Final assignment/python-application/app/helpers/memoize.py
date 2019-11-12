import hashlib
from datetime import datetime, timedelta
from functools import wraps
from flask import current_app

import logging


class _Memoizer(object):
    """
    In memory cache.
    The memoize() method can be used as a decorator to a function to memoize the decorated function.
    The decorated function must be called with kwargs only
    TODO - work with *args too
    """

    def __init__(self, expires: timedelta = timedelta(hours=1)):
        self._cache_storage = {}  # {"hashed_request":{"inserted_at":, "content":} }
        self.expires_at = expires

    def init_app(self, app):
        config_expires_hours = app.config.get("MEMOIZE_EXPIRE_AFTER_HOURS")
        if config_expires_hours:
            self.expires_at = timedelta(hours=config_expires_hours)

    @staticmethod
    def _get_request_hash(**kwargs):
        sorted_kwargs = sorted([(k, v) for k, v in kwargs.items()])
        return hashlib.md5(str(sorted_kwargs).encode('utf-8')).hexdigest()

    def is_in_cache(self, **kwargs):
        """
        first will invalidate stale entries, then will check if we have a valid entry for the given kwargs
        :param kwargs:
        :return:
        """
        request_hash = self._get_request_hash(**kwargs)
        self._clean_stale()
        return request_hash in self._cache_storage

    def _clean_stale(self):
        now = datetime.utcnow()
        to_invalidate = []
        for hash, item in self._cache_storage.items():
            if (now - item['inserted_at']) > self.expires_at:
                to_invalidate.append(hash)
        _ = [self._cache_storage.pop(hash) for hash in to_invalidate]

    def get_from_cache(self, **kwargs):
        return self._cache_storage[self._get_request_hash(**kwargs)]['content']

    def set_cache(self, content, **kwargs):
        now = datetime.utcnow()
        self._cache_storage[self._get_request_hash(**kwargs)] = {'inserted_at': now, 'content': content}

    def memoize_decorator(self, func):
        @wraps(func)
        def inner(**kwargs):
            inner_kwargs = {**kwargs, '__func_name': func.__name__}
            if self.is_in_cache(**inner_kwargs):
                logging.debug(f'cache hit for {str(inner_kwargs)[:100]}')
                return self.get_from_cache(**inner_kwargs)
            else:
                logging.debug(f'cache miss for {str(inner_kwargs)[:100]}')

                response = func(**kwargs)
                self.set_cache(content=response, **inner_kwargs)
                return response

        return inner


memoizer = _Memoizer()


def memoized():
    return memoizer.memoize_decorator
