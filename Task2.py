import random


class Environment:
    def __init__(self):
        self.systems = {}
        for i in range(5):
            server = i + 1
            if i < 2:
                self.systems[server] = 0  # 0 = Underloaded
            elif i == 2:
                self.systems[server] = 1  # 1 = Balanced
            else:
                self.systems[server] = 2  # 2 = Overloaded

    def get_percept(self, index):
        return (
            "Balanced"
            if self.systems[index]==1
            else "Overloaded" if self.systems[index] == 2 else "Underloaded"
        )


class Agent:
    def __init__(self):
        pass

    def scan(self, percept):
        if percept == "Balanced":
            return "balanced server"
        elif percept == "Overloaded":
            return "overloaded server"
        else:
            return "underloaded server"

    def load_balancer(self, env):
        for i in env.systems:
            if env.systems[i] == 2:
                for j in env.systems:
                    if env.systems[j] == 0:
                        env.systems[j] = 1
                env.systems[i] = 1


def display(numb, str):
    print(f"Server {numb} is an {str}")


def run_agent(env, agent):
    for i in range(5):
        percept = env.get_percept(i+1)
        action = agent.scan(percept)
        display(i + 1, action)
    print("\nScanning Complete. Balancing loaded servers")
    agent.load_balancer(env)
    print("\nBalancing Complete. Scanning servers again\n")
    for i in range(5):
        percept = env.get_percept(i+1)
        action = agent.scan(percept)
        display(i + 1, action)


env = Environment()
agent = Agent()

run_agent(env, agent)
