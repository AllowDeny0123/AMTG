from nmapmode import syn_scan
from attacks import Attacks

class Attacker:
    def __init__(self, target:str, ports:list[int]=None):
        print(f"Target {target} locked!")
        self.target = target
        if ports != None:
            self.ports = ports
        else:
            self.ports = None

    def ensure_declared_ports(self):
        ports, is_declared_true = syn_scan(self.target, declared=self.ports)
        if self.ports:
            if is_declared_true == False:
                self.ports = list(set(self.ports) & set(ports))
        else:
            self.ports = ports

    def select_attack(self):
        self.ensure_declared_ports()
        self.possible_attacks = []
        for i in self.ports:
            try:
                self.possible_attacks.append((Attacks._KNOWN_ATTACK_METHODS[str(i)], i))
            except KeyError:
                continue
    
    def attack(self):
        self.select_attack()
        for i, p in self.possible_attacks:
            for j in i:
                print(f"Attacking {self.target}:{p}")
                j(self.target, p)
