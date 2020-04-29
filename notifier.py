#Corona notifier
import os
import platform
import requests
from bs4 import BeautifulSoup
from plyer import notification

def get_data(url):
	return requests.get(url).text

def notifyWindows(title,message):
	 notification.notify(
	 		title=title,
	 		message = message,
	 		app_icon = None,
	 		timeout=10
	 	)

def notifyMac(title, message):
    cmd = 'ntfy -t "{0}" send "{1}"'.format(title,message)
    os.system(cmd)

def forward_notif(title,message,system):
	if(system=='Darwin'):
		notifyMac(title,message)
	elif(system=='Windows'):
		notifyWindows(title,message)

if __name__=='__main__':
	html = get_data("https://www.mohfw.gov.in")
	soup = BeautifulSoup(html,'html.parser')
	#print(soup.prettify())
	myData=""
	for tr in soup.find_all('tbody')[0].find_all('tr'):
		myData+=tr.get_text()
	myData=myData[1:]
	itemList = myData.split("\n\n")
	states = ['West Bengal','Maharashtra','Gujarat']
	notif="";
	total=0
	dataList=[]
	for item in itemList[0:32]:
		dataList.append(item.split("\n"))
	for statesdata in dataList:
		total=total+int(statesdata[2])
		#print(statesdata)
		if statesdata[1] in states:
			notif+=f'{statesdata[1]} : {statesdata[2]}\n'
	forward_notif(f'Total Cases : {total}',notif,platform.system())














