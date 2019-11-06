# Python
## Python 2 vs  python 3
* If you can, use Python 3. Support for Python 2 will stop in a couple of months, 
* Python 3.0 is 11 years old.
* Considerations
    * Not the fastest language around. Think how much you care about this. Python is fast to write. 
    * [Duck typing](https://en.wikipedia.org/wiki/Duck_typing). If you don’t have a background in programming, the way Python handles typing can actually be easier to understand.
* [standard library](https://docs.python.org/3/library/functions.html)
[variables, functions, if-else, for-loop, exceptions](https://gist.github.com/jorotenev/d0463edd1dd0f21c967bb0cc9830baa4#file-python_basics_1-py)
* [split strings, dictionaries](https://gist.github.com/jorotenev/d0463edd1dd0f21c967bb0cc9830baa4#file-dictionaries_and_more-py)
* [parsing command line arguments](https://gist.github.com/jorotenev/d0463edd1dd0f21c967bb0cc9830baa4#file-parse_args-py)
* [reading env vars](https://gist.github.com/jorotenev/d0463edd1dd0f21c967bb0cc9830baa4#file-env_vars-py)
* [file IO & requests library](https://gist.github.com/jorotenev/d0463edd1dd0f21c967bb0cc9830baa4#file-file_io-py)
* pip
    * a tool to manage 3rd party packages  that we use in our code
    * how to install it
        * download the get-pip.py file and then run it with via python
    * install & freeze commands
        * `pip install boto3` to install the newest version of the boto3 package
        * `pip install boto3==1.9.219` - install a specific version
        * `pip freeze` - show the installed packages in the current environment
    * convention - put your code’s required packages in the the [requirements.txt file](https://pip.readthedocs.io/en/1.1/requirements.html#the-requirements-file-format)
* PyCharm - nice IDE for writing Python. 

* good to know (read in your own time)
    * modules and packages
    * error handling with exceptions in python
    * virtualenv and pipenv
