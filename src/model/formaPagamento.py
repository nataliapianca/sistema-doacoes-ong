class FormaPagamento:
    def __init__(self,
                id_forma: int = None,
                FormaPagamento: str = None):
        self.set_id_forma(id_forma)
        self.set_FormaPagamento(FormaPagamento)

        
def set_id_forma(self, id_forma):
    self.id_forma = id_forma

def set_FormaPagamento(self, FormaPagamento: str):
    self.FormaPagamento = FormaPagamento



def get_id_forma(self):
    return self.id_forma

def get_FormaPagamento(self):
    return self.FormaPagamento


def toString(self) -> str:
    return (f"ID Forma de Pagamento: {self.get_id_forma()} | Forma de Pagamento: {self.get_FormaPagamento()}")