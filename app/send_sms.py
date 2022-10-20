'''
Send sms service
v0.01
2022.01.23
'''

import time
import random

def SendSMS(aMessage: str, aPhoneNumber : str, aCountSMS: int):
    for i in range(aCountSMS):
        # N/Count, Sleep, Message, PhoneNumber
        # 1/3, 3, Hello, +38xxx
        # 2/3, 6, Hello, +38xxx
        # 3/3, 2, Hello, +38xxx
        #print(aMessage, aPhoneNumber)
        Rnd = random.randint(3, 10)
        print('%s/%s, %s, %s, %s' % (i + 1, aCountSMS, Rnd , aMessage , aPhoneNumber))
        
        #time.sleep(2)
        time.sleep(random.randint(3, 10))

def Input() -> list:
    PhoneNumber = '+380686418151'
    CountSMS = 5
    Message = 'Hello'

    #PhoneNumber = input('Phone number: ')
    #CountSMS = int(input('SMS count: '))
    #Message = input('SMS text: ')

    #Send message "XXX" to phone "XXX" X times ?
    #print('Send message "' + Message + '" to phone "' + PhoneNumber + '" ' + str(CountSMS) + ' times ?')
    YN = input('Send message "%s" to phone "%s" %s times y/n ?' % (Message, PhoneNumber, CountSMS))
    if (YN == 'y') or (YN == 'Y'):
        print('okey')
        return [Message, PhoneNumber, CountSMS]
    else:
        print ('sorry')
        return []

#Message1, PhoneNumber1, CountSMS1 = Input()
Res = Input()
if (Res):
    Message1, PhoneNumber1, CountSMS1 = Res
    SendSMS(Message1, PhoneNumber1, CountSMS1)
