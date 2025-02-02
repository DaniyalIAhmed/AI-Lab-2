import random


class Environment:
    def __init__(self):
        self.components = {}  # supposing A = 0, B = 1, C = 2.... I=8 Indexes
        for i in range(9):
            self.components[i] = random.choice(
                [0, 1, 2]
            )  # 0 indicates safe,1 indicates low risk and 2 indicates high risk

    def get_percept(self, index):
        return (
            "Low"
            if self.components[index] == 1
            else "High" if self.components[index] == 2 else "Safe"
        )


class Agent:
    def __init__(self):
        pass

    def scan(self, percept):
        if percept == "Low":
            return "low vulnerable to attacks"
        elif percept == "High":
            return "highly vulnerable to attacks"
        return "safe from attacks"

    def patch(self, env):
        for i in env.components:
            if env.components[i] == 1:
                env.components[i] = 0
            elif env.components[i] == 2:
                print(f"Component {chr(65 + i)} is highly vulnerable. Requires premium patching")


def display(char, str):
    print(f"The component {char} is {str}")


def run_agent(env, agent):
    for i in range(9):
        percept = env.get_percept(i)
        action = agent.scan(percept)
        display(chr(65 + i), action)
    print("\nScanning Complete. Patching vulnerable components")
    agent.patch(env)
    print("\nPatching Complete. Scanning components again\n")
    for i in range(9):
        percept = env.get_percept(i)
        action = agent.scan(percept)
        print(chr(65 + i), action)


env = Environment()
agent = Agent()

run_agent(env, agent)
