def practice_6_1():

    MEM = 70
    SUB = 3

    scores = []

    for i in range(MEM):
        sub = []
        sub.append((i * 87 + 71) % 101)
        sub.append((i * 79 + 23) % 101)
        sub.append((i * 59 + 55) % 101)
        scores.append(sub)

    sub_totals = [0] * SUB

    for p in scores:
        for i in range(SUB):
            sub_totals[i] += p[i]

    for i in range(SUB):
        print(f"科目{i+1}:{sub_totals[i] / MEM:.2f}")

practice_6_1()