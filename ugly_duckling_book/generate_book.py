#!/usr/bin/env python3
"""
The Ugly Duckling - Premium 6-Page Landscape Children's Picture Book
Professional graphic design + storytelling + education
"""

from reportlab.lib.pagesizes import landscape
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import Color, HexColor
from reportlab.lib.utils import ImageReader
from PIL import Image
import os
import textwrap

# Page size: 11" x 8.5" landscape (classic picture book proportion)
PAGE_WIDTH = 11 * inch
PAGE_HEIGHT = 8.5 * inch

# Project paths
BASE_DIR = r"C:\Users\amira\ugly_duckling_book"
IMAGES_DIR = os.path.join(BASE_DIR, "images")
OUTPUT_PDF = os.path.join(BASE_DIR, "output", "The_Ugly_Duckling_Premium_Edition.pdf")

# Premium Color Palette
DEEP_TEAL = HexColor("#1E3A3A")
WARM_SLATE = HexColor("#2C3E50")
CREAM = HexColor("#FDF8F0")
SOFT_MINT_CREAM = HexColor("#F0F7F4")
WARM_TAUPE = HexColor("#D4C9B8")
GOLD_ACCENT = HexColor("#C9A227")
CORAL_ACCENT = HexColor("#D35400")
SOFT_GOLD = HexColor("#E8C547")

# Font paths (Windows system)
FONT_BRUSH = r"C:\Windows\Fonts\BRUSHSCI.TTF"
FONT_GEORGIA = r"C:\Windows\Fonts\georgia.ttf"
FONT_GEORGIA_BOLD = r"C:\Windows\Fonts\georgiab.ttf"
FONT_GEORGIA_ITALIC = r"C:\Windows\Fonts\georgiai.ttf"

# Register fonts
pdfmetrics.registerFont(TTFont("BrushScript", FONT_BRUSH))
pdfmetrics.registerFont(TTFont("Georgia", FONT_GEORGIA))
pdfmetrics.registerFont(TTFont("GeorgiaBold", FONT_GEORGIA_BOLD))
pdfmetrics.registerFont(TTFont("GeorgiaItalic", FONT_GEORGIA_ITALIC))

# Page content - refined for perfect pacing and emotional arc
PAGES = {
    1: {  # COVER
        "type": "cover",
        "title": "THE UGLY DUCKLING",
        "subtitle": "A Story About Courage, Kindness,\nand Becoming Who You Are Meant to Be",
        "footer": "For every child who has ever felt different",
    },
    2: {  # HATCHING
        "type": "story",
        "header": "A Different Kind of Beautiful",
        "body": "In a cozy nest tucked among the reeds, Mother Duck waited patiently.\n\nOne by one, the shells cracked. Five tiny yellow ducklings tumbled out, peeping with joy.\n\nBut the biggest egg took the longest.\n\nWhen it finally opened, out wobbled a large grey duckling with a long neck and very big feet.\n\nThe yellow ducklings stared in surprise.\n\nMother Duck smiled warmly and gathered him close with her wing.\n\n\"You are different, little one,\" she whispered. \"But you are mine. And you are loved.\"",
    },
    3: {  # TEASING
        "type": "story",
        "header": "The Unkind Words",
        "body": "When the family swam to the big pond, the other ducks gathered around.\n\n\"Look at that one!\" squawked a proud white duck. \"He's so grey and clumsy!\"\n\n\"His feet are too big!\" laughed another.\n\n\"His neck is too long!\" said a third.\n\nThe little grey duckling tried to hide behind his mother. His heart felt heavy and sore.\n\nEven his yellow brothers and sisters swam away to play without him.\n\n\"Why am I so ugly?\" he asked the still water.\n\nA tear rolled down his cheek and made a tiny ripple.",
    },
    4: {  # WINTER
        "type": "story",
        "header": "The Long Winter",
        "body": "The little duckling could not bear the cruel words any longer.\n\nOne foggy morning he slipped away from the only home he knew.\n\nHe walked through golden autumn fields, then into lonely marshes where wild ducks hissed, \"Go away, ugly thing!\"\n\nWinter arrived with bitter winds. Snow covered everything.\n\nCold and hungry, the little duckling found shelter under an old wooden bridge.\n\nHe curled into a tiny ball, listening to the howling wind, and wondered if anyone in the whole wide world would ever be kind to him.",
    },
    5: {  # REFLECTION
        "type": "story",
        "header": "The Reflection",
        "body": "At last, the ice melted. Warm sun touched the earth again.\n\nThe little duckling, now much bigger, came to a peaceful lake.\n\nThere he saw the most magnificent birds he had ever seen — swans! Their feathers were whiter than clouds. Their necks curved like the most graceful music.\n\nHe watched them in awe, his heart aching with a strange new feeling.\n\nSlowly he paddled closer, expecting them to chase him away too.\n\nThen he saw his own reflection in the glassy water...\n\nA long elegant white neck. Brilliant white wings. Eyes that sparkled like stars.\n\nHe was not an ugly duckling at all.\n\nHe was a swan.",
    },
    6: {  # ENDING
        "type": "ending",
        "header": "You Are Beautiful",
        "body": "The swans welcomed him with open wings.\n\n\"You are one of us,\" they said gently.\n\nChildren playing by the shore pointed and laughed with delight.\n\n\"Look! The most beautiful swan has joined the family!\"\n\nThe young swan raised his long neck proudly and smiled.\n\nHe finally understood: He had always been beautiful. He simply needed time, patience, and the right place to grow into himself.\n\nAnd so he lived happily, swimming with grace and kindness, never forgetting how it felt to be left out.\n\nBecause true beauty lives in the heart that chooses to be kind.",
        "moral": "Being different is not being less.\nIt is often the first sign that you are something truly special.",
        "questions": "Talk together: Have you ever felt different? What helps you feel brave when you are new or unsure?",
    },
}

