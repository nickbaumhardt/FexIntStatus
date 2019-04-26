import paramiko

username = 'baumhana'
password = ''

def ssh_login(switch_ip, command, command_param):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=switch_ip,
                       username=username,
                       password=password)
    stdin, stdout, stderr = ssh_client.exec_command(f'{command}{command_param}')
    return stdout

def main():
    switch_ip = input('Switch IP: ')
    fex = input('Fex Number: ')

    stdout = ssh_login(switch_ip, 'sh int status fex ', fex)
    ssh_output = stdout.read()
    raw_output = ssh_output.decode(encoding='utf-8')
    print(raw_output)

while True:
    main()
    again = input('Would you like to get info on another FEX? <Y or N>: ')
    if again == 'Y' or again == 'y':
        continue
    else:
        exit() 
