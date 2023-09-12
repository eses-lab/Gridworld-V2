import numpy as np
from simulator.Gridworld import Gridworld

class Experiment:
    def __init__(self, grid_size, num_agents, num_episodes, batch_size):
        self.grid_size = grid_size
        self.num_agents = num_agents
        self.num_episodes = num_episodes
        self.batch_size = batch_size
        self.gridworld = Gridworld(grid_size, num_agents)

    def run(self):
        for episode in range(self.num_episodes):
            self.gridworld.reset()
            state = self.gridworld.grid.flatten()
            done = False
            while not done:
                actions = [agent.act(state) for agent in self.gridworld.agents]
                next_state, rewards = self.gridworld.step(actions)
                next_state = next_state.flatten()
                for agent, action, reward in zip(self.gridworld.agents, actions, rewards):
                    agent.remember(state, action, reward, next_state, done)
                    if len(agent.memory) > self.batch_size:
                        agent.replay(self.batch_size)
                state = next_state
                if np.sum(state) == self.num_agents:  # All agents have reached their goal
                    done = True
            print(f"Episode {episode + 1}/{self.num_episodes} finished")

    def analyze_results(self):
        # This function should be implemented to analyze the results of the experiment
        total_rewards = []
        for agent in self.gridworld.agents:
            total_rewards.append(sum(agent.memory))
        average_reward = np.mean(total_rewards)
        print(f"Average reward: {average_reward}")
        
        pass
