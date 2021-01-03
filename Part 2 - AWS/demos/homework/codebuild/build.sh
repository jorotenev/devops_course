mkdir -p /tmp/output
# for an actual python applicaiton we would install any dependancies from the requirements.txt here
# pip install -r requirements.txt -t . # installs the packages in the current directory

aws cloudformation package \
--template-file template.yml \
--s3-bucket=homework-progressbg-cf-packaged \
--s3-prefix=${APP} \
--output-template-file=packaged_template.yml


