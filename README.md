# 🔐 Express.js HMAC Session Brute-Force Tool

## Overview

This tool is designed for **security researchers, penetration testers, and bug bounty hunters** to analyze and brute-force **HMAC-signed Express.js session cookies**. It helps determine the **hashing algorithm** used for signing the session and attempts to crack the **secret key** using a wordlist-based brute-force approach.

🚀 **Key Features:**

- **Brute-force Express.js session secrets** to validate security configurations.
    
- **Identify hashing algorithms** used for session signing based on signature length.
    
- **Supports multiple hashing algorithms** (SHA1, SHA256, SHA512, MD5, etc.).
    
- **Interactive ASCII tables** for analyzing hashing algorithms.
    
- **Handles Base64 encoding detection** for encoded signatures.
    

## ⚠️ Legal Disclaimer

This tool is intended for **ethical security testing and bug bounty research ONLY**. It **must NOT** be used for unauthorized or illegal activities. The developer **assumes no responsibility** for any misuse or unlawful intent. Use at your **own risk** and ensure compliance with applicable laws.

---

## 🛠 Installation

### **1️⃣ Clone the Repository**

```
git clone https://github.com/yourusername/express-hmac-brute.git
cd express-hmac-brute
```

### **2️⃣ Install Dependencies**

This script requires **Python 3.6+** and some additional dependencies.

```
pip install -r requirements.txt
```

#### Required Python Libraries:

- `tabulate` (for ASCII tables)
    
- `argparse` (for CLI handling)
    

Install manually if needed:

```
pip install tabulate argparse
```

---

## 🚀 Usage

### **Brute-Force an Express.js Session Secret**

```
python3 brute-force-hmac-express.py -c "s:<SESSION_ID>.<SIGNATURE>" -w rockyou.txt
```

**Example:**

```
python3 brute-force-hmac-express.py -c "s:Sro2O_Rv6bVcBJ_IhPjbJBKHw3ACiJMl.TYRYO4N+sf9AZd8K9dFnmBVdn7x9KFJzolb90r7Dt70" -w rockyou.txt
```

### **Specify a Different Hashing Algorithm** (default: SHA256)

```
python3 brute-force-hmac-express.py -c "s:<SESSION_ID>.<SIGNATURE>" -w rockyou.txt -a sha1
```

### **Identify the Hashing Algorithm of a Session Signature**

```
python3 brute-force-hmac-express.py -s "<SIGNATURE>"
```

**Example:**

```
python3 brute-force-hmac-express.py -s "TYRYO4N+sf9AZd8K9dFnmBVdn7x9KFJzolb90r7Dt70"
```

🔍 **Example Output:**

```
🔎 Hash Algorithm Identification:
+-----------------+-----------------------+
| Algorithm      | Confidence            |
+=================+=======================+
| SHA256        | ✅ Highly Likely       |
| Base64 Encoded?| ❌ No                 |
+-----------------+-----------------------+
```

### **Show Help Menu**

```
python3 brute-force-hmac-express.py --help
```

---

## 🔎 Hash Length Reference Table

|**Hash Algorithm**|**Hex Digest Length**|**Base64 Length**|
|---|---|---|
|MD5|32 chars|22 chars|
|SHA1|40 chars|27 chars|
|SHA256|64 chars|43 chars|
|SHA512|128 chars|86 chars|

---

## 🛡️ Intended Use & Ethical Hacking

This tool is created **solely for educational and security auditing purposes**. It is intended to help **pentesters & bug bounty hunters** understand **Express.js session security weaknesses** and **identify misconfigured secrets**.

⚠️ **Unauthorized use is illegal.** Ensure you have **explicit permission** before testing any systems. The developer does not take responsibility for misuse.

---

## 📜 License

This tool is released under the **MIT License**. See the LICENSE file for more details.

---

## 🛠 Contributing

Want to improve this tool? Contributions are welcome!

1. Fork the repository
    
2. Create a new branch (`git checkout -b feature-name`)
    
3. Commit your changes (`git commit -m 'Added new feature'`)
    
4. Push to your branch (`git push origin feature-name`)
    
5. Open a pull request 🚀
    

---

## 📬 Contact

🐺 **The Nightmare Wolf**

- **GitHub:** [github.com/nightmare-wolf](https://github.com/nightmare-wolf)
    

---

### **⭐ If you find this tool useful, please consider starring the repo!** ⭐
