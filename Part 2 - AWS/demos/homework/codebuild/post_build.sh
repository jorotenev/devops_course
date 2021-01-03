# https://docs.aws.amazon.com/cli/latest/reference/cloudformation/deploy/index.html
aws cloudformation deploy \
--stack-name=${APP} \
--template-file=packaged_template.yml \
--parameter-overrides AppName=${APP} \
--tags app=${APP}


