
class Environment:
    def __init__(self):
        self.hospital_map = {
            "A": "Storage",
            "B": "Corridor 1",
            "C": "Patient Room 1",
            "D": "Nurse Station 1",
            "E": "Patient Room 2",
            "F": "Corridor 2",
            "G": "Patient Room 3",
            "H": "Corridor 3",
            "J": "Nurse Station 2",
        }
        self.medicine_needed = {"C": "Painkiller", "E": "Antibiotic", "G": "Vitamin"}
        self.staff_available = {"D": True, "J": False}
    
    def get_percept(self, location):
        percept = {
            "Room Type": self.hospital_map[location],
            "Medicine Needed": self.medicine_needed.get(location, None),
            "Staff Available": self.staff_available.get(location, None)
        }
        return percept

class Agent:
    def __init__(self):
        self.path = ["A", "B", "C", "D", "E", "F", "G", "H", "J"]
        self.medicine_carried = None
    
    def perform_action(self, location, percept):
        if percept["Room Type"] == "Storage":
            print("Picking up medicines...")
            self.medicine_carried = "Gathered all required Medicines"
        elif location in ["C", "E", "G"] and self.medicine_carried:
            print(f"Delivering {percept['Medicine Needed']} to {location}.")
            self.medicine_carried = None
        elif percept["Room Type"] == "Nurse Station" and not percept["Staff Available"]:
            print(f"Alerting staff at {location}!")

def run_agent(env, agent):
    for location in agent.path:
        percept = env.get_percept(location)
        print(f"Robot at {location}: {percept}")
        agent.perform_action(location, percept)
    print("\nAll deliveries completed, and alerts issued where necessary.")

env = Environment()
agent = Agent()
run_agent(env, agent)
