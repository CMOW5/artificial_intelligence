# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).
from re import search


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    from game import Directions
    from util import Stack
    import itertools

    strategy = 'dfs';
    fringe = Stack()
    fringe.push([problem.getStartState(),[],0])
    actions = graphSearch(problem, fringe, strategy)
    return actions

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    from util import Queue
    import itertools

    strategy = "bfs"
    fringe = Queue()
    fringe.push([problem.getStartState(), [], 0])
    actions = graphSearch(problem, fringe, strategy)
    return actions
          

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    from util import PriorityQueue
    import itertools

    strategy = "ucs"
    fringe = PriorityQueue()
    fringe.push([problem.getStartState(), [], 0], 0)
    actions = graphSearch(problem, fringe, strategy)
    return actions


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    from util import PriorityQueue
    import itertools

    strategy = 'astar'
    fringe = PriorityQueue()
    fringe.push([problem.getStartState(), [], 0], 0)
    actions = graphSearch(problem, fringe, strategy, heuristic)
    return actions

    util.raiseNotDefined()

def graphSearch(problem, fringe, strategy, heuristic=nullHeuristic):
    closed = set()

    while True:
        if fringe.isEmpty():
            print "Failure, fringe is empty"
            return []

        node = removeFront(fringe, strategy)
        state = node[0]

        if problem.isGoalState(state):
            path = node[1]
            print 'path = ', path
            print 'steps = ', len(path)
            # return []
            return path

        if not state in closed:
            closed.add(state)
            for child_node in problem.getSuccessors(state):
                fringe = insert(problem, fringe, strategy, heuristic, node, child_node)  # push in fringe

    util.raiseNotDefined()

def removeFront(fringe, strategy):
    node = fringe.pop()
    return node

"""inserts a new node into the fringe .

   Args:
       node: the current removed node.
       [state, [path to state], cost]
       
       childNode: the current state childNode
       [state, action, cost]
       
       fringe: the current fringe
       [node1, node2, node3, ...]
       
       strategy: the insertion strategy
       'dfs', 'bfs', 'ucs', 'astar'

   Returns:
       the new fringe
   """
def insert(problem, fringe, strategy, heuristic, node, childNode):

    nodeCost = node[2]
    childNodeCost = childNode[2]
    newState = childNode[0]
    newAction = childNode[1]
    path = list(node[1]) #copy node[1] to path
    path.append(newAction)

    if (strategy == 'ucs'):
        cumulativeCost = nodeCost + childNodeCost
        fringe.push([newState, path, cumulativeCost], cumulativeCost)

    elif (strategy == 'astar'):
        nextPosition = childNode[0]
        h = heuristic(nextPosition, problem)
        g = nodeCost + childNodeCost
        f = g + h
        fringe.push([newState, path, g], f)

    elif (strategy == 'dfs' or strategy == 'bfs'):
        fringe.push([newState, path, childNodeCost])

    return fringe


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
