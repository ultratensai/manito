#!/home/flatwhite/botato/bin/python
from twilio.rest import Client
import configparser

config = configparser.ConfigParser()
config.read('/etc/auth.conf')

account_sid = config['manito_token']['sid']
auth_token = config['manito_token']['token']

client = Client(account_sid, auth_token)


def send_msg(number, sms_text):
    message = client.messages.create(body=sms_text, from_='manito', to=number)
    print(message.sid)

target = ['+61403646240']

for t in target:
    send_msg(t, 'Have a wonderful day ❤️!')
