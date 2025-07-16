### Open [Neovim](https://neovim.io/) with [WezTerm](https://wezterm.org/)
This small project opens Neovim in WezTerm terminal.
The project tested on Windows 11.

### How to compile python file into `.exe`?
Run this inside the project's directory:
```bash
uv run pyinstaller main.py --onefile --noconsole --icon=neovim-original.ico
```

### Registry edit
If you want to run this project's .exe file by a mouse double left click or items in the Windows context menus, you need to edit your registry.
I provide an example [file](open_with_nvim_with_wezterm.reg) to do it.
You should only change all paths in to your own (`C:\\Users\\User\\Desktop\\open-nvim-with-wezterm\\` -> your path to a directory with an icon and .exe file).
> [!WARNING]
> **Please double-check this file before run it! Understand all changes it will apply. Manual registry edit can be dangerous!**

### Sources
[Icon](https://github.com/devicons/devicon/blob/master/icons/neovim/neovim-original.svg)
