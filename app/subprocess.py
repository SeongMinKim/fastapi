import subprocess


def look(edge: str, domain: str):
    proc = subprocess.Popen(
        ["./echo.sh", edge, domain],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    output, err = proc.communicate()

    if err:
        raise Exception(err.decode())

    print(output.decode())
