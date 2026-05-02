from pathlib import Path
import base64

svg_path = Path("assets/am-i-dreaming-player.svg")
cover_path = Path("assets/am-i-dreaming-cover.png")

svg = svg_path.read_text(encoding="utf-8")
cover_b64 = base64.b64encode(cover_path.read_bytes()).decode("utf-8")
data_uri = f"data:image/png;base64,{cover_b64}"

svg = svg.replace('href="./am-i-dreaming-cover.png"', f'href="{data_uri}"')
svg = svg.replace('href="am-i-dreaming-cover.png"', f'href="{data_uri}"')
svg = svg.replace(
    'xmlns="http://www.w3.org/2000/svg"',
    'xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"'
)

svg_path.write_text(svg, encoding="utf-8")
