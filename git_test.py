import platform
import socket
import os
from datetime import datetime

def get_system_info(user_name):
    info = []
    
    # Date & Time
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    info.append(f"Date & Time : {now}")
    info.append(f"User Name   : {user_name}")
    info.append("-" * 40)

    # System Information
    info.append(f"Computer Name : {socket.gethostname()}")
    info.append(f"OS            : {platform.system()} {platform.release()}")
    info.append(f"OS Version    : {platform.version()}")
    info.append(f"Machine       : {platform.machine()}")
    info.append(f"Processor     : {platform.processor()}")
    info.append(f"Architecture  : {' '.join(platform.architecture())}")
    info.append(f"Python Version: {platform.python_version()}")
    
    return "\n".join(info)

def save_to_file(data, user_name):
    filename = f"system_info_{user_name}.txt"
    with open(filename, "w") as file:
        file.write(data)
    print(f"\n✅ System information saved to '{filename}'")

# -------- MAIN PROGRAM --------
if __name__ == "__main__":
    user_name = input("Enter your name: ").strip()
    
    system_info = get_system_info(user_name)
    save_to_file(system_info, user_name)
