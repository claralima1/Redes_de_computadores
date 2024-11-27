import re
import json

class Verifica:
    def __init__(self, id, ip1, ip2, mascara):
        self.id = id
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
    
    def verifica_IPs(self, ip1, ip2, mascara):
    
        if not self.valida_ip(ip1) or not self.valida_ip(ip2) or not self.valida_ip(mascara):
            return "Erro: IP ou máscara inválidos."
    
        self.ip1_sep = self.separa_octeto(ip1)
        self.ip2_sep = self.separa_octeto(ip2)
        self.mascara_sep = self.separa_octeto(mascara)

   
        self.end_rede1 = self.op_end(self.ip1_sep, self.mascara_sep)
        self.end_rede2 = self.op_end(self.ip2_sep, self.mascara_sep)
        
    
        if self.end_rede1 == self.end_rede2:
            return "Os IPs pertencem à mesma rede."
        else:
            return "Os IPs NÃO pertencem à mesma rede."
    
    def op_end(self, ip, mascara):

        end_rede = []
        for i in range(len(ip)):
        
            end_rede.append(int(ip[i]) & int(mascara[i]))
        return end_rede
    
    def separa_octeto(self, valor):
    
        ip1_numero = valor.split('.')
        binario = ''
        for octeto in ip1_numero:
            binario += self.decimal_binario(int(octeto)).zfill(8)  # Completa com zeros à esquerda para 8 bits
        return list(binario)  # Retorna uma lista de caracteres (0 e 1)

    def decimal_binario(self, octeto):
    
        if octeto == 0:
            return '0'
        elif octeto == 1:
            return '1'
        else:
            return self.decimal_binario(octeto // 2) + str(octeto % 2)
        
    def valida_ip(self, ip):

    #Valida se o IP é no formato correto (4 octetos entre 0 e 255).
    
        regex_ip = r'^([0-9]{1,3}\.){3}[0-9]{1,3}$'
        if re.match(regex_ip, self.ip):
            octetos = self.ip.split('.')
            # Verifica se cada octeto está no intervalo de 0 a 255
            for octeto in octetos:
                if not (0 <= int(octeto) <= 255):
                    return False
            return True
        return False
        
    

    
    def __str__(self):
        return f"IP 1: {self.ip1}\nIP 2: {self.ip2}\nMask: {self.mascara}"
    
class persistencia:

    objetos = []               
    @classmethod
    def inserir(cls, obj):     
        cls.abrir()             
        id = 0                 
        for x in cls.objetos:
            if x.id > id: id = x.id
        id += 1    
        obj.id = id             
        cls.objetos.append(obj) 
        cls.salvar()            
    @classmethod
    def listar(cls):           
        cls.abrir()
        return cls.objetos  
    @classmethod
    def listar_id(cls, id):           
        cls.abrir() 
        for x in cls.objetos: 
            if x.id == id: return x
        return None      
    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.id) 
        if x != None:
            x.ip1 = obj.ip1
            x.ip2 = obj.ip2
            x.mascara = obj.mascara
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.id) 
        if x != None: 
            cls.objetos.remove(x)
            cls.salvar()
            
    @classmethod
    def salvar(cls):    
        with open("../verif.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)
    @classmethod
    def abrir(cls):
        cls.objetos = []
    
        try:
          with open("../verif.json", mode="r") as arquivo:
              texto_arquivo = json.load(arquivo)
              for obj in texto_arquivo:
                  c = Verifica(obj["id"], obj["ip1"], obj["ip2"], obj["mascara"])
                  cls.objetos.append(c)
        except FileNotFoundError:
          pass   

    

    

