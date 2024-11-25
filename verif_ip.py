import re

def verifica_IPs(ip1, ip2, mascara):
    
    if not valida_ip(ip1) or not valida_ip(ip2) or not valida_ip(mascara):
        return "Erro: IP ou máscara inválidos."
    
    ip1_sep = separa_octeto(ip1)
    ip2_sep = separa_octeto(ip2)
    mascara_sep = separa_octeto(mascara)

   
    end_rede1 = op_end(ip1_sep, mascara_sep)
    end_rede2 = op_end(ip2_sep, mascara_sep)
    
  
    if end_rede1 == end_rede2:
        return "Os IPs pertencem à mesma rede."
    else:
        return "Os IPs NÃO pertencem à mesma rede."
  
def op_end(ip, mascara):
    end_rede = []
    for i in range(len(ip)):
       
        end_rede.append(int(ip[i]) & int(mascara[i]))
    return end_rede

def separa_octeto(valor):
    
    ip1_numero = valor.split('.')
    binario = ''
    for octeto in ip1_numero:
        binario += decimal_binario(int(octeto)).zfill(8)  # Completa com zeros à esquerda para 8 bits
    return list(binario)  # Retorna uma lista de caracteres (0 e 1)

def decimal_binario(octeto):
    
    if octeto == 0:
        return '0'
    elif octeto == 1:
        return '1'
    else:
        return decimal_binario(octeto // 2) + str(octeto % 2)

def valida_ip(ip):
    """
    Valida se o IP é no formato correto (4 octetos entre 0 e 255).
    """
    regex_ip = r'^([0-9]{1,3}\.){3}[0-9]{1,3}$'
    if re.match(regex_ip, ip):
        octetos = ip.split('.')
        # Verifica se cada octeto está no intervalo de 0 a 255
        for octeto in octetos:
            if not (0 <= int(octeto) <= 255):
                return False
        return True
    return False


ip1 = input("Digite o primeiro IP: ")     
ip2 = input("Digite o segundo IP: ")     
mascara = input("Digite a máscara de rede: ")  

# Exibe o resultado da verificação de rede
resultado = verifica_IPs(ip1, ip2, mascara)
print(resultado)
