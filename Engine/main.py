#!/usr/bin/python3

import notify2
import playsound
import time
import daemon
import cpImage
import reportGen
import os


def gain():
	notify2.init("Test")
	notice = notify2.Notification("CCS Service", "You gained points!", "/home/Scoring/icon.png")
	notice.set_timeout(1000)
	notice.show()
	playsound.playsound("/home/Scoring/gain.wav")
	
def loss():
	notice = notify2.Notification("CCS Service", "You lost points!", "/home/Scoring/icon.png")
	notice.set_timeout(1000)
	notice.show()
	playsound.playsound("/home/Scoring/alarm.wav")
	
def writeReport(vulns, pens):
	texts = []
	pTexts= []
	points = 0
	maxPoints = 0
	lossPoints = 0
	maxVulns = len(vulns)
	
	for vuln in vulns:
		maxPoints += vuln.getPoints()
		if vuln.getStatus():
			texts.append(vuln.getText())
			points += vuln.getPoints()
			
	for pen in pens:
		if pen.getStatus():
			pTexts.append(pen.getText())
			lossPoints += pen.getPoints()
			
	reportGen.generateReport("/home/Scoring/score.html", texts, pTexts, points, maxPoints, maxVulns, lossPoints, 8)
	
def main():
	notify2.init("Test")
	vulns = cpImage.getVulns()
	pens = cpImage.getPenalties()
	checkInterval = 15
	for vuln in vulns:
		try:
			vuln.check()
		except:
			pass
			
	for pen in pens:
		try:
			pen.check()
		except:
			pass
	writeReport(vulns, pens)
	
	while True:
		time.sleep(checkInterval)
		for vuln in vulns:
			try:
				vuln.check()
				if vuln.isGain():
					writeReport(vulns, pens)
					gain()
					break
				elif vuln.isLoss():
					writeReport(vulns, pens)
					loss()
					break
			except:
				vuln.setAsInitial()
		for pen in pens:
			try:
				pen.check()
				if pen.isGain():
					writeReport(vulns, pens)
					loss()
					break
				elif pen.isLoss():
					writeReport(vulns, pens)
					break
			except:
				pen.setAsInitial()

if not 'DISPLAY' in os.environ:
    os.environ['DISPLAY'] = ':0'

main()
