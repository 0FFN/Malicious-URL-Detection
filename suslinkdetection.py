import requests
from time import sleep as wait
from colorama import Fore, init
init()

grabify = ["grabify", "cutt.ly", "gestyy", "anthargo", "bc.vc", "soo.gd", "ouo.io", "zzb.bz", "adfoc.us"]
iploggerorg = ["iplogger", "2no", "yip.su", "iplis", "02ip", "ezstat.ru"]

print(Fore.YELLOW + r'''
 ____  __ _  __  ____    ____  _  _   ___  __ _  ____  ____ 
/ ___)(  / )(  )(    \  (  __)/ )( \ / __)(  / )(  __)(  _ \
\___ \ )  (  )(  ) D (   ) _) ) \/ (( (__  )  (  ) _)  )   /
(____/(__\_)(__)(____/  (__)  \____/ \___)(__\_)(____)(__\_)
IP Pulling detection By arc. All unshortening requests go through a server, not through your network. (:-3)
''')

wait(1)

InputtedUrl = input("\n>>> Enter the URL of a suspicious link -> ")
wait(0.5)
url = str(InputtedUrl)
print("\n>>> Checking link for suspicious endpoints... ")

for domain in grabify:
    if domain in url:
        print(Fore.RED +"\n[!] Malicious Link Detected => grabify.link URL!. SKID ALERT!!!")
        print(Fore.YELLOW +"[?] => Use unshorten.it for endpoint because of Grabify dual layer shit.")
        wait(99999)
for domain in iploggerorg:
    if domain in url:
        print(Fore.RED +"\n[!] Malicious Link Detected => iplogger.org URL!. SKID ALERT!!!")
        print(Fore.YELLOW +"[?] => Use unshorten.it for endpoint.")
        wait(99999)
if('pnrtscr.com' in url):
    print('\n[i] Screamer detected, not malicious jumpscare.')
    wait(99999)

print("\n[I] No immediate threats detected in link, unshortening and doing more checks...")
reqloc = 'https://unshorten.me/s/%s' % (url)
r = requests.get(reqloc)
resp = str(r.text)
for domain in iploggerorg:
    if domain in resp:
        print(Fore.RED +"\n[!] Malicious Link Detected => iplogger.org URL with attempted dual layer hide!. SKID ALERT!!!")
        print(Fore.YELLOW +"[?] => Use unshorten.it for endpoint because of dual layer shit.")
        wait(99999)
for domain in grabify:
    if domain in resp:
        print(Fore.RED +"\n[!] Malicious Link Detected => grabify.link URL!. SKID ALERT!!!")
        print(Fore.YELLOW +"[?] => Use unshorten.it for endpoint because of Grabify dual layer shit.")
        wait(99999)
if('pnrtscr.com' in resp):
    print('\n[i] Screamer detected, not malicious jumpscare.')
    wait(99999)
print(Fore.GREEN + "\n[:)] Link is likely safe from IP Loggers, to be sure, use unshorten.it after reading below.")
print(Fore.RED + "Endpoint => %s, if the endpoint is already short, why would they shorten it? Dual-layed iplogger.org formats are untraceable!!!")
wait(99999)
