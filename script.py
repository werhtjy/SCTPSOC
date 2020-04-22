import socket
import subprocess
import os

ending = True

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("gmail.com",80))
adress=s.getsockname()[0]
s.close()
port = "5201"

#with open("tmp.txt","w+") as f_out:
proc = subprocess.Popen(["sctp_darn","-H",adress,"-P",port,"--listen"], shell=False)
while ending:
	out = subprocess.check_output(['sudo', 'tshark', '-i', 'ens33', '-c', '2', '-f', "sctp and port " + port, '-V'])
	out=str(out)
	#os.system("echo '{}'>> tmp.txt".format(out))
	index = out.find("Data: ")
	s_index = out.find("[Length:",index)
	out = str(out[index+6:s_index])
	out=out.strip()
	out = str(out)[:-4]
	#os.system("echo '{}'>> tmp.txt".format(out))
	out = bytes.fromhex(out).decode('utf-8')
	#os.system("echo '{}'>> tmp.txt".format(out))
	if(out != ''):
		if 'close' in out:
			ending = False
		else:
			os.system("echo '{}'>> tmp.txt".format(out.strip()))
#				f_out.write(str(out)+"\n")

proc.terminate()
#, '-T', 'fields', '-e', 'data.data'
#, '-T', 'fields', '-e', 'data.data'


#, '-T', 'fields', '-e', 'data.data'
