import re
import os
import sys
import shutil
import tkinter as tk
from tkinter import filedialog
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from pystyle import Colors, Colorate, Center, Cursor, Box , System , Write

def load_combo_list():
    folder_list = os.listdir('combos')
    combo_list = []
    for combo_file in folder_list:
        combo_list.append(combo_file)
    return combo_list
def load_proxy_list():
    folder_list = os.listdir('proxies')
    proxy_list = []
    for proxy_file in folder_list:
        proxy_list.append(proxy_file)
    return proxy_list
def load_script_list():
    folder_list = os.listdir('scripts')
    scripts_list = []
    for script_list in folder_list:
        scripts_list.append(script_list)
    return scripts_list
def load_wordlist(file_name):
    with open(f'wordlists/{file_name}', 'r') as wordlist_file:
        return [word.strip() for word in wordlist_file.readlines()]

def load_proxy(file_name):
    with open(f'proxies/{file_name}', 'r') as proxylist_file:
        return [proxy.strip() for proxy in proxylist_file.readlines()]
def respect_author(web_link):
    os.system(f"start {web_link}")
def style_title(title):
    System.Title(f'{title}')
def get_os():
    return sys.platform
def get_file_size(file_path):
    return os.path.getsize(file_path)
import os, sys

import os, sys, re

def optimize_performance():
    os.system('powercfg -create ULT-FORCE > nul 2>&1')  
    output = os.popen('powercfg -list').read()
    match = re.search(r'Power Scheme GUID: ([a-f0-9\-]+)', output)
    if match:
        plan_id = match.group(1)
        for cmd in [
            f'powercfg -setactive {plan_id}',
            'powercfg -change -monitor-timeout-ac 30',
            'powercfg -change -disk-timeout-ac 0',
            'powercfg -change -standby-timeout-ac 0',
            'powercfg -change -hibernate-timeout-ac 0'
        ]:
            os.system(cmd + " > nul 2>&1")
        style_text("[+] ULT-FORCE power plan applied successfully!")
    else:
        style_text("[!] Failed to create power plan.")


def style_clearscreen():
    System.Clear()
def style_banner(text):
    return Center.XCenter(Colorate.Horizontal(Colors.rainbow, text))
def style_copyright(author, script_name):
    return Center.XCenter(Colorate.Horizontal(Colors.rainbow,Box.Lines(f"By: {author}          Config: {script_name}")))
def style_copyright_name(author):
    return Center.XCenter(Colorate.Horizontal(Colors.rainbow,Box.Lines(f"{author}")))
def style_hide_cursor():
    Cursor.HideCursor()
def style_type(text):
    Write.Print(text,Colors.rainbow, interval=0.05)
def style_text(text):
    System.Init()
    print(Colorate.Horizontal(Colors.rainbow, text))
def style_input(text):
    System.Init()
    return input(Colorate.Horizontal(Colors.rainbow, text))
def upload_wordlist():
    COMBO_DIR = os.getcwd() + "\combos" 
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
            title="Choose your wordlist file",
            filetypes=[("Text Files", "*.txt")]
        )

    if not file_path:
            style_text("[!] No file selected.")
            return
    style_text(f"[+] {os.path.abspath(file_path)} -> {COMBO_DIR}")
    shutil.copy(file_path, COMBO_DIR)
def upload_proxylist():
    PROXIES_DIR = os.getcwd() + "\proxies" 
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
            title="Choose your proxy list",
            filetypes=[("Text Files", "*.txt")]
        )

    if not file_path:
            style_text("[!] No file selected.")
            return
    style_text(f"[+] {os.path.abspath(file_path)} -> {PROXIES_DIR}")
    shutil.copy(file_path, PROXIES_DIR)
def select_script():
    scripts = load_script_list()
    script = inquirer.select(
         message="Select a script:",
         choices=scripts,
    ).execute()
    return script

def select_combo():
    combo_list = load_combo_list()
    combo = inquirer.select(
         message="Select a worldlist:",
         choices=combo_list,
    ).execute()
    return combo
def select_proxylist():
    proxy_list = load_proxy_list()
    proxy = inquirer.select(
         message="Select a proxy list:",
         choices=proxy_list,
    ).execute()
    return proxy
def view_wordlists():
    combo_list = load_combo_list()
    for index, file_name in enumerate(combo_list, start=1):
        style_text(f"[{index}] - {file_name.ljust(35)} | {get_file_size(f'combos/{file_name}')}KB")

def view_proxy_list():
    proxy_list = load_proxy_list()
    for index, file_name in enumerate(proxy_list, start=1):
        style_text(f"[{index}] - {file_name.ljust(35)} | {get_file_size(f'proxies/{file_name}')}KB")
        