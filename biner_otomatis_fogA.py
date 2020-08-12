from datetime import datetime
import operator
import random
import socket

#main
ip2 ='192.168.43.207'
#ip2 = map_network.ip()
#print (ip2)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip2,8080))
ops = {'&':operator.and_}
ops1 = {'|':operator.or_}
ops2 = {'^':operator.xor}
num1 = random.randint(10,99)
num2 = random.randint(10,99)
#bits = '1111111'
#binum1= bin(num1)[2:]
#binum2= bin(num2)[2:]
#binernum1 = '{0:0{1}b}'.format(int(num1),len(bits))
#binernum2 = '{0:0{1}b}'.format(int(num2),len(bits))
#print(num1)
#print(num2)
op = random.choice(list(ops.keys()))
op1 = random.choice(list(ops1.keys()))
op2= random.choice(list(ops2.keys()))
answer = ops.get(op)(int(num1),int(num2))
answer1 = ops1.get(op1)(int(num1),int(num2))
answer2 = ops2.get(op2)(int(num1),int(num2))
#jawabanA = '{0:0{1}b}'.format(answer,len(bits))
#jawabanB = '{0:0{1}b}'.format(answer1,len(bits))
#jawabanC = '{0:0{1}b}'.format(answer2,len(bits))
a= datetime.now().strftime('%M')
print('pemberian challenge response pada menit {} '.format(a))
if a<='20':
	print ("maka masuk pada sesi 1")
	#print(jawabanA)
	soal = ('selesaikan {} {} {} ?\n'.format(num1, op, num2))
	s.send(soal)
	jawaban = s.recv(1024)
	if  str(answer)== str(jawaban):
		respon = ("jawaban anda benar")
		s.send(respon)
		print("mulai tersambung dengan fog B")
	else :
		respon= ("jawaban anda salah")
		s.send(respon)
		print("gagal terhubung dengan fog B")
elif a<='40':
	print("maka masuk pada sesi 2")
	#print(jawabanB)
	soal1 = ('selesaikan  {} {} {} ?\n'.format(num1, op1, num2))
	s.send(soal1)
	jawaban = s.recv(1024)
	if str(jawaban) == str(answer1):
		respon = ("jawaban anda benar")
		s.send(respon)
		print("mulai tersambung dengan fog B")
	else :
		respon= ("jawaban anda salah")
		s.send(respon)
		print("gagal terhubung dengan fog B")
elif a<='59':
	print("maka masuk pada sesi 3")
	#print(jawabanC)
	soal2 = ('selesaikan  {} {} {} ?\n'.format(num1, op2, num2))
	s.send(soal2)
	jawaban = s.recv(1024)
	if str(jawaban) == str(answer2):
		respon = ("jawaban anda benar")
		s.send(respon)
		print("mulai tersambung dengan fog B")
	else :
		respon= ("jawaban anda salah")
		s.send(respon)
		print("gagal terhubung dengan fog B")

#s.close()
