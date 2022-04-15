# 	Hearts of Iron IV discord rich presence
This is a program built to show rich presence in discord while playing HOI4 using the python presence library.

The time library is used for counting the seconds since start,os for file pathing and psutil for the detecting
the hoi4.exe process.

The array info_txt has 3 values.They are the 3 first values found in the autosave.hoi4 file.

The values are

* the country tag,

* the ideology,

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

An image example of how it looks:

![image](https://user-images.githubusercontent.com/88626764/163652812-bccfc672-550a-462c-835a-47463b3db3a0.png)

