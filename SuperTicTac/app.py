from include import SuperTicTacToe

app = SuperTicTacToe()

while not app.winner:
    app.draw_console()
    pos = list(map(int, input('Position: ').split()))
    while (pos[0] < 0 or pos[0] > 2) or (pos[1] < 0 or pos[1] > 2):
        print('Invalid input')
        pos = list(map(int, input('Position: ').split()))
    app.play(pos[0], pos[1])
    print()