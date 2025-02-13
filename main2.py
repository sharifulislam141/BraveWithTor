import asyncio
import aiohttp
from selenium_driverless import webdriver
from selenium_driverless.types.by import By

# Use Privoxy (HTTP Proxy) instead of SOCKS5
PROXY_HTTP = "http://127.0.0.1:8118"  # Privoxy listens on this port

async def get_public_ip():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.ipify.org?format=json') as response:
                data = await response.json()
                return data.get('ip', 'Unknown')
    except Exception as e:
        print(f"Error getting IP: {e}")
        return 'Unknown'

async def main():
    public_ip = await get_public_ip()
    print(f"🌍 Your Public IP: {public_ip}")

    # Linux Brave Browser path
    brave_path = "/snap/bin/brave"

    # Browser options
    options = webdriver.ChromeOptions()
    options.binary_location = brave_path
    options.add_argument(f"--proxy-server={PROXY_HTTP}")  # Use Privoxy HTTP Proxy

    try:
        async with webdriver.Chrome(options=options) as driver:
            await driver.get('https://whatismyipaddress.com/')
            await asyncio.sleep(30)

    except Exception as e:
        print(f"🚨 Browser error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
