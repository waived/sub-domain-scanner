# -*- coding: utf-8 -*-

import sys
import os
import requests
from urllib.parse import urlparse

def rslv(_site):
    _site = _site.lower()
    if not (_site.startswith('http://') or _site.startswith('https://')):
        _site = 'http://' + _site
        
    try:
        _domain = urlparse(_site).netloc
        
        if _domain.startswith('www.'):
            _domain = _domain[4:]

        return _domain
    except:
        sys.exit('\r\nDNS resolution failed! Exiting...\r\n')

def main():
    global _active
    
    os.system("cls")
    
    print('''\033[22m
  _________    ___                         __        
 /   _____/__ _\_ |__   __________   ____ |__| ____  
 \_____  \|  |  \ __ \ /  ___/  _ \ /    \|  |/ ___\ 
 /        \  |  / \_\ \\\___ (  <_> )   |  \  \  \___ 
/_______  /____/|___  /____  >____/|___|  /__|\___  >
        \/          \/     \/           \/        \/           
''')
    _sd = []

    #capture user input
    try:
        _site = input('Domain/URL: ')
        
        _site = rslv(_site) # correctly format target
        
        _list = input('Worldlist (ex- /tmp/subs.txt): ')
        
        #ensure list exists
        if os.path.exists(_list):
            #import content
            try:
                with open(_list, "r") as f:
                    for line in f:
                        if "\n" in line:
                            # remove any carriage return/s
                            line = line.replace("\n", "")
                            _sd.append(line)
                        else:
                            _sd.append(line)

            except Exception as e: #FileNotFoundError:
                print(e)
                sys.exit('\r\nError importing! Exiting...\r\n')
        else:
            sys.exit('\r\nFile not found! Exiting...\r\n')
        
        _tout = int(input('Timeout sec. (default 2): '))
        
        input('\r\nReady? Strike <ENTER> to scan and <CTRL+C> to abort...\r\n')
    except KeyboardInterrupt:
        sys.exit()
    except:        
        main()
        
    #manage scan
    for _sub in _sd:
        
        _url = f"http://{_sub}.{_site}"
    
        try:
            response = requests.get(_url, timeout=int(_tout))
            if response.status_code == 200:
                print(f'[\033[32mALIVE\033[37m] Sub-domain active @ {_url}')
            else:
                print(f'[\033[31mDEAD\033[37m] Nothing found for "{_sub}"')
        except KeyboardInterrupt:
            sys.exit('\r\n\033[37mAborted.\r\n')
        except:
            print(f'[\033[31mDEAD\033[37m] Nothing found for "{_sub}"')

    sys.exit('\r\n\r\n\033[37mDone.\r\n')

if __name__ == "__main__":
    main()