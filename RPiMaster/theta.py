import requests
import os
import subprocess

class Theta:

	def __init__(self):
		self.url = 'http://192.168.1.1/osc/commands/execute'

		self.commands = {"start": {"name": "camera.startCapture"},
		"stop": {"name": "camera.stopCapture"},
		"list": {"name": "camera.listFiles", "parameters": {"fileType": "all","entryCount": 50,"maxThumbSize": 0}},
		"delete": {"name": "camera.delete", "parameters": {"fileUrls": ["all"]}},
		"storage": {"name": "camera.getOptions", "parameters": {"optionNames": ["remainingvideoSeconds"]}},
		"frequency": {"name": "camera.getOptions", "parameters": {"optionNames": ["_wlanFrequency"]}}
		}

	def request(self, command):
		response = requests.post(self.url, self.commands[command])
		return response

	def download(self):
		resonse = self.request('list')
		fileUrl = response.json()['results']['entries'][0]['fileUrl']
		os.system("wget " + fileUrl)

	def rssi(self):
		proc = subprocess.Popen(["iwconfig", "wlan0"], stdout=subprocess.PIPE, shell=False)
		(out, err) = proc.communicate()
		out = out.decode('utf-8')
		out = out.split("\n",8)[5]
		out = out.split("=", 3)[2]
		out = out[:3]
		return int(out)





