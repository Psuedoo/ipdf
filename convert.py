import img2pdf
import argparse

parser = argparse.ArgumentParser(
    description="A CLI utility to convert an image to a PDF."
)

parser.add_argument(
    "--img", action="store", type=str, help="Path to the image", dest="img"
)

parser.add_argument(
    "--output", action="store", type=str, help="Desired path to the PDF", dest="output"
)


args = parser.parse_args()

with open(f"{args.output}.pdf", "wb") as f:
    f.write(img2pdf.convert(args.img))
