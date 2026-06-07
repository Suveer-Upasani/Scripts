import subprocess
from pathlib import Path
from datetime import datetime

# ANSI Colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"

targets = [
    "scanme.nmap.org"  # Replace with systems you own or are authorized to test
]

results_dir = Path("results")
results_dir.mkdir(exist_ok=True)

print(f"\n{CYAN}{'=' * 60}")
print("           NMAP Automation Scanner")
print(f"{'=' * 60}{RESET}\n")

for target in targets:

    hostname = (
        target.replace("https://", "")
        .replace("http://", "")
        .replace("/", "_")
    )

    output_file = results_dir / f"{hostname}.xml"

    print(f"{BLUE}[*] Target:{RESET} {target}")
    print(f"{BLUE}[*] Output:{RESET} {output_file}")
    print(f"{YELLOW}[*] Started:{RESET} {datetime.now()}\n")

    cmd = [
        "nmap",
        "-sV",                # Service detection
        "-Pn",                # Skip host discovery
        "-T4",                # Faster timing
        "-oX", str(output_file),
        target
    ]

    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1
    )

    for line in process.stdout:
        print(line, end="")

    process.wait()

    print()

    if process.returncode == 0:
        print(f"{GREEN}[+] Scan Completed Successfully{RESET}")
        print(f"{GREEN}[+] Results saved to:{RESET} {output_file}")
    else:
        print(f"{RED}[!] Nmap Scan Failed{RESET}")

    print(f"{YELLOW}[*] Finished:{RESET} {datetime.now()}")
    print(f"{CYAN}{'-' * 60}{RESET}\n")