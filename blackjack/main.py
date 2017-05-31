import blackjack_interface

game = blackjack_interface.Game()

players = game.start_game()

num_players = len(players.keys()) -1

for i in range(1, num_players+1):
    print('Player ' + str(i) + '\n')
    players[i].display_hand()
    score = game.score_hand(players[i])
    print('score: ' + str(score))
    stay = False
    bust =False
    while stay == False and bust == False:
        query = input('1. hit \n'
                      '2. stay \n')

        if query == '1':
            players[i].add_card(game.deck.draw_card())
            players[i].display_hand()
            if game.score_hand(players[i]) > 21:
                print('{} Busted!'.format(game.score_hand(players[i])))
                bust = True
            else:
                print('{} \n'.format(game.score_hand(players[i])))

        if query == '2':
            stay = True
cont = True
while cont == True:
    if game.score_hand(players[0]) < 16:
        players[0].add_card(game.deck.draw_card())
    else:
        cont = False

print('Dealer: ')
players[0].display_hand()
score = game.score_hand(players[0])
if score < 22:
    print('score: {} \n'.format(score))
elif score > 21:
    print('bust')

final_scores = {"dealer": game.score_hand(players[0])}

if final_scores['dealer'] > 21:
    print('dealer:' + ' bust \n')
for i in range(1, num_players+1):
    if game.score_hand(players[i]) < 22:
        final_scores['player' + str(i)] = game.score_hand(players[i])
        if final_scores['player' + str(i)] > final_scores["dealer"]:
            print('player' +str(i) +': winner \n')
        elif final_scores["dealer"] > 21:
            print('player' + str(i) + ': winner \n')
        elif final_scores['player' + str(i) ]== final_scores["dealer"]:
            print('player' + str(i) + ': push \n')
        else:
            print('player' + str(i) + ': lost \n')

    else:
        final_scores['player' + str(i)] = 0
        print('player' + str(i) + ': bust \n')

