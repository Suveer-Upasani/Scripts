import subprocess
import json
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
    "https://demo.owasp-juice.shop"
]

wordlist = "Wordlist/common.txt"

results_dir = Path("results")
results_dir.mkdir(exist_ok=True)

print(f"\n{CYAN}{'=' * 60}")
print("        FFUF Automation Scanner")
print(f"{'=' * 60}{RESET}\n")

for target in targets:
    hostname = (
        target.replace("https://", "")
        .replace("http://", "")
        .replace("/", "_")
    )

    output_file = results_dir / f"{hostname}.json"

    print(f"{BLUE}[*] Target:{RESET} {target}")
    print(f"{BLUE}[*] Wordlist:{RESET} {wordlist}")
    print(f"{BLUE}[*] Output:{RESET} {output_file}")
    print(f"{YELLOW}[*] Started:{RESET} {datetime.now()}\n")

    cmd = [
        "ffuf",
        "-u", f"{target}/FUZZ",
        "-w", wordlist,
        "-v",
        "-c",                    # FFUF color output
        "-t", "20",              # Threads
        "-rate", "50",           # Requests/sec
        "-mc", "200,301,302,401,403",
        "-of", "json",
        "-o", str(output_file)
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

        try:
            with open(output_file, "r") as f:
                data = json.load(f)

            # Detailed TXT report
            report_file = results_dir / f"{hostname}_report.txt"

            with open(report_file, "w") as report:
                report.write(f"Target: {target}\n")
                report.write(f"Scan Time: {datetime.now()}\n")
                report.write("=" * 70 + "\n\n")

                for result in data.get("results", []):
                    report.write(
                        f"[{result['status']}] "
                        f"{result['url']} "
                        f"(Size: {result['length']}, "
                        f"Words: {result['words']}, "
                        f"Lines: {result['lines']})\n"
                    )

            # URLs-only TXT file
            urls_file = results_dir / f"{hostname}_urls.txt"

            with open(urls_file, "w") as urls:
                for result in data.get("results", []):
                    urls.write(result["url"] + "\n")

            print(f"{GREEN}[+] Report saved to:{RESET} {report_file}")
            print(f"{GREEN}[+] URLs saved to:{RESET} {urls_file}")
            print(
                f"{GREEN}[+] Total routes found:{RESET} "
                f"{len(data.get('results', []))}"
            )

        except Exception as e:
            print(f"{RED}[!] Error creating TXT reports: {e}{RESET}")

    else:
        print(f"{RED}[!] FFUF Scan Failed{RESET}")

    print(f"{YELLOW}[*] Finished:{RESET} {datetime.now()}")
    print(f"{CYAN}{'-' * 60}{RESET}\n")