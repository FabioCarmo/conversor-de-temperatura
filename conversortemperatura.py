# Programa para converter temperatura de Celsius para Fahrenheit e vice-versa
# Autor: Fabio Goncalves
# Data: 02-05-2025 // Versao Final 1.0

# importar biblioteca time para usar sleep
import time

# Definindo a funcao para conversao de temperatura
def exibirMenu():
    print("--" * 10, "CONVERSOR DE TEMPERATURA", "--" * 10)
    print("C - Celsius para Fahrenheit")
    print("F - Fahrenheit para Celsius")
    print("0 - Sair")
    return

# Conversao de Celsius para Fahrenheit
def converterCelsius(celsius):
    resultado = (celsius*1.8) + 32
    return resultado

# Conversao de Farenheit para Celsius
def converterFarenheit(farenheit):
    resultado = (farenheit - 32) / 1.8
    return resultado

# Loop principal para manter as opcao do menu e chamar a funcao de conversao
while True:
    exibirMenu()
    tipoTemp = input("Digite a opcao indicada")

    if (tipoTemp == "0"):
      print("Encerrando...")
      time.sleep(2)
      break
    elif (tipoTemp == "C" or tipoTemp == "c"):
      celsius = float(input("Digite a temperatura em Celsius: "))
      resConvertido = converterCelsius(celsius)
      print(f"A temperatura em Farenheit é: {resConvertido: .2f} F\n")
      time.sleep(1)
    elif (tipoTemp == "F" or tipoTemp == "f"):
       farenheit = float(input("Digite a temperatura em Farenheit: "))
       resConvertido = converterFarenheit(farenheit)
       print(f"A temperatura em Celsius é: {resConvertido: .2f} C\n")
       time.sleep(1)
    else:
       print("Opcao invalida! Tente novamente.\n")
       time.sleep(2)  # Pausa de 2 segundos antes de reiniciar o loop
       