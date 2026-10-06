"""Cover picture of the profile README: name and tagline next to four real screens of the AK Base Kit demo.

  python tools/make_banner.py <folder with the demo screenshots (*.pbm)> assets/banner.png
"""
import os
import sys

from PIL import Image, ImageDraw, ImageFont

W, H = 1600, 420
TEAL_DARK, TEAL, NAVY, WHITE, PIXEL = "#2C6E6E", "#3A8F8F", "#2E4057", "#FFFFFF", "#E8F5F5"
FONTS = "C:/Windows/Fonts/"
SCREENS = ["2_clock_rtc", "35_tetris_autoplay", "28_maze_start", "50_scope_test_wave"]


def screen(path, scale):
    lines = open(path).read().split("\n")[2:]
    img = Image.new("RGB", (128, 64), "#000000")
    px = img.load()
    for y in range(64):
        for x in range(128):
            if lines[y][x] == "1":
                px[x, y] = (232, 245, 245)
    return img.resize((128 * scale, 64 * scale), Image.NEAREST)


def main():
    shots, out = sys.argv[1], sys.argv[2]
    img = Image.new("RGB", (W, H), TEAL_DARK)
    d = ImageDraw.Draw(img)
    # a quiet grid of display pixels behind everything
    for x in range(0, W, 16):
        for y in range(0, H, 16):
            d.rectangle([x + 6, y + 6, x + 8, y + 8], fill="#327878")

    name = ImageFont.truetype(FONTS + "segoeuib.ttf", 84)
    alias = ImageFont.truetype(FONTS + "segoeuib.ttf", 34)
    line = ImageFont.truetype(FONTS + "segoeui.ttf", 30)
    small = ImageFont.truetype(FONTS + "consola.ttf", 24)

    d.rectangle([80, 96, 88, 324], fill=PIXEL)
    d.text((120, 84), "Hồ Hoàng Anh", font=name, fill=WHITE)
    d.text((122, 190), "ANH MAKERX", font=alias, fill=PIXEL)
    d.text((122, 250), "Hardware Engineer — thiết kế mạch, firmware nhúng,", font=line, fill=WHITE)
    d.text((122, 290), "công cụ kiểm thử cho sản xuất", font=line, fill=WHITE)

    scale, gap = 2, 16
    sw, sh = 128 * scale, 64 * scale
    x0, y0 = W - 80 - 2 * sw - gap, (H - 2 * sh - gap) // 2 - 10
    for i, s in enumerate(SCREENS):
        x, y = x0 + (i % 2) * (sw + gap), y0 + (i // 2) * (sh + gap)
        d.rectangle([x - 6, y - 6, x + sw + 5, y + sh + 5], fill="#000000", outline=NAVY, width=2)
        img.paste(screen(os.path.join(shots, s + ".pbm"), scale), (x, y))
    d.text((x0 - 6, y0 + 2 * sh + gap + 14), "firmware thật trên OLED của AK Base Kit", font=small, fill=PIXEL)

    os.makedirs(os.path.dirname(out), exist_ok=True)
    img.save(out, optimize=True)
    print(out, img.size, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
