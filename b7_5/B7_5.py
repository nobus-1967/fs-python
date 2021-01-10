#!/usr/bin/env python
import random

class Cell:
    """Класс ячейки игрового поля."""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cell_state = 'free'
        self.is_shoot_in = 'nay'
        
    @property
    def state(self):
        """Возвращает статус, свободна ячейка или занята своим кораблем,
        скрытым кораблем противника (free/ship/hidden).
        """
        return self.cell_state
    
    @state.setter
    def change_state(self, new_state):
        """Изменяет статус ячейки (free/ship/hidden)."""        
        self.cell_state = new_state
        
    @property
    def shoot_in(self):
        """Возвращает значение, можно ли использовать ли ячейку для стрельбы 
        (nay/yep).
        """        
        return self.is_shoot_in
    
    @shoot_in.setter
    def change_shoot_in(self, new_value):
        """Изменяет значение ячейки для стрельбы (nay/yep)."""        
        self.is_shoot_in = new_value
        
    def __repr__(self):
        """Возвращает координаты ячейки."""
        return f'({self.x}, {self.y})'


class Board:
    """Класс для создания и управления состоянием игровой доски."""
    def __init__(self, user):
        """Инициализирует новую доску (6x6) для игрока."""
        self.player = user
        self.game_board = []
        for row in range(0, 6):
            new_row = []
            for col in range(0, 6):
                new_cell = Cell(row, col)
                new_row.append(new_cell)
            self.game_board.append(new_row)
    
    def board(self):
        """Выводит игровое поле с координатами и условными обозначениями."""
        print(f'\n\n\tИгровое поле: {self.player}')
        print(f'\t  1 2 3 4 5 6', end='')
        for index, row in enumerate(self.game_board):
            print(f'\n\t{index + 1} ', end = '')
            for cell in row:
                if cell.state == 'free' and cell.shoot_in == 'nay':
                    print('.', end=' ')
                elif cell.state == 'free' and cell.shoot_in == 'yep':
                    print('*', end=' ')
                elif cell.state == 'ship' and cell.shoot_in == 'nay':
                    print('#', end=' ')
                elif cell.state == 'ship' and cell.shoot_in == 'yep':
                    print('X', end=' ')
                elif cell.state == 'hidden' and cell.shoot_in == 'nay':
                    print('.', end=' ')
                elif cell.state == 'hidden' and cell.shoot_in == 'yep':
                    print('X', end=' ')


class User:
    """Класс для определения игрока и управления стрельбой."""
    def __init__(self, player_type):
        """Инициализирует игрока, устанавливает его тип (Человек/AI)"""
        self.type = player_type
        self.shot = None
        
    @property
    def shoot(self):
        """Устанавливает кординаты обстреливаемой ячейки"""
        pass

    
class Human(User):
    """Класс для определения игрока-человека и управления стрельбой."""
    def __init__(self, player_type='Человек'):
        """Инициализирует игрока-человека."""
        super().__init__(player_type)
        
    @property
    def shoot(self):
        """Устанавливает координаты обстреливаемой ячейки."""
        while True:
            choice = input('\n\nТвой выбор: ')
            if len(choice) != 2:
                print('Координаты должны быть в формате xy, где x и y - целые числа!\n')
                continue        
            x = choice[0]
            y = choice[1]
            if not(x.isdigit()) or not(y.isdigit()):
                print('Координаты должны быть числами в диапазоне 1-6!\n')
                continue
            x = int(x)
            y = int(y)
            if 0 < x < 7:
                if 0 < y < 7:
                    x -= 1
                    y -= 1
                    if game.ai_board.game_board[x][y].shoot_in != 'yep':
                        game.ai_board.game_board[x][y].is_shoot_in = 'yep'
                        self.shot = (x, y)
                        return self.shot
                    else:
                        print('Сюда уже стреляли!\n')
                        continue
                else:
                    print('Координаты должны быть числами в диапазоне 1-6!\n')
                    continue
            else:
                print('Координаты должны быть числами в диапазоне 1-6!\n')
                continue


class AI(User):
    """Класс для определения AI-игрока и управления стрельбой."""
    def __init__(self, player_type='AI'):
        """Инициализирует AI-игрока."""
        super().__init__(player_type)
        
    @property
    def shoot(self):
        """Устанавливает координаты обстреливаемой ячейки."""
        while True:
            x = random.randint(0, 5)
            y = random.randint(0, 5)
            if game.human_board.game_board[x][y].shoot_in != 'yep':
                game.human_board.game_board[x][y].is_shoot_in = 'yep'
                self.shot = (x, y)
                return self.shot
            else:
                continue 


