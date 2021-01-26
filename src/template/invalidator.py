import json
import re
from pathlib import Path
from . import metadata


class CheckInvalid:
    """
    Parse and verify invalid links from the community Readme list
    """

    def __init__(self, load, dump, invalidated):
        self.load = Path(load)
        self.dump = Path(dump)
        self.invalidated = Path(invalidated)

    def parse_links(self):
        invite_pattern = re.compile(r"\[__(.+?)__]\(https?://(discord)\.(com|gg)(/invite)?/(.+?)\)")
        invite_codes = {}
        with open(self.load, encoding="utf-8", mode="r") as readme:
            for _ in readme:
                codes = invite_pattern.findall(_)
                if codes:
                    for c in codes:
                        invite_codes[c[4]] = c[0]

        with open(self.dump, encoding="utf-8", newline="\n", mode="w+") as dump:
            json.dump(invite_codes, dump, indent=4, ensure_ascii=False)

    def check_invites(self, sleep: int):
        invalid_codes = {}
        with open(self.dump, encoding="utf-8", newline="\n", mode="r") as d:
            invites = json.load(d)
            for k in invites.keys():
                r = metadata.DiscordCommunityMetadata(invite_code=k, sleep=sleep)
                if not r.parse_data():
                    invalid_codes[k] = invites[k]

        with open(self.invalidated, encoding="utf-8", newline="\n", mode="w+") as i:
            json.dump(invalid_codes, i, indent=4, ensure_ascii=False)
