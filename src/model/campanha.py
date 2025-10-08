from datetime import date
import pessoa

class Campanha:
    def __init__(self,
                 id_campanha: int = None,
                 nome: str = None,
                 descricao: str = None,
                 data_inicio: date = None,
                 data_fim: date = None,
                 usuario: pessoa = None):
        self.set_id_campanha(id_campanha),
        self.set_nome(nome),
        self.set_descricao(descricao),
        self.set_data_inicio(data_inicio),
        self.set_data_fim(data_fim)
        self.set_usuario(usuario)

def set_id_campanha(self, id_campanha: int):
    self.id_campanha = id_campanha

def set_nome(self, nome: str):
    self.nome = nome

def set_descricao(self, descricao: str):
    self.descricao = descricao

def set_data_inicio(self, data_inicio: date):
    self.data_inicio = data_inicio

def set_data_fim(self, data_fim: date):
    self.data_fim = data_fim

def set_usuario(self, usuario: pessoa):
    self.usuario = usuario



def get_id_campanha(self) -> int:
    return self.id_campanha

def get_nome(self) -> str:
    return self.nome

def get_descricao(self) -> str:
    return self.descricao

def get_data_inicio(self) -> date:
    return self.data_inicio

def get_data_fim(self)  -> date:
    return self.data_fim

def get_usuario(self) -> pessoa:
    return self.usuario




def toString(self) -> str:
    return (f"ID Campanha: {self.get_id_campanha()} | Nome: {self.get_id_campanha()} | Descrição: {self.get_descricao()} | Data de Início: {self.get_data_inicio()} | Data de Fim: {self.get_data_fim()}")