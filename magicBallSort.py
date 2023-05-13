import numpy as np


class Tube:
    def __init__(self, balls, magicTubes=False):
        self.magicTubes = magicTubes
        self.balls = balls

    def state(self):
        print(self.balls)

    def isSorted(self):
        if len(self.balls) != 4:
            return False
        if len(self.balls) == 0:
            return True
        color = self.balls[0]
        for ball in self.balls:
            if color != ball:
                return False
        return True


class GameManager():
    def __init__(self, initState, magicTubes):
        self.tubes = []

        for state in initState:
            balls = []
            for i in range(len(state)):
                if state[i] != 0:
                    balls.append(state[i])

            self.tubes.append(Tube(balls))

        for magicTube in magicTubes:
            self.tubes[magicTube].magicTubes = True

    def move(self, from_tube, to_tube):

        if len(self.tubes[to_tube].balls) == 4 or len(self.tubes[from_tube].balls) == 0:
            print('Invalid Move')
        if self.tubes[from_tube].magicTubes:
            move_ball = self.tubes[from_tube].balls[0]
            self.tubes[from_tube].balls = self.tubes[from_tube].balls[1:]
            self.tubes[to_tube].balls.append(move_ball)
        else:
            move_ball = self.tubes[from_tube].balls[len(
                self.tubes[from_tube].balls) - 1]
            self.tubes[from_tube].balls.pop()
            self.tubes[to_tube].balls.append(move_ball)

    def state(self):
        for tube in self.tubes:
            tube.state()

    def isWin(self):
        for tube in self.tubes:
            if not tube.isSorted():
                return False
        return True

    def run(self):
        while not self.isWin():
            from_tube = input("Move From Tube: ")
            to_tube = input("To Tube: ")
            self.move(int(from_tube), int(to_tube))
        print('You Win')


gameManager = GameManager([[1, 2, 3, 2],
                           [2, 1, 3, 1],
                           [3, 1, 2, 3],
                           [0, 0, 0, 0]], [0])
gameManager.move(0, 3)
gameManager.move(1, 3)
gameManager.move(2, 1)
gameManager.move(2, 0)
gameManager.move(2, 3)
gameManager.move(1, 2)
gameManager.move(1, 2)
gameManager.move(1, 3)
gameManager.move(0, 1)
gameManager.move(0, 2)
gameManager.move(0, 1)
gameManager.move(0, 1)
gameManager.state()
print(gameManager.isWin())
# gameManager.run()
