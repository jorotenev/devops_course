from flask import render_template, current_app, request, redirect, flash
from . import pages
from boto3 import client

sns = client('sns')


def send_sms(phone, msg):

    sns.publish(
        # 'TopicArn='arn:aws:sns:us-east-1:750385577863:test',
        PhoneNumber=phone,
        Message=msg
    )


@pages.route('/', methods=['GET', 'POST'])
def index_stores():
    if request.method == 'POST':
        print(request.data)
        phone, msg = request.form.get('phonenumber'), request.form.get('msg')
        print(phone, msg)
        flash(f'Successfully sent a text message to <strong>{phone}</strong>')
        send_sms(phone, msg)
        return redirect('/')

    return render_template('index.html.jinja')
