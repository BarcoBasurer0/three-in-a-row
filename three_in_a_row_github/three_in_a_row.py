import PySimpleGUI as sg

button_size = (7, 3)
PLAYER_ONE = "X"
PLAYER_TWO = "O"
deck = [0,0,0,
        0,0,0,
        0,0,0 ]
current_player = PLAYER_ONE
winner_plays = [[0,1,2],[3,4,5 ],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
layout = [[
    sg.Button("", key="-0-", size=button_size),
    sg.Button("", key="-1-", size=button_size),
    sg.Button("", key="-2-", size=button_size)],
    [
        sg.Button("", key="-3-", size=button_size),
        sg.Button("", key="-4-", size=button_size),
        sg.Button("", key="-5-", size=button_size)
    ],
    [
        sg.Button("", key="-6-", size=button_size),
        sg.Button("", key="-7-", size=button_size),
        sg.Button("", key="-8-", size=button_size)
    ],
    [sg.Button("He terminado", key="-Ok-")]]

window = sg.Window("DEMO", layout)
game_end=False
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "-Ok-":
        break
    if window.Element(event).ButtonText == "" and not game_end:
        index = int(event.replace("-",""))
        deck[index] = current_player
        window.Element(event).Update(text=current_player)

        for winner_play in winner_plays:
            if deck[winner_play[0]] == deck[winner_play[1]] == deck[winner_play[2]] != 0 :
                if deck[winner_play[0]] == PLAYER_ONE:
                    print("El jugaodor 1 gano")
                    game_end = True
                else:
                    print("El jugador 2 gano")
                    game_end= True

        if 0 not in deck:
            print("juego terminado!")
            game_end = True

    if current_player == PLAYER_ONE:
        current_player = PLAYER_TWO
    else:
        current_player = PLAYER_ONE


window.close()