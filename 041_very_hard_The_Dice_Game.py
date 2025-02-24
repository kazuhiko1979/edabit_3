"""
The Dice Game
Four friends are playing a simple dice game (players are denoted p1, p2, p3 and p4). In each round, all players roll a pair of six-sided dice. The player with the lowest total score is removed. If the lowest score is shared by two or more players, the player in that group with the lowest score from their first dice is removed. If the lowest score is still shared (i.e. two or more players have the same rolls in the same order), then all players roll again. This process continues until one player remains. Given a list of scores only (given in player order for each round), return the winning player.

Example
dice_game([(6, 2), (4, 3), (3, 4), (5, 4), (3, 5), (1, 5), (4, 3), (1, 5), (1, 5), (5, 6), (2, 2)]) ➞ "p1"

             p1      p2      p3      p4
Round 1 -> (6, 2), (4, 3), (3, 4), (5, 4)  Player 3 removed.
Round 2 -> (3, 5), (1, 5),         (4, 3)  Player 2 removed.
Round 3 -> (1, 5),                 (1, 5)  No lowest score, players roll again.
Round 4 -> (5, 6),                 (2, 2)  Player 1 wins!
"""


def dice_game(scores):
    players = ['p1', 'p2', 'p3', 'p4']
    
    while len(players) > 1:
        results = list(zip(players, scores))
        scores = scores[len(players):]
        results.sort(key=lambda x: (sum(x[1]), x[1][0]))
        if results[0][1] != results[1][1]:
            players.remove(results[0][0])
    return players[0]

# def dice_game(scores):
#     players = ["p" + str(i+1) for i in range(4)]  # プレイヤーリスト
#     round_number = 1
    
#     while len(players) > 1:
#         total_scores = [sum(scores[i]) for i in range(len(players))]
#         min_score = min(total_scores)
        
#         # 最小スコアを持つプレイヤーを特定
#         candidates = [i for i, score in enumerate(total_scores) if score == min_score]
        
#         if len(candidates) == 1:
#             eliminated_index = candidates[0]  # 1人ならそのまま脱落
#         else:
#             first_dice_scores = [scores[i][0] for i in candidates]
#             min_first_dice = min(first_dice_scores)
#             sub_candidates = [candidates[i] for i, score in enumerate(first_dice_scores) if score == min_first_dice]
            
#             if len(sub_candidates) == 1:
#                 eliminated_index = sub_candidates[0]  # 1人ならそのまま脱落
#             else:
#                 # すべてのダイスが同じ場合は振り直し
#                 scores = scores[len(players):]  # 次のデータにスライド
#                 continue
        
#         # 脱落者を削除（スコアを先に削除して、インデックスずれを防ぐ）
#         del scores[eliminated_index]
#         del players[eliminated_index]
        
#         round_number += 1
    
#     return players[0]  # 最後に残ったプレイヤーが勝者

    
print(dice_game([(1, 3), (2, 6), (6, 3), (5, 6), (2, 2), (5, 6), (5, 4), (1, 3), (5, 6)])) # 'p4')
print(dice_game([(4, 4), (4, 3), (1, 1), (1, 1), (3, 1), (4, 5), (2, 6), (2, 3), (1, 5), (5, 3), (4, 5), (5, 2), (2, 1)])) # 'p3')
print(dice_game([(6, 1), (4, 3), (2, 5), (1, 4), (6, 2), (2, 5), (1, 4), (6, 4), (4, 3)])) # 'p1')
print(dice_game([(1, 2), (2, 1), (4, 4), (1, 2), (1, 3), (1, 5), (2, 1), (4, 1), (5, 6), (5, 1), (4, 2), (5, 2), (5, 1)])) # 'p1')
print(dice_game([(1, 2), (5, 6), (1, 3), (6, 5), (4, 6), (1, 3), (1, 3), (5, 3), (4, 1), (1, 1), (3, 3), (4, 1)])) # 'p2')
print(dice_game([(1, 2), (2, 3), (5, 4), (4, 4), (5, 2), (1, 1), (3, 6), (4, 4), (2, 2)])) # 'p2')
print(dice_game([(1, 4), (4, 2), (3, 5), (4, 2), (1, 2), (1, 2), (2, 4), (3, 5), (4, 1), (2, 2), (1, 1), (1, 1), (4, 3), (1, 1)])) # 'p2')
print(dice_game([(2, 6), (3, 6), (6, 3), (6, 5), (4, 5), (5, 3), (5, 6), (2, 6), (6, 5)])) # 'p4')
print(dice_game([(1, 1), (4, 3), (2, 1), (6, 2), (3, 2), (3, 2), (4, 2), (2, 1), (6, 5), (6, 2), (4, 5), (4, 5), (5, 3), (3, 3)])) # 'p3')
print(dice_game([(5, 1), (2, 6), (1, 6), (6, 4), (3, 4), (2, 5), (6, 1), (3, 2), (4, 1)])) # 'p4')
print(dice_game([(1, 4), (3, 6), (1, 6), (6, 1), (4, 1), (4, 3), (6, 5), (5, 6), (5, 6), (2, 1), (2, 4)])) # 'p4')
print(dice_game([(1, 3), (6, 5), (5, 4), (5, 4), (2, 2), (4, 6), (4, 1), (5, 5), (4, 5)])) # 'p3')
print(dice_game([(2, 3), (3, 6), (5, 4), (3, 1), (2, 5), (1, 5), (5, 3), (4, 3), (2, 1)])) # 'p1')
print(dice_game([(4, 2), (4, 4), (1, 4), (1, 4), (1, 3), (3, 5), (6, 5), (1, 2), (5, 1), (6, 1), (2, 4), (2, 4), (5, 4)])) # 'p2')
print(dice_game([(2, 5), (4, 1), (2, 1), (4, 4), (6, 5), (4, 4), (1, 4), (3, 1), (1, 5)])) # 'p2')
print(dice_game([(6, 3), (5, 5), (2, 3), (6, 6), (2, 5), (5, 1), (4, 4), (2, 2), (1, 3)])) # 'p1')
print(dice_game([(6, 2), (6, 1), (6, 1), (2, 2), (1, 1), (4, 3), (2, 6), (4, 6), (4, 6), (3, 4), (3, 5)])) # 'p3')
print(dice_game([(1, 6), (3, 2), (3, 4), (1, 2), (4, 1), (4, 2), (2, 5), (4, 1), (5, 1)])) # 'p3')
print(dice_game([(3, 4), (2, 5), (5, 5), (2, 5), (6, 4), (6, 5), (6, 2), (6, 2), (3, 5), (6, 4), (4, 2), (5, 2), (3, 2), (6, 4), (1, 2), (5, 4), (5, 5)])) # 'p2')
print(dice_game([(1, 5), (3, 1), (2, 3), (5, 3), (1, 2), (1, 2), (6, 3), (2, 2), (6, 3), (2, 2), (5, 5), (3, 1), (3, 1), (6, 6), (6, 4), (5, 3), (3, 4), (6, 4)])) # 'p3')