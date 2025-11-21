"""Week 7 project sandbox"""

import json

# A list of dictionaries (simulating a project inventory or expense list)
inventory = [
{"id": 1, "item": "Potion", "cost": 50},
{"id": 2, "item": "Shield", "cost": 150}
]

def save_inventory(inventory, f="save_game.json"):
    with open(f, "w") as f:
        json.dump(inventory, f, indent=4)
        
def load_inventory(f="save_game.json"):
    with open(f, "r") as f:
        return json.load(f)
    
    
save_inventory(inventory)
loaded_data = load_inventory()       
print(f"Loaded inventory: {loaded_data}")