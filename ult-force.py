from engine.engine import *

################################

if get_os() == "win32":
    pass
else:
    style_text("[!] This script is not compatible with your operating system!")
    exit()

################################

versoin = 1.0

style_title(f'ULT-FORCE ^| VERSION: {versoin} ^| By: U8SEF')
style_clearscreen()
style_hide_cursor()


################################

print(style_copyright_name("U8SEF"))
print(style_banner("""
                        ██╗░░░██╗██╗░░░░░████████╗░░░░░░███████╗░█████╗░██████╗░░█████╗░███████╗
                        ██║░░░██║██║░░░░░╚══██╔══╝░░░░░░██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝
                        ██║░░░██║██║░░░░░░░░██║░░░█████╗█████╗░░██║░░██║██████╔╝██║░░╚═╝█████╗░░
                        ██║░░░██║██║░░░░░░░░██║░░░╚════╝██╔══╝░░██║░░██║██╔══██╗██║░░██╗██╔══╝░░
                        ╚██████╔╝███████╗░░░██║░░░░░░░░░██║░░░░░╚█████╔╝██║░░██║╚█████╔╝███████╗
                        ░╚═════╝░╚══════╝░░░╚═╝░░░░░░░░░╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░╚════╝░╚══════╝
                   
                   """))
style_text("[+] Select a service:")
style_text("    ")
style_text("    1- Run a Script")
style_text("    2- View Wordlists")
style_text("    3- View Proxy List")
style_text("    4- Upload a Wordlist")
style_text("    5- Upload a Proxy List")
style_text("    6- Optimize PC Performance")
style_text("    7- Exit")
style_text("    ")
def console():
    try:
        service = int(style_input("[?] -->"))
    except:
        style_text("[!] Invalid input. Please enter a number.")
        console()
    if service == 1:
        select_script()
    elif service == 2:
        view_wordlists()
        console()
    elif service == 3:
        view_proxy_list()
        console()
    elif service == 4:
        upload_wordlist()
        console()
    elif service == 5:
        upload_proxylist()
        console()

    elif service == 6:
        optimize_performance()
        console()

    elif service == 7:
        style_text("[+] Exiting...")
        exit()
    else:
        style_text("[!] Invalid option. Please choose a number between 1 and 7.")
        exit()
console()
print("")
style_type("[♥] Thank you for using ULT-FORCE !")
