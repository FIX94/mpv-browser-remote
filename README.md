# mpv-browser-remote
This is a very simple project to control a few features of MPV directly from a web browser, namely pausing, seeking forward and backwards and quitting.  
You could easily add in many more features by just editing the index.html and mpv-remote.py python script with the commands found in the mpv refernce manual.    

# Basic Usage
If you want to give this a try, make sure you have any version of python installed, it should work on both version 2 and 3.  
Simply download a .zip of this repository and extract its contents into a folder of your choice.  
Then make an edit to your mpv.conf, add in the following line if you are on Windows:  
input-ipc-server=\\.\pipe\mpv-pipe  
or if you are on any other OS, add this line instead:  
input-ipc-server=/tmp/mpv-socket  
Alternatively, if you are just opening MPV from a command line, you can just call it with the argument --input-ipc-server=\\.\pipe\mpv-pipe on Windows or  
--input-ipc-server=/tmp/mpv-socket on any other OS and it should work the same way.  
Now you should be able to just execute the mpv-remote.py script which reads in the index.html and starts a server,  
this small server is at port 8000 in your network by default, you can edit that port in the script if needed.  
From there, just see what the IP is in the network, I'll use 192.168.0.100 in this example for mine, you should be able to just enter something like  
http://192.168.0.100:8000 in your browser on whatever system is in the same network, say a phone, and it should bring up the page.  
Now all you have to do is fire up MPV with your file of choice and pressing the buttons on that page should control the player.    

You can also edit the button size and text size in the index.html to whatever pixel values would fit your device better, these are just sample values.  
This project is meant just as a demonstration of the remote feature so if you want anything more in it, feel free to just extend the code to your needs.  
