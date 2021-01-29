import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class DiscordCommunityMetadata:
    def __init__(self, invite_code: str, api_version: int = 8, protocol: str = 'https', sleep: int = 1):
        self.invite_code = invite_code
        self.sleep = sleep
        self.api_version = api_version
        self.protocol = protocol

    def request(self):
        s = requests.Session()
        # Discord has strict rate limit: https://discord.com/developers/docs/topics/rate-limits
        Retry.BACKOFF_MAX = 5
        retries = Retry(total=5, backoff_factor=self.sleep, status_forcelist=[429])
        s.mount(f'{self.protocol}://', HTTPAdapter(max_retries=retries))
        return s.get(f'{self.protocol}://discord.com/api/v{self.api_version}/invites/{self.invite_code}')

    def parse_data(self):
        data = self.request().json()
        try:
            status = data["code"] == self.invite_code or data["code"] == self.invite_code.lower()
            if status:
                data_captured = {"invite_code": data["code"], "name": data["guild"]["name"],
                                 "unique": data["guild"]["id"], "icon_id": data["guild"]["icon"]}
                return data_captured
            return None

        except KeyError:
            raise requests.exceptions.Timeout(f'Possible rate limit. Reply: {self.invite_code} : {data}')
