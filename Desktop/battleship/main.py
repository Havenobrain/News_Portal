from board import Board
from utils import place_ships, random_shot

def parse_input(input_str):
    # Удаляем все пробелы из строки
    cleaned_input = input_str.replace(" ", "")
    # Проверяем, что строка состоит только из цифр и её длина равна 2
    if len(cleaned_input) == 2 and cleaned_input.isdigit():
        # Преобразуем в координаты
        return int(cleaned_input[0]), int(cleaned_input[1])
    else:
        raise ValueError("Неверный формат ввода. Введите координаты в формате 'x y' или 'xy'.")

def play_game():
    player_board = Board(place_ships())
    computer_board = Board(place_ships())
    
    while True:
        # Отображение доски игрока
        print("Ваша доска:")
        player_board.display()
        
        # Отображение доски противника
        print("Доска противника:")
        computer_board.display_opponent_view()

        # Ход игрока
        try:
            shot_input = input("Введите координаты для стрельбы (x y): ")
            shot = parse_input(shot_input)
            result = computer_board.take_shot((shot[0] - 1, shot[1] - 1))
            print(f"Вы {result}!")
            if computer_board.is_all_sunk():
                print("Вы выиграли!")
                break
        except ValueError as e:
            print(e)
        except IndexError as e:
            print("Неверный формат координат. Попробуйте снова.")
        
        # Ход компьютера
        shot = random_shot(player_board)
        result = player_board.take_shot(shot)
        print(f"Компьютер стреляет в {shot[0]+1} {shot[1]+1} и {result}!")
        if player_board.is_all_sunk():
            print("Компьютер выиграл!")
            break

if __name__ == "__main__":
    play_game()
