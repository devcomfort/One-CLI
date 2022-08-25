from enum import Enum
import platform


OS = Enum("OS", "Windows Linux Mac")


def system() -> OS:
    name: str = platform.system()
    if name == 'Darwin':
        return 'Mac'
    return name
