print("                 SEJA BEM VINDO!                      ")
nome = input("Qual seu nome? ")
comecar = input(f"Olá! {nome} deseja jogar? [S/N] ")
pontos = 0
if comecar != "S":
    quit()
else:
    print("Começando...")

print("\n 1º)De quem é a famosa frase “Penso, logo existo”?")
print("(A)Descartes")
print("(B)Galileu Galilei")
print("(C)Platão")
print("(D)Sócrates")
resposta1 = input("Qual o item certo? ")
if resposta1 == "A":
    pontos = pontos + 1
    print("Parabéns, Resposta correta!\n")
else:
    print("Resposta errada!\n")

print("\n2º)De onde é a invenção do chuveiro elétrico?")
print("(A)França")
print("(B)Inglaterra")
print("(C)Brasil")
print("(D)Austrália")
resposta2 = input("Qual o item certo? ")
if resposta2 == "C":
    pontos = pontos + 1
    print("Parabéns, Resposta correta!\n")
else:
    print("Resposta errada!\n")

print("\n3º)Quais o menor e o maior país do mundo?")
print("(A)Malta e Estados Unidos")
print("(B)Nauru e China")
print("(C)Nauru e China")
print("(D)Vaticano e Rússia")
resposta3 = input("Qual o item certo? ")
if resposta3 == "D":
    pontos = pontos + 1
    print("Parabéns, Resposta correta!\n")
else:
    print("Resposta errada!\n")

print("\n4º)Em que período da pré-história o fogo foi descoberto?")
print("(A)Neolítico")
print("(B)Idade dos Metais")
print("(C)Período da Pedra Polida")
print("(D) Paleolítico")
resposta4 = input("Qual o item certo? ")
if resposta4 == "D":
    pontos = pontos + 1
    print("Parabéns, Resposta correta!\n")
else:
    print("Resposta errada!\n")
    
print("\n5º)Qual o nome do presidente do Brasil que ficou conhecido como Jango?")
print("(A)João Goulart")
print("(B)Jânio Quadros")
print("(C)Jacinto Anjos")
print("(D)Getúlio Vargas")
resposta5 = input("Qual o item certo? ")
if resposta5 == "A":
    pontos = pontos + 1
    print(f"\nParabéns, Resposta correta! \n         Pontuação: {pontos}/5"           )
else:
    print("Resposta errada!\n")
print("              FIM DE JOGO ;)              ")