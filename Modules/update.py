# Auto Almost Everything
# Youtube Channel https://www.youtube.com/c/AutoAlmostEverything
# Please read README.md carefully before use

# Solve captcha by using 2Captcha, register here https://2captcha.com?from=11528745.

import requests

current_version_tag = 'v1.5'


def check():
    new_version_tag = requests.get(
        'https://raw.githubusercontent.com/autoalmosteverything/AlienWorlds/main/RELEASE.md').text
    if new_version_tag != current_version_tag:
        return True
    return False
