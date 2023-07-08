import asyncio
import aiohttp

username = "username"
password = "password"
host = "https://caldav.yandex.ru"


async def change_yandex_calendar(caldav_calendar_url: str, new_events: str) -> None:
    """Function for deleting events and creating new ones"""

    auth = aiohttp.BasicAuth(login=username, password=password)
    async with aiohttp.ClientSession() as session:
        async with session.request(method="GET", url=caldav_calendar_url, auth=auth) as resp:
            ics_urls = await resp.text()
        for ics_uid in ics_urls.splitlines():
            if ics_uid != "$":
                async with session.request(method="DELETE", url=host + ics_uid, auth=auth):
                    pass
        async with session.request(method="PUT", url=caldav_calendar_url + ' ', auth=auth, data=new_events):
            pass


if __name__ == '__main__':
    asyncio.run(change_yandex_calendar("link to yandex caldav calendar",
                                       """.ics text"""))

