#!/usr/bin/python

import os, sys, re 

def wifiScan():
	wifi = 'wlan0'
	cmd = 'sudo iwlist ' + wifi + ' scan'
	wifiData = os.popen(cmd)
	wifiData = wifiData.read().strip()
	if wifiData == wifi +"     No scan results":
			print wifiData
	return wifiData

def extractCells():
	wifiData = wifiScan()
	wData = wifiData.replace("\n", " ")
	wData = re.sub('\s+',' ', wData)
	wData = re.sub('Cell','SPLIT Cell', wData)
	wData = wData.split('SPLIT ')
	wCell = {}
	for cell in wData:
		#print cell
		cellKey = re.search('Cell\s\d\d', cell)
		if cellKey:
			key = cellKey.group()
			wCell[key] = cell
	return wCell

#def macChange(data):

def parseCells():
	
	wCells = extractCells()
	
	print '${color blue}ESSID          Signal(dBm)     Channel     Encryption     Address $color'

	for w in wCells:
		cellESSID = re.search(r'ESSID:([\w\d\S]+)', wCells[w])
		
		cellSignal = re.search(r'Signal level=([\w\d\c\S]+)', wCells[w])

		cellChannel = re.search(r'Channel:([\w\d\c\S]+)', wCells[w])

		cellEncryption = re.search(r'IE: IEEE 802.11i/([\w\d\c\S]+)', wCells[w])

		cellMAC = re.search('([\w\d]+):([\w\d]+):([\w\d]+):([\w\d]+):([\w\d]+):([\w\d]+)', wCells[w]) 
		cellMAC = cellMAC.group(1)+'-'+cellMAC.group(2)+'-'+cellMAC.group(3)+'-'+cellMAC.group(4)+'-'+cellMAC.group(5)+'-'+cellMAC.group(6)
		#		wCells[w] = re.sub('([\w\d]+):([\w\d]+):([\w\d]+):([\w\d]+):([\w\d]+):([\w\d]+)', macFormatted, wCells[w])

		if cellESSID:
				cellESSID = cellESSID.group(1)
		else:
				cellESSID = "--"
		if cellSignal:
				cellSignal = cellSignal.group(1)
		else:
				cellSignal = "--"
		if cellChannel:
				cellChannel = cellChannel.group(1)
		else:
				cellChannel = "--"
		if cellEncryption:
				cellEncryption = cellEncryption.group(1)			
		else:
				cellEncryption = "--"

		print cellESSID + "    "  + cellSignal + "    " + cellChannel + "    " + cellEncryption + "    " + cellMAC

def main():
	parseCells()
	
if __name__ == "__main__":
	main()
