# personaltools

Collection of personal tools that can be installed using uv and used globally

## Installation

Install using uv:

```bash
uv tool install git+https://github.com/mkofler96/personaltools
```

Or install from a local clone:

```bash
uv tool install /path/to/personaltools
```

## Tools

### qr-gen

Generate QR codes from text or URLs.

**Usage:**

```bash
# Display QR code in terminal
qr-gen "https://example.com"

# Save QR code to file
qr-gen "Hello World" -o qr.png

# Customize QR code size and border
qr-gen "https://example.com" -o qr.png --box-size 15 --border 2
```

**Options:**

- `text` - Text or URL to encode in the QR code (required)
- `-o, --output` - Output file path (e.g., qr.png). If not provided, displays in terminal
- `--box-size` - Size of each box in pixels (default: 10)
- `--border` - Border size in boxes (default: 4)
