import os

def syn_scan(ip:str, ports:list=None, declared:list=None):
    if declared == None:
        return (syn_scan_inter(ip, ports), True)
    else:
        rports = syn_scan_inter(ip, ports)
        is_declare_true = set(declared).issubset(rports)
        return (rports, is_declare_true)

def syn_scan_inter(ip, ports=None):
    if ports != None:
            out = os.popen("nmap -T5 -Pn {} -p {} --open | grep open | awk '{{ print $1 }}' | grep tcp | cut -d '/' -f1".format(ip, ",".join(ports))).read()
            return list(map(int, out.split()))

    else:
        out = os.popen("nmap -T5 -Pn {} --open | grep open | awk \'{{ print $1 }}' | grep tcp | cut -d '/' -f1".format(ip)).read()
        return list(map(int, out.split()))
