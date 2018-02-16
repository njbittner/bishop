from difflib import SequenceMatcher
import pprint
pp = pprint.pprint
import numpy
import gym
ALL_ENVS = list(map(str, list(gym.envs.registry.all())))

def do_rollout(agent, env, num_steps, render=False, render_step=2):
    total_reward = 0
    initial_observation = env.reset()
    obs = initial_observation
    for t in range(num_steps):
        agent_action = agent.act(obs)
        ob, reward, done, _info = env.step(agent_action)
        total_reward += reward
        if render and t%render_step==0: env.render()
        if done: break
    return total_reward, t+1

def env_search(query, n_return=5, _print=False):
    query_results = [x[0] for x in
         sorted(list(map(lambda x: (x, SequenceMatcher(None, query, x).ratio()), ALL_ENVS)), key=lambda x: x[1],
                reverse=True)][:n_return]
    if _print:
        pp(query_results)

    return query_results
