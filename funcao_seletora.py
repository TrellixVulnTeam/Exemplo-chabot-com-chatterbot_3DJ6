import Levenshtein
from unidecode import unidecode


#função para comparar as msg inseridas com o banco de dados

def compare(statement_a_text, statement_b_text):
  statement_a_text = unidecode(str(statement_a_text.text).lower())
  statement_b_text = unidecode(str(statement_b_text.text).lower())

  percent = float(round(Levenshtein.ratio(statement_a_text, statement_b_text), 2))

  if percent < 0.7:
    percent = float(0.0)
  else:
    print("Mensagem do usuario:", statement_a_text,
          "\nMensagem candidata:", statement_b_text,
          "\nGrau de semelhança:", percent)

  return percent

#função para selecionar a msg que vai ser enviada

def select(statement_a_text, statement_list, storage=None):
    response = statement_list[0]
    print("Msg escolhida:", response)
    return response
