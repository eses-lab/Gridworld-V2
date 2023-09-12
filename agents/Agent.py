import numpy as np
import random
import torch
from torch import nn
from torch import optim
from web3 import Web3
from solc import compile_source
import json

class Agent:
    def __init__(self, state_size, action_size, learning_rate=0.01, gamma=0.99):
        self.state_size = state_size
        self.action_size = action_size
        self.learning_rate = learning_rate
        self.gamma = gamma

        # Initialize Q-network
        self.model = nn.Sequential(
            nn.Linear(self.state_size, 24),
            nn.ReLU(),
            nn.Linear(24, 24),
            nn.ReLU(),
            nn.Linear(24, self.action_size)
        )

        self.optimizer = optim.Adam(self.model.parameters(), lr=self.learning_rate)
        self.criterion = nn.MSELoss()

        # Initialize replay memory
        self.memory = []

        # Initialize Ethereum client
        self.web3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
        if self.web3.isConnected():
            print("Connected to Ethereum network")
        else:
            print("Failed to connect to Ethereum network")

        # Initialize the smart contracts
        with open('contracts/GridCoinABI.json', 'r') as f:
            gridCoinABI = json.load(f)
        with open('contracts/IncentiveABI.json', 'r') as f:
            incentiveABI = json.load(f)

        gridCoinAddress = self.web3.toChecksumAddress('0xB045c3a1a7Feb7a500d182d51748f01CA204a7EE')  # Replace with your GridCoin contract address
        incentiveAddress = self.web3.toChecksumAddress('0x7899cB2Ae7891687e3C2baDA2DC6c7E779dc4bb6')  # Replace with your Incentive contract address

        self.gridCoinContract = self.web3.eth.contract(address=gridCoinAddress, abi=gridCoinABI)
        self.incentiveContract = self.web3.eth.contract(address=incentiveAddress, abi=incentiveABI)

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        state = torch.from_numpy(state).float().unsqueeze(0)
        with torch.no_grad():
            action_values = self.model(state)
        return np.argmax(action_values.cpu().data.numpy())

    def replay(self, batch_size):
        minibatch = random.sample(self.memory, batch_size)
        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                next_state = torch.from_numpy(next_state).float().unsqueeze(0)
                target = (reward + self.gamma * np.amax(self.model(next_state).detach().numpy()))
            state = torch.from_numpy(state).float().unsqueeze(0)
            target_f = self.model(state)
            target_f[0][action] = target
            self.optimizer.zero_grad()
            loss = self.criterion(target_f, self.model(state))
            loss.backward()
            self.optimizer.step()

    def get_reward(self):
        # Call the smart contract to get the reward for this agent
        reward = self.contract.functions.rewards(self.web3.eth.defaultAccount).call()
        return reward

