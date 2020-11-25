import json
import pathlib
import re
import requests


class CheckInvalid:
    """
    Parse and verify invalid links from the community Readme list
    """

    def __init__(self, load, dump, invalidated="./invalidated.json"):
        self.load = pathlib.Path(load)
        self.dump = pathlib.Path(dump)
        self.invalidated = pathlib.Path(invalidated)

    def parse_links(self):
        invite_pattern = re.compile(r"\[__(.+?)__]\(https?://(discord)\.(com|gg)(/invite)?/(.+?)\)")
        invite_codes = {}
        with open(self.load, encoding="utf-8", mode="r") as readme:
            for _ in readme:
                codes = invite_pattern.findall(_)
                if codes:
                    for c in codes:
                        invite_codes[c[4]] = c[0].replace("<br>", " ")

        with open(self.dump, encoding="utf-8", newline="\n", mode="w+") as dump:
            json.dump(invite_codes, dump, indent=4, ensure_ascii=False)

    def check_invites(self):
        api_version = 8
        invalid_codes = {}
        with open(self.dump, encoding="utf-8", newline="\n", mode="r") as d:
            invites = json.load(d)
            for _ in invites.keys():
                r = requests.get(f"https://discord.com/api/v{api_version}/invites/{_}")
                data = r.json()
                invite_status = data["code"]
                if invite_status == 10006:
                    invalid_codes[_] = invites[_]

        with open(self.invalidated, encoding="utf-8", newline="\n", mode="w+") as i:
            json.dump(invalid_codes, i, indent=4, ensure_ascii=False)


discord_links = CheckInvalid(load="../README.md", dump="../dump.json")
discord_links.parse_links()
# discord_links.check_invites()
