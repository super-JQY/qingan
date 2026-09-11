from pathlib import Path
from PIL import Image, ImageOps, ImageDraw
import sys

source = Path(sys.argv[1])
output = Path(sys.argv[2])
output.mkdir(parents=True, exist_ok=True)

for item in source.glob("*.jpg"):
    with Image.open(item) as image:
        image = ImageOps.exif_transpose(image).convert("RGB")
        image.thumbnail((1400, 1400), Image.Resampling.LANCZOS)
        image.save(output / f"{item.stem}.webp", "WEBP", quality=78, method=6)

files = sorted(output.glob("*.webp"))
thumbs = []
for item in files:
    with Image.open(item) as image:
        thumb = ImageOps.fit(image.convert("RGB"), (280, 180), method=Image.Resampling.LANCZOS)
        thumbs.append((item.stem, thumb.copy()))

sheet = Image.new("RGB", (600, 5 * 220), "#e8e2d5")
draw = ImageDraw.Draw(sheet)
for index, (name, thumb) in enumerate(thumbs):
    col, row = index % 2, index // 2
    x, y = 15 + col * 300, 12 + row * 220
    sheet.paste(thumb, (x, y))
    draw.text((x, y + 184), name, fill="#153b42")
sheet.save(output.parent.parent / "background-contact-sheet.jpg", quality=88)

