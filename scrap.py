 #!/bin/python3


import requests as req , bs4
import pyperclip as pc
import sys , os


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
            print(f"(3) : create a wordlist from {url}")
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

            elif number == 3:

                                
                texts = []
                tag = input('[+] Specify the tag to scrap : ')
                for p_tag in soup.find_all(tag):

                    paras = p_tag.text
      
                    sp_paras = paras.split()

                    for j in sp_paras:
                        texts.append(j.replace('"','').replace("’","").replace(".","").replace(":","").replace("!","").replace("?","").replace(",",""))
                    
                for i in texts:
                    print(i)
                    
                wanna_save = input("[+] Want to save the wordlist in a file? (y/n) : ")
                    
                if wanna_save == 'y' :
                        
                    with open('web_wordlist.txt' , 'a' , encoding="utf-8") as file:
                                  
                        for t in texts:
                            file.write(str(t))
                            file.write("\n")
                        
                    pwd = os.getcwd()
                    print()
                    print(f"[+] Saved the wordlist in {pwd}")
    
                else:
                    print('\n[+] Ok ...........................')



            
            else:
                print('ERROR : enter only 1 , 2 or 3')   
        else:
            print('[+] ERROR 404 not found......... \n')
            print(f'[+] plzzzz check the url({url})')

    except KeyboardInterrupt:

        print("\n[+] Terminating......................")

    
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
