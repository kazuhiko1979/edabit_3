"""
Broken Bridge
A broken bridge can be represented by 1s and 0s, where contiguous 0s represent holes. You can walk across a bridge with a hole with a maximum width of 1, but any holes bigger than that you must fix first. For example, the bridge below is walkeable:

[1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1]
This bridge is not:

[1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
You own several wooden planks, each with different widths. You can patch the holes on the bridge with these planks. More specifically, a plank size n can fill a n-sized hole. If you had a plank of size 2, the un-walkeable bridge above could be filled in:

[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
But even if you only had a plank of size 1, you could still transform the unwalkeable bridge into a walkeable one:

[1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
Write a function that takes in a broken bridge, a list of plank sizes, and returns True if the bridge can be patched up enough to walk over, and False otherwise.

Examples
can_patch([1, 0, 0, 0, 0, 0, 0, 1], [5, 1, 2]) ➞ True
# You can use the 5 plank to transform the 6 hole to a 1 hole.
# Leftover planks [1, 2] are okay.

can_patch([1, 0, 0, 0, 0, 0, 0, 1], [4, 1, 2, 3, 4]) ➞ False
# None of your planks are long enough (you can't combine them).

can_patch([1, 0, 0, 1, 1, 0, 0, 0, 1], [1, 2]) ➞ True

can_patch([1, 0, 0, 1, 1, 0, 0, 0, 1], [1, 1]) ➞ False
"""
def can_patch(bridge, planks):
    """
    1. bridge(0と1のリスト)を文字列に直す
    2. '1' で区切って、連続した0の長さリスト holes を得る
    3. holesが全部1以下なら、そのまま渡れる(True)
    4. そうでなければ、穴の長さ i に対して板サイズが i か (i-1) の枚数を調べ、
       すべての穴を埋め(もしくは1マスだけ残す)だけの板があればOK(True)、なければNG(False)
    """

    # 1) bridge リストを文字列に変換
    bridge_str = ""
    for x in bridge:
        bridge_str += str(x)

    # 2) '1'で区切って、それぞれの長さを holes に入れる
    parts = bridge_str.split('1')  # 例: "1001" -> ["", "00", ""]
    holes = []
    for part in parts:
        holes.append(len(part))  # 例: ["", "00", ""] -> [0, 2, 0]

    # 3) 全部1以下なら修理不要でOK
    #    (2以上の穴があればジャンプだけでは無理)
    all_small = True
    for hole_size in holes:
        if hole_size > 1:
            all_small = False
            break
    if all_small:
        return True

    # 4) 2以上の穴に対応できるだけの板があるかチェック
    #    「穴の長さ i には、板サイズ i か (i-1) を使える」
    #    なので、穴がいくつあるか vs そのサイズの板(または -1)が何枚あるか、を比べる。
    for hole_size in set(holes):
        if hole_size > 1:
            need_count = holes.count(hole_size)  # 長さ hole_size の穴がいくつあるか
            # 「板サイズ hole_size または (hole_size - 1)」が何枚あるか
            have_count = planks.count(hole_size) + planks.count(hole_size - 1)

            # 必要な数より板が少なければアウト
            if have_count < need_count:
                return False

    # 全部カバーできれば True
    return True


# --- 動作チェック ---
print(can_patch([1, 0, 0, 0, 0, 0, 0, 1], [5, 1, 2]))        # True
print(can_patch([1, 0, 0, 0, 0, 0, 0, 1], [4, 1, 2, 3, 4]))  # False
print(can_patch([1, 0, 0, 1, 1, 0, 0, 0, 1], [1, 2]))        # True
print(can_patch([1, 0, 0, 1, 1, 0, 0, 0, 1], [1, 1]))        # False





# def can_patch(bridge, planks):
#     # 1) 連続した0のかたまりの長さを取得
#     zero_runs = []
#     current_run = 0
    
#     for cell in bridge:
#         if cell == 0:
#             current_run += 1
#         else:
#             if current_run > 0:
#                 zero_runs.append(current_run)
#             current_run = 0
#     # ループ後に最後が0で終わっていたら、そのrunを追加
#     if current_run > 0:
#         zero_runs.append(current_run)
    
#     zero_runs = [run for run in zero_runs if run > 1]
    
#     # 3) それぞれの長さを満たすplankがあるか確認
#     if not zero_runs:
#         return True
    
#     # 3) 大きいかたまりから先に処理
#     zero_runs.sort(reverse=True)
    
#     planks.sort(reverse=True)
    
#     # 4) かたまりを順番に修復していく
#     for run_length in zero_runs:
#         # 1以下ならそのまま通過
#         if run_length <= 1:
#             continue
#         # run_length >= 2のときはrun_length-1以下のplankを探す
#         needed = run_length - 1
        
#         # 使える板を探す
#         used_index = -1
#         for idx, plank_size in enumerate(planks):
#             if plank_size >= needed:
#                 used_index = idx
#                 break
        
#         if used_index == -1:
#             # 使える板が無いので修復不可能
#             return False
        
#         # 板を使う
#         planks.pop(used_index)
        
#     # 最後まで修復できたらTrue
#     return True
        
    

# --- テスト ---
# print(can_patch([1, 0, 0, 0, 0, 0, 0, 1], [5, 1, 2]))  # True
# print(can_patch([1, 0, 0, 0, 0, 0, 0, 1], [4, 1, 2, 3, 4]))  # False
# print(can_patch([1, 0, 0, 1, 1, 0, 0, 0, 1], [1, 2]))  # True
# print(can_patch([1, 0, 0, 1, 1, 0, 0, 0, 1], [1, 1]))  # False