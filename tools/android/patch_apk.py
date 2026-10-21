"""Point the Android PTCGO APK + OBB at a Spirit server and re-sign the APK for sideloading."""

import argparse
import os
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SRC = ROOT / "game_apk_binaries"
DEFAULT_OUT = ROOT / "game_apk_binaries" / "patched"
SDK = Path(os.environ.get("ANDROID_HOME") or Path(os.environ["LOCALAPPDATA"]) / "Android" / "Sdk")


def build_tool(name):
    tools = sorted((SDK / "build-tools").glob("*"), reverse=True)
    for folder in tools:
        for candidate in (folder / f"{name}.exe", folder / f"{name}.bat", folder / name):
            if candidate.exists():
                return str(candidate)
    sys.exit(f"{name} not found under {SDK / 'build-tools'}; run tools/android/setup_emulator.ps1 first")


def patch_cfg(data, host, port):
    lines = data.decode("utf-8").splitlines()
    values = {"hostname": host, "versionURL": f"http://{host}:{port}/", "assetURL": f"http://{host}:{port}/"}
    out = []
    for line in lines:
        key = line.split("=", 1)[0]
        out.append(f"{key}={values.pop(key)}" if key in values else line)
    out.extend(f"{k}={v}" for k, v in values.items())
    return "\n".join(out).encode("utf-8")


def rewrite_zip(src, dst, host, port, drop_signature):
    patched = []
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w") as zout:
        for info in zin.infolist():
            name = info.filename
            if drop_signature and name.startswith("META-INF/") and name.rsplit(".", 1)[-1].upper() in ("SF", "RSA", "DSA", "EC", "MF"):
                continue
            data = zin.read(info)
            if name.endswith("cake.cfg"):
                data = patch_cfg(data, host, port)
                patched.append(name)
            zout.writestr(info, data, compress_type=info.compress_type)
    return patched


def ensure_keystore():
    keystore = Path.home() / ".android" / "debug.keystore"
    if not keystore.exists():
        keystore.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["keytool", "-genkeypair", "-keystore", str(keystore), "-storepass", "android",
                        "-keypass", "android", "-alias", "androiddebugkey", "-keyalg", "RSA", "-keysize", "2048",
                        "-validity", "10000", "-dname", "CN=Android Debug,O=Android,C=US"], check=True)
    return keystore


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="127.0.0.1", help="address the device dials (127.0.0.1 with adb reverse)")
    parser.add_argument("--http-port", type=int, default=8000)
    parser.add_argument("--src", type=Path, default=DEFAULT_SRC)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    apk = next(args.src.glob("*.apk"))
    obb = next(args.src.glob("main.*.obb"))
    args.out.mkdir(parents=True, exist_ok=True)

    unsigned = args.out / "unsigned.apk"
    aligned = args.out / "aligned.apk"
    signed = args.out / "ptcgo-spirit.apk"
    print("APK cake.cfg:", rewrite_zip(apk, unsigned, args.host, args.http_port, True))
    subprocess.run([build_tool("zipalign"), "-p", "-f", "4", str(unsigned), str(aligned)], check=True)
    keystore = ensure_keystore()
    subprocess.run([build_tool("apksigner"), "sign", "--ks", str(keystore), "--ks-pass", "pass:android",
                    "--key-pass", "pass:android", "--out", str(signed), str(aligned)], check=True)
    unsigned.unlink()
    aligned.unlink()
    for leftover in args.out.glob("*.idsig"):
        leftover.unlink()

    out_obb = args.out / obb.name
    print("OBB cake.cfg:", rewrite_zip(obb, out_obb, args.host, args.http_port, False))
    shutil.copystat(obb, out_obb)
    print(f"Wrote {signed}\nWrote {out_obb}")


if __name__ == "__main__":
    main()
