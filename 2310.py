class Team():
    def __init__(self):
        self.players = []
        self.serve = 0
        self.serve_points = 0
        self.block = 0
        self.block_points = 0
        self.attack = 0
        self.attack_points = 0
    
    def serve_point_chance(self):
        chance = (self.serve_points / self.serve) * 100
        return chance
        
    def block_point_chance(self):
        chance = (self.block_points / self.block) * 100
        return chance

    def attack_point_chance(self):
        chance = (self.attack_points / self.attack) * 100
        return chance

def main():
    
    players_on_team = int(input())
    team = Team()
    
    while players_on_team > 0:
        name_player = input()
        serve_tried, block_tried, attack_tried = map(int, input().split())
        serve_points, block_points, attack_points = map(int, input().split())
        
        team.players.append(name_player)
        
        team.serve += serve_tried
        team.block += block_tried
        team.attack += attack_tried
        
        team.serve_points += serve_points
        team.block_points += block_points
        team.attack_points += attack_points
        
        players_on_team -= 1
    
    print('Pontos de Saque:', '%.2f' %team.serve_point_chance(), '%.')
    print('Pontos de Bloqueio:', '%.2f' %team.block_point_chance(), '%.')
    print('Pontos de Ataque:', '%.2f' %team.attack_point_chance(), '%.')

if __name__ == '__main__':
    main()
