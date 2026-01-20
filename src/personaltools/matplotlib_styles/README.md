# Matplotlib Styles

This directory contains matplotlib style files for creating publication-quality plots.

## Available Styles

### ieee.mplstyle

A matplotlib style optimized for IEEE publications and two-column journals. This style is based on SciencePlots and includes:

- Appropriate figure sizing for two-column layouts (2.5" x 2.2")
- Scientific fonts (Computer Modern Roman with LaTeX support)
- Proper tick styling with inward-facing ticks
- Color cycle optimized for both color and black-and-white printing
- Tight layout for space efficiency

## Usage

The easiest way to use a style from this collection:

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

Alternatively, you can copy the style to your matplotlib config directory:

```bash
# Find your matplotlib config directory
python -c "import matplotlib; print(matplotlib.get_configdir())"

# Copy the style file to the stylelib directory
cp ieee.mplstyle ~/.matplotlib/stylelib/

# Then use it directly by name
python -c "import matplotlib.pyplot as plt; plt.style.use('ieee')"
```

## Requirements

The IEEE style requires:
- LaTeX installation (for text.usetex = True)
- amsmath and amssymb LaTeX packages

If you don't have LaTeX installed, you can modify the style file to set `text.usetex : False`.
