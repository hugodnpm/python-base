#!/usr/bin/env python3

''' Exibir relatório de crianças por atividade

Imprimir a lista de crianças agrupadas por sala que frequanta cada atividade.
'''
__version__="0.0.0"
__author__='Hugo Carvalho'

#Dados
sala_1=['Erick', 'Maia', 'Gustavo', 'Manuel', 'Sofia', 'Joana']
sala_2=['Joao', 'Antonio', 'Carlos', 'Maria', 'Isolda']
aula_ingles=['Erick','Maia','Joana', 'Carlos','Antonio']
aula_musica=['Erick','Erick','Maria']
aula_danca=['Gustavo','Sofia','Joana','Antonio']

atividades = [
('Inglês',aula_ingles),
('Música',aula_musica),
('Dança',aula_danca),
]

#Listar alunos em cada atividade por sala
for nome_atividade, atividade in atividades:
    atividade_sala1 = []
    atividade_sala2 = []

    for aluno in atividade:
        if aluno in sala_1:
            atividade_sala1.append(aluno)
        elif aluno in sala_2:
            atividade_sala2.append(aluno)

    print(f"A aula de {nome_atividade} da Sala 1:", atividade_sala1)
    print(f"A aula de {nome_atividade} da Sala 2:", atividade_sala2)
    print('-' *30)
