class Pessoa:
    def __init__(self, nome = None, idade = None, sexo = None   ):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
    def cumprimentar(self):
        return f'Olá '
if __name__ == '__main__':
    p = Pessoa('João',56)
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'César'
    p.sexo = 'M'
    print(p.cumprimentar(),p.nome, p.idade, p.sexo)
    print ('Teste de commit', 3)