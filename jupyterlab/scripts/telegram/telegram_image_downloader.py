import argparse
import asyncio
import logging
import os
from datetime import datetime
from telethon import TelegramClient, events
from telethon.tl.types import MessageMediaPhoto
from tqdm import tqdm

# Setup logging
logging.basicConfig(
    filename='error.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

async def download_channel_images(args):
    client = TelegramClient('session_name', args.api_id, args.api_hash)
    await client.start()
    
    try:
        print(f"Connecting to channel: {args.channel}")
        entity = await client.get_entity(args.channel)
        all_messages = await client.get_messages(entity, limit=args.limit)
        
        # Create output directory if needed
        os.makedirs(args.output, exist_ok=True)
        
        # Filter and process messages
        photo_messages = [msg for msg in all_messages if isinstance(msg.media, MessageMediaPhoto)]
        print(f"Found {len(photo_messages)} images in {len(all_messages)} messages")
        
        for msg in tqdm(photo_messages, desc="Downloading images"):
            try:
                # Generate filename based on date and message ID
                date_str = msg.date.strftime("%Y%m%d") # _%H%M%S")
                filename = f"{msg.id}_{date_str}.jpg"
                # filename = f"{msg.id}.jpg"
                file_path = os.path.join(args.output, filename)
                
                # Skip if file already exists
                if os.path.exists(file_path):
                    continue
                    
                # Download the image
                await client.download_media(msg.media, file=file_path)
                
            except Exception as e:
                logging.error(f"Message {msg.id} failed: {str(e)}")
                
    except Exception as e:
        logging.error(f"Channel connection failed: {str(e)}")
        print(f"Error: {str(e)}")
    finally:
        await client.disconnect()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download images from Telegram channel')
    parser.add_argument('--api-id', required=True, help='Telegram API ID')
    parser.add_argument('--api-hash', required=True, help='Telegram API Hash')
    parser.add_argument('--channel', required=True, help='Channel link (t.me/channel_name)')
    parser.add_argument('--output', default='./downloads/', help='Output directory')
    parser.add_argument('--limit', type=int, default=0, help='Number of messages to process (0=all)')
    args = parser.parse_args()

    # Convert channel username to entity format
    if args.channel.startswith('t.me/'):
        args.channel = args.channel.split('t.me/')[-1]
    if args.channel.startswith('@'):
        args.channel = args.channel[1:]

    print(f"Starting download to: {args.output}")
    asyncio.run(download_channel_images(args))
    print("Download completed. Check error.log for any failures")