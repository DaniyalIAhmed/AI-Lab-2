import random


class Environment:
    def __init__(self):
        self.components = {}  # supposing A = 0, B = 1, C = 2.... I=8 Indexes
        for i in range(9):
            self.components[i] = random.choice(
                [0, 1]
            )  # 0 indicates vulnerable and 1 indicates safe

    def get_percept(self, index):
        return "Safe" if self.components[index] else "Vulnerable"


class Agent:
    def __init__(self):
        pass

    def scan(self, percept):
        if percept == "Vulnerable":
            return "vulnerable to attacks"
        return "safe from attacks"

    def patch(self, env):
        for i in env.components:
            env.components[i] = 1


def display(char,str):
    print(f"The component {char} is {str}")


def run_agent(env, agent):
    for i in range(9):
        percept = env.get_percept(i)
        action = agent.scan(percept)
        display(chr(65+i), action)
    print("\nScanning Complete. Patching vulnerable components")
    agent.patch(env)
    print("\nPatching Complete. Scanning components again\n")
    for i in range(9):
        percept = env.get_percept(i)
        action = agent.scan(percept)
        print(chr(65+i), action)


env = Environment()
agent = Agent()

run_agent(env, agent)
