nome = input("Insira seu nome: ")
nota1 = float(input("Insira a 1º nota: "))
nota2 = float(input("Insira a 2º nota: "))
nota3 = float(input("Insira a 3º nota: "))

media = (nota1 + nota2 + nota3) /3

arquivo = open("desempemho_escolico.txt", "a")
arquivo.write(nome + " | " + str(media) + "\n")
arquivo.close()
