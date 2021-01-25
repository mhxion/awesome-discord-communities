"""
This script isn't documented anywhere else. It's only meant to make the template generation easier.
It will be replaced soon with a fully automated GitHub Action using the modules used in here.

Requirements:
- Python >= 3.7
- requests
- Pillow

Usage:
- Fill out your community details from the sample file community.json in ./data/ directory
- You can download and save your community icon by calling i.save()
- Run the script directly from terminal: python main.py
- The generated output on terminal is your community template that is ready for pull request.
"""

from src.template import generator, parse, icon

'''Parse given community metadata'''
parsed = parse.Content(path='./data/community.json')

'''Download and save the community icon to icon_path'''
i = icon.GetIcon(icon_path='./images/server_icons', **parsed.icon())
# Uncomment i.save() to save the community icon
# i.save()

'''Generate template'''
t = generator.GenerateTemplate(**parsed.community())
print(f'''{t.format_icon()}

[__{t.format_name()}__]({t.format_invite()}){t.format_official()}{t.format_reddit()}{t.format_homepage()}{t.format_git()} \\
Notable Channels: {t.format_channels()} \\
Language: {t.format_language()}{t.padding()}''')
