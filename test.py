import time
import subprocess

print("=== プログラム 実行開始===")
timer = time.time()
actual = (
    subprocess.run(
        ["bash", "-c", "python script.py < input.txt"], stdout=subprocess.PIPE
    )
    .stdout.decode()
    .removesuffix("\n")
)
print(actual)
timer_total = (time.time() - timer) * 100
print("=== プログラム 実行終了===")

with open("./answer.txt") as f:
    expected = f.read().removesuffix("\n")

if actual == expected:
    print("テスト OK")
else:
    print(f"テスト NG: expected: {expected}, actual: {actual}")

print(f"所要時間: { timer_total } ms")
