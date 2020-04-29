#!/bin/python3


import requests as req , bs4
import pyperclip as pc
import sys


def scrap(url):
    try:
        res = req.get(url)
        code = res.status_code   
        
        if code != 404:
            text  = res.text
            print("\n[+] Handshake successful........ \n")
            soup = bs4.BeautifulSoup(text,"lxml")
            
            print("\n")
            print(f'(1) : print the entire content from {url}')
            print(f'(2) : print the only the specified tags from {url}')
            print('\n')
            
            number = int(input('-> '))
            
            if number == 2: 
                print('[+] Specify the tag you want to scrap .....')
                print('''
                Eg: 
                   b for <b> tag 
                   a for <a> tag \n''')
                que = input('-> ')
            
                if que == 'a':
                    a_tag = soup.find_all('a')
                    choice = input('[+] are you looking for all the links ? (y/n) : ')
                    print('\n')
                    if choice == 'y':
                        for links in a_tag:
                            print(f"| {links.attrs['href']} \n")
                    else:
                        print(f"{a} \n")
                else:
                    tags = soup.find_all(que)
                    
                    for t in tags:
                        print(f'{t} \n')
            
            elif number == 1:
                print('\n')
                print(text)
            
            else:
                print('ERROR : enter only 1 or 2')   
        else:
            print('[+] ERROR 404 not found......... \n')
            print(f'[+] plzzzz check the url({url})')
    except:
        print("\n")
        print(f'[+] the copied url is : {url}')
        print("[+] failed to connect.........")


arg = sys.argv


if len(arg) == 2 :
    url = arg[1]
    scrap(url)

else:
    url = pc.paste()
    print('\n')
    print(f'[+] Pasted url : {url}')
    scrap(url)
