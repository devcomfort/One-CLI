from ..get_my_operating_system import system, OS
import windows


def auto_permission():
    """
    OS를 구분하여 자동으로 권한을 가져오는 함수
    """

    os_name = system()

    if os_name == OS.Windows:
        windows.get_permission()
    elif os_name == OS.Linux:
        # 미구현
        pass
    elif os_name == OS.Mac:
        # 미구현
        pass
    else:
        raise Exception('등록되지 않은 운영체제 정보.')
