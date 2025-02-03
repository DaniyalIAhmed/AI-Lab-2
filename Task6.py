import random


class Environment:
    def __init__(self):
        self.grid = {
            "a": "Safe",
            "b": "Safe",
            "c": "Fire",
            "d": "Safe",
            "e": "Fire",
            "f": "Safe",
            "g": "Safe",
            "h": "Safe",
            "j": "Fire",
        }

    def get_percept(self, index):
        return "🔥" if self.grid[index] == "Fire" else " "


class Agent:
    def __init__(self):
        self.path = ["a", "b", "c", "d", "e", "f", "g", "h", "j"]

    def scan(self, percept):
        return "Extinguishing needed" if percept == "🔥" else " "

    def extinguish(self):
        for room in self.path:
            print(f"Moving to {room}...")
            if self.environment.grid[room] == "Fire":
                print(f"Extinguishing fire in {room}!")
                self.environment.grid[room] = "Safe"


def run_firefighting_robot(env, agent):
    for room in agent.path:
        percept = env.get_percept(room)
        action = agent.scan(percept)
        print(f"Room {room} is {percept}. {action}")
    print("\nScanning Complete. Fires Extenguished\n")

env = Environment()
agent = Agent()
run_firefighting_robot(env, agent)