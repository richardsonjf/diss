"""
Class to make the maze in Python
"""

import numpy as np
import Qagent
import operator
import random

class maze:
    def __init__(self):
        self.maze = np.array([
            [ 1,  0,  1,  1,  1,  1,  1,  1,  1,  1],
            [ 1,  1,  1,  1,  1,  0,  1,  1,  1,  1],
            [ 1,  1,  1,  1,  1,  0,  1,  1,  1,  1],
            [ 0,  0,  1,  0,  0,  1,  0,  1,  1,  1],
            [ 1,  1,  0,  1,  0,  1,  0,  0,  0,  1],
            [ 1,  1,  0,  1,  0,  1,  1,  1,  1,  1],
            [ 1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
            [ 1,  1,  1,  1,  1,  1,  0,  0,  0,  0],
            [ 1,  0,  0,  0,  0,  0,  1,  1,  1,  1],
            [ 1,  1,  1,  1,  1,  1,  1,  0,  1,  1]
        ])
        self.row = 10
        self.col = 10
        self.agentLocation = (0, 0)
        self.moves = {"Up": (1, 0), "Down": (-1, 0), "Left": (0, -1), "Right": (0, 1)}
        self.action = (0, 0)

    def getMaze(self):
        return self.maze
    def getSizeOfMaze(self):
        return len(self.maze)
    def getRandomMove(self):
            legalMoves = self.getLegalMoves()
            return random.choice(list(legalMoves.values()))
    def vectorAddition(self, tup1, tup2):
        # since we want to add coords together element wise
        # (0, 0) + (1, 1) = (0, 0, 1, 1). this makes the result (1, 1).
        if tup1 == 0:
            tup1 == self.agentLocation
        if tup2 == 0:
            tup2 = self.getRandomMove()
        return tuple(map(operator.add, tup1, tup2))
    def setAgentLocation(self, location):
        # keeps a record of where the agent is currently located
        self.agentLocation = location
    def getAgentLocation(self):
        return self.agentLocation
    def agentMovement(self, action):
        # Moves the agent
        # gets first coords from action, and adds that to agents current location
        # agent can only make legal moves
        if isinstance(action, dict):
            opt = action[next(iter(action))]
        else:
            opt = action
        if action == 0:
            opt = self.getRandomMove()
        ret = self.vectorAddition(opt, self.getAgentLocation())
        self.setAgentLocation(ret)
    def getLegalMoves(self):
        # 0 is a wall
        # 1 is valid
        moves = self.moves
        legalMoves = {}
        for move in self.moves:
            try:
                newCoords = self.vectorAddition(self.agentLocation, moves[move])
                # checks to see if there is an illegal move
                negativeCoords = True if any(y < 0 for y in newCoords) else False
                outsideMap = True if any(y > len(self.maze[0]) - 1 for y in newCoords) else False
                illegalMove = True if negativeCoords + outsideMap == True else False
                if not illegalMove and newCoords != 0:
                    legalMoves[move] = moves[move]
                    # append to dictionary
                    
            except IndexError as e:
                # Not a valid move as it goes out of bounds
                continue
        # returns dictionary of legal moves
        # (0, 0) input
        # {'Up': (1, 0), 'Right': (0, 1)} output
        return legalMoves

if __name__ == '__main__':
    m = maze()
    a = Qagent.agent(m)
    a.run()