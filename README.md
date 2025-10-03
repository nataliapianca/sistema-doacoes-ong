<h1 align="center">🌟 Sistema de Doações para ONG 🌟</h1> <p align="center"> <i>Um sistema simples e organizado pra gerenciar doações, doadores e relatórios, com CRUD completo e interface amigável.</i> </p>






diarama de relacionamentos@startuml
title Diagrama de Classes - Sistema de Doações

' ======= Classes principais =======

class Pessoa {
  +id_pessoa : int
  +nome : string
  +cpf : string
  +email : string
  +senha : string
  +perfil : string = "doador"
  +tipo_pessoa : string <<{doador, usuario}>>
}

class Endereco {
  +id_endereco : int
  +logradouro : string
  +numero : string
  +complemento : string
  +bairro : string
  +cidade : string
  +estado : string
  +cep : string
}

class StatusCampanha {
  +id_status : int
  +descricao : string
}

class Campanha {
  +id_campanha : int
  +nome : string
  +descricao : text
  +data_inicio : date
  +data_fim : date
}

class FormaPagamento {
  +id_forma : int
  +descricao : string
}

class TipoDoacao {
  +id_tipo : int
  +descricao : string
}

class Doacao {
  +id_doacao : int
  +valor : decimal
  +data_doacao : timestamp
}

class Recibo {
  +id_recibo : int
  +data_emissao : timestamp
  +codigo_validacao : uuid
}

class CampanhaTipoDoacao {
}

class CampanhaFormaPagamento {
}

class FavoritoCampanha {
  +data_favorito : timestamp
}

class VoluntarioCampanha {
  +funcao : string
  +data_entrada : timestamp
}

' ======= Relacionamentos =======

Pessoa "1" -- "0..*" Endereco : possui >
Pessoa "1" -- "0..*" Campanha : cria >
Pessoa "1" -- "0..*" Doacao : realiza >
Pessoa "1" -- "0..*" FavoritoCampanha
Pessoa "1" -- "0..*" VoluntarioCampanha

Campanha "1" -- "0..*" Doacao : recebe >
Campanha "1" -- "0..*" CampanhaTipoDoacao
Campanha "1" -- "0..*" CampanhaFormaPagamento
Campanha "1" -- "0..*" FavoritoCampanha
Campanha "1" -- "0..*" VoluntarioCampanha

StatusCampanha "1" -- "0..*" Campanha : classifica >

Doacao "1" -- "1" Recibo : gera >

FormaPagamento "1" -- "0..*" Doacao
TipoDoacao "1" -- "0..*" Doacao
TipoDoacao "1" -- "0..*" CampanhaTipoDoacao
FormaPagamento "1" -- "0..*" CampanhaFormaPagamento

@enduml


LINK DO  DOCUMENTO COM DIAGRAMAS:
https://edufaesa-my.sharepoint.com/:w:/g/personal/wanessa_guisso_aluno_faesa_br/EcRyt9IhPa5Bjfc0YuKg46IBqT6JCLd7ZAwy9UUCmUsgTQ?e=hesadx


