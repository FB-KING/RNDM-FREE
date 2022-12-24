import os, platform
 
try:
 
        import requests
        os.system("git pull")
        print('\x1b[38;5;46m checking new update')
        os.system("xdg-open https://www.facebook.com/groups/fb.king.cyber/?ref=share")
 
except:
 
        os.system('pip2 install requests')
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from iam_back import XYZ
 
        XYZ()
 
 
 
elif bit == "32bit":
 
        from iam_back32 import XYZ
 
 
        XYZ()
        
