# Modules importation
import os
import base64
try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
init()

banner = (Fore.MAGENTA + """
54| / |41|| / | | <| 241| 1363| / |I)
""" + Fore.LIGHTCYAN_EX)
print(banner)
userid = input(" ID: ")
encodedBytes = base64.b64encode(userid.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")
print(f'\n Token: {encodedStr}')
os.system('pause >nul')  # Pause command in Batch (press any key to exit the code)
