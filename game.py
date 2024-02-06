from random import choice
player_score = 0
computer_score = 0
choices = ["камень", "бумага", "ножницы"]
print("Камень давит ножницы. Ножницы режут бумагу. Бумага накрывает камень.")
while True:
    player = input("Выберите: камень, бумага, или ножницы (выйти) ? ")
    player = player.lower()
    if player == "выйти":
        break
    computer = choice(choices)
    print("Твой выбор " +player+ ", компьютер выбрал " +computer+ ".")
    if player == computer:
        print("Ничья")
    elif player =="камень":
        if computer == "ножницы":
            print("ты победил!")
            player_score = player_score + 1
        else:
            print("Победил компьютер!")
            computer_score = computer_score + 1
        print ("Общий счёт: у вас ", player_score, "у компьютера ", computer_score, "счёт: у вас ", player_score, "у компьютера ", computer_score)
    elif player == "бумага":
        if computer == "камень":
            print ("Ты победил!")
            player_score = player_score + 1
        else:
            print("Победил компьютер!")
            computer_score = computer_score + 1
        print ("Общий счёт: у вас ", player_score, "у компьютера",computer_score)
    elif player == "бумага":
        if computer == "камень":
            print ("Ты победил!")
            player_score = player_score + 1
        else:
            print ("Победил компьютер!")
            computer_score = computer_score + 1
        print ("Общий счёт: у вас ", player_score, "у компьютера ", computer_score)
    elif player == "ножницы":
        if computer == "бумага":
            print ("Ты победил!")
            player_score = player_score + 1
        else:
            print ("Победил компьютер!")
            computer_score = computer_score + 1
        print ("Обший счёт: у вас", player_score, "у компьютера", computer_score)
    else:
        print ("По-моему, произошла ошибка...")
        player = input ("Выберите: камень, бумага, или ножницы (выйти) ? " )

