""" nvm 설치 코드

- 테스트 명령: py -m codesets.install.nvm.install

"""

from ...get_my_operating_system import system
from ...permissions import windows as windows_permission


def install():
    pass


if __name__ == '__main__':
    my_system = system()

    if my_system == 'Windows':
        windows_permission.get_admin()

    install()
