'''
    This program helps to send sms notification to specified mobile.

    usage :
    1. Using Program to send sms
        python sendSms.py [<Message needs to be sent>]
    2. Using module in other script to nofiy via sms
       from sendSms import send_sms
       send_sms(<msg>,[<To Number>])
'''
import sys
import json
import logging
import platform
from twilio.rest import Client

logging.basicConfig(level=logging.ERROR, format=" [%(asctime)s][%(levelname)s] %(message)s")

try:
    CONFIG = json.loads(open('config.json').read())
    logging.debug(CONFIG)
except IOError:
    logging.critical("Configuration file not found! \
    Please make sure config.json file is in same directory")
    exit(1)

client = Client(CONFIG['account'], CONFIG['token'])

def send_sms(msg_body, to_num = CONFIG['to_default']):
    '''
    This function is used to send message with give mobile number and message
    '''
    try:
        logging.debug("To : {}, From : {}, Message is : {}".format(to_num, CONFIG['from'], msg))
        client.messages.create(to=to_num, from_=CONFIG['from'], body=msg_body)
    except:
        logging.error("Opps !! Check you Internet connection after that credentials ....")
    else:
        logging.info("Message has been sent sucessfully")

def usage():
    ''' This is the help function to print usage'''
    print '''
    This program helps to send sms notification to specified mobile.

    usage :
    1. Using Program to send sms
        python sendSms.py [<Message needs to be sent>]
    2. Using module in other script to nofiy via sms
       from sendSms import send_sms
       send_sms(<msg>,[<To Number>])
    '''

if __name__ == '__main__':
    logging.debug("Inside main function")
    msg = "Default msg : " + str(platform.uname())
    if len(sys.argv) > 1:
        msg = ' '.join(sys.argv[1:])
    else:
        usage()
    send_sms(msg)
