class Pessoa:
    def __init__(self, *filhos, nome=None, idade=None, sexo=None):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá '
if __name__ == '__main__':
    rafael = Pessoa(nome='rafael',idade=27,sexo='m')
    joao = Pessoa(rafael, nome='João', idade=56, sexo='m')
    jurandyr = Pessoa(joao,nome='jurandyr',idade=90,sexo='m')
    print(Pessoa.cumprimentar(joao))
    print(id(joao))
    print(jurandyr.cumprimentar())
    print(jurandyr.nome)
    print(jurandyr.filhos)
    for filho in jurandyr.filhos:
        print (filho.nome)




