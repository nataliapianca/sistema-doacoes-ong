from conexion.connection import PostgresQueries

class SplashScreen:

    def __init__(self):
        self.created_by = "Hevellyn Monteiro \n Lorena Moreira De Nadai \n Natalia Pianca Martins \n Wanessa Silva Guisso"
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2025/2"

    def contar_registros(self, tabela: str) -> int:
        postGree = PostgresQueries()
        postGree.connect()
        try:
            query = f"SELECT COUNT(1) as total FROM {tabela}"
            df = postGree.sqlToDataFrame(query)
            total = df.total[0] if not df.empty else 0
            return total
        except Exception as e:
            print(f"Erro ao contar registros da tabela {tabela}: {e}")
            return 0

    def get_updated_screen(self):
        total_pessoas = self.contar_registros("pessoa")
        total_campanhas = self.contar_registros("campanha")
   

        return f"""
        ########################################################
        #                                                      #
        #           SISTEMA DE DOAÇÕES PARA ONG                #
        #                                                      #
        #  TOTAL DE REGISTROS:                                 #
        #     1 - PESSOAS:     {str(total_pessoas).rjust(5)}   #
        #     2 - CAMPANHAS:   {str(total_campanhas).rjust(5)} #
        #    
        # 
        #                                                       #
        #  CRIADO POR: {self.created_by}                       #
        #                                                      #
        #  PROFESSOR:  {self.professor}                        #
        #                                                      #
        #  DISCPLINA: {self.disciplina}                        #
        #             {self.semestre}                          #
        ########################################################
        """