class Ship:
    """Класс для управления состоянием кораблей в игре."""
    def __init__(self, player, level, name, cells_ship):
        self.player = player
        if self.player == 'Человек':
            self.board = game.human_board
        else:
            self.board = game.ai_board
        self.name = name
        self.ship_level = level
        self.ship_lives = level
        self.ship_status = 'alive'
        self.cells_ship = cells_ship
        if level > 1:
            for cell in cells_ship:
                x, y = cell
                if self.player == 'Человек':
                    self.board.game_board[x][y].change_state = 'ship'
                else:
                    self.board.game_board[x][y].change_state = 'hidden'
        else:
            x, y = cells_ship
            if self.player == 'Человек':
                self.board.game_board[x][y].change_state = 'ship'
            else:
                self.board.game_board[x][y].change_state = 'hidden'
         
    @property
    def lives(self):
        """Возвращает уровень живучести корабля."""
        return self.ship_lives
        
    def check_ship(self, cell):
        """Изменяет уровень живучести корабля при попадании в его ячейку."""
        if self.ship_level > 1:
            if cell in self.cells_ship:
                self.ship_lives -= 1
                return True
            else:
                return False
        else:
            xs, ys = self.cells_ship
            xc, yc = cell
            if xs == xc and ys == yc:
                self.ship_lives -= 1
                return True
            else:
                return False
  
    @property
    def status(self):
        """Изменяет статус корабля, утратившего свою живучесть."""
        if self.lives == 0:
            self.ship_status = 'dead'        
        return self.ship_status


class Squadron:
    """Класс устанавливает корабали игрока на доске."""
    def __init__(self, player):
        """Инициализирует расстановку кораблей на доске."""
        self.player = player
        self.ships = []
            
    def place_ships(self):
        """Расставляет корабли из паттернов."""
        user_pattern = [((3, 0), (4, 0), (5, 0)),
                     ((0, 1), (1, 1)), ((1, 3), (1, 4)),
                     (3, 2), (3, 4), (5, 3), (5, 5)]
        ship_3 = Ship(self.player, 3, 'ship_3', user_pattern[0])
        self.ships.append(ship_3)
        ship_2_1 = Ship(self.player, 2, 'ship_2_1', user_pattern[1])
        self.ships.append(ship_2_1)
        ship_2_2 = Ship(self.player, 2, 'ship_2_2', user_pattern[2])
        self.ships.append(ship_2_2)
        ship_1_1 = Ship(self.player, 1, 'ship_1_1', user_pattern[3])
        self.ships.append(ship_1_1)
        ship_1_2 = Ship(self.player, 1, 'ship_1_2', user_pattern[4])
        self.ships.append(ship_1_2)
        ship_1_3 = Ship(self.player, 1, 'ship_1_3', user_pattern[5])
        self.ships.append(ship_1_3)
        ship_1_4 = Ship(self.player, 1, 'ship_1_4', user_pattern[6])
        self.ships.append(ship_1_4)


class Game:
    """Класс для управления всей игрой "Морской бой"."""
    def __init__(self):
        """Инициализирует игру, создает игроков, их игровые поля."""
        self.human = Human()
        self.human_board = Board('Человек')
        self.human_squadron = Squadron('Человек')
        self.ai = AI('AI')
        self.ai_board = Board('AI')
        self.ai_squadron = Squadron('AI')
          
    def place_squadrons(self):
        """Расставляет корабли на игровых полях."""
        self.human_squadron.place_ships()
        self.ai_squadron.place_ships()
        
    @property
    def plays(self):
        """Управляет последовательностью игры"""
        self.human_board.board()
        print()
        self.ai_board.board()
        move_number = 0
        while True:
            move_number += 1
            if move_number % 2 == 0:
                print('\n\nХожу я!')
                self.human_board.board()
                self.ai.shoot
                target = self.ai.shot
                x, y = target
                print(f'\n\nМой выбор: {x + 1}{y + 1}')
                self.human_board.board()
                for ship in self.human_squadron.ships:
                    result = ship.check_ship(target)
                    if result:
                        print('\n\nПопал!')
                        ship.status
                        move_number -=1
                        human_alive = 0
                        for ship in self.human_squadron.ships:
                            alive = 0
                            if ship.status == 'alive':
                                human_alive += 1
                        print(f'Оставшихся кораблей Человека: {human_alive}')
                        if human_alive > 0:
                            continue                        
                        else:
                            print('\n\nЧеловек, я победил!')
                            return False
                    else:
                        continue             
            else:
                print('\n\nЧеловек, твой ход!')
                self.ai_board.board()
                self.human.shoot
                self.ai_board.board()
                target = self.human.shot
                for ship in self.ai_squadron.ships:
                    result = ship.check_ship(target)
                    if result:
                        print('\n\nПопал!')
                        ship.status
                        move_number -=1
                        ai_alive = 0
                        for ship in self.ai_squadron.ships:
                            if ship.status == 'alive':
                                ai_alive += 1
                        print(f'Оставшихся кораблей AI: {ai_alive}')
                        if ai_alive > 0:
                            continue                        
                        else: 
                            print('\n\nЧеловек, ты победил!')
                            return False
                    else:
                        continue

    def greet(self):
        """Приветствует игрока перед игрой"""
        print('Добро пожаловать в игру "Морской бой"!')
        print('Я - AI (искусственный интеллект) и я сражусь с тобой, Человек.')
        print('Корабли на местах, капитаны на мостиках. Начинаем!')
        print('\n\nВведи цель для выстрела - координаты формата xy,')
        print('где x - номер строки, y - номер столбца (например, 01 или 33)')

    def goodbye(self):
        """Прощается с игроком по окончании игры."""
        print('Прощай, Человек! Спасибо, что играл в мою игру!')       


game = Game()
game.place_squadrons()  
game.greet()
game.plays
game.goodbye()
