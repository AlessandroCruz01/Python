from datetime import date
dias = int(input('Dias: '))
hoje = date.today()
print(hoje.toordinal())
print(type(hoje))
futuro = date.fromordinal(hoje.toordinal()+dias)
print(futuro)
futuro = futuro.strftime("%d/%m/%Y")
hoje = hoje.strftime("%d/%m/%Y")
print(futuro)
print("A data de Hoje é: {} e daqui {} dias teremos a seguinte data {}".format(hoje,dias,futuro))

