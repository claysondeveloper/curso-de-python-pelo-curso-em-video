'''
Nessa aula, vamos aprender operações com String no Python.
As principais operações que vamos aprender são o
Fatiamento de String, Análise com len(), count(), find(),
transformações com replace(), upper(), lower(),
capitalize(), title(), strip(), junção com join().
'''

phase = 'Curso em Video Python'

print(phase[6]) # Adicionando o valor dentro de chaves ele mostar a letra que se encontra no valor desejado
print(phase[9:16]) # Mostra as letras do valor inicial 9 ate o valor final 16 nao contando o valor 16
print(phase[9:16:2]) # Mostar as letras do valor inicial 9 ate o valor final 16 pulando de 2

print("""Para colocar texto em varias 
linhas sem precisar adicionando 
print toda hora pode colocar o texto dentro de 
tres aspas duplas """)

print(phase.count('o')) # count metodo que conta quantas vezes a letra desejada existe no texto

print(len(phase)) # Mostar o tamanho do text contando os espaços

print(phase.upper()) # Mostar a farse em texto grande

print(phase.lower())  # Mostar a farse em texto pequeno

print(phase.title()) # Mostra o texto com toda primeira letra apos um espaço em letra grande

print(phase.strip()) # Mostra o texto sem espaços no inicio e nem no fim

print(phase.replace('Python','Android')) # Mostar a frase com a palavra alterada pela palavra desejada

print('Curso' in phase) # Verifica se a palavra desejada esta dentro do texto

print(phase.find('Python')) # Mostar o local de inicio da palavra se a palavra nao existir retorna -1

print(phase.split()) # Fatia o texto transformando em uma lista com cada palavra