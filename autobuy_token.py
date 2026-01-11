import re
from telethon import TelegramClient, events

# Replace these with your credentials
API_ID = 29199461  # Get this from https://my.telegram.org
API_HASH = '5d5c0797293505649aaa30aa8d1af14a'  # Get this from https://my.telegram.org
SESSION_NAME = 'auto_buy_session'

# Replace these with the IDs of the source group and Trojan bot
SOURCE_GROUP_ID = '@RJ_Insights'  # Use @userinfobot to get the group ID
TROJAN_BOT_ID = '@@solana_trojanbot'  # Replace with Trojan Bot's username (e.g., "@TrojanOnSolana")

# Solana address regex pattern (matches valid Solana token contract addresses)
SOLANA_ADDRESS_REGEX = r'\b[1-9A-HJ-NP-Za-km-z]{32,44}\b'

# Initialize the Telegram client
client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

# Event listener for new messages in the source group
@client.on(events.NewMessage(chats=SOURCE_GROUP_ID))
async def forward_to_trojan(event):
    try:
        # Extract Solana contract addresses using regex
        message_text = event.message.message  # Get message text
        sol_addresses = re.findall(SOLANA_ADDRESS_REGEX, message_text)

        if sol_addresses:
            for address in sol_addresses:
                # Forward each valid Solana address to the Trojan Bot
                await client.send_message(TROJAN_BOT_ID, address)
                print(f"Forwarded Solana address to Trojan Bot: {address}")
        else:
            print("No valid Solana address found in the message.")
    except Exception as e:
        print(f"Error occurred: {e}")

# Start the client and listen for new messages
def main():
    print("Starting the Telegram client...")
    with client:
        print("Listening for new messages...")
        client.run_until_disconnected()

if __name__ == "__main__":
    main()




