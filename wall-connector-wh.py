import asyncio
from tesla_wall_connector import WallConnector
from datetime import date, timedelta

yesterday = date.today() - timedelta(1)

async def main():
    async with WallConnector('192.168.1.88') as wall_connector:
        lifetime = await wall_connector.async_get_lifetime()
        with open("wall-connector-wh.csv", "a") as output:
            output.write("{},{}\n".format(yesterday, lifetime.energy_wh))

asyncio.run(main())
