# GREFlashCard

Help remembering GRE words when doing misc stuff

This is a tiny project that helped me remembering boring GRE words.  

I usually spend lots of time in front of computer. Therefore, I was thinking 
what if I write a mini-program that would push notification to my computer periodically. 

Therefore, this project will read the word list from **res** directory and push notification to 
my MacBook periodically. 


## Deploy

Just download this Git repo and add src/main.py to crontab. 

### Add to crontab

I personally let this program push notification every 3 minutes. 

Open the terminal and type:
```bash
crontab -e
```

Then, write this line in the opened file
``` 
*/3 * * * * cd <path_to_this_project>/GREFlashCard/src; ./main.py
```
