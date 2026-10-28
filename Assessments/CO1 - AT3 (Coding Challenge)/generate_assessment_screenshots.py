"""
Tokyo Night Terminal Screenshot Generator for CO1 - AT3 Coding Challenge
Course: DSA0302 - Natural Language Processing
Author: Ravilla Bhanu Prakash
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
    elif l_str.startswith("[+]") or "PASSED" in l_str or "ACCEPT" in l_str or "AGREED" in l_str:
        return "#9ece6a"  # Tokyo Night Green
    elif l_str.startswith("[-]") or "REJECT" in l_str or "FAILED" in l_str:
        return "#f7768e"  # Tokyo Night Red
    elif l_str.startswith("[*]") or l_str.startswith(">>>") or (l_str.startswith("[") and "]" in l_str):
        return "#e0af68"  # Warm Amber
    elif ":" in l_str and len(l_str.split(":")[0]) < 25:
        return "#7dcfff"  # Soft Cyan label
    elif "+" in l_str:
        return "#bb9af7"  # Parse tag highlight
    return "#c0caf5"      # Crisp Tokyo Night foreground text

def create_terminal_screenshot(prob_name, script_name, output_text, target_png):
    lines = output_text.splitlines()

    # Dimensions
    pad_x = 35
    pad_y = 35
    term_width = 1050
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

    # Shadow
    for offset in range(10, 0, -2):
        draw.rounded_rectangle([x0 - offset, y0 - offset, x1 + offset, y1 + offset], radius=16, fill="#090a0f")

    # Terminal Container
    draw.rounded_rectangle([x0, y0, x1, y1], radius=12, fill="#1a1b26", outline="#292e42", width=1)

    # Title Bar
    draw.rounded_rectangle([x0, y0, x1, y0 + title_bar_height], radius=12, fill="#1f2335")
    draw.rectangle([x0, y0 + 15, x1, y0 + title_bar_height], fill="#1f2335")
    draw.line([(x0, y0 + title_bar_height), (x1, y0 + title_bar_height)], fill="#292e42", width=1)

    # Window Controls
    btn_y = y0 + title_bar_height // 2
    draw.ellipse([x0 + 16, btn_y - 6, x0 + 28, btn_y + 6], fill="#f7768e")
    draw.ellipse([x0 + 36, btn_y - 6, x0 + 48, btn_y + 6], fill="#e0af68")
    draw.ellipse([x0 + 56, btn_y - 6, x0 + 68, btn_y + 6], fill="#9ece6a")

    # Title Text
    title_label = f"bhanu-prakash@simats-nlp-lab: ~/DSA0302-NLP/Assessments/CO1/Programs/{script_name}"
    draw.text((x0 + 85, btn_y - 9), title_label, font=title_font, fill="#9aa5ce")

    # 3. Terminal Prompt Line
    curr_y = y0 + title_bar_height + content_pad_y
    curr_x = x0 + content_pad_x

    prompt_prefix = "bhanu@nlp-workstation:~/Assessments/CO1/Programs$ "
    draw.text((curr_x, curr_y), prompt_prefix, font=bold_font, fill="#bb9af7")
    prefix_w = int(draw.textlength(prompt_prefix, font=bold_font))
    draw.text((curr_x + prefix_w, curr_y), f"python {script_name}", font=bold_font, fill="#7aa2f7")
    curr_y += LINE_HEIGHT + 6

    # 4. Render Body Lines
    for line in lines:
        c = get_line_color(line)
        draw.text((curr_x, curr_y), line, font=font, fill=c)
        curr_y += LINE_HEIGHT

    # 5. Footer Bar
    footer_y = y1 - footer_height
    draw.line([(x0, footer_y), (x1, footer_y)], fill="#292e42", width=1)
    footer_text = "Verified by Bhanu Prakash  •  CO1 - AT3 Coding Challenge  •  SIMATS Engineering"
    draw.text((curr_x, footer_y + 7), footer_text, font=footer_font, fill="#565f89")

    # Save target image
    os.makedirs(os.path.dirname(target_png), exist_ok=True)
    img.save(target_png, "PNG", optimize=True)
    print(f"Generated assessment screenshot: {os.path.basename(target_png)}")

def main():
    problems = [
        ("P01", "01_Tokenization_Regex.py", "P01_01_Tokenization_Regex_Output.png"),
        ("P02", "02_Simulate_FSA.py", "P02_02_Simulate_FSA_Output.png"),
        ("P03", "03_Inflectional_Morphology.py", "P03_03_Inflectional_Morphology_Output.png"),
        ("P04", "04_Morphological_Parsing.py", "P04_04_Morphological_Parsing_Output.png"),
        ("P05", "05_Porter_Stemmer_Step1.py", "P05_05_Porter_Stemmer_Step1_Output.png"),
    ]

    for p_id, script_name, png_name in problems:
        txt_file = os.path.join(OUTPUTS_DIR, f"{p_id}_Output.txt")
        png_file = os.path.join(OUTPUTS_DIR, png_name)

        if not os.path.exists(txt_file):
            print(f"Warning: {txt_file} missing. Skipping.")
            continue

        with open(txt_file, "r", encoding="utf-8") as f:
            output_text = f.read()

        create_terminal_screenshot(p_id, script_name, output_text, png_file)

    print("All assessment screenshots generated successfully.")

if __name__ == "__main__":
    main()
