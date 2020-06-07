#!/usr/bin/env python3


class APDTemplateGenerator:
    """A simple markdown template generator for Awesome Programming Discord"""

    def __init__(self, name, invite_link, server_icon, is_reddit, is_official, homepage, git_repo, channels, language):
        self.name = name
        self.invite_link = invite_link
        self.server_icon = server_icon
        self.is_reddit = is_reddit
        self.is_official = is_official
        self.homepage = homepage
        self.git_repo = git_repo
        self.channels = channels
        self.language = language

    @classmethod
    def validate(cls):
        def check_name():
            while True:
                name = input("➜ Enter the name of the Discord community/server:\n")
                if name.isascii():
                    return name
                else:
                    print(f"Looks like the server name contains non-ascii characters. Emoji are discouraged.\n"
                          f"But you can change that later. Moving on.")
                    return name

        def check_invite():
            while True:
                # TODO: This needs to be displaced with a better domain traceroute check.
                link = input("\n➜ Enter a permanent invite link to the server:\n")
                for _ in link.split(".com") + link.split(".gg"):
                    if _ in ["https://discord", "https://discordapp", "http://discord", "http://discordapp",
                             "https://www.discord", "https://www.discordapp", "http://www.discord",
                             "http://www.discordapp", "discord", "discordapp"]:
                        return link
                else:
                    print(f"Only invite link that is generated from Discord platform itself is allowed.")
                    continue

        def icon_link():
            while True:
                try:
                    img = input("\n➜ Enter server icon (PNG/JPG) URL. Make sure it's a static link:\n")
                except ValueError:
                    print(f"Sorry, the URL you entered was not in a valid text format.")
                    continue
                return img

        def is_reddit_check():
            while True:
                rdt = input(
                    "\n➜ Does the server belong to or officially recognized by an existing sub-Reddit? "
                    "Enter Yes/y or No/n:\n").lower()
                if rdt not in ["y", "yes", "n", "no"]:
                    print(f'''Sorry that did not go through. Simply enter "yes" or "no".''')
                    continue
                elif rdt in ["n", "no"]:
                    return False
                else:
                    return True

        def is_official_check():
            while True:
                org = input("\n➜ Is the server owned or recognized by an established entity "
                            "e.g., a company, organization, open-source project, content creator?\n"
                            "Enter Yes/y or No/n:\n").lower()
                if org not in ["y", "yes", "n", "no"]:
                    print(f'''Sorry that did not go through. Simply enter "yes" or "no".''')
                    continue
                elif org in ["n", "no"]:
                    return False
                else:
                    return True

        def get_homepage():
            home = input("\n➜ Enter homepage URL of the community (if any). To skip press Enter. \n")
            while not home and (is_reddit_check or is_official_check):
                # if not home and (is_reddit_check or is_official_check):
                home = input(f"If you're an official entity or a sub-reddit, you must have an homepage.\n"
                             f"It can be a link to the sub-reddit URL or the content creator's profile.\n"
                             f"Please enter the URL:\n")
                continue
            return home

        def get_git_repo():
            git = input("\n➜ Enter the link to the community-maintained remote Git repository. Press Enter to skip:\n")
            return git

        def get_channels():
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
                return ", ".join(notable_trunc)
            return ", ".join(notable_trunc)

        def get_language():
            lang = input("\n➜ Enter the languages the server has dedicated channels for, separated by comma:\n")
            return lang

        return cls(check_name(), check_invite(), icon_link(), is_reddit_check(), is_official_check(), get_homepage(),
                   get_git_repo(), get_channels(), get_language())

    def valid_name(self):
        return f"{self.name}"

    def valid_invite(self):
        return f"{self.invite_link}"

    def valid_icon(self):
        return f'<img align="left" height="94px" width="94px" alt="Server Icon" src="{self.server_icon}" />'

    def valid_reddit(self):
        if self.is_reddit:
            return f' [<img height="16px" width="16px" alt="Reddit Badge" src="images/badges/reddit.png">]' \
                   f'(badges.md#reddit-badge)'
        return f""

    def valid_official(self):
        if self.is_official:
            return f' [<img height="16px" width="16px" alt="Official Badge" src="images/badges/official.png">]' \
                   f'(badges.md#official-identification-badge)'
        return f""

    def valid_home(self):
        if self.homepage:
            return f' [<img height="16px" width="16px" alt="Homepage URL" src="images/badges/homepage.png">]' \
                   f'({self.homepage})'
        return f""

    def valid_git(self):
        if self.git_repo:
            return f' [<img height="16px" width="16px" alt="Git Repository" src="images/badges/git.png">]({self.git_repo})'
        return f""

    def valid_channels(self):
        return self.channels

    def valid_language(self):
        return self.language if len(self.channels) >= 76 else self.language + " \\\n<br />"


if __name__ == '__main__':
    plate = APDTemplateGenerator.validate()
    print(f"""
Here's your snippet to copy.
=========================================================================
{plate.valid_icon()}
    
[__{plate.valid_name()}__]({plate.valid_invite()}){plate.valid_official()}{plate.valid_reddit()}{plate.valid_home()}{plate.valid_git()} \\
    
Notable Channels: {plate.valid_channels()} \\
Language: {plate.valid_language()}
""")
