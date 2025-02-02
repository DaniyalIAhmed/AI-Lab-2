import random


class Environment:
    def __init__(self):
        self.tasks = {}
        for i in range(1, 6):
            self.tasks[i] = random.choice(["Completed", "Failed"])

    def get_percept(self, index):
        return self.tasks[index]


class Agent:
    def __init__(self):
        pass

    def scan(self, percept):
        if percept == "Completed":
            return "successful backup"
        else:
            return "failed backup"
    def retry(self, env):
        for i in env.tasks:
            if env.tasks[i] == "Failed":
                env.tasks[i] = "Completed"

def run_agent(env, agent):
    for i in range(1,6):
        percept = env.get_percept(i)
        action = agent.scan(percept)
        display(i, action)
    print("\nScanning Complete. Rerunning failed backups")
    agent.retry(env)
    print("\nComplete. Scanning servers again\n")
    for i in range(1,6):
        percept = env.get_percept(i)
        action = agent.scan(percept)
        display(i, action)


def display(numb, str):
    print(f"Server {numb} has {str}")


env = Environment()
agent = Agent()
run_agent(env, agent)