from difflib import SequenceMatcher
import pprint
pp = pprint.pprint
import numpy
import gym
ALL_ENVS = list(map(str, list(gym.envs.registry.all())))

def env_search(query, n_return=10, _print=False):
    query_results = [x[0] for x in
         sorted(list(map(lambda x: (x, SequenceMatcher(None, query, x).ratio()), ALL_ENVS)), key=lambda x: x[1],
                reverse=True)][:n_return]
    if _print:
        pp(query_results)

    return query_results
