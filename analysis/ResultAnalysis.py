import matplotlib.pyplot as plt
import numpy as np
from experiments.Experiment import Experiment

class ResultAnalysis:
    def __init__(self, experiment):
        if not isinstance(experiment, Experiment):
            raise ValueError("experiment must be an instance of the Experiment class")
        self.experiment = experiment

    def plot_rewards(self):
        rewards = []
        for agent in self.experiment.gridworld.agents:
            rewards.append([memory[2] for memory in agent.memory])  # Extract rewards from agent's memory

        # Calculate average reward per episode
        avg_rewards = np.mean(rewards, axis=0)

        plt.plot(avg_rewards)
        plt.title('Average Reward per Episode')
        plt.xlabel('Episode')
        plt.ylabel('Average Reward')
        plt.show()

    def plot_actions(self):
        actions = []
        for agent in self.experiment.gridworld.agents:
            actions.append([memory[1] for memory in agent.memory])  # Extract actions from agent's memory

        # Calculate action distribution
        action_counts = np.bincount(np.concatenate(actions))

        plt.bar(range(len(action_counts)), action_counts)
        plt.title('Action Distribution')
        plt.xlabel('Action')
        plt.ylabel('Count')
        plt.show()

    def analyze(self):
        self.plot_rewards()
        self.plot_actions()
