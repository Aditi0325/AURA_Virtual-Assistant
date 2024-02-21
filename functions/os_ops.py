import os
import subprocess as sp

paths = {
    'notepad': "C:\Windows\System32\notepad.exe",
    'calculator': "C:\Windows\System32\calc.exe",
   # 'command_prompt': "C:\Windows\System32\cmd.exe",
    'edge': "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
    'clean_manager': "C:\Windows\System32\cleanmgr.exe",
    'control_panel': "C:\Windows\System32\control.exe",
    'Game_Panel': "C:\Windows\System32\GamePanel.exe"
}

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def open_notepad():
    os.startfile(paths['notepad'])

def open_cmd():
    os.system('start cmd')

def open_calculator():
    sp.Popen(paths['calculator'])

def open_edge():
    sp.Popen(paths['edge'])
    
def open_clean_manager():
    sp.Popen(paths['clean_manager'])

def open_control_panel():
    sp.Popen(paths['control_panel'])

def open_game_panel():
    sp.Popen(paths['Game_Panel'])