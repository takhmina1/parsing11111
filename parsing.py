                                                  # pip install requests beautifulsoup4
                                                  # pip install aiohttp




import aiohttp
import asyncio
import json
import time


start = time.time()


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "device": "pc"
}

lalafo_url = 'https://lalafo.kg/api/search/v3/feed/details/57367396?expand=url'

async def fetch_lalafo_data(session, url):
    async with session.get(url, headers=headers) as response:
        if response.status == 200:
            data = await response.json()
            return data
        else:
            print(f"Error fetching data: {response.status}")
    return None

async def main():
    async with aiohttp.ClientSession() as session:
        lalafo_data = await fetch_lalafo_data(session, lalafo_url)
        if lalafo_data:
            with open('Продажа авто.json', 'a', encoding='UTF-8') as file:
                json.dump(lalafo_data, file, indent=2, ensure_ascii=False)
                print(f'Данные сохранены в Продажа авто.json')

if __name__ == '__main__':
    asyncio.run(main())


end_time = time.time()


res = end_time - start



print(res)