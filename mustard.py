from random import randint
from time import sleep
from sausages import *

def fight(currentEnemy):
    round=randint(1, 2)
    enemy=pbar65[currentEnemy]
    hpEnemy=pbar65[currentEnemy]["HP"]
    print(f"Battle started: {currentEnemy}")
    input("press S↵ to begin")
    while player["HP"]>1 and hpEnemy>0:
        if round % 2 == 1:
            print("* Player attacks Enemy *")
            chance=randint(3, 101)
            if chance < player["luck"]:
                hpEnemy -= player["Attack"]*3
            else:
                hpEnemy -= player["Attack"]
        else:
            player["HP"] -= enemy["Attack"]