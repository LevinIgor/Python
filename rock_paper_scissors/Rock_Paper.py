import json
import random
from pathlib import Path
from json.decoder import JSONDecodeError


if __name__ == "__main__":
    RockPaperScissors()
    
class Player:
    def __init__(self) -> None:
        self.name = input('Введите имя: ')
        self.rating = self.get_rating()

    def get_rating(self):
        file = Path('rock_paper_scissors/rating.json')
        rating = None

        if not file.exists():
            file.touch()

        self.file = file

        with file.open('r') as file:
            try:
                data = json.load(file)
                data_rating = data.get(self.name)
            except JSONDecodeError:
                pass

            if rating:
                rating = data_rating
            else:
                rating = 0

        return rating

    def choose_gesture(self, playin_gestures, input_gest):
        while True:
            for gest_ in playin_gestures:
                if input_gest == gest_.title:
                    self.gesture = gest_
                    return
            else:
                print('Error: Такого жеста не существует!')
                input_gest = input('Какой ваш жест?:')

    def increase_rating(self, points):
        with self.file.open('r') as fl_r:
            try:
                data = json.load(fl_r)
            except JSONDecodeError:
                pass

        with open(self.file, 'w') as fl_a:
            try:
                data.update({self.name: self.rating + points})
                self.rating += points
            except Exception:
                data = {self.name: self.rating + points}
            finally:
                json.dump(data, fl_a)
class Gest():
    gestures = []

    def __init__(self, title) -> None:
        self.title = title
        self.beat = []
        self.gestures.append(self)

    def add_gesture(self, gesture):
        self.beat.append(gesture)

    @staticmethod
    def get(_k):
        for gest_ in Gest.gestures:
            if gest_.title == _k:
                return gest_
        return None
class RockPaperScissors:
    base_gestures = [
            'камень', 'огонь', 'ножницы', 'змея', 'человек',
            'дерево', 'волк', 'губка', 'бумага', 'воздух',
            'вода', 'дракон', 'дьявол', 'свет', 'оружие'
        ]
    playin_gestures = []

    def __init__(self) -> None:
        self.init_gestures()

        playin_gestures = input('Введите жесты: ')
        self.pick_playin_gestures(playin_gestures)

        if not self.playin_gestures:
            print('Игра не может начаться, не хватает жестов')
            return

        player = Player()

        while True:
            command = input('')
            if command[0] == '!':
                if command == '!exit':
                    break
                if command == '!rating':
                    print('Your rating is {}'.format(player.rating))
                if command == '_':
                    print('There is no command {}'.format(command))
                    
            else:
                player.choose_gesture(self.playin_gestures, command)
                self.compete(player)

    def choose_pc_gesture(self):
        return random.choice(self.playin_gestures)

    def compete(self, player):
        pc_gesture = self.choose_pc_gesture()

        if pc_gesture.title in player.gesture.beat:
            print('Вы выиграли!')
            player.increase_rating(100)
        elif pc_gesture.title == player.gesture.title:
            print('Ничья')
            player.increase_rating(50)
        else:
            print('Вы проиграли!')

        print('Компьютер выбрал: {}'.format(pc_gesture.title))

    def pick_playin_gestures(self, playing_gestures):
        for gest_ in playing_gestures.split(','):
            cl_gest = Gest.get(gest_)
            if cl_gest:
                self.playin_gestures.append(cl_gest)
            else:
                print('Это не жест {}'.format(gest_))

    def init_gestures(self):
        for i, gesture in enumerate(self.base_gestures):
            gesture_ = Gest(gesture)

            for beat_gesture in range(i+1, i+8):

                if beat_gesture == len(self.base_gestures):
                    for beat_gesture in range(0, i - 7):
                        gesture_.add_gesture(self.base_gestures[beat_gesture])

                    break

                gesture_.add_gesture(self.base_gestures[beat_gesture])

