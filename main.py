from experiments.Experiment import Experiment
from analysis.ResultAnalysis import ResultAnalysis

def main():
    # Define experiment parameters
    grid_size = 10
    num_agents = 5
    num_episodes = 1000
    batch_size = 32

    # Run the experiment
    experiment = Experiment(grid_size, num_agents, num_episodes, batch_size)
    experiment.run()

    # Analyze the results
    analysis = ResultAnalysis(experiment)
    analysis.analyze()

if __name__ == "__main__":
    main()
