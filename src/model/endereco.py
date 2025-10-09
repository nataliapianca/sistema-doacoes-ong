class Endereco:
    def __init__(self,
                 id_endereco: int = None,
                 id_pessoa: int = None,
                 logradouro: str = None,
                 numero: str = None,
                 complemento: str = None,
                 bairro: str = None,
                 cidade: str = None,
                 estado: str = None,
                 cep: str = None):
        self.set_id_endereco(id_endereco)
        self.set_id_pessoa(id_pessoa)
        self.set_logradouro(logradouro)
        self.set_numero(numero)
        self.set_complemento(complemento)
        self.set_bairro(bairro)
        self.set_cidade(cidade)
        self.set_estado(estado)
        self.set_cep(cep)

    def set_id_endereco(self, id_endereco: int):
        self.id_endereco = id_endereco

    def set_id_pessoa(self, id_pessoa: int):
        self.id_pessoa = id_pessoa

    def set_logradouro(self, logradouro: str):
        self.logradouro = logradouro

    def set_numero(self, numero: str):
        self.numero = numero

    def set_complemento(self, complemento: str):
        self.complemento = complemento

    def set_bairro(self, bairro: str):
        self.bairro = bairro

    def set_cidade(self, cidade: str):
        self.cidade = cidade

    def set_estado(self, estado: str):
        if estado is not None and len(estado) != 2:
            raise ValueError("O estado deve ter 2 caracteres (ex: 'SP', 'RJ').")
        self.estado = estado.upper() if estado else None

    def set_cep(self, cep: str):
        if cep is not None and len(cep) != 8:
            raise ValueError("O CEP deve ter exatamente 8 dígitos.")
        self.cep = cep


    def get_id_endereco(self) -> int:
        return self.id_endereco

    def get_id_pessoa(self) -> int:
        return self.id_pessoa

    def get_logradouro(self) -> str:
        return self.logradouro

    def get_numero(self) -> str:
        return self.numero

    def get_complemento(self) -> str:
        return self.complemento

    def get_bairro(self) -> str:
        return self.bairro

    def get_cidade(self) -> str:
        return self.cidade

    def get_estado(self) -> str:
        return self.estado

    def get_cep(self) -> str:
        return self.cep

 
    def to_string(self) -> str:
        return (f"ID Endereço: {self.get_id_endereco()} | Pessoa: {self.get_id_pessoa()} | "
                f"{self.get_logradouro()}, {self.get_numero()} - {self.get_bairro()} - "
                f"{self.get_cidade()}/{self.get_estado()} | CEP: {self.get_cep()}")
