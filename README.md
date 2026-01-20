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

### Matplotlib Styles

Publication-quality matplotlib style files for scientific plotting.

**Available styles:**

- `ieee.mplstyle` - Optimized for IEEE publications and two-column journals

**Usage:**

```python
import matplotlib.pyplot as plt
from personaltools import pltstyles

# Use the IEEE style
plt.style.use(pltstyles.ieee)

# Create your plot
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9])
plt.savefig('plot.png')
```

See `src/personaltools/matplotlib_styles/README.md` for more details and usage examples.

