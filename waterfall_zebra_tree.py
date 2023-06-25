#Health and Wellness Retreats for Mindful Living

#Libraries
import os
import json
import requests

# Global Variables
retreats_data = []

# Retreat class
class Retreat():
    def __init__(self, name, location, cost, description, type):
        self.name = name
        self.location = location
        self.cost = cost
        self.description = description
        self.type = type

# Function to get retreats data from online source
def get_retreat_data():
    response = requests.get("https://raw.githubusercontent.com/erikaterzic/Health-Retreat-Data/master/retreats.json")
    data = json.loads(response.text)
    return data

# Function to create retreats
def create_retreats(retreats_data):
    retreats = []
    for retreat in retreats_data:
        name = retreat.get('name')
        location = retreat.get('location')
        cost = retreat.get('cost')
        description = retreat.get('description')
        type = retreat.get('type')
        new_retreat = Retreat(name, location, cost, description, type)
        retreats.append(new_retreat)
    return retreats

# Function to print retreats    
def display_retreats(retreats):
    for retreat in retreats:
        print(''' Name: {name} 
        Location: {location} 
        Cost: {cost} 
        Description: {description} 
        Type: {type} 
        '''.format(name=retreat.name, location=retreat.location, cost=retreat.cost, description=retreat.description, type=retreat.type))

# Function to save retreats data to file
def save_data_to_file(retreats):
    retreats_list = []
    for retreat in retreats:
        retreat_dict = {
            'name': retreat.name,
            'location': retreat.location,
            'cost': retreat.cost,
            'description': retreat.description,
            'type': retreat.type
        }
        retreats_list.append(retreat_dict)
    with open('retreats.txt', 'w') as outfile:
        json.dump(retreats_list, outfile)

# Function to read retreats data from file
def read_data_from_file():
    if os.path.exists("retreats.txt"):
        with open('retreats.txt', 'r') as infile:
            retreats_data = json.load(infile)
            return retreats_data

# Main Function
def main():
    retreats_data = get_retreat_data()
    retreats = create_retreats(retreats_data)
    display_retreats(retreats)
    save_data_to_file(retreats)
    read_data_from_file()

# Run Main Program
if __name__ == "__main__":
    main()