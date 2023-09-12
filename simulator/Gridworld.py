import numpy as np
from agents.Agent import Agent

class Gridworld:
    def __init__(self, grid_size, num_agents):
        self.grid_size = grid_size
        self.num_agents = num_agents
        self.agents = [Agent(state_size=grid_size*grid_size, action_size=4) for _ in range(num_agents)]
        self.grid = np.zeros((grid_size, grid_size))

    def reset(self):
        self.grid = np.zeros((self.grid_size, self.grid_size))
        for agent in self.agents:
            # Place each agent in a random position in the grid
            x, y = np.random.randint(0, self.grid_size, 2)
            self.grid[x, y] = 1
            agent.position = (x, y)

    def step(self, actions):
        rewards = []
        for agent, action in zip(self.agents, actions):
            x, y = agent.position
            self.grid[x, y] = 0  # Remove agent from current position

            # Update agent position based on action
            if action == 0:  # Move up
                x = max(0, x - 1)
            elif action == 1:  # Move right
                y = min(self.grid_size - 1, y + 1)
            elif action == 2:  # Move down
                x = min(self.grid_size - 1, x + 1)
            elif action == 3:  # Move left
                y = max(0, y - 1)

            agent.position = (x, y)
            self.grid[x, y] = 1  # Place agent in new position

            # Get reward from smart contract
            reward = agent.get_reward()
            rewards.append(reward)

        return self.grid, rewards

    def render(self):
        print(self.grid)
