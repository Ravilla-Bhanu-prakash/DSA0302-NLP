"""
Tokyo Night Terminal Screenshot Generator for NLP Laboratory Experiments
Course: DSA0302 - Natural Language Processing
Repository: Ravilla-Bhanu-prakash/DSA0302-NLP
Student: Ravilla Bhanu Prakash
"""

import os
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUTS_DIR = os.path.join(BASE_DIR, "outputs")
PROGRAMS_DIR = os.path.join(BASE_DIR, "Programs")

FONT_PATH = "C:/Windows/Fonts/consola.ttf"
BOLD_FONT_PATH = "C:/Windows/Fonts/consolab.ttf"
TITLE_FONT_PATH = "C:/Windows/Fonts/segoeui.ttf"
FONT_SIZE = 15
LINE_HEIGHT = 22

try:
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    bold_font = ImageFont.truetype(BOLD_FONT_PATH, FONT_SIZE)
    title_font = ImageFont.truetype(TITLE_FONT_PATH, 13)
    footer_font = ImageFont.truetype(TITLE_FONT_PATH, 11)
except Exception:
    font = ImageFont.load_default()
    bold_font = font
    title_font = font
    footer_font = font

def get_line_color(line):
    l_str = line.strip()
    if l_str.startswith("=" * 10):
        return "#7aa2f7"  # Electric Indigo
    elif l_str.startswith("-" * 10):
        return "#bb9af7"  # Soft Lavender / Purple
    elif l_str.startswith("[+]") or "PASSED" in l_str or "ACCEPTED" in l_str or "AGREED" in l_str:
        return "#9ece6a"  # Tokyo Night Green
    elif l_str.startswith("[-]") or "REJECTED" in l_str or "FAILED" in l_str:
        return "#f7768e"  # Tokyo Night Red
    elif l_str.startswith("[*]") or l_str.startswith(">>>") or (l_str.startswith("[") and "]" in l_str):
        return "#e0af68"  # Warm Amber
    elif ":" in l_str and len(l_str.split(":")[0]) < 25:
        return "#7dcfff"  # Soft Cyan label
    elif l_str.startswith("Step") or l_str.startswith("Rank") or l_str.startswith("Pair"):
        return "#bb9af7"  # Light Purple
    return "#c0caf5"      # Crisp Tokyo Night foreground text

def create_terminal_screenshot(exp_num, exp_folder, output_text, target_png):
    lines = output_text.splitlines()
    if len(lines) > 48:
        lines = lines[:45] + ["... [Output truncated for display; see Exp" + exp_num + "_Output.txt for full log] ..."] + lines[-2:]

    # Dimensions
    pad_x = 35
    pad_y = 35
    term_width = 1180
    title_bar_height = 40
    content_pad_x = 24
    content_pad_y = 18
    footer_height = 28

    # Calculate height
    num_content_lines = len(lines) + 2  # Include prompt lines
    term_height = title_bar_height + (content_pad_y * 2) + (num_content_lines * LINE_HEIGHT) + footer_height
    img_width = term_width + (pad_x * 2)
    img_height = term_height + (pad_y * 2)

    # 1. Base Canvas (Deep Obsidian Void)
    img = Image.new("RGB", (img_width, img_height), "#13141c")
    draw = ImageDraw.Draw(img)

    # 2. Terminal Shadow & Background Window
    x0, y0 = pad_x, pad_y
    x1, y1 = pad_x + term_width, pad_y + term_height

    # Glowing subtle shadow effect
    for offset in range(10, 0, -2):
        alpha_color = "#090a0f"
        draw.rounded_rectangle([x0 - offset, y0 - offset, x1 + offset, y1 + offset], radius=16, fill=alpha_color)

    # Terminal Container (Tokyo Night Storm)
    draw.rounded_rectangle([x0, y0, x1, y1], radius=12, fill="#1a1b26", outline="#292e42", width=1)

    # Title Bar
    draw.rounded_rectangle([x0, y0, x1, y0 + title_bar_height], radius=12, fill="#1f2335")
    draw.rectangle([x0, y0 + 15, x1, y0 + title_bar_height], fill="#1f2335")  # Square bottom corners
    draw.line([(x0, y0 + title_bar_height), (x1, y0 + title_bar_height)], fill="#292e42", width=1)

    # Window Controls (macOS frosted dots)
    btn_y = y0 + title_bar_height // 2
    draw.ellipse([x0 + 16, btn_y - 6, x0 + 28, btn_y + 6], fill="#f7768e")  # Close
    draw.ellipse([x0 + 36, btn_y - 6, x0 + 48, btn_y + 6], fill="#e0af68")  # Minimize
    draw.ellipse([x0 + 56, btn_y - 6, x0 + 68, btn_y + 6], fill="#9ece6a")  # Maximize

    # Title Text
    title_label = f"bhanu-prakash@simats-nlp-lab: ~/DSA0302-NLP/Lab/Programs/{exp_folder} (python main.py)"
    draw.text((x0 + 85, btn_y - 9), title_label, font=title_font, fill="#9aa5ce")

    # 3. Terminal Prompt Line
    curr_y = y0 + title_bar_height + content_pad_y
    curr_x = x0 + content_pad_x

    prompt_prefix = "bhanu@nlp-workstation:~/DSA0302-NLP/Lab/Programs/" + exp_folder + "$ "
    draw.text((curr_x, curr_y), prompt_prefix, font=bold_font, fill="#bb9af7")
    prefix_w = int(draw.textlength(prompt_prefix, font=bold_font))
    draw.text((curr_x + prefix_w, curr_y), "python main.py", font=bold_font, fill="#7aa2f7")
    curr_y += LINE_HEIGHT + 6

    # 4. Render Body Output Lines
    for line in lines:
        c = get_line_color(line)
        draw.text((curr_x, curr_y), line, font=font, fill=c)
        curr_y += LINE_HEIGHT

    # 5. Footer Bar (Divider + Verification Tag)
    footer_y = y1 - footer_height
    draw.line([(x0, footer_y), (x1, footer_y)], fill="#292e42", width=1)
    footer_text = "Verified by Bhanu Prakash  •  DSA0302 Automated NLP Lab Suite  •  SIMATS Engineering"
    draw.text((curr_x, footer_y + 7), footer_text, font=footer_font, fill="#565f89")

    # Save target image
    os.makedirs(os.path.dirname(target_png), exist_ok=True)
    img.save(target_png, "PNG", optimize=True)
    print(f"Generated screenshot: {os.path.basename(target_png)}")

def main():
    experiments = sorted([d for d in os.listdir(PROGRAMS_DIR) if os.path.isdir(os.path.join(PROGRAMS_DIR, d))])
    print(f"Generating Tokyo Night screenshots for {len(experiments)} experiments...")

    for exp_folder in experiments:
        exp_num = exp_folder[:2]
        txt_file = os.path.join(OUTPUTS_DIR, f"Exp{exp_num}_Output.txt")
        png_file = os.path.join(OUTPUTS_DIR, f"Exp{exp_num}_{exp_folder}.png")

        if not os.path.exists(txt_file):
            print(f"Warning: Transcript {txt_file} missing. Skipping.")
            continue

        with open(txt_file, "r", encoding="utf-8") as f:
            output_text = f.read()

        create_terminal_screenshot(exp_num, exp_folder, output_text, png_file)

    print("All screenshots generated successfully.")

if __name__ == "__main__":
    main()
