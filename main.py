import random, string, requests, os
import colorama, time, datetime, json
from colorama import Fore, init
from dhooks import Webhook, Embed

os.system("cls")
print("Hey, welcome, so look this and idk, do something with this)?")
input("REMEMBER THAT THE CODES ARE CHECKED INSTANTLY, NOW PRESS ENTER TO CONTINUE")

with open('config.json') as f:
  config = json.load(f)
hook = Webhook(config.get("webhook"))
version = config.get("version")

good = open("txts/Hits.txt", "w", encoding="utf-8")

while True:
  code=('').join(random.choices(string.ascii_letters + string.digits, k=16))
  r = requests.get(f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true")
  if r.status_code == 200:
    print(f"{Fore.CYAN}[+] Hit Nitro = discord.gift/{code}{Fore.RESET}")
    good.write(f"discord.gift/{code}\n")
    hook.send("@everyone")
    embed = Embed(description='VALIDO CONCHETUMARE', color=0x19FA03, timestamp='now')
    image1 = 'https://images-ext-1.discordapp.net/external/Rt5g_9NQx-ESXzenymkBVtG15vxR9RV_5XKQw07c8zo/https/media.discordapp.net/attachments/730614146629894204/821390440024244255/image0-6-1-1-1.gif'
    embed.set_author(name='VALID CODE')
    embed.add_field(name='**Alive Code**', value='```{}```'.format(code), inline=True)
    embed.add_field(name='**Time?**', value='```{}```'.format(datetime.datetime.now()), inline=True)
    embed.set_footer(text='The AutoPilot by Chirimoya | WebHook Log | Version: {}'.format(version))
    embed.set_thumbnail(image1)
    hook.send(embed=embed)
  else:
      print(f"{Fore.RED}[-] Invalid = discord.gift/{code}{Fore.RESET}")
      embed = Embed(description='Nope, nothing', color=0xFA0303, timestamp='now')
      image1 = 'https://images-ext-1.discordapp.net/external/Rt5g_9NQx-ESXzenymkBVtG15vxR9RV_5XKQw07c8zo/https/media.discordapp.net/attachments/730614146629894204/821390440024244255/image0-6-1-1-1.gif'
      embed.set_author(name='INVALID CODE')
      embed.add_field(name='**Tried Code**', value='```{}```'.format(code), inline=True)
      embed.add_field(name='**Time?**', value='```{}```'.format(datetime.datetime.now()), inline=True)
      embed.set_footer(text='The AutoPilot by Chirimoya | WebHook Log | Version: {}'.format(version))
      embed.set_thumbnail(image1)
      hook.send(embed=embed)