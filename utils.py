from difflib import SequenceMatcher
import numpy
import gym
ALL_ENVS = list(map(str, list(gym.envs.registry.all())))

def env_search(query):
    return [x for x in ALL_ENVS if SequenceMatcher(None, query, x).ratio() > 0.2]
