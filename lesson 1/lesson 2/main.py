from character import Character

player1 = Character(name='Vasya', health=5000, damage=500, defence=250)
player2 = Character(name='Minik', health=6000, damage=600, defence=300)
player3 = Character(name='Groznii', health=7000, damage=700, defence=350)
player4 = Character(name='Mini_Boss', health=10000, damage=2000, defence=1000)

print(player1)
print(player2)
print(player3)
print(player4)

print('------------------------------------------')

player1.attack(player2)
player2.attack(player1)

print(player1)
print(player2)
