bar_1 = ["[ ]", "[ ]", "[ ]"]
bar_2 = ["[ ]", "[ ]", "[ ]"]
bar_3 = ["[ ]", "[ ]", "[ ]"]
symbol_x = "x"
symbol_o = "o"
used_cells = set()
def game_x():
    print("".join(bar_1), "".join(bar_2), "".join(bar_3), sep="\n")
    try:
        symb_idv = int(input(f"{player_1.capitalize()}, введите порядковый номер ячейки по вертикали: "))
    except ValueError:
        print("Неккоректные координаты")
        game_x()
    try:
        symb_idh = int(input(f"{player_1.capitalize()}, введите порядковый номер ячейки по горизонтали: "))
    except ValueError:
        print("Неккоректные координаты")
        game_x()
    if ((str(symb_idv) + str(symb_idh)) not in used_cells) and ((0 < symb_idv < 4) and (0 < symb_idh < 4)):
        if symb_idv == 1:
            bar_1[symb_idh - 1] = f"[{symbol_x}]"
        elif symb_idv == 2:
            bar_2[symb_idh - 1] = f"[{symbol_x}]"
        elif symb_idv == 3:
            bar_3[symb_idh - 1] = f"[{symbol_x}]"
        used_cells.add(str(symb_idv) + str(symb_idh))
        for num in range(0, 3):
            if (bar_1[num] == bar_2[num] == bar_3[num] == "[x]") or (bar_1[0] == bar_1[1] == bar_1[2] == "[x]") \
                    or (bar_2[0] == bar_2[1] == bar_2[2] == "[x]") or (bar_3[0] == bar_3[1] == bar_3[2] == "[x]") \
                    or (bar_1[0] == bar_2[1] == bar_3[2] == "[x]") or (bar_1[2] == bar_2[1] == bar_3[0] == "[x]"):
                print("".join(bar_1), "".join(bar_2), "".join(bar_3), sep="\n")
                return print("Победил", player_1.capitalize(), "!!!")
            else:
                return game_o()
    else:
        print("Неккоректные координаты")
        game_x()


def game_o():
    print("".join(bar_1), "".join(bar_2), "".join(bar_3), sep="\n")
    try:
        symb_idv = int(input(f"{player_2.capitalize()}, введите порядковый номер ячейки по вертикали: "))
    except ValueError:
        print("Неккоректные координаты")
        game_x()
    try:
        symb_idh = int(input(f"{player_2.capitalize()}, введите порядковый номер ячейки по горизонтали: "))
    except ValueError:
        print("Неккоректные координаты")
        game_x()
    if ((str(symb_idv) + str(symb_idh)) not in used_cells) and ((0 < symb_idv < 4) and (0 < symb_idh < 4)):
        if symb_idv == 1:
            bar_1[symb_idh - 1] = f"[{symbol_o}]"
        elif symb_idv == 2:
            bar_2[symb_idh - 1] = f"[{symbol_o}]"
        elif symb_idv == 3:
            bar_3[symb_idh - 1] = f"[{symbol_o}]"
        used_cells.add(str(symb_idv) + str(symb_idh))
        for num in range(0, 3):
            if (bar_1[num] == bar_2[num] == bar_3[num] == "[o]") or (bar_1[0] == bar_1[1] == bar_1[2] == "[o]") \
                    or (bar_2[0] == bar_2[1] == bar_2[2] == "[o]") or (bar_3[0] == bar_3[1] == bar_3[2] == "[o]") \
                    or (bar_1[0] == bar_2[1] == bar_3[2] == "[o]") or (bar_1[2] == bar_2[1] == bar_3[0] == "[o]"):
                print("".join(bar_1), "".join(bar_2), "".join(bar_3), sep="\n")
                return print("Победил", player_2.capitalize(), "!!!")
            else:
                return game_x()
    else:
        print("Неккоректные координаты")
        game_o()


print("Инициализация программы для игры в \"крестики-нолики\"\nПравила игры:"
      "\n 1) Первым ходит игрок, ставящий крестики"
      "\n 2) Крестики могут ставиться в любом свободном поле и только один раз за ход."
      "\n 3) Игрок, ставящий нолики, делает свой ход сразу после игрока, ставившего крестик и располагает нолики по тому же принципу."
      "\n 4) Исчисление идёт слева направо и сверху вниз."
      "\n 5) Побеждает игрок, первым поставивший свои символы в ряд "
      "(3 символа по вертикали |или| 3 символа по горзионтали |или| 3 символа по диагонали)\n")
player_1 = input("Введите имя игрока, ставящего крестики: ")
if len(player_1) > 35:
    while len(player_1) > 35:
        player_1 = input("Имя игрока не может превышать 35 символов. Попробуйте ввести другое имя: ")
player_2 = input("Введите имя игрока, ставящего нолики: ")
if len(player_2) > 35:
    while len(player_2) > 35:
        player_2 = input("Имя игрока не может превышать 35 символов. Попробуйте ввести другое имя: ")
game_x()
