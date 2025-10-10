from model.campanha import Campanha
from model.pessoa import Pessoa


class FormaPagamento:
    def __init__(self,
                id_forma: int = None,
                campanha: Campanha = None,
                pessoa: Pessoa = None,
                formaPagamento: str = None):
        self.set_id_forma(id_forma)
        self.set_campanha(campanha)
        self.set_FormaPagamento(formaPagamento)
        self.set_pessoa(pessoa)
        
def set_id_forma(self, id_forma: int):
    self.id_forma = id_forma

def set_campanha(self, campanha: Campanha):
    self.campanha = campanha

def set_pessoa(self, pessoa: Pessoa):
    self.pessoa = pessoa

def set_FormaPagamento(self, formaPagamento: str):
    self.formaPagamento = formaPagamento



def get_id_forma(self):
    return self.id_forma

def get_campanha(self) -> Campanha:
    return self.campanha

def get_pessoa(self) -> Pessoa:
    return self.pessoa

def get_FormaPagamento(self):
    return self.FormaPagamento


def toString(self) -> str:
    return (f"Forma de Pagamento: {self.get_id_forma()} | Forma de Pagamento: {self.get_FormaPagamento()} | Campanha: {self.campanha.get_descricao()} | Pessoa: {self.pessoa.get_nome}")