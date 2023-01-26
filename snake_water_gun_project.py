import random
def match(c, m):
    if (comp == mine):
        return None
    elif (comp == 's' and mine == 'g'):
        return True
    elif (comp == 'w' and mine == 's'):
        return True
    elif (comp == 'g' and mine == 'w'):
        return True
    else:
        return False


scoreComp = 0
scoreMine = 0
choice = ('s', 'w', 'g')
mine = ""
while (True):
    comp = choice[random.randint(0, 2)]
    mine = input("Choose from 's' 'w' and 'g' | Press 'e' to END to game\nPress 'r' to reset the score\n")
    if mine == 'e':
        break
    while (mine != 's' and mine != 'w' and mine != 'g' and mine != 'e' and mine != 'r'):
        mine = input(
            "Invalid Choice! Enter valid choice from 's' 'w' 'g' 'r' and 'e'!!!!\n")
    result = match(comp, mine)
    if(mine=="r"):
        scoreMine=0
        scoreComp=0
        print("Now Score is Zero for both player\n")
        continue
    if result is None:
        print(f"You Chose {mine} and Computer chose {comp}, Match Drawn!\n")
        pass
    elif result:
        print(f"You Chose {mine} and Computer chose {comp}, You WIN!\n")
        scoreMine += 1
    else:
        print(f"You Chose {mine} and Computer chose {comp}, You LOOSE!\n")
        scoreComp += 1
print(f"\nScore:\nYours -> {scoreMine}\nComputer -> {scoreComp}")
if scoreMine>scoreComp:
    print("You Win!🎉")
elif scoreMine<scoreComp:
    print("You LOOSE😫 Computer Win!")
else:
    print("Match Tie!")
