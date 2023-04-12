students = {
    'João':{
        'Idade': 18,
        'Cidade': 'São Paulo',
        'notas': [7.5, 8.0, 9.0]
        
    },
    'Maria': {
        'Idade': 20,
        'Cidade': 'Rio de Janeiro',
        'notas': [6.5, 7.0, 8,.5]
    },
    'Pedro': {
        'Idade': 19,
        'Cidade': 'Belo Horizonte',
        'notas': [8.0,8.5,9.5]
    }
    
}

#Imprimir a idade de João
print('A idade de João é: ' + str(students['João']['Idade']))
#Adicionar uma nova nota para Maria
students['Maria']['notas'].append(9.0)
#Imprimir todas as informações dos alunos
for student, info in students.items():
    print(student + ':')
    print('Idade: ' + str(info['Idade']))
    print('Cidade: ' + info['Cidade'])
    print('Notas: ' + str(info['notas']))
    print('Média: ' + str(sum(info['notas']) / len(info['notas'])))