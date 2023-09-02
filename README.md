# Disclaimer

Any actions and or activities related to Zphisher is solely your responsibility. The misuse of this toolkit can result in criminal charges brought against the persons in question. The contributors will not be held responsible in the event any criminal charges be brought against any individuals misusing this toolkit to break the law.

This toolkit contains materials that can be potentially damaging or dangerous for social media. Refer to the laws in your province/country before accessing, using,or in any other way utilizing this in a wrong way.

This Tool is made for educational purposes only. Do not attempt to violate the law with anything contained here. If this is your intention, then Get the hell out of here!

It only demonstrates "how phishing works". You shall not misuse the information to gain unauthorized access to someones social media. However you may try out this at your own risk.

### Installation Linux

##### Clone this repository

 - ```git clone https://github.com/tayko9222/screamtool```

##### Enter the directory
 - ```cd screamtool```

##### Install all modules
 - ```pip install -r requirements.txt```

##### Run the tool
 - ```python SCReam.py```

#### Or, directly run
```
wget https://raw.githubusercontent.com/tayko9222/screamtool/main/SCReam.py && python SCReam.py

```

### Installation Termux

##### Clone this repository

 - ```git clone https://github.com/tayko9222/screamtool.git```

##### Enter the directory
 - ```cd screamtool```

##### Install all modules
 - ```pip install -r requirements.txt```

##### Run the tool
 - ```python3 SCReam.py```

### Installation Windows

##### Download the repertory in ZIP

 - ```Just download```

##### Copy the path where is locate screamtool and do
 - ```cd C:/path/screamtool```

##### Install all modules
 - ```pip install -r requirements.txt```

##### Run the tool
 - ```python SCReam.py```

##### Or just see this tuto and use git clone
 - '''https://www.youtube.com/watch?v=Jge57UHvYto'''

### Docker

 - `sudo docker pull tayko9222/screamtool`
 - `sudo docker run --rm -it tayko9222/screamtool`
 - `sudo docker cp $(sudo docker ps | grep screamtool | awk '{print $1}'):/root/Media media` [Run this on another terminal to copy received files from docker to media folder while keeping the container running]
