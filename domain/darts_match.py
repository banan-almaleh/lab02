class DartsMatch:

    def __init__(self, type, player1, player2):
        self.type = type
        self.player1 = player1
        self.player2 = player2

    def __init__(self):
        self.active = True
        self.players = []
        self.last_players_index = -1
        self.visits = []
        self.winning_num_darts = -1
        self.winning_player_index = -1

    def register_player(self, username):
        if username not in self.players:
            index = len(self.players)
            self.players.append(username)
            self.visits.append([])
            return index
        else:
            return -1

