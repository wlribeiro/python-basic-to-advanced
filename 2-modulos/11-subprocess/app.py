import subprocess


# windows ping 127.0.0.1
# linux ping 127.0.0.1 -c 4


proc = subprocess.run(
    ['ping', '127.0.0.1'],
    capture_output = True,
    text = True
)


print(proc.stdout)