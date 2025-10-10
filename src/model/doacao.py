from decimal import Decimal
from datetime import datetime
from recibo import Recibo


class Doacao:
    def __init__(
        self,
        id_doacao: int = None,
        id_pessoa: int = None,
        id_campanha: int = None,
        valor: Decimal = None,
        data_doacao: datetime = None,
        recibo: Recibo = None
    ):
        self.set_id_doacao(id_doacao)
        self.set_id_pessoa(id_pessoa)
        self.set_id_campanha(id_campanha)
        self.set_valor(valor)
        self.set_data_doacao(data_doacao)

    def set_id_doacao(self, id_doacao: int):
        self._id_doacao = id_doacao

    def set_id_pessoa(self, id_pessoa: int):
        self._id_pessoa = id_pessoa

    def set_id_campanha(self, id_campanha: int):
        self._id_campanha = id_campanha

    def set_valor(self, valor: Decimal):
        self._valor = Decimal(valor) if valor is not None else None

    def set_data_doacao(self, data_doacao: datetime):
        if data_doacao is None:
            self.data_doacao = datetime.now()  # define data atual se não for passada
        else:
            self.data_doacao = data_doacao

    def get_id_doacao(self):
        return self._id_doacao

    def get_id_pessoa(self):
        return self._id_pessoa

    def get_id_campanha(self):
        return self._id_campanha

    def get_valor(self):
        return self._valor

    def get_data_doacao(self):
        return self._data_doacao

    #toString
    def to_str(self):
        return (f"Doação:id={self._id_doacao}, pessoa={self._id_pessoa}, "
                f"campanha={self._id_campanha}, valor=R${self._valor}, "
                f"data={self._data_doacao.strftime('%d/%m/%Y %H:%M:%S')})")
