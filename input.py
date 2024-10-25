# Create a dictionary to store fruit information
fruits = {
    "apple": {"color": "red", "price": 0.5},
    "banana": {"color": "yellow", "price": 0.3},
    "grape": {"color": "purple", "price": 0.4},
    "orange": {"color": "orange", "price": 0.6},
}

# Function to display fruit information
def display_fruit_info(fruit_dict):
    for fruit, info in fruit_dict.items():
        print(f"{fruit.capitalize()}:")
        print(f"  Color: {info['color']}")
        print(f"  Price: ${info['price']:.2f}\n")

# Call the function to display information
display_fruit_info(fruits)
