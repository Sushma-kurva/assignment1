import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to send a confirmation email
def send_confirmation_email(customer_email, hotel_name, room_type, total_cost):
    sender_email = "shusmashusma69@gmail.com"  # Replace with your email
    receiver_email = customer_email
    password = "sushma1625"  # Replace with your email password

    subject = "Hotel Booking Confirmation"
    body = f"Dear Customer,\n\nYour booking at {hotel_name} has been confirmed.\n\n"
    body += f"Room Type: {room_type}\nTotal Cost: ${total_cost:.2f}\n\nThank you for choosing us!"
    
    # Create the email
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        # Set up the server
        server = smtplib.SMTP("shusmashusma69@gmail.com", 587)  # Using Gmail's SMTP server
        server.starttls()  # Use TLS for security
        server.login("shusmashusma69@gmail.com","qdtj vxnl zsxu grxq")
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print("Confirmation email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

# Function to check availability
def check_availability(room_type, available_rooms):
    if room_type in available_rooms and available_rooms[room_type] > 0:
        return True
    return False

# Function to book a room
def book_room(customer_name, customer_email, room_type, available_rooms, room_prices):
    if check_availability(room_type, available_rooms):
        # Book the room
        available_rooms[room_type] -= 1
        total_cost = room_prices[room_type]

        print(f"Booking successful for {customer_name} in a {room_type} room.")
        print(f"Total cost: ${total_cost:.2f}")

        # Send confirmation email
        send_confirmation_email("shusmashusma69@gmail.com", "Grand Hotel", room_type, total_cost)
    else:
        print(f"Sorry, no {room_type} rooms available.")

# Example usage:
available_rooms = {
    "Single": 5,
    "Double": 3,
    "Suite": 2
}

room_prices = {
    "Single": 100,
    "Double": 150,
    "Suite": 250
}

customer_name = "sushma"
customer_email = "customer_shusmashusma69@gmail.com"  # Replace with the customer's email
room_type = "Double"  # Customer wants to book a Double room

# Book the room
book_room(customer_name, customer_email, room_type, available_rooms, room_prices)

