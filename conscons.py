import json

def join_top_holdings(json_file_name):
    # Read the JSON file and load its contents into a Python object
    with open(json_file_name, 'r') as file:
        data = json.load(file)

    # Extract the top holdings list from the loaded JSON object
    top_holdings = data['top_holdings']

    # Create a new list and iterate over the top holdings list
    new_list = []
    for item in top_holdings:
        # Add the JSON file name as a property to each item
        item['json_file_name'] = json_file_name
        # Append each modified item to the new list
        new_list.append(item)

    # Return the new list with the JSON file name added to each item
    return new_list
