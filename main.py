import sys
import json
import asyncio
import aiohttp
from config import words_file, concurrency
from checker import check_from_file, id_turber

async def main():
    print("[1] ID Chekcer (from words.json)")
    print("[2] ID Turber")
    mode = input("Select mode (1/2): ").strip()

    connector = aiohttp.TCPConnector(ssl=False, limit=50 if mode == '1' else concurrency)
    
    async with aiohttp.ClientSession(connector=connector) as session:
        if mode == '1':
            with open(words_file) as f:
                words = json.load(f)
            await check_from_file(session, words)
        elif mode == '2':
            word = input("Enter ID for turbing (example: vampire): ").strip()
            await id_turber(session, word)
        else:
            print("Wrong select...")

if __name__ == "__main__":
    if sys.platform == 'win32': # checking if 32bit
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())