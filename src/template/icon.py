import requests
from io import BytesIO
from pathlib import Path
from PIL import Image
import re


class GetIcon:
    def __init__(self, name, unique, icon_id, icon_path: str):
        self.icon_path = Path(icon_path)
        self.name = name
        self.guild_id = unique
        self.guild_icon = icon_id

    @staticmethod
    def icon_name(s: str) -> str:
        form = re.sub(r'[^\w]', '_', s)        
        return form.lower()

    def save(self, size: int = 512, encode='webp', quality: int = 75):
        icon_name = self.icon_name(self.name)
        icon_url = f'https://cdn.discordapp.com/icons/{self.guild_id}/{self.guild_icon}.png?size={size}'
        with requests.get(icon_url, stream=True) as r:
            im = Image.open(BytesIO(r.content))
            im.save(self.icon_path / f'{icon_name}.{encode}', format=encode, quality=quality)
