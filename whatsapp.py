import pywhatkit as kit
# Send a WhatsApp message
phone_number = "+918393095919"  # Replace with recipient's phone number (include country code)
message = "Hello! This is an automated message sent using Python." \
"This is good"
hour = 14  # Specify the hour in 24-hour format
minute = 30  # Specify the minute
try:
    kit.sendwhatmsg_instantly(phone_number, message)
    print("Message scheduled successfully!")
except Exception as e:
    print(f"An error occurred: {e}")