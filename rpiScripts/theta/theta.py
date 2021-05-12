import requests
import os

url = 'http://192.168.1.1/osc/commands/execute'
#myobj = {"name": "camera.stopCapture"}
'''
myobj = {"name": "camera.listFiles", "parameters":
	{
	"fileType": "all",
	"entryCount": 50,
	"maxThumbSize": 0
	}

}
'''
myobj = {"name": "camera.getOptions", "parameters":
	{
	"optionNames": ["gpsInfo"]
	}
}
x = requests.post(url, json=myobj)

print(x.text)
os.system("iwconfig wlan0 | grep -i --color signal")
