import chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.comparisons import LevenshteinDistance, JaccardSimilarity
from chatterbot.response_selection import get_most_frequent_response, get_first_response
from funcao_seletora import compare, select
from dados import pergunta_custo, pergunta_custo1, pergunta_custo2, pergunta_custo3, resposta_custo

# import pandas as pd
# import json
# from chatterbot.exceptions import OptionalDependencyImportError
# from chatterbot.logic import LogicAdapter


# Criando o chat
chatbot = ChatBot('Chat - PROCON',
                  read_only=False,
                  #statement_comparison_function=compare,
                  #response_selection_method=select,
                  logic_adapters=[
                      {
                          "import_path": "chatterbot.logic.BestMatch",
                      }
                  ]
                  )

#Treinando o chat

trainer = ListTrainer(chatbot)

trainer.train(["Oi", "Olá, tudo bem ?", 
               "Tudo bem!", "Que bom",
               'Olá, tudo bem?', 'Tudo bem sim, e você?',
               "Como você esta?", "Estou bem, melhor agora!",
               "Onde é a barraca de pão de queijo?", "Opa, você está no lugar certo!"
               ])  

trainer.train(
    "chatterbot.corpus.portuguese"
)


#loop para a conversa

name = input("Opa! Tudo bem? Posso saber o seu nome ?")
print('Oi {}. Vamos conversar? '.format(name))

while True:
    try:
        response = (chatbot.get_response(input(name + ":")))
        if float(response.confidence) > 0.7:
            print("Chat: ", response.text)
        else:
            print('Chat: Poderia por favor refazer a sua pergunta ?')
            print(response.confidence)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break

print('Muito obrigado {}, volte sempre!'.format(name))
