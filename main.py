import asyncio
import aiohttp
from selenium_driverless import webdriver
from selenium_driverless.types.by import By

TOR_PROXY = "socks5://127.0.0.1:9050"  # Tor's default SOCKS5 proxy

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
        # Linux default
    brave_path = "/snap/bin/brave"

    # brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"  # Windows

    # Browser options
    options = webdriver.ChromeOptions()
    options.binary_location = brave_path
    options.add_argument(f"--proxy-server={TOR_PROXY}")  # Use Tor

    try:
        async with webdriver.Chrome(options=options) as driver:
            await driver.get('https://whatismyipaddress.com/')
            # await driver.get("https://api.ipify.org")


            # body = await driver.find_element(By.TAG_NAME, "body")
            # browser_ip = await body.text
            # print(f"🖥️ Browser IP via Tor: {browser_ip}")

            # if browser_ip != public_ip:
            #     print("✅ Tor is working! Your IP is hidden.")
            # else:
            #     print("⚠️ Tor is NOT working. Check your Tor service.")

            await asyncio.sleep(5)

    except Exception as e:
        print(f"🚨 Browser error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
