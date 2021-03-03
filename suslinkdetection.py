import requests
from time import sleep as wait
from colorama import Fore, init
init()

print(Fore.YELLOW + r'''
 ____  __ _  __  ____    ____  _  _   ___  __ _  ____  ____ 
/ ___)(  / )(  )(    \  (  __)/ )( \ / __)(  / )(  __)(  _ \
\___ \ )  (  )(  ) D (   ) _) ) \/ (( (__  )  (  ) _)  )   /
(____/(__\_)(__)(____/  (__)  \____/ \___)(__\_)(____)(__\_)
IP Pulling detection By 0WNED//Zexor321. All unshortening requests go through a server, not through your network. (:-3)
''')

wait(1)

InputtedUrl = input("\n>>> Enter the URL of a suspicious link -> ")
wait(0.5)
url = str(InputtedUrl)
print("\n>>> Checking link for suspicious endpoints... ")

if('grabify' in url or 'cutt.ly' in url or 'gestyy' in url or 'anthargo' in url or 'bc.vc' in url or 'soo.gd' in url or 'ouo.io' in url or 'zzb.bz' in url or 'adfoc.us' in url):
    print(Fore.RED +"\n[!] Malicious Link Detected => grabify.link URL!. SKID ALERT!!!")
    print(Fore.YELLOW +"[?] => Use unshorten.it for endpoint because of Grabify dual layer shit.")
    wait(99999)
elif('iplogger' in url or '2no' in url or 'yip.su' in url or 'iplis' in url or '02ip' in url or 'ezstat.ru' in url):
    print(Fore.RED +"\n[!] Malicious Link Detected => iplogger.org URL!. SKID ALERT!!!")
    print(Fore.YELLOW +"[?] => Use unshorten.it for endpoint.")
    wait(99999)
else:
    print("\n[I] No immediate threats detected in link, unshortening and doing more checks...")
    reqloc = 'https://unshorten.me/s/%s' % (url)
    r = requests.get(reqloc)
    resp = str(r.text)
    if('iplogger' in resp or '2no' in resp or 'yip.su' in resp or 'iplis' in resp or '02ip' in resp or 'ezstat.ru' in resp):
        print(Fore.RED +"\n[!] Malicious Link Detected => iplogger.org URL with attempted dual layer hide!. SKID ALERT!!!")
        print(Fore.YELLOW +"[?] => Use unshorten.it for endpoint because of dual layer shit.")
        wait(99999)
    elif('grabify' in resp or 'cutt.ly' in resp or 'gestyy' in resp or 'anthargo' in resp or 'bc.vc' in resp or 'soo.gd' in resp or 'ouo.io' in resp or 'zzb.bz' in resp or 'adfoc.us' in resp):
        print(Fore.RED +"\n[!] Malicious Link Detected => grabify.link URL!. SKID ALERT!!!")
        print(Fore.YELLOW +"[?] => Use unshorten.it for endpoint because of Grabify dual layer shit.")
        wait(99999)
    else:
        print(Fore.GREEN + "\n[:)] Link is likely safe from IP Loggers, to be sure, use unshorten.it after reading below.")
        print(Fore.RED + "Endpoint => %s, if the endpoint is already short, why would they shorten it? Dual-layed iplogger.org formats are untraceable!!!")
        wait(99999)
# -- End Of script.