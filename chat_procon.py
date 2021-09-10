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
                  statement_comparison_function=compare,
                  # statement_comparison_function=JaccardSimilarity,
                  response_selection_method=get_most_frequent_response,
                  logic_adapters=[
                      {
                          "import_path": "chatterbot.logic.BestMatch",
                      }
                  ]
                  )

#Treinando o chat

trainer = ListTrainer(chatbot)

for pergunta, resposta in zip(pergunta_custo, resposta_custo):
    trainer.train([pergunta, resposta])

for pergunta1, resposta in zip(pergunta_custo1, resposta_custo):
    trainer.train([pergunta1, resposta])

for pergunta2, resposta in zip(pergunta_custo2, resposta_custo):
    trainer.train([pergunta2, resposta])

for pergunta3, resposta in zip(pergunta_custo3, resposta_custo):
    trainer.train([pergunta3, resposta])

trainer.train(
    "chatterbot.corpus.portuguese"
)


#loop para a conversa

name = input("Opa! Tudo bem? Posso saber o seu nome ?")
print('Seja bem vindo {}. Aqui podemos te ajudar a verificar os melhores preços de Itajubá - MG! '.format(name))

while True:
    try:
        response = (chatbot.get_response(input(name + ":")))
        if float(response.confidence) > 0.7:
            print("Chat - PROCON: ", response.text)
        else:
            print('Chat - PROCON: Poderia por favor refazer a sua pergunta ?')
            print(response.confidence)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break

print('Muito obrigado {}, volte sempre!'.format(name))