def team_lineup(*args):
    players = {}
    for player_name, country in args:
        if country not in players:
            players[country] = []
        players[country].append(player_name)

    sorted_players = sorted(players.items(), key=lambda x: (len(x[1]), x[0]), reverse=True)

    result = ''
    for country, players in sorted_players:
        result += f'{country}:\n'
        for player in players:
            result += f'  -{player}\n'

    return result


print(team_lineup(

   ("Lionel Messi", "Argentina"),

   ("Neymar", "Brazil"),

   ("Cristiano Ronaldo", "Portugal"),

   ("Harry Kane", "England"),

   ("Kylian Mbappe", "France"),

   ("Raheem Sterling", "England")))
