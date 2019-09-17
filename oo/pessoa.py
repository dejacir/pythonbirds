class Pessoa:
    olhos = 2

    def __init__(self,  *filhos, nome=None, idade=47):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

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
    dejacir.olhos = 1
    del dejacir.olhos
    print(dejacir.__dict__)
    print(elias.__dict__)
    print(calebe.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(dejacir.olhos)
    print(elias.olhos)
    print(id(Pessoa.olhos), id(dejacir.olhos), id(elias.olhos))
    print(Pessoa.metodo_estatico(), dejacir.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), dejacir.nome_e_atributos_de_classe())











