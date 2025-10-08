import campanha
import formaPagamento

class CampanhaFormaPagamento:
    def __init__(self,
                id_campanha: campanha = None,
                id_formaPagamento: formaPagamento = None
                ):
        self.set_id_campanha(id_campanha),
        self.set_id_formaPagamento(id_formaPagamento)

def set_id_campanha(self, id_campanha: campanha):
    self.id_campanha = id_campanha

def set_id_formaPagamento(self, id_formaPagamento: formaPagamento):
    self.id_formaPagamento = id_formaPagamento


def get_id_campanha(self) -> campanha:
    return self.id_campanha

def get_id_formaPagamento(self) -> formaPagamento:
    return self.id_formaPagamento


def toString(self) -> str:
    return (f"ID Campanha: {self.get_id_campanha()} | ID Forma de Pagamento: {self.get_id_formaPagamento}")
