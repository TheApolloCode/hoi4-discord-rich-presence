import pypresence as pres
import time, os, psutil

'''
                            Hearts of Iron IV discord rich presence
This is a program built to show rich presence in discord while playing HOI4 using the python presence library.
The time library is used for counting the seconds since start,os for file pathing and psutil for the detecting
the hoi4.exe process.
The array info_txt has 3 values.They are the 3 first values found in the autosave.hoi4 file.
The values are
* the country tag,
* the the ideology,
* the date.
As long as this is running,they are shown in Discord.
The program constantly reads and updates based on the autosave file information.
The autosave file is located either in %userprofile/Documents/Paradox Interactive/Hearts of Iron IV/save games
or its OneDrive equivalent.This program treats both cases.
In a case where this isn't the case,just change it to your path.
The startepoch variable counts the time the program and implicitly the game started.
If you want to improve this program,feel free to do so.I just worked on its bare minimum for the moment.
Whenever the game autosaves,the save is re-written,therefore the except case just waits 20 seconds before
verifying and updating again.
IMPORTANT NOTE:For this program to work you need to disable the saves being written in binary.
               This is done in the settings.txt file in the Paradox Interactive folder
             save_as_binary=no(you will find it by default as save_as_binary=yes
I wish to recommend and cite as inspiration,and also a start guidance project 
the EU4 equivalent of this project that can be found at:
https://github.com/stefastra/eu4-discord-rich-presence done by stefastra.
THANK YOU!
'''
info_txt=['', '', '']
count=0
process=0
for proc in psutil.process_iter():
    if proc.name() == "hoi4.exe":
        print("Hoi4 detected with pid: " + str(proc.pid))
        process=int(proc.pid)
savefile_path = os.environ['USERPROFILE'] + "\\Documents\\Paradox Interactive\\Hearts of Iron IV\\save games\\"
startepoch = time.time()
startepoch=int(startepoch)
RPC = pres.Presence('964281925277720666')
RPC.connect()
RPC.update(state="Loading...", start=startepoch)
try:
    os.listdir(savefile_path)
except:
    print('using alternate savefile path...')
    savefile_path = os.environ['USERPROFILE'] + "\\OneDrive\\Documents\\Paradox Interactive\\Europa Universalis IV\\save games\\"


while (True):
    autosave = savefile_path + "autosave.hoi4"
    try:
     f = open(autosave, "r")
     for i in range(4):
        text=f.readline().strip()
        if text!='HOI4txt':
             info_txt[count]=text
             count+=1
     info_txt[0]=info_txt[0].removeprefix("player=").strip()
     info_txt[0]=info_txt[0].replace('"','') #Country tag
     info_txt[1]=info_txt[1].removeprefix("ideology=").strip().title() #Ideology
     info_txt[2]=info_txt[2].removeprefix("date=").strip()
     info_txt[2] = info_txt[2].replace('"', '')
     info_txt[2]=info_txt[2][0:4] #Year
     f.close()
     count=0
    except:
        time.sleep(20)

    RPC.update(
    pid=process,
    state=f"{info_txt[2]}",
    details=f"{info_txt[0]},{info_txt[1]}",
    large_text="Hearts of Iron IV",
    large_image="large",
    start=startepoch
    )


