import os.path
import os
import subprocess

class FileExistsVuln:
	 def __init__(self, path):
	 	self.path = path
	 	
	 def check(self):
	 	return os.path.isfile(self.path)
	 	
class CommandContainsVuln:
	def __init__(self, cmd, rexp):
		self.cmd = cmd
		self.rexp = rexp
		
	def check(self):
		try:
			os.setuid(os.geteuid())
			out = str(subprocess.check_output(self.cmd))
			return self.rexp in out
		except:
			return False
		
class FileContainsVuln:
	def __init__(self, path, rexp):
		self.path = path
		self.rexp = rexp
	
	def check(self):
		f = open(self.path, "r")
		return self.rexp in f.read()
		
class ForensicVuln:
	def __init__(self, path, line0, answers):
		pass
		
	def check(self):
		pass
		
class VulnWrap:
	def __init__(self, vuln, initial, target, text, points):
		self.target = target
		self.vuln = vuln
		self.text = text
		self.initial = initial
		self.status = initial
		self.gain = False
		self.loss = False
		self.points = points
		
	def getText(self):
		return self.text
		
	def getStatus(self):
		return self.status == self.target
	
	def setAsInitial(self):
		self.status = self.initial
		
	def getPoints(self):
		return self.points
		
	def isGain(self):
		return self.gain
	
	def isLoss(self):
		return self.loss
				
	def check(self):
		newStatus = self.vuln.check()
		if newStatus != self.status:
			if newStatus == self.target:
				self.gain = True
				self.loss = False
			else:
				self.gain = False
				self.loss = True
		else:
			self.gain = False
			self.loss = False
		self.status = newStatus
		
		
		
		
		
