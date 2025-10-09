from datetime import date
import pessoa

class Campanha:
    def __init__(self,
                 id_campanha: int = None,
                 pessoa: pessoa = None,
                 nome: str = None,
                 descricao: str = None,
                 data_inicio: date = None,
                 data_fim: date = None,
                 status: bool = None,
                 formaPagamento: str = None
                ):
        self.set_id_campanha(id_campanha),
        self.set_pessoa(pessoa.get_pessoa() if pessoa else None),
        self.set_nome(nome),
        self.set_descricao(descricao),
        self.set_data_inicio(data_inicio),
        self.set_data_fim(data_fim)
       

def set_id_campanha(self, id_campanha: int):
    self.id_campanha = id_campanha
    
def set_pessoa(self, pessoa: pessoa):
    self.pessoa = pessoa

def set_nome(self, nome: str):
    self.nome = nome

def set_descricao(self, descricao: str):
    self.descricao = descricao

def set_data_inicio(self, data_inicio: date):
    self.data_inicio = data_inicio

def set_data_fim(self, data_fim: date):
    self.data_fim = data_fim

def set_status(self, status: bool):
    self.status = status

def set_formaPagamento(self, formaPagamento: str):
    self.formaPagamento = formaPagamento



def get_id_campanha(self) -> int:
    return self.id_campanha

def get_pessoa(self) -> pessoa:
    return self.pessoa

def get_nome(self) -> str:
    return self.nome

def get_descricao(self) -> str:
    return self.descricao

def get_data_inicio(self) -> date:
    return self.data_inicio

def get_data_fim(self)  -> date:
    return self.data_fim

def is_ativa(self) -> bool:
    return self.status

def get_formaPagamento(self) -> str:
    return self.formaPagamento


def toString(self) -> str:
    return (f"Campanha: {self.get_id_campanha()} | Pessoa Responsável: {self.get_pessoa()} | Nome: {self.get_nome()} | Descrição: {self.get_descricao()} | Data de Início: {self.get_data_inicio()} | Data de Fim: {self.get_data_fim()} | Ativa: {self.is_ativa()} | Forma de Pagamento aceita: {self.getformaPamento()}")