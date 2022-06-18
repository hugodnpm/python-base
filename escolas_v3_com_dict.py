#!/usr/bin/env python3

''' Exibir relatório de crianças por atividade

Imprimir a lista de crianças agrupadas por sala que frequanta cada atividade.
'''
__version__="0.0.0"
__author__='Hugo Carvalho'

#Dados
sala = { 
    1: ['Erick', 'Maia', 'Gustavo', 'Manuel', 'Sofia', 'Joana'],
    2: ['Joao', 'Antonio', 'Carlos', 'Maria', 'Isolda']
}


#sala_1=['Erick', 'Maia', 'Gustavo', 'Manuel', 'Sofia', 'Joana']
#sala_2=['Joao', 'Antonio', 'Carlos', 'Maria', 'Isolda']
#aula_ingles=['Erick','Maia','Joana', 'Carlos','Antonio']
#aula_musica=['Erick','Erick','Maria']
#aula_danca=['Gustavo','Sofia','Joana','Antonio']
aula = {
    "ingles": ['Erick','Maia','Joana', 'Carlos','Antonio'],
    "musica": ['Erick','Erick','Maria'],
    "danca":['Gustavo','Sofia','Joana','Antonio']
}
#atividades = [
#('Inglês',aula_ingles),
#('Música',aula_musica),
#('Dança',aula_danca),
#]

atividades = {
    "Ingles": aula["ingles"],
    "Musica": aula["musica"],
    "Danca": aula["danca"]
}
#Listar alunos em cada atividade por sala
print(f"Aula Inglês", atividades["Ingles"])
#for nome_atividade, atividade in atividades:
#    atividade_sala1 = set(sala_1) & set(atividade)
#    atividade_sala2 = set(sala_2).intersection(atividade)

#    print("Sala1", atividade_sala1)
#    print("Sala2", atividade_sala2)
    

   # for aluno in atividade:
       # if aluno in sala_1:
           #atividade_sala1.append(aluno)
       # elif aluno in sala_2:
           # atividade_sala2.append(aluno)

   # print(f"A aula de {nome_atividade} da Sala 1:", atividade_sala1)
   # print(f"A aula de {nome_atividade} da Sala 2:", atividade_sala2)
   # print('-' *30)
