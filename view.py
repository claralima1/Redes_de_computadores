from models.verifica import Verifica

class View:

    @staticmethod
    def inserir(ip1:str, ip2:str, mascara:str):
        c = Verifica(0, ip1, ip2, mascara)
        Verifica.inserir(c)
    @staticmethod
    def listar():
        return Verifica.listar()
    @staticmethod
    def listar_id(id:int):
        return Verifica.listar_id(id)
    @staticmethod
    def atualizar(id:int, ip1:str, ip2:str, mascara:str):
        c = Verifica(id, ip1, ip2, mascara)
        Verifica.atualizar(c)
    @staticmethod
    def excluir(id:int):
        c = Verifica(id, "", "", "")
        Verifica.excluir(c)
