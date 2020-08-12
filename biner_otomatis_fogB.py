import socket
import datetime

import socket    
import operator

class Timer(object):
    """A simple timer class"""
    
    def __init__(self):
        pass
    def start(self):
        """Starts the timer"""
        self.start = datetime.datetime.now()
    def stop(self):
        """Stops the timer.  Returns the time elapsed"""
        self.stop = datetime.datetime.now()
        print str(self.stop - self.start)
    def elapsed(self):
        """Time elapsed since start was called"""
        print str(datetime.datetime.now() - self.start)[:-1]
    def now(self):
	print str(datetime.datetime.now())[:-3]

#main
watch=Timer()
s = socket.socket()
port=8080
ip =''
s.bind(('',port))
s.listen(5)
soc, client_address = s.accept()
watch.start()
soal = soc.recv(1024)
watch.elapsed()#capture waktu
print (soal)
watch.elapsed()#capture waktu	
print ('jawabannya  ' )
#jawaban= ''
char1 = soal[12]
char2 = soal[13]
char3 = soal[17]
char4 = soal[18]
combine1 = char1 + char2
combine2 = char3 + char4
operasi = soal[15]
#print (char1)
if operasi == '&':
	jawaban = int(combine1) & int(combine2)	
	print(jawaban)
	soc.send(str(jawaban))
	watch.elapsed()#capture waktu
	respon = soc.recv(1024)
	watch.elapsed()#capture waktu
	print(respon)
	pem = ("jawaban anda benar")
	if respon == pem :
		print("mulai terhubung dengan Fog A")
		watch.elapsed()#capture waktu
		soc.close()
	else :
		print("gagal terhubung dengan Fog A")
		soc.close()
elif operasi == '|':
	jawaban = int(combine1) | int(combine2)
	print(jawaban)
	soc.send(str(jawaban))
	watch.elapsed()#capture waktu
	respon = soc.recv(1024)
	watch.elapsed()#capture waktu
	print(respon)
	pem = ("jawaban anda benar")
	if respon == pem :
		print("mulai terhubung dengan Fog A")
		watch.elapsed()#capture waktu
		soc.close()
	else :
		print("gagal terhubung dengan Fog A")
		soc.close()
elif operasi == '^':
	jawaban = int(combine1) ^ int(combine2)
	print(jawaban)
	soc.send(str(jawaban))
	watch.elapsed()#capture waktu
	respon = soc.recv(1024)
	watch.elapsed()#capture waktu
	print(respon)
	pem = ("jawaban anda benar")
	if respon == pem :
		print("mulai terhubung dengan Fog A")
		watch.elapsed()#capture waktu
		soc.close()
	else :
		print("gagal terhubung dengan Fog A")
		soc.close()
