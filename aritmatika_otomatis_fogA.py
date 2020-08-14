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
ops = {'+':operator.add}
ops1 = {'-':operator.sub}
ops2 = {'*':operator.mul}
ops3 = {'%':operator.mod}
num1 = random.randint(1,100)
num2 = random.randint(1,100)  
op = random.choice(list(ops.keys()))
op1 = random.choice(list(ops1.keys()))
op2= random.choice(list(ops2.keys()))
op3= random.choice(list(ops3.keys()))
answer = ops.get(op)(num1,num2)
answer1 = ops1.get(op1)(num1,num2)
answer2 = ops2.get(op2)(num1,num2)
answer3 = ops3.get(op3)(num1,num2)
a= datetime.now().strftime('%M')
print('pemberian challenge response pada menit {} '.format(a))
if a<='15':
	print ("maka masuk pada sesi 1")
	soal = ('berapa hasil operasi perhitungan  {} {} {} ?\n'.format(num1, op, num2))
	s.send(soal)
	jawaban = s.recv(1024)
	if jawaban == str(answer):
		respon = ("jawaban anda benar")
		s.send(respon)
		print("mulai tersambung dengan Fog B")
	else :
		respon= ("jawaban anda salah")
		s.send(respon)
		print("gagal terhubung dengan Fog B")
elif a<='30':
	print("maka masuk pada sesi 2")
	soal1 = ('berapa hasil operasi perhitungan  {} {} {} ?\n'.format(num1, op1, num2))
	s.send(soal1)
	jawaban = s.recv(1024)
	if jawaban == str(answer1):
		respon = ("jawaban anda benar")
		s.send(respon)
		print("mulai tersambung dengan Fog B")
	else :
		respon= ("jawaban anda salah")
		s.send(respon)
		print("gagal terhubung dengan Fog B")
elif a<='45':
	print("maka masuk pada sesi 3")
	soal2 = ('berapa hasil operasi perhitungan  {} {} {} ?\n'.format(num1, op2, num2))
	s.send(soal2)
	jawaban = s.recv(1024)
	if jawaban == str(answer2):
		respon = ("jawaban anda benar")
		s.send(respon)
		print("mulai tersambung dengan Fog B")
	else :
		respon= ("jawaban anda salah")
		s.send(respon)
		print("gagal terhubung dengan Fog B")
elif a<='59':
	print("maka masuk pada sesi 4")
	soal3 = ('berapa hasil operasi perhitungan  {} {} {} ?\n'.format(num1, op3, num2))
	s.send(soal3)
	jawaban = s.recv(1024)
	if jawaban == str(answer3):
		respon = ("jawaban anda benar")
		s.send(respon)
		print("mulai tersambung dengan Fog B")
	else :
		respon= ("jawaban anda salah")
		s.send(respon)
		print("gagal terhubung dengan Fog B")