def draw_rounded_rect(c, x, y, width, height, radius=12, fill_color=None, stroke_color=None, stroke_width=0.5, alpha=0.92):
    """Draw a beautiful rounded rectangle panel"""
    c.saveState()
    if fill_color:
        if alpha < 1.0:
            r, g, b = fill_color.red, fill_color.green, fill_color.blue
            c.setFillColor(Color(r, g, b, alpha))
        else:
            c.setFillColor(fill_color)
        c.roundRect(x, y, width, height, radius, fill=1, stroke=0)
    if stroke_color:
        c.setStrokeColor(stroke_color)
        c.setLineWidth(stroke_width)
        c.roundRect(x, y, width, height, radius, fill=0, stroke=1)
    c.restoreState()

def draw_image_full_bleed(c, image_path, page_width, page_height):
    """Scale and center-crop image to completely fill the landscape page with premium cinematic framing"""
    img = Image.open(image_path)
    img_w, img_h = img.size
    img_ratio = img_w / img_h
    page_ratio = page_width / page_height

    # Calculate scale to cover the entire page (crop if needed)
    if img_ratio > page_ratio:
        # Image is wider: fit to height, crop left/right
        scale = page_height / img_h
        new_h = page_height
        new_w = img_w * scale
        x_offset = (new_w - page_width) / 2
        c.drawImage(image_path, -x_offset, 0, width=new_w, height=new_h, preserveAspectRatio=False)
    else:
        # Image is taller: fit to width, crop top/bottom
        scale = page_width / img_w
        new_w = page_width
        new_h = img_h * scale
        y_offset = (new_h - page_height) / 2
        c.drawImage(image_path, 0, -y_offset, width=new_w, height=new_h, preserveAspectRatio=False)

def draw_soft_vignette(c, width, height, intensity=0.18):
    """Add subtle professional vignette for depth and premium book feel"""
    c.saveState()
    steps = 8
    for i in range(steps):
        alpha = intensity * (i + 1) / steps
        inset = i * 14
        c.setFillColor(Color(0.06, 0.1, 0.09, alpha))
        c.rect(inset, inset, width - 2*inset, height - 2*inset, fill=1, stroke=0)
    c.restoreState()

def draw_header_ornament(c, x, y, width=120):
    """Simple elegant reed/leaf ornament"""
    c.saveState()
    c.setStrokeColor(Color(0.3, 0.45, 0.35, 0.6))
    c.setLineWidth(0.8)
    # Central stem
    c.line(x, y, x + width, y)
    # Small leaves
    for i, offset in enumerate([0.2, 0.45, 0.7]):
        lx = x + width * offset
        c.setLineWidth(0.6)
        c.line(lx, y, lx - 6, y + 5)
        c.line(lx, y, lx + 6, y + 4)
        c.line(lx, y, lx - 5, y - 4)
    c.restoreState()

def draw_feather_page_number(c, page_num, total=6, y=32):
    """Elegant centered page number with tiny feather motif"""
    c.saveState()
    text = f"— {page_num} —"
    c.setFont("Georgia", 9.5)
    c.setFillColor(Color(0.22, 0.32, 0.28, 0.8))
    text_width = c.stringWidth(text, "Georgia", 9.5)
    c.drawString((PAGE_WIDTH - text_width) / 2, y, text)
    c.restoreState()

