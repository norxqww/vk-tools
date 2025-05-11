import aiohttp
import random
import asyncio
from datetime import datetime
from win10toast import ToastNotifier
from config import (
    api, api_ver, client,
    user_agents, timeout, file_prefix
)

async def check_id(session, word):
    try:
        headers = {
            'User-Agent': random.choice(user_agents),
            'Accept-Language': 'ru-RU,ru;q=0.9',
        }

        params = {
            'user_ids': word,
            'access_token': 'undefined',
            'v': api_ver,
            'client_id': client
        }

        async with session.get(
            api,
            headers=headers,
            params=params,
            timeout=aiohttp.ClientTimeout(total=timeout)
        ) as response:
            api_data = await response.json()
            
            if 'response' in api_data and len(api_data['response']) > 0:
                return (word, False)
            
            # alternative
            async with session.get(
                f"https://vk.com/{word}",
                headers=headers,
                allow_redirects=False
            ) as page_response:
                if page_response.status == 404:
                    return (word, True)
                
                content = await page_response.text()
                if 'error_msg_title' in content:
                    return (word, True)

                return (word, False)

    except Exception as e:
        print(f"⚠️ Error while check: {word}: {e}")
        return (word, False)

async def check_from_file(session, words):
    """[1]: ID Checker (from words.json)"""
    tasks = [check_id(session, word) for word in words]
    found = []
    
    for future in asyncio.as_completed(tasks):
        word, status = await future
        if status:
            found.append(word)
            print(f"✅ Unoccupied: {word}")
        else:
            print(f"❌ Taken: {word}")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    with open(f"{file_prefix}{timestamp}.txt", "w") as f:
        f.write('\n'.join(found))

async def id_turber(session, word):
    """[2]: ID Turber"""
    while True:
        _, status = await check_id(session, word)
        if status:
            print(f"✅ ID {word} unoccupied!")
            try:
                toaster = ToastNotifier()
                toaster.show_toast(
                    "VK Checker", 
                    f"ID {word} unoccupied! Take it!", 
                    duration=10
                )
            except Exception as e:
                print(f"⚠️ Error while trying to send notification: {e}")
            break
        else:
            print(f"❌ ID {word} Taken. Recheck in 60 sec.")
            await asyncio.sleep(60)