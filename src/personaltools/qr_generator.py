"""QR Code Generator CLI tool."""

import argparse
import sys
import qrcode


def main():
    """Generate QR codes from command line."""
    parser = argparse.ArgumentParser(
        description="Generate QR codes from text or URLs"
    )
    parser.add_argument(
        "text",
        help="Text or URL to encode in the QR code"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output file path (e.g., qr.png). If not provided, displays in terminal.",
        default=None
    )
    parser.add_argument(
        "--box-size",
        type=int,
        default=10,
        help="Size of each box in pixels (default: 10)"
    )
    parser.add_argument(
        "--border",
        type=int,
        default=4,
        help="Border size in boxes (default: 4)"
    )
    
    args = parser.parse_args()
    
    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=args.box_size,
        border=args.border,
    )
    qr.add_data(args.text)
    qr.make(fit=True)
    
    if args.output:
        # Save to file
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(args.output)
        print(f"QR code saved to {args.output}")
    else:
        # Print to terminal
        qr.print_ascii()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
