import random
import copy

import numpy as np

r = 100
rewards = [[r, -1, 10],
           [-1, -1, -1],
           [-1, -1, 200]]
actions = ['Up', 'Down', 'Left', 'Right']
policy = [[0]*3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        policy[i][j] = actions[random.randint(0, 3)]
grid_value = [[0]*3 for _ in range(3)]

def get_next(i,j,action):
    possibles = ['Up', 'Down', 'Left', 'Right']
    if action == 'Up':
        possibles.remove('Down')
    elif action == 'Down':
        possibles.remove('Up')
    elif action == 'Left':
        possibles.remove('Right')
    elif action == 'Right':
        possibles.remove('Left')

    possibles.remove(action)
    possibles.insert(0,action)
    stochastic=random.randint(1,100)
    if(stochastic>90):
        action=possibles[2]
    elif(stochastic>80):
        action=possibles[1]
    else:
        action=possibles[0]

    if action == 'Up':
        next_j = j
        if (i - 1 < 0):
            next_i = 0
        else:
            next_i = i - 1

    elif action == 'Down':
        next_j = j
        if (i + 1 > 2):
            next_i = 2
        else:
            next_i = i + 1

    elif action == 'Left':
        next_i = i
        if (j - 1 < 0):
            next_j = 0
        else:
            next_j = j - 1
    elif action == 'Right':
        next_i = i
        if (j + 1 > 2):
            next_j = 2
        else:
            next_j = j + 1
    return next_i,next_j

def evaluate_policy(policy, rewards, gamma, N):
    global grid_value
    for k in range(N):
        for i in range(3):
            for j in range(3):
                action = policy[i][j]
                next_i,next_j=get_next(i,j,action)
                reward = rewards[next_i][next_j]
                V_pi = reward + gamma * grid_value[next_i][next_j]
                grid_value[i][j] = V_pi


def improve_policy(policy, rewards, gamma):
    global grid_value
    for i in range(3):
        for j in range(3):
            max_value = -1000000
            best_action = 0
            for k in range(4):
                action = actions[k]
                next_i, next_j = get_next(i, j, action)
                value = rewards[next_i][next_j] + gamma * grid_value[next_i][next_j]
                if value > max_value:
                    max_value = value
                    best_action = action

            policy[i][j] = best_action


old_policy = [[0]*3 for _ in range(3)]
i = 0
while (1):
    i = i + 1
    old_policy=copy.deepcopy(policy)
    evaluate_policy(policy, rewards, 0.99, 2000)
    improve_policy(policy, rewards, 0.99)
    if policy == old_policy:
        break
print(i)
print("Policy: ")
print(policy[0])
print(policy[1])
print(policy[2])