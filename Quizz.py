
perguntas = [
    {
        "pergunta": "1. Qual é a capital do Brasil?",

        "opcoes": ["A) São Paulo", "B) Rio de Janeiro", "C) Brasília", "D) Salvador"],
        "correta_maiuscula": "C",
        "correta_minuscula": "c"
    },
    {
         "pergunta": "2. Qual é o jogo em que os meninos do 2B não param de jogar?",

        "opcoes": ["A) Round6", "B) Confeitaria da Moranguinho ", "C) CS2/CS", "D) Roblox(Blox Fruits)"],
        "correta_maiuscula": "B",
        "correta_minuscula": "b"
    },
    {
        "pergunta": "3. Qual a frase característica do Gustavo Daniel?",

        "opcoes": ["A) Vocês são imaturos demais", "B) *assobio", "C) Você é patinho! Quack, Quack", "D) Guardem os computadores"],
        "correta_maiuscula": "D",
        "correta_minuscula": "d"
    },
    {
        "pergunta": "4.  Qual é o resultado de Bixteca + Limbert?",

        "opcoes": ["A) Valdirene", "B) Akira", "C) Moisés", "D) Felipão"],
        "correta_maiuscula": "B",
        "correta_minuscula": "b"
    },
    {
        "pergunta": "5. Quantos anos tem o Dielme?",

        "opcoes": ["A) 22", "B) 29", "C) 33", "D) 40"],
        "correta_maiuscula": "C",
        "correta_minuscula": "c"
    }
]

while True:
    pontos = 0 
    saiu = False
    
    print("\n=== INICIANDO O QUIZ (Digite 'stop' a qualquer momento para sair) ===\n")

    for item in perguntas:
        print(item["pergunta"] + "\n")
        
        for opcao in item["opcoes"]:
            print(opcao)
            
        resposta = input("\nSua resposta (A, B, C, D ou 'stop'): ")
  
        if resposta == "stop" or resposta == "STOP":
            saiu = True
            break 
            
        if resposta == item["correta_maiuscula"] or resposta == item["correta_minuscula"]:
            print("Correto! +2 pontos.\n")
            pontos += 2
        else:
            print(f"Errado! A resposta certa era {item['correta_maiuscula']}.\n")

    if saiu:
        print("\nVocê saiu do quiz.")
        break

    print(f"Fim da rodada! Você totalizou {pontos} pontos.")

    if pontos >= 10:
        print("Parabéns! Você atingiu os 10 pontos necessários e venceu o quiz!")
        break 
    else:
        print("Você não atingiu q quantidade de pontos necessários. Tente novamente!")
        continuar = input("Pressione Enter para repetir ou digite 'stop' para sair: ")
        
        if continuar == "stop" or continuar == "STOP":
            print("\nVocê saiu do quiz.")
            break

