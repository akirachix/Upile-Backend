# Create a simple dictionary to simulate a database
user_data = {}

# Step 1: Register user
def register_user():
    phone_number = input("Enter your phone number for registration: 0703289374 ")
    # Save the phone number to simulate registration
    user_data['phone_number'] = phone_number
    print("Registration successful!")
    
# Step 2: Login
def login_user():
    login_phone_number = input("Enter your phone number to log in: 0703289374 ")
    
    # Step 3: Check if the entered phone number matches the registered one
    if user_data['phone_number'] == login_phone_number:
        print("Login successful! Phone number matches.")
    else:
        print("Login failed! Phone number does not match.")

# Example usage:
register_user()
login_user()
