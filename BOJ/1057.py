total, kim, im = map(int, input().split())
game_round = 0
while kim != im:
    kim -= kim//2
    im -= im//2
    game_round += 1

print(game_round)
