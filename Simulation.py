from matplotlib import pyplot as plt
import math2d as m2d
import numpy as np
import math
from fieldInfo import * #Maybe bad
import helperFunctions as h

import Action as A
import potentialField as pf



def simulateConsequences(action): #Todo Check for Collisions with opp goal and if ball is out
  action_consequencesI = [m2d.Vector2()]*A.numParticles
  for i in range(0, A.numParticles):
    action_consequencesI[i] = pose * action.predict(ballPosition)
    #Check if ball hits the goal contruction for each particle
    intersection1 = h.intersect(ballPosition,action_consequencesI[i], oppGoalBackLeft,oppGoalBackRight)
    intersection2 = h.intersect(ballPosition,action_consequencesI[i], opponentGoalPostLeft,oppGoalBackLeft)
    intersection3 = h.intersect(ballPosition,action_consequencesI[i], opponentGoalPostRight,oppGoalBackRight)

    #Check if ball hits the own goal

    #Check if particle scores a goal
  ActionConsequences.append(action_consequencesI)
  return ActionConsequences

def decide_smart(ActionConsequences):
  #First simple evaluate by potential field
  sumPotentialList = []
  for action in ActionConsequences:
    sumPotential = 0
    for i in range(0, A.numParticles):
      sumPotential += pf.evaluateAction(action[i].x, action[i].y)

    sumPotentialList.append(sumPotential)

  min = 10000
  minIndex = 0
  for i in range(0, len(sumPotentialList)):
    if(sumPotentialList[i] <  min):
      min = sumPotentialList[i]
      minIndex = i
  return minIndex

def drawActions(): #Todo draw good looking field
  plt.clf()
  ax = plt.gca()
  ax.plot([0.0, 0.0], [yPosLeftSideline, yPosRightSideline], "k:")
  ax.plot([xPosOwnGroundline, xPosOpponentGroundline], [0.0, 0.0], "k:")

  #im = plt.imread("export.png")
  #implot = plt.imshow(im)

  plotColor = ['ro','go','bo']
  for idx,action in enumerate(ActionConsequences):
    for i in range(0, A.numParticles):
      plt.plot(action[i].x, action[i].y, plotColor[idx])

  plt.pause(0.001)
  ax.set_aspect("equal")
  #plt.show()

if __name__ == "__main__":

  plt.show(block=False)

  # Robot Position
  pose = m2d.Pose2D()
  rotation = 0
  pose.x = 1000.0
  pose.y = -2000.0
  pose.rotation = math.radians(rotation)

  # Ball Position
  ballPosition = m2d.Vector2()
  ballPosition.x = 0.0
  ballPosition.y = 0.0

  #Test Plot Field
  #xRange = np.linspace(xPosOwnGroundline, xPosOpponentGroundline, 1000)
  #yRange = np.linspace(yPosRightSideline, yPosLeftSideline, 1000)

  sidekick_right = A.Action("sidekick_right", 750, 150, -89.657943335302260, 10.553726275058064)
  sidekick_left = A.Action("sidekick_left", 750, 150, 86.170795364136380, 10.669170653645670)
  kick_short = A.Action("kick_short", 780, 150, 8.454482265522328, 6.992268841997358)

  ActionList = [sidekick_right,sidekick_left, kick_short]

  while True:
    ActionConsequences = []

    #Simulate Consequences
    for action in ActionList:
      ActionConsequences = simulateConsequences(action)

    #Decide best action
    bestAction = decide_smart(ActionConsequences)

    drawActions()