import gymnasium as gym

env = gym.make('HalfCheetah-v4')

env.reset()

for _ in range(1000):
    action = env.action_space.sample() # Replace with your own agent's action
    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated: 
        observation, info = env.reset()

env.close()