
def  verifica_IPs(ip1, ip2, mascara):
    ip1_sep = separa_octeto(ip1)
    ip2_sep = separa_octeto(ip2)
    mascara_sep = separa_octeto(mascara)

    end_rede1 = op_end(ip1_sep, mascara_sep)
    end_rede2 = op_end(ip2_sep, mascara_sep)
    
    if end_rede1 == end_rede2:
        return True
    else:
        return False 
  
def op_end(ip, mascara):
    end_rede = []
    for x in range(len(ip)):
        if ip[x] == 1 and mascara[x] == 1:
            end_rede.append(1)
        else:
            end_rede.append(0)
    return end_rede

def separa_octeto(valor):
    ip1_numero = valor.split('.')
    octeto1 = int(ip1_numero[0])
    octeto2 = int(ip1_numero[1])
    octeto3 = int(ip1_numero[2])
    octeto4 = int(ip1_numero[3])

    binario = list(decimal_binario(octeto1)) + list(decimal_binario(octeto2)) + list(decimal_binario(octeto3)) + list(decimal_binario(octeto4))

    return binario

def decimal_binario(octeto):
    if octeto == 0:
        return '0'
    elif octeto == 1:
        return '1'
    else:
        return decimal_binario(octeto//2) + str(octeto % 2)

    '''oc1 = bin(octeto1) [2:]
    oc2 = bin(octeto2) [2:]
    oc3 = bin(octeto3) [2:]
    oc4 = bin(octeto4) [2:]
    str(oc1)
    str(oc2)
    str(oc3)
    str(oc4)

    binario = list(oc1) + list(oc2) + list(oc3) + list(oc4)

    return binario'''

    
ip1 = input()     
ip2 = input()     
mascara = input()  
print(verifica_IPs(ip1, ip2, mascara))
