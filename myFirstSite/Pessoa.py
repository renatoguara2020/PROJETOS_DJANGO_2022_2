class Pessoa:
    def __init__(self, nome, sexo, cpf):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf


if __name__ == "__main__":
    pessoa1 = Pessoa("RENATO ALVES SOARES", "Masculino", "489.708.933.89")

    print(pessoa1.nome)
    print(pessoa1.cpf)
    print(pessoa1.sexo)
