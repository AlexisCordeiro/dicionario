agenda = {}

while True:
    nome = input('Digite o nome da pessoa: ')
    if nome == '':
        break
    
    telefone = input('Digite o telefone: ')
    
    # Adicione o telefone ao dicionario
    agenda[nome] = telefone
    
#Pesquisa em telefone na agenda 
nome_pesquisa = input('Digite o nome para pesquisar: ')
if nome_pesquisa in agenda:
    print('Telefone de', nome_pesquisa, ':', agenda[nome_pesquisa])
else:
    print('Nome não encontrado na agenda.')