def pegaEntradas(mensagem):
    entradas = []
    while True:
        entrada = str(input(mensagem))
        if (entrada == "fim" or len(entradas) >= 40):
            break
        
        entradas.append(int(entrada))
    
    return entradas

def gerarMedia(entradas):
    soma = 0
    
    if (len(entradas) == 0):
        return soma
    
    for entrada in entradas:
        soma += entrada
    return soma / len(entradas)

def categorizar(entradas):
    jovem = adulto = idoso = -1
    for entrada in entradas:
        if entrada <= 25 and entrada > jovem:
            jovem = entrada
        elif entrada <= 60 and entrada > adulto:
            adulto = entrada
        elif entrada > 60 and entrada > idoso:
            idoso = entrada
    return [jovem, adulto, idoso]

def renderizarEntradaCategorizada(entrada):
    if (entrada >= 0):
        return entrada
    else:
        return "Não existe"

entradas = pegaEntradas("Digite sua idade: ")

media = gerarMedia(entradas)

entradasCategorizadas = categorizar(entradas)

print("Média: ", media)
print("O mais jovem é: ", renderizarEntradaCategorizada(entradasCategorizadas[0]))
print("O mais adulto é: ", renderizarEntradaCategorizada(entradasCategorizadas[1]))
print("O mais idoso é: ", renderizarEntradaCategorizada(entradasCategorizadas[2]))
