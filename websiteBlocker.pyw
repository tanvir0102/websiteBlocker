import time
from _datetime import datetime as dt

hosts_temp=r"D:\GoogleDrive\Programming\Python\Build_10_RealWorldApplication\websiteBlocker\hosts"
hosts_path=r"C:\Windows\System32\Drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","www.gmail.com","www.youtube.com"]
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,19):
        print("Working Hours...")
        with open(hosts_temp,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
    else:
        with open(hosts_temp,'r+') as file:
            content=file.readline()
            file.seek(0,0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun Hours...")
    time.sleep(5)