def draw_text_wrapped(c, text, x, y, max_width, font_name, font_size, leading, color, align="left"):
    """Simple word-wrapped text drawing"""
    c.setFont(font_name, font_size)
    c.setFillColor(color)
    lines = []
    for paragraph in text.split("\n"):
        if not paragraph.strip():
            lines.append("")
            continue
        wrapped = textwrap.wrap(paragraph, width=int(max_width / (font_size * 0.48)))
        lines.extend(wrapped if wrapped else [""])
    
    current_y = y
    for line in lines:
        if align == "center":
            w = c.stringWidth(line, font_name, font_size)
            c.drawString(x - w/2, current_y, line)
        else:
            c.drawString(x, current_y, line)
        current_y -= leading
    return current_y

def create_book():
    os.makedirs(os.path.dirname(OUTPUT_PDF), exist_ok=True)
    c = canvas.Canvas(OUTPUT_PDF, pagesize=(PAGE_WIDTH, PAGE_HEIGHT))
    
    # Page 1: COVER
    print("Creating Page 1 - Cover...")
    img_path = os.path.join(IMAGES_DIR, "page_01_cover.jpg")
    draw_image_full_bleed(c, img_path, PAGE_WIDTH, PAGE_HEIGHT)
    draw_soft_vignette(c, PAGE_WIDTH, PAGE_HEIGHT, intensity=0.12)
    
    # Elegant dark gradient bar at top for title legibility
    c.setFillColor(Color(0.08, 0.15, 0.14, 0.55))
    c.rect(0, PAGE_HEIGHT - 145, PAGE_WIDTH, 145, fill=1, stroke=0)
    
    # Main title
    c.setFont("BrushScript", 54)
    c.setFillColor(HexColor("#F8F1E3"))
    title = PAGES[1]["title"]
    title_w = c.stringWidth(title, "BrushScript", 54)
    c.drawString((PAGE_WIDTH - title_w) / 2, PAGE_HEIGHT - 66, title)
    
    # Decorative line under title
    c.setStrokeColor(GOLD_ACCENT)
    c.setLineWidth(1.2)
    c.line(PAGE_WIDTH/2 - 145, PAGE_HEIGHT - 82, PAGE_WIDTH/2 + 145, PAGE_HEIGHT - 82)
    
    # Subtitle
    c.setFont("GeorgiaItalic", 14)
    c.setFillColor(HexColor("#F5E6D3"))
    sub_lines = PAGES[1]["subtitle"].split("\n")
    sub_y = PAGE_HEIGHT - 108
    for line in sub_lines:
        w = c.stringWidth(line, "GeorgiaItalic", 14)
        c.drawString((PAGE_WIDTH - w) / 2, sub_y, line)
        sub_y -= 18
    
    # Footer dedication
    c.setFont("Georgia", 9.5)
    c.setFillColor(Color(0.95, 0.9, 0.82, 0.85))
    foot_w = c.stringWidth(PAGES[1]["footer"], "Georgia", 9.5)
    c.drawString((PAGE_WIDTH - foot_w) / 2, 38, PAGES[1]["footer"])
    
    # Tiny elegant swans at bottom corners (simple shapes)
    c.setFillColor(Color(0.96, 0.95, 0.92, 0.35))
    c.circle(52, 52, 3.5, fill=1, stroke=0)
    c.circle(PAGE_WIDTH - 52, 52, 3.5, fill=1, stroke=0)
    
    c.showPage()
    
    # Pages 2-6: Story pages
    image_files = {
        2: "page_02_hatching.jpg",
        3: "page_03_teasing.jpg",
        4: "page_04_winter.jpg",
        5: "page_05_reflection.jpg",
        6: "page_06_ending.jpg",
    }
    
    for page_num in range(2, 7):
        print(f"Creating Page {page_num}...")
        page = PAGES[page_num]
        img_path = os.path.join(IMAGES_DIR, image_files[page_num])
        draw_image_full_bleed(c, img_path, PAGE_WIDTH, PAGE_HEIGHT)
        draw_soft_vignette(c, PAGE_WIDTH, PAGE_HEIGHT, intensity=0.09)
        
        # Subtle top bar for header consistency
        c.setFillColor(Color(0.06, 0.12, 0.11, 0.38))
        c.rect(0, PAGE_HEIGHT - 52, PAGE_WIDTH, 52, fill=1, stroke=0)
        
        # Small book title in header
        c.setFont("Georgia", 8)
        c.setFillColor(Color(0.92, 0.88, 0.8, 0.7))
        c.drawString(36, PAGE_HEIGHT - 32, "THE UGLY DUCKLING")
        
        # Elegant divider
        draw_header_ornament(c, PAGE_WIDTH/2 - 60, PAGE_HEIGHT - 35, 120)
        
        # Page header title
        c.setFont("GeorgiaBold", 11)
        c.setFillColor(HexColor("#F5E6D3"))
        header_w = c.stringWidth(page["header"], "GeorgiaBold", 11)
        c.drawString((PAGE_WIDTH - header_w) / 2, PAGE_HEIGHT - 32, page["header"])
        
        # === TEXT PANEL ===
        # Calculate panel position and size based on page for best composition
        if page_num == 2:  # Hatching - text at bottom
            panel_x, panel_y = 42, 36
            panel_w, panel_h = PAGE_WIDTH - 84, 168
        elif page_num == 3:  # Teasing - larger panel bottom
            panel_x, panel_y = 38, 32
            panel_w, panel_h = PAGE_WIDTH - 76, 195
        elif page_num == 4:  # Winter - left side panel (vast landscape)
            panel_x, panel_y = 32, 38
            panel_w, panel_h = 295, PAGE_HEIGHT - 95
        elif page_num == 5:  # Reflection - bottom elegant panel
            panel_x, panel_y = 42, 30
            panel_w, panel_h = PAGE_WIDTH - 84, 182
        else:  # Page 6 ending - beautiful bottom panel
            panel_x, panel_y = 40, 28
            panel_w, panel_h = PAGE_WIDTH - 80, 205
        
        # Draw the elegant cream panel
        draw_rounded_rect(c, panel_x, panel_y, panel_w, panel_h,
                          radius=14, fill_color=CREAM, stroke_color=WARM_TAUPE,
                          stroke_width=0.6, alpha=0.935)
        
        # Inner accent line at top of panel
        c.setStrokeColor(Color(0.78, 0.68, 0.52, 0.35))
        c.setLineWidth(0.5)
        c.line(panel_x + 18, panel_y + panel_h - 14, panel_x + panel_w - 18, panel_y + panel_h - 14)
        
        # Text content
        text_x = panel_x + 22
        text_y = panel_y + panel_h - 28
        max_text_width = panel_w - 44
        
        # Header inside panel for some pages
        if page_num in (4, 6):
            c.setFont("GeorgiaBold", 12.5)
            c.setFillColor(DEEP_TEAL)
            c.drawString(text_x, text_y, page["header"])
            text_y -= 20
            # Small gold underline
            c.setStrokeColor(GOLD_ACCENT)
            c.setLineWidth(0.8)
            c.line(text_x, text_y + 4, text_x + 118, text_y + 4)
            text_y -= 8
        
        # Body text - premium readable size for children and parents
        body_color = WARM_SLATE
        text_y = draw_text_wrapped(c, page["body"], text_x, text_y, max_text_width,
                                   "Georgia", 10.8, 14.6, body_color)
        
        # Special elements for ending page
        if page_num == 6:
            # Moral box
            text_y -= 8
            c.setStrokeColor(GOLD_ACCENT)
            c.setLineWidth(0.7)
            c.line(text_x, text_y + 3, text_x + 165, text_y + 3)
            text_y -= 14
            
            c.setFont("GeorgiaItalic", 9.5)
            c.setFillColor(CORAL_ACCENT)
            for line in page["moral"].split("\n"):
                c.drawString(text_x, text_y, line)
                text_y -= 13
            
            # Discussion prompt
            text_y -= 6
            c.setFont("Georgia", 8.5)
            c.setFillColor(Color(0.35, 0.42, 0.38))
            c.drawString(text_x, text_y, page["questions"])
        
        # Page number
        draw_feather_page_number(c, page_num)
        
        # Subtle corner decoration (tiny leaf)
        c.setFillColor(Color(0.35, 0.48, 0.38, 0.25))
        c.circle(PAGE_WIDTH - 28, 52, 2.2, fill=1, stroke=0)
        
        c.showPage()
    
    c.save()
    print("\n[OK] Premium PDF created successfully!")
    print(f"  Location: {OUTPUT_PDF}")
    print(f"  Pages: 6 (landscape 11\" x 8.5\")")
    return OUTPUT_PDF

if __name__ == "__main__":
    create_book()