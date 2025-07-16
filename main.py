from subprocess import Popen
from sys import argv


WEZTERM_PATH: str = r'C:\Program Files\WezTerm\wezterm-gui.exe'


def main() -> None:
    Popen([
        WEZTERM_PATH,
        'start',
        '--',
        'nvim',
    ] + argv[1:])


if __name__ == '__main__':
    main()
