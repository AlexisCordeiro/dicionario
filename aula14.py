votos = {}

while True:
    candidato = input("Digite o nome canditado (ou 'fim' para encerrar): ")
    if candidato == 'fim':
        break 
    
    # Verifica se o cadidato já recebeu votos antes
    if candidato in votos:
        votos[candidato] += 1
    else:
        votos[candidato] = 1
        
#imprime o resultado da votação 
print('Resultado da votação: ')
for candidato, quantidade in votos.items():
    print(candidato, '-', quantidade, 'votos')
    
print(votos)