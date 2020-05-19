import random
from map_components.point import Point
from map_components.ball import Ball
from map_components.player import Player


class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.lower_left = Point(0, 0)
        self.upper_right = Point(width, height)
        self.count_of_playesrs = 0
        self.players = {}
        self.food = []
        # Game settings
        self.START_RADIUS = 10
        self.COUNT_OF_FOOD = 100
        self.FOOD_RADIUS = 4
        self.MAP_WIDTH = width
        self.MAP_HEIGHT = height
        self.SCORE_PER_BALL = 10
        self.id_for_next_player = 1000
        self.WINNER_SCORE = 500

    def get_id_for_next_player(self):
        self.id_for_next_player += 1
        self.count_of_playesrs += 1
        return self.id_for_next_player

    def get_random_ball(self, radius):
        random_ball = Ball(Point(-1, -1), radius)
        while True:
            x = random.randint(self.lower_left.x, self.upper_right.x)
            y = random.randint(self.lower_left.y, self.upper_right.y)
            random_ball.middle.x = x
            random_ball.middle.y = y
            for p in self.players:
                if self.players[p].ball == random_ball:
                    continue
            return random_ball

    def create_new_player(self, player_id, name, elem):
        str_id = str(player_id)
        player_ball = self.get_random_ball(self.START_RADIUS)
        player = Player(player_ball, player_id, name, elem)
        self.players[str_id] = player
        return player.ball.middle.x, player.ball.middle.y

    def rand_food(self):
        return self.get_random_ball(self.FOOD_RADIUS)

    def start_new_game(self):
        # global food
        for _ in range(self.COUNT_OF_FOOD):
            self.food.append(self.rand_food())

    def update_player(self, player_id, x, y):
        str_id = str(player_id)
        self.players[str_id].ball.middle.x = x
        self.players[str_id].ball.middle.y = y

    def get_players(self):
        return self.players

    def get_food(self):
        return self.food

    def food_eating(self):
        # global food,players
        for p in self.players:
            for i, f in enumerate(self.food):
                if self.players[p].ball.can_eat(f):
                    self.players[p].score += self.SCORE_PER_BALL
                    self.players[p].ball.calculate_radius_after_eating(f)
                    self.food.pop(i)
                    self.food.append(self.rand_food())

    def player_eat_player(self):
        for p1 in self.players:
            for p2 in self.players:
                if self.players[p1].score > self.players[p2].score and self.players[p1].can_eat_player(
                        self.players[p2]):  # check wchich ball is bigger and if it is possible to eat it
                    self.players[p1].score += self.players[p2].score
                    self.players[p1].ball.calculate_radius_after_eating(self.players[p2].ball)
                    new_p2_ball = self.get_random_ball(self.START_RADIUS)
                    self.players[p2].create_new(new_p2_ball)  # create new ball in different place afer beeing eaten
                    self.players[p2].score = 0  # reset score

    def eating(self):
        self.food_eating()
        self.player_eat_player()

    def game_end_check(self):
        players_list = list(self.players.values())
        players_list = sorted(players_list, key=lambda p: p.score)
        players_list.reverse()
        if players_list[0].score >= self.WINNER_SCORE:
            for p in self.players:
                new_p_ball = self.get_random_ball(self.START_RADIUS)
                self.players[p].create_new(new_p_ball)
                self.players[p].score = 0 
            