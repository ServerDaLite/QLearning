class QTable:
    def __init__(self):
        self.memory = list()
        
    def append(self, state, num_actions):
        self.memory.append({"state": state, "value": [0 for i in range(num_actions)]})
    
    def get_value(self, x, y, action_position):
        for cell in self.memory:
            if cell["state"] != (x, y):
                continue
            return cell["value"][action_position]
        raise OSError("Position not found...")
    
    def set_value(self, x, y, action_position, value):
        for cell in self.memory:
            if cell["state"] != (x, y):
                continue
            cell["value"][action_position] = value
            return 0
        raise OSError("Position not found...")
    
    def display(self):
        for cell in self.memory:
            print(cell["state"])
            print(f"\t- {cell['value']}\n")
            
        

if __name__ == "__main__":
    actions = ["up", "down", "left", "right"]
    
    table = QTable()
    for y in range(5):
        for x in range(5):
            table.append((x, y), len(actions))
            
    value1 = table.get_value(2, 3, 0)
    table.set_value(2, 3, 0, 5)
    value2 = table.get_value(2, 3, 0)
    
    print(value1, " | " , value2)
    
    table.display()
