import paramiko
import time

username = 'clara'
password = 'cFilia'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('172.21.0.6', username=username, password=password)

shell = ssh.invoke_shell()

shell.send('sudo ls /root\n')
time.sleep(1)
shell.send(password + '\n')
time.sleep(1)
output = shell.recv(1024).decode()
print(output)

time.sleep(600)

shell.close()
ssh.close()