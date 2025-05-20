import re
import requests
import os
import json

# Log file from Rocky forwarded to Ubuntu
LOG_FILE = "/var/log/remote/rocky-cloud/sshd.log"

# Your ngrok-exposed AI endpoint
NGROK_API = "https://0c95-81-106-89-198.ngrok-free.app/api/generate"

# Target service we're interested in
ATTACKED_SERVICE = "sshd"

def parse_failed_logins():
    entries = []
    with open(LOG_FILE, "r") as file:
        for line in file:
            if "Failed password" in line and ATTACKED_SERVICE in line:
                ip_match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
                if ip_match:
                    ip = ip_match.group(1)
                    prompt = f"{line.strip()}"
                    entry = {
                        "model": "llama3",
                        "prompt": prompt,
                        "system": "You are a cybersecurity AI trained to detect brute force login attempts. Respond with the risk level, reasoning, and recommendation."
                    }
                    entries.append((entry, ip))
    return entries

def send_to_ai(entries):
    for log, ip in entries:
        try:
            response = requests.post(NGROK_API, json=log)
            print(f"\n🟡 Prompt: {log['prompt']}")
            print("🔵 RAW RESPONSE:", response.text)

            # Try to parse the first JSON object only
            first_line = response.text.strip().splitlines()[0]
            result = json.loads(first_line)

            print("✅ AI Response:", result)

            if result.get("result") == "brute_force":
                os.system(f"sudo iptables -A INPUT -s {ip} -j DROP")
                print(f"🚫 Blocked IP: {ip}")
        except Exception as e:
            print("❌ Error sending to AI or parsing response:", e)

if __name__ == "__main__":
    failed_entries = parse_failed_logins()
    if not failed_entries:
        print("✅ No failed SSH login attempts found.")
    else:
        send_to_ai(failed_entries)
