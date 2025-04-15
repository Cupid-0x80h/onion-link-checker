
# 🧅 Onion Link Status Checker (Tor-Enabled)

This Python script is designed for cybersecurity researchers, ethical hackers, and privacy enthusiasts who want to **check the availability of `.onion` links** hosted on the Tor network. It categorizes the links based on their HTTP status codes and saves them into separate files.

> ✅ This script uses the Tor SOCKS5 proxy for anonymous access to `.onion` services.

---

## 📌 Features

- 🔒 Connects via Tor (SOCKS5 proxy)
- 📄 Reads `.onion` links from a `.docx` file
- 🔁 Follows redirects (301/302)
- ✅ Detects working links (200)
- ❌ Detects not working / unreachable links (timeouts, 4xx, 5xx)
- 📝 Outputs organized results to:
  - `working-links.txt`
  - `redirect-links.txt`
  - `notworking-links.txt`

---

## 📂 File Structure

```
.
├── onion-links.docx         # Input file containing onion links (one per line or paragraph)
├── working-links.txt        # Output file: links with 200 OK
├── redirect-links.txt       # Output file: links with 301/302
├── notworking-links.txt     # Output file: everything else
├── onion_checker.py         # The Python script
└── README.md                # You're here :)
```

---

## 🚀 Installation

### On Arch Linux

Install the required modules using the official Arch repo:

```bash
sudo pacman -S python-requests python-docx
```

Make sure Tor is installed and running:

```bash
sudo pacman -S tor
tor
```

---

## 🧠 Usage

1. Add all your `.onion` links to a file named `onion-links.docx`
2. Start the Tor service:
   ```bash
   tor
   ```
3. Run the script:
   ```bash
   python onion_checker.py
   ```

4. Check the output files for results.

---

## ⚠️ Disclaimer

This tool is intended for **educational and ethical research purposes only.**  
You are solely responsible for how you use this script.

- ❌ Do **NOT** use this tool to access or interact with illegal content or services.
- ✅ Always ensure you are complying with local laws and ethical standards.
- 👨‍💻 This is built as part of a white-hat research project.

---

## 💡 Future Ideas

- Add threading for faster scanning
- Support `.txt` and `.csv` input
- Add timestamped logs
  
---

## 🙌 Credits

Built with 💻 + ☕ by Cupid-0x80h  
Inspired by privacy, security, and responsible hacking.
