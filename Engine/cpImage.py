from vulns import *

def getPenalties():
	return [
		VulnWrap(FileExistsVuln("/home/jlibano/Desktop/Forensics Question 1.txt"), True, False, "Forensics Question 1 deleted - 3 pts", 3),
		VulnWrap(FileExistsVuln("/home/jlibano/Desktop/Forensics Question 2.txt"), True, False, "Forensics Question 2 deleted - 3 pts", 3),
		
		VulnWrap(CommandContainsVuln(["cat", "/etc/passwd"], "amahajan"), True, False, "amahajan removed - 2 pts", 2),
		VulnWrap(CommandContainsVuln(["cat", "/etc/passwd"], "fwang"), True, False, "fwang removed - 2 pts", 2),
		VulnWrap(CommandContainsVuln(["cat", "/etc/passwd"], "tcharest"), True, False, "tcharest removed - 2 pts", 2),
		VulnWrap(CommandContainsVuln(["cat", "/etc/passwd"], "smishra"), True, False, "smishra removed - 2 pts", 2),
		VulnWrap(CommandContainsVuln(["cat", "/etc/passwd"], "csalvatore"), True, False, "csalvatore removed - 2 pts", 2),
		VulnWrap(CommandContainsVuln(["cat", "/etc/passwd"], "oeastman"), True, False, "oeastman removed - 2 pts", 2),
		
		VulnWrap(CommandContainsVuln(["getent", "group", "sudo"], "tcharest"), True, False, "tcharest is an admin - 3 pts", 3),
		VulnWrap(CommandContainsVuln(["getent", "group", "sudo"], "vchinnam"), False, True, "vchinnam is not an admin - 2 pts", 2),
		VulnWrap(CommandContainsVuln(["getent", "group", "sudo"], "csalvatore"), False, True, "csalvatore is not an admin - 2 pts", 2),
		VulnWrap(CommandContainsVuln(["getent", "group", "sudo"], "oeastman"), False, True, "oeastman is not an admin - 2 pts", 2),
		VulnWrap(CommandContainsVuln(["getent", "group", "sudo"], "bpottepalem"), False, True, "bpottepalem is not an admin - 4 pts", 4)
	]


def getVulns():
	return [
		VulnWrap(CommandContainsVuln(["getent", "group", "sudo"], "amahajan"), False, True, "amahajan is an admin - 1 pt", 1),
		VulnWrap(CommandContainsVuln(["getent", "group", "sudo"], "fwang"), False, True, "fwang is an admin - 1 pt", 1),
		VulnWrap(CommandContainsVuln(["getent", "group", "sudo"], "smishra"), True, False, "smishra is not an admin - 2 pts", 2),

		VulnWrap(CommandContainsVuln(["cat", "/etc/passwd"], "vchinnam"), False, True, "vchinnam is authorized - 1 pt", 1),
		VulnWrap(CommandContainsVuln(["cat", "/etc/passwd"], "bpottepalem"), True, False, "bpottepalem is not authorized - 2 pts", 2),
		
		VulnWrap(FileContainsVuln("/home/jlibano/Desktop/Forensics Question 1.txt", "ANSWER: favoritegame.mp4"), False, True, "Forensics Question 1 correct - 6 pts", 6),
		VulnWrap(FileContainsVuln("/home/jlibano/Desktop/Forensics Question 2.txt", "ANSWER: 54.0"), False, True, "Forensics Question 2 correct - 6 pts", 6),
		
		VulnWrap(FileExistsVuln("/home/jlibano/Videos/favoritegame.mp4"), True, False, "Prohibited media file removed - 3 pts", 3),
		VulnWrap(FileExistsVuln("/home/jlibano/Pictures/funnymeme.png"), True, False, "Prohibited media file removed - 3 pts", 3),
		
		VulnWrap(CommandContainsVuln(["dpkg-query", "-f", "'${Package}###${Version}'", "-W"], "minetest"), True, False, "Prohibited program minetest removed - 2 pts", 2),
		VulnWrap(CommandContainsVuln(["dpkg-query", "-f", "'${Package}###${Version}'", "-W"], "nmap"), True, False, "Prohibited program nmap removed - 2 pts", 2),
		VulnWrap(CommandContainsVuln(["dpkg-query", "-f", "'${Package}###${Version}'", "-W"], "gufw"), False, True, "Installed gufw - 4 pts", 4)
	]

