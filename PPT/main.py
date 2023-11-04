import random

while True:
  user_action = input("Escolha uma opção(pedra, papel, tesoura): ")

  if user_action == computer_action:
      print(f"Ambos os jogadores selecionados {user_action}. É um empate!")
  elif user_action == "pedra":
      if computer_action == "tesoura":
          print("Pedra esmaga tesoura! Você Ganhou!")
      else:
          print("Papel cobre pedra! Você Perdeu!")
  elif user_action == "papel":
      if computer_action == "pedra":
          print("Papel cobre pedra! Você Ganhou!")
      else:
          print("Tesoura corta papel! Você Perdeu!")
  elif user_action == "tesoura":
      if computer_action == "papel":
          print("Tesoura corta papel! Você Ganhou!")
      else:
          print("Pedra esmaga Tesoura! Você Perdeu!.")
    
  play_again = input("\nDeseja jogar novamente? (s/n): ")
  if play_again.lower() != "s":
      print("Fim de Jogo.")
      break