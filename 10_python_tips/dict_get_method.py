''' This document demonstrates the use of get() method in dictionary 
and the option to set a default value '''

name_for_userid = {
    550:'Alice',
    660:'Bob',
    980:'Jack',
    }

def greeting(userid):
    ''' Takes in a userid and greets the corresponding person '''
    return "Hello %s!" %name_for_userid.get(userid,'there')

print(greeting(660)) #a user id in the the dictionary

print(greeting(1111111111)) # user id not in the dictionary