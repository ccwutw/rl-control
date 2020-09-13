#!/usr/bin/env python
# -*- coding: utf-8 -*-

import agent as ag
import sumoenv as se

env_train = se.SumoEnv(gui_f=False)
env_test = se.SumoEnv(gui_f=True)
agent = ag.Agent()

EPS = 2

for ieps in range(EPS):
    for i in range(20):
        print "Start Training"
        state = env_train.reset()
        done = False
        while not done:
            action = agent.policy(state)
            next_state, reward, done, rewards = env_train.step_d(action)

            agent.train(state, action, reward, 0.001, [1, 1, done, 1, 1])

            state = next_state
        print "Stop Training"
        env_train.close()

    print "Start Testing"
    state = env_test.reset()
    done = False
    while not done:
        action = agent.policy(state)
        next_state, reward, done, rewards = env_test.step_d(action)
        print(state)

        state = next_state
    print "Stop Testing"
    env_test.close()

