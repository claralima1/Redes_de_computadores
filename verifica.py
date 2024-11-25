import re

class Verifica:
    def __init__(self, ip1, ip2, mascara):
        self.ip1 = ip1
        self.ip2 = ip2
        self.mascara = mascara

    def set_mascara(self, m):
        self.mascara = m

    def set_ip1(self, m):
        self.mascara = m

    def set_ip2(self, m):
        self.ip2 = m

    def get_mascara(self):
        return self.mascara
    
    def get_ip1(self):
        return self.ip1
    
    def get_ip2(self):
        return self.ip2
    

    

    

