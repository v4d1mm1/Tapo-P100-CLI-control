#!/usr/bin/env python3

#You can make this file executable and add variable $PATH typing in CLI commands "chmod +х p100.py" and "PATH=$PATH:. or edit /etc/environment"

from PyP100 import PyP100
import sys
import time

def get_device_state():
    response=p100.getDeviceInfo()
    result=response['result']
    device_state=result['device_on']   
    return(device_state)    

def get_timeout():
    if ':' in sys.argv[2]:
        hhmm = sys.argv[2].split(':')
        if not len(hhmm)>2:
            try:
                timeout = (int(hhmm[0])*60 + int(hhmm[1]))
            except:
                sys.stderr.write('Please enter correct action (state/on/off) and optional timeout in MM or HH:MM format\n')
                sys.exit(1)
        else:
             sys.stderr.write('Please enter correct action (state/on/off) and optional timeout in MM or HH:MM format\n')
             sys.exit(1)
    elif sys.argv[2].isdecimal():
        timeout = sys.argv[2]
    return(timeout)
    
num_arguments = len(sys.argv)-1

if num_arguments > 2:
   sys.stderr.write('Please enter correct action (state/on/off) and optional timeout in MM or HH:MM format\n')
   sys.exit(1)
elif num_arguments == 2:
    timeout = get_timeout()
    if sys.argv[1] == 'off':
        action = sys.argv[1]     
    elif sys.argv[1] == 'on':
        action = sys.argv[1]
    elif sys.argv[1] == 'state':    
        action = sys.argv[1]  
    else:
        sys.stderr.write('Please enter correct action (state/on/off) and optional timeout in MM or HH:MM format\n')
        sys.exit(1)
elif num_arguments == 1:
    timeout = 0
    if sys.argv[1] == 'off':
        action = sys.argv[1]     
    elif sys.argv[1] == 'on':
        action = sys.argv[1]
    elif sys.argv[1] == 'state':    
        action = sys.argv[1]  
    else:
        sys.stderr.write('Please enter correct action (state/on/off) and optional timeout in MM or HH:MM format\n')
        sys.exit(1)
else:
    print ('No arguments (state/on/off and optional timeout). Switching device state to opposite\n')
    action = 'to opposite state'
    timeout = 0

if action != 'state':
    print ('Will switch %s after %s minutes' % (action, timeout))
    time.sleep(int(timeout)*60)
else:
    pass

p100 = PyP100.P100("Your_Tapo_P100_IP", "Your_Tapo_account_email", "Your_Tapo_account_password")
p100.handshake()
p100.login()

if action == 'off':
    p100.turnOff()
    if get_device_state() == 0:
        print('Device switched off')
    else:
        print('Please check device state again using argument "state"')    
    
elif action =='on':
    p100.turnOn()
    if get_device_state() == 1:
        print('Device switched on')
    else:
        print('Please check device state again using argument "state"')
        
elif action == 'to opposite state':
    if get_device_state() == 1:
       p100.turnOff()
       if get_device_state() == 0:
           print('Device switched off')
       else:
           print('Please check device state again using argument "state"')
    else: 
       p100.turnOn()
       if get_device_state() == 1:
           print('Device switched on')
       else:
           print('Please check device state again using argument "state"')
elif action == 'state':
    if get_device_state()==1:
        print ('Device is on')
    elif get_device_state()==0: 
        print ('Device is off')
