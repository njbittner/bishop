import gym
from gym import wrappers, logger
import numpy as np
import argparse
import utils
import agents


if __name__ == "__main__":
    logger.set_level(logger.DEBUG)
    parser = argparse.ArgumentParser()
    parser.add_argument("--display", action='store_true')
    parser.add_argument('target', nargs='?', default="CartPole-v1")
    args = parser.parse_args()
    env = gym.make(args.target)

    agent = agents.RandomAgent(env.action_space)
    utils.do_rollout(agent, env, 1000, render=True)


