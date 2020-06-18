#!/usr/bin/env python3


class APDTemplateGenerator:
    """A simple markdown template generator for Awesome Programming Discord"""

    def __init__(self):
        self.name = ""
        self.invite_link = ""
        self.server_icon = ""
        self.is_reddit = ""
        self.is_official = ""
        self.homepage = ""
        self.git_repo = ""
        self.channels = ""
        self.language = ""

    def __check_name(self):
        while True:
            name = input("➜ Enter the name of the Discord community/server:\n")
            if name.isascii():
                self.name = name
            else:
                print(f"Looks like the server name contains non-ascii characters. Emoji are discouraged.\n"
                      f"But you can change that later. Moving on.")
                self.name = name

    def __check_invite(self):
        while True:
            # TODO: This needs to be displaced with a better domain traceroute check.
            link = input("\n➜ Enter a permanent invite link to the server:\n")
            for _ in link.split(".com") + link.split(".gg"):
                if _ in ["https://discord", "https://discordapp", "http://discord", "http://discordapp",
                         "https://www.discord", "https://www.discordapp", "http://www.discord",
                         "http://www.discordapp", "discord", "discordapp"]:
                    self.invite_link = link
                    return
            else:
                print(f"Only invite link that is generated from Discord platform itself is allowed.")
                continue

    def __icon_link(self):
        while True:
            try:
                img = input("\n➜ Enter server icon (PNG/JPG) URL. Make sure it's a static link:\n")
            except ValueError:
                print(f"Sorry, the URL you entered was not in a valid text format.")
                continue
            self.server_icon = img
            return

    def __is_reddit_check(self):
        while True:
            rdt = input(
                "\n➜ Does the server belong to or officially recognized by an existing sub-Reddit? "
                "Enter Yes/y or No/n:\n").lower()
            if rdt not in ["y", "yes", "n", "no"]:
                print(f'''Sorry that did not go through. Simply enter "yes" or "no".''')
                continue
            else:
                self.is_reddit = rdt in ["y", "yes"]
                return

    def __is_official_check(self):
        while True:
            org = input("\n➜ Is the server owned or recognized by an established entity "
                        "e.g., a company, organization, open-source project, content creator?\n"
                        "Enter Yes/y or No/n:\n").lower()
            if org not in ["y", "yes", "n", "no"]:
                print(f'''Sorry that did not go through. Simply enter "yes" or "no".''')
                continue
            else:
                self.is_official = org in ["y", "yes"]
                return

    def __get_homepage(self):
        home = input("\n➜ Enter homepage URL of the community (if any). To skip press Enter. \n")
        while not home and (self.is_reddit or self.is_official):
            home = input(f"If you're an official entity or a sub-reddit, you must have an homepage.\n"
                         f"It can be a link to the sub-reddit URL or the content creator's profile.\n"
                         f"Please enter the URL:\n")
            continue
        self.homepage = home

    def __get_git_repo(self):
        self.git_repo = input("\n➜ Enter the link to the community-maintained remote Git repository. Press Enter to skip:\n")

    def __get_channels(self):
        notable = input('\n➜ Enter the notable channels separated by comma.'
                        'E.g.,"channel-1, channel-2, channel-3". Make sure channel names do not contain spaces:\n')
        notable_trunc = ["`#" + _ + "`" for _ in "".join([_ if _ != " " else "" for _ in notable]).split(",")]
        # notable_trunc_il = len(", ".join(notable_trunc))
        notable_trunc_l = notable_trunc_il = len(", ".join(notable_trunc))

        while notable_trunc_l > 195:
            notable_trunc.pop()
            notable_trunc_l = len(", ".join(notable_trunc))

        if notable_trunc_il >= 271:
            for i in range(2):
                notable_trunc.pop()
            notable_trunc.append("**[`so much more`](badges.md#so-much-more)**")

        self.channels = ", ".join(notable_trunc)

    def __get_language(self):
        self.language = input("\n➜ Enter the languages the server has dedicated channels for, separated by comma:\n")

    def validate(self):
        self.__check_name()
        self.__check_invite()
        self.__icon_link()
        self.__is_reddit_check()
        self.__is_official_check()
        self.__get_homepage()
        self.__get_git_repo()
        self.__get_channels()
        self.__get_language()

    def __valid_name(self):
        return f"{self.name}"

    def __valid_invite(self):
        return f"{self.invite_link}"

    def __valid_icon(self):
        return f'<img align="left" height="94px" width="94px" alt="Server Icon" src="{self.server_icon}" />'

    def __valid_reddit(self):
        if self.is_reddit:
            return f' [<img height="16px" width="16px" alt="Reddit Badge" src="images/badges/reddit.png">]' \
                   f'(badges.md#reddit-badge)'
        return f""

    def __valid_official(self):
        if self.is_official:
            return f' [<img height="16px" width="16px" alt="Official Badge" src="images/badges/official.png">]' \
                   f'(badges.md#official-identification-badge)'
        return f""

    def __valid_home(self):
        if self.homepage:
            return f' [<img height="16px" width="16px" alt="Homepage URL" src="images/badges/homepage.png">]' \
                   f'({self.homepage})'
        return f""

    def __valid_git(self):
        if self.git_repo:
            return f' [<img height="16px" width="16px" alt="Git Repository" src="images/badges/git.png">]({self.git_repo})'
        return f""

    def __valid_channels(self):
        return self.channels

    def __valid_language(self):
        return self.language if len(self.channels) >= 76 else self.language + " \\\n<br />"

    def format(self):
        return f"""
Here's your snippet to copy.
=========================================================================
{self.__valid_icon()}

[__{self.__valid_name()}__]({self.__valid_invite()}){self.__valid_official()}{self.__valid_reddit()}{self.__valid_home()}{self.__valid_git()} \\
Notable Channels: {self.__valid_channels()} \\
Language: {self.__valid_language()}
"""


if __name__ == '__main__':
    plate = APDTemplateGenerator()
    plate.validate()
    print(plate.format())
