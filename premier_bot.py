TOKEN = "EAAbzoiZCDJywBPVRYQh145IBEqm2MIHmmHNqyqpnCkduCX8bv2BhVbJDet1vpiCG9LAT4TG2LWam90loPfJHeZBeEavgg7loYFOEG1gpjl2htO1OwWvtz6u4KD4YZCSnU8bwkAoI40yfNviDSXfwiwO4a6yEZCPBgTdqzNnVxTFojftZC2CJpcugFdPn5daJutZCIycVMzHZCJGOoz1PqhOpasGhYFGZBZAxERSqEcY3sMN1kQAZDZD"
PHONE_NUMBER_ID = "769109669622747"
RECIPIENT = "971554945080"  # e.g. 971XXXXXXXXX



import requests, json

#TOKEN = "YOUR_TEMP_TOKEN"
#PHONE_NUMBER_ID = "YOUR_PHONE_NUMBER_ID"
#RECIPIENT = "971554945080"

url = f"https://graph.facebook.com/v22.0/{PHONE_NUMBER_ID}/messages"
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}
data = {
    "messaging_product": "whatsapp",
    "to": RECIPIENT,
    "type": "text",
    "text": {"body": "Hello! This is a custom message from my Python bot 🎉"}
}

res = requests.post(url, headers=headers, json=data)
print("Status Code:", res.status_code)
print("Response:", json.dumps(res.json(), indent=2))
