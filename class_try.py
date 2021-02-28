import json
file = 'lobby_data2.json'

with open(file) as f:
    nums = json.load(f)


class Player:
    def __init__(self, name, kills):
        self.name = name
        self.kills = kills


class Team:
    def __init__(self, team, place):
        self.team = team
        self.place = place
        self.total_kills = 0
        self.players = []

    def add_player(self, name, kills):
        self.players.append(Player(name, kills))
        self.total_kills += kills

    def __repr__(self):
        _players = [(i.name, i.kills,) for i in self.players]
        return f'============================\n' \
               f'Team name: {self.team}\n' \
               f'Team place: {self.place}\n' \
               f'Total Kills: {self.total_kills}\n'\
               f'Players: {_players}'

    def get_players(self):
        return self.players


matches = nums.get("matches")

if __name__ == '__main__':
    out_dict = {}
    for match in matches:
        for result in match.get("player_results"):
            name = result.get("playerName")
            team = result.get("teamName")
            kills = result.get("kills")
            place = result.get("teamPlacement")
            if team in out_dict.keys():
                out_dict[team].add_player(name, kills)
            else:
                out_dict.update({team: Team(team, place)})
                out_dict[team].add_player(name, kills)
            sorted(out_dict, key=out_dict.get(place))

    sort_dict = {}
    for i in out_dict.items():
        sort_dict.update({i[1].place: i[1]})

    sort = sorted(sort_dict)
    for i in sort:
        print(sort_dict[i])
