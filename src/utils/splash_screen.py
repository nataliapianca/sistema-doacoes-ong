from conexion import conectar

class SplashScreen:

    def __init__(self):
        self.created_by = "Hevellyn Monteiro"
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2025/2"

    def contar_registros(self, tabela: str) -> int:
        conn = conectar()
        if conn is None:
            return 0

        cursor = conn.cursor()
        
        try:
            query = f"SELECT COUNT(1) FROM {tabela}"
            cursor.execute(query)
            total = cursor.fetchone()[0]
            return total
        except Exception as e:
            print(f"Erro ao contar registros da tabela {tabela}: {e}")
            return 0
        finally:
            cursor.close()
            conn.close()

    def get_updated_screen(self):
        total_pessoas = self.contar_registros("pessoas")
        total_campanhas = self.contar_registros("campanha")
        total_enderecos = self.contar_registros("endereco")

        return f"""
        ########################################################
        #                                                      #
        #           SISTEMA DE DOAÇÕES PARA ONG                #
        #                                                      #
        #  TOTAL DE REGISTROS:                                 #
        #     1 - PESSOAS:     {str(total_pessoas).rjust(5)}   #
        #     2 - CAMPANHAS:   {str(total_campanhas).rjust(5)} #
        #     3 - ENDEREÇOS:   {str(total_enderecos).rjust(5)} #
        #                                                      #
        #  CRIADO POR: {self.created_by}                       #
        #                                                      #
        #  PROFESSOR:  {self.professor}                        #
        #                                                      #
        #  DISCPLINA: {self.disciplina}                        #
        #             {self.semestre}                          #
        ########################################################
        """