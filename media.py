soma = 0
total = 0
jovem = 0
adulto = 0
idoso = 0

while True:
    entrada = str(input("Digite sua idade: "))
    if (entrada == "fim"):
        break
    else:
        numeroEntrada = int(entrada)
        soma = soma + numeroEntrada
        total = total + 1
        if numeroEntrada <= 25 and numeroEntrada > jovem:
            jovem = numeroEntrada
        elif numeroEntrada <= 60 and numeroEntrada > adulto:
            adulto = numeroEntrada
        elif numeroEntrada > idoso:
            idoso = numeroEntrada
    if total >= 40:
        break

media = soma / total

print("Media: " + str(media))

print("A media é: ")
if media <= 25:
    print("Jovem")
elif media <= 60:
    print("adulto")
else:
    print("idoso")

print("O mais jovem " + str(jovem))
print("O mais adulto " + str(adulto))
print("O mais idoso " + str(idoso))