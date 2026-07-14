```
███╗   ███╗██╗██████╗ ██╗   ██╗███████╗
████╗ ████║██║██╔══██╗██║   ██║██╔════╝
██╔████╔██║██║██████╔╝██║   ██║███████╗
██║╚██╔╝██║██║██╔══██╗██║   ██║╚════██║
██║ ╚═╝ ██║██║██║  ██║╚██████╔╝███████║
╚═╝     ╚═╝╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝
```

<div align="center">

# Mirus Launcher

«A cross-platform launcher that automatically runs the correct script for your operating system.»

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)
![Cross Platform](https://img.shields.io/badge/Cross--Platform-yes-brightgreen)
![License](https://img.shields.io/badge/License-Proprietary-red)

</div>

## 🚀 Usage

Run:

```bash
python MirusLauncher.py
```

The launcher automatically detects your operating system and executes the matching script.

## 🖥️ Supported OS

| Operating System | Executed File |
|---|---|
| 🪟 Windows | `MirusWindows.bat` |
| 🍎 macOS | `MirusMac.command` |
| 🐧 Linux | `MirusLinux.sh` |

## 📁 Repository Structure

```
.
├── LICENSE
├── README.md
├── MirusLauncher.py
├── MirusWindows.bat
├── MirusMac.command
└── MirusLinux.sh
```

## ℹ️ Notes

- Keep all files in the same folder.
- Requires Python 3.
- The launcher only opens the matching script for your system.
- The included scripts only display a harmless message — handy for a GitHub demo/showcase.
