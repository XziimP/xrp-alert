import json
import os
import time
import requests
from playsound import playsound



print("""






                
                
                
                
                
                @@@@@@@@@@@@@@@o@ooooooooo@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*@OOOOO@*@@@
@@@@@@@@@@@@@@o@oooooooooooo#°@@@@@@@@@@@@@@@@OOOOO@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@O@OoOoO@o@@@@@@@@@@@@@@@@@@@
@@@#o****o#@@o@o**oooooooo*o#o@@@@@@@@@O*@@@@@OOOOO@o@@@@oo@@@@@oO@@@@@@@@oO@@@@@oO@@O@OOOOO@o@@oO@@@@@@Oo@@@@@@@
@#o@@@@@@@@*@*@********oooooo@@@@@@@@@@@@Ooo@@@OO@@@@@@@@@@@ooo@@@@o@@@@@@@@@OoO@@@@oO@OOOOO@oo@@@@@OO*@@@*@@@@@@
#@@oooooo*o@@**************o@o@@o@OOOOOOOOOOO@OOOOO@OOOOOOOOOOOOOOO@o@OOOOOOOOOOOOOO@O@OOOOO@o@OOOOOOOOOOO@@@@@@@
@oooooo******@@@**********o@°@@@O@OoOOOoOOOOO@OoOoO@OOOOOOoOOOOoOOOO@@OOOOOoOOOOoOOOO@@OOOOO@@OOOOOOOOOOOOOo@@@@@
oooooooooo***************@@o@@@@O@OOOOOOOOOOO@OOOOO@OOOOOOOOOOOOOOOOO@OOOOOOOoOOOOOOOO@OOOOO@OOOOOOOOOOOOOOO@o@@@
ooooooooooo*********@@@@@o*@@@@@O@OOOOO@@@@@@@OOOOO@OOOOOO@@@@@@OOOOO@OOOOO@@@@@@OOOOO@OOOOO@OOOOOOOOOOOOOoO@@@@@
ooooooooooo**************@@°@@@@O@OOOOO@o@@*@@OOOOO@OOOOOO@@@@@OOOOOO@OOOOOo@@@@OOOOoO@OOOOO@OoOOOOOOOOOOOOO*@@@@
@ooooooo**o**@@@o*******ooo@#@@@O@OOOOO@@@@@@@OOOOO@OOOOOOOOOOOOOOOOO@OOOOOOOOOOOOOOOO@OOOOO@OOOOOOOOOOOOOOO@@@@@
#@@oooooooo@@o**o*oooooooooo@*@@O@OoOOO@@@@@@@OOOoO@OOOOOOOooooOOOO@@@OOOOOOooooOOOOO@@OoOoO@@@OOOooooooOOOO@@@@@
@°*@@@@@@@@o#o@o*oooooooooooo@o@@@OOOOO@@@@@@@OOOOO@OOOOOOOOOOOOO@@@@@OOOOOOOOOOOOO@@o@OOOOO@*@@@OOOOOOOO@@@@@@@@
@@@oo*****°@@o#oooooooooooooo°#@@@@@@@@@@@@@@@@@@@@@OOOOOO@@@@@@@@o@@@OOOOO@@@@@@@@O@@@@@@@@@@@o@@@@@@@@@@o@@@@@@
@@@@@@@@@@@@@@o@oooooooooooo@o@@@@@oooo@@@@@@@oooo@@OOOOOO@@@@@@*@@@@@OoOoO@@@@@@*@@@@@*OOOo@@@@@@oOOOOo@@@@@@@@@
@@@@@@@@@@@@@@@o@Ooooooooo@@#@@@@@@@@@@@@@@@@@@@@@@@OOOOOO@ @@@@@@@@@@OOOOO@*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                      
                             Ripple Price Alert
                                       
    Donate XRP rhsZa1NR9GqA7NtQjDe5HtYWZxPAZ4oGrE (Destination #) 3788553174


""")



time.sleep(4)


value = input("Enter the price in BTC for Ripple to be alerted for examp. 0.0001 > ")


while True:


    val = requests.get('https://tradeogre.com/api/v1/ticker/btc-xrp').json()['price']

    


 
    
    
    #time.sleep(60)
    print("~___________________________________________________________________________~")
    
    if val == value:
        print("                           💎️", val, "BTC/XRP 💎️")
        print("~____________________________________________________________________________~")
        time.sleep(20)   
    
    if val < value:
        print("                           😭️", val, "BTC/XRP 😭️")
        print("~____________________________________________________________________________~")     
        time.sleep(20)
        
    if val > value:
        print(val, "   BTC/XRP   👏️👏️  ALERT!!!! Your Goal Price Has Occured!  👏️👏️")
        print("~____________________________________________________________________________~")
        playsound("alarm.wav")
        time.sleep(60)
else:
    print("Stop playing around! Please use decimal")           
