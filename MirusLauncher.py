from pathlib import Path
import platform, subprocess, sys

base = Path(__file__).resolve().parent
system = platform.system().lower()

if system == "windows":
    script = base / "MirusWindows.bat"
    subprocess.run(["cmd","/c",str(script)], cwd=base)
elif system == "darwin":
    script = base / "MirusMac.command"
    subprocess.run(["/bin/bash",str(script)], cwd=base)
elif system == "linux":
    script = base / "MirusLinux.sh"
    subprocess.run(["/bin/sh",str(script)], cwd=base)
else:
    print("Unsupported OS:", platform.system())
    sys.exit(1)
