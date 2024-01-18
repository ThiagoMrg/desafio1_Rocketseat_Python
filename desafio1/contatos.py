def adicionar_contato(contatos, nome_contato, telefone, email):
  contato = {"contato": nome_contato, "telefone": telefone, "email": email, "favorito": False}
  contatos.append(contato)
  print(f"O contato {nome_contato} foi adicionado com sucesso!")
  return

def ver_contatos(contatos):
  print("\nLista de contatos:")
  for indice, contato in enumerate (contatos, start=1):
    status = "★" if contato["favorito"] else " "
    nome_contato = contato["contato"]
    telefone = contato["telefone"]
    email = contato["email"]
    print(f"{indice}.[{status}] {nome_contato} | {telefone} | {email}")
  return

def editar_contato(contatos, indice_contato, novo_contato, novo_telefone, novo_email):
  indice_contato_ajustado = int(indice_contato) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
    contatos[indice_contato_ajustado]["contato"] = novo_contato
    contatos[indice_contato_ajustado]["telefone"] = novo_telefone
    contatos[indice_contato_ajustado]["email"] = novo_email
    print(f"\nContato {indice_contato} atualizado para {novo_contato} | {novo_telefone} | {novo_email}")
  else:
    print("Indice de contato inválido")
  return

def favoritar_contato(contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
    contatos[indice_contato_ajustado]["favorito"] = True
    print(f"Contato {indice_contato} marcado como favorito")
  else:
    print("Indice do contato inválido.")
  return

def desmarcar_contato_favorito(contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
    contatos[indice_contato_ajustado]["favorito"] = False
    print(f"Contato {indice_contato} desmarcado como favorito")
  else:
    print("Indice de contato inválido")
  return
  
def ver_contatos_favoritos(contatos):
  print("\nLista de contatos favoritos:")
  favoritos = [contato for contato in contatos if contato["favorito"]]
  for indice, contato in enumerate (favoritos, start=1):
    print(f"{indice}.[★] {contato["contato"]} | {contato["telefone"]} | {contato["email"]}")
  return

def deletar_contato(contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
    contato = contatos[indice_contato_ajustado]
    contatos.remove(contato)
    print(f"Contato {indice_contato} deletado com sucesso")
  else: 
    print("Indice do contato inválido.")
  return

contatos = []
while True:
  print("\nMenu do Gerenciador de Lista de contatos:")
  print("1. Adicionar um contato")
  print("2. Visualizar a lista de contatos")
  print("3. Editar contato")
  print("4. Marcar um contato como favorito")
  print("5. Desmarcar um contato como favorito")
  print("6. Ver contatos favoritos")
  print("7. Apagar um contato")
  print("8. Sair")

  escolha = input("Digite a sua escolha: ")

  if escolha == "1":
    nome_contato = input("Digite o nome do novo contato: ")
    telefone = input("Digite apenas os números com o DDD(sem espaço ou parenteses) do novo contato: ")
    email = input("Digite o Email do novo contato: ")
    adicionar_contato(contatos, nome_contato, telefone, email)
  elif escolha == "2":
    ver_contatos(contatos)
  elif escolha == "3":
    ver_contatos(contatos)
    indice_contato = input("\nDigite o número do contato que deseja atualizar: ")
    novo_contato = input("Digite o novo nome do contato: ")
    novo_telefone = input("Digite o novo telefone do contato: ")
    novo_email = input("Digite o novo email do contato: ")
    editar_contato(contatos, indice_contato, novo_contato, novo_telefone, novo_email)
  elif escolha == "4":
    ver_contatos(contatos)
    indice_contato = input("Digite o número do contato que deseja favoritar: ")
    favoritar_contato(contatos, indice_contato)
  elif escolha == "5":
    ver_contatos(contatos)
    indice_contato = input("Digite o número do contato que deseja retirar dos favoritos: ")
    desmarcar_contato_favorito(contatos, indice_contato)
  elif escolha == "6":
    ver_contatos_favoritos(contatos)
  elif escolha == "7":
    ver_contatos(contatos)
    indice_contato = input("Digite o número do contato que deseja deletar: ")
    deletar_contato(contatos, indice_contato)
  elif escolha == "8":
    break

print("Programa finalizado.")
