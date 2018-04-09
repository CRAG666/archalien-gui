import os
import time
os.system("clear")
n=str(input('desea instalar el archalien-gui s/n: '))
if(n=="s"):
    os.system("sudo cp -r archalien /opt/")
    os.system("sudo cp archalien-GUI.desktop /usr/share/applications/")
if(n=="n"):
    print("cerrando........")
    time.sleep(2)
    os.system("clear")
    exit()
