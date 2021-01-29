import json
from pathlib import Path
from . import metadata


class DumpMetadata:
    def __init__(self, path: str):
        self.path = Path(path)

    def user(self) -> dict:
        with open(self.path, encoding='utf-8', mode="r") as f:
            u = json.load(f)
        return u

    def server(self) -> dict:
        s = metadata.DiscordCommunityMetadata(self.user()["invite_code"])
        des = s.parse_data()
        if des:
            return des
        raise ValueError("Invalid invite code")


class Content:
    def __init__(self, path):
        self.path = Path(path)
        data = DumpMetadata(self.path)
        self.user = data.user()
        self.server = data.server()

    def community(self) -> dict:
        d = {}
        # TODO: For compatibility reasons. For the future: d = d | x
        d.update(self.user)
        d["name"] = self.server["name"] if not d["name"] else d["name"]
        d["invite_code"] = self.server["invite_code"]
        return d

    def icon(self) -> dict:
        d = {}
        d.update(self.server)
        d["name"] = self.community().get("name")
        d.pop("invite_code")
        return d
