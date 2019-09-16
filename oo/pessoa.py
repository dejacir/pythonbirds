class Pessoa:
    def __init__(self,  *filhos, nome=None, idade=47):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    elias = Pessoa(nome='Elias')
    calebe = Pessoa(nome='Calebe')
    debora = Pessoa(nome='Débora')
    dyhellen = Pessoa(nome='Dyhellen')
    dejacir = Pessoa(elias, calebe, debora, dyhellen,  nome='Dejacir')
    print(Pessoa.cumprimentar(dejacir))
    print(id(dejacir))
    print(dejacir.cumprimentar())
    print(dejacir.nome)
    print(dejacir.idade)
    for filho in dejacir.filhos:
        print(filho.nome)
    dejacir.sobrenome = 'Marques'
    del dejacir.filhos
    print(dejacir.__dict__)
    print(elias.__dict__)








