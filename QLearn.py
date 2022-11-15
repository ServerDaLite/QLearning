import numpy as np # Linear Algebra

ENVIROMENT_ROWS, ENVIROMENT_COLUMNS = 11, 11
ACTIONS = ["up", "down", "left", "right"]

q_values = np.zeros((ENVIROMENT_ROWS, ENVIROMENT_COLUMNS, len(ACTIONS)))

rewards = np.full((ENVIROMENT_ROWS, ENVIROMENT_COLUMNS), -100)
rewards[0, 5] = 100

aisles = {}
aisles[1] = [i for i in range(1, 10)]
aisles[2] = [1, 7, 9]
aisles[3] = [i for i in range(1, 8)]
aisles[3].append(9)
aisles[4] = [3, 7]
aisles[5] = [i for i in range(11)]
aisles[6] = [5]
aisles[7] = [i for i in range(1, 10)]
aisles[8] = [3, 7]
aisles[9] = [i for i in range(11)]

for row in range(1, 10):
    for column in aisles[row]:
        rewards[row, column] = -1
    
def is_terminal_state(row, column):
    if rewards[row, column] == -1:
        return False
    else:
        return True
        
def get_starting_location():
    current_row = np.random.randint(ENVIROMENT_ROWS)
    current_column = np.random.randint(ENVIROMENT_COLUMNS)
    
    while is_terminal_state(current_row, current_column):
        current_row = np.random.randint(ENVIROMENT_ROWS)
        current_column = np.random.randint(ENVIROMENT_COLUMNS)
    return current_row, current_column
    
def get_next_action(current_row, current_column, epsilon):
    if np.random.random() < epsilon:
        return np.argmax(q_values[current_row, current_column])
    else:
        return np.random.randint(len(ACTIONS))
        
def get_next_location(current_row, current_column, action_index):
    new_row = current_row
    new_column = current_column
    
    if ACTIONS[action_index] == "up" and current_row > 0:
        new_row -= 1
    elif ACTIONS[action_index] == "right" and current_column < ENVIROMENT_COLUMNS - 1:
        new_column += 1
    elif ACTIONS[action_index] == "down" and current_row < ENVIROMENT_ROWS - 1:
        new_row += 1
    elif ACTIONS[action_index] == "left" and current_column > 0:
        new_column -= 1
    return new_row, new_column
    
def get_shortest_path(start_row, start_column):
    if is_terminal_state(start_row, start_column):
        return []
    
    current_row, current_column = start_row, start_column
    shortest_path = []
    shortest_path.append([current_row, current_column])
    
    while not is_terminal_state(current_row, current_column):
        action_index = get_next_action(current_row, current_column, 1)
        current_row, current_column = get_next_location(current_row, current_column, action_index)
        shortest_path.append([current_row, current_column])
    return shortest_path
    
epsilon = 0.9
discount_factor = 0.9
learning_rate = 0.9

for episode in range(1000):
    row, column = get_starting_location()
    
    while not is_terminal_state(row, column):
        action_index = get_next_action(row, column, epsilon)
        
        old_row, old_column = row, column
        row, column = get_next_location(row, column, action_index)
        
        reward = rewards[row, column]
        old_q_value = q_values[old_row, old_column, action_index]
        temperoal_difference = reward + (discount_factor * np.max(q_values[row, column])) - old_q_value
        
        new_q_value = old_q_value + (learning_rate * temperoal_difference)
        q_values[old_row, old_column, action_index] = new_q_value
        
print("DONE!")

print(rewards)

print(get_shortest_path(3, 9))
