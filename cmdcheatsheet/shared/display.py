from rich import print


BLUE = "turquoise2"
RED = "deep_pink2"
GREEN = "spring_green1"
YELLOW = "yellow"

def display_info(message):
    print(f"[{BLUE}]{message}")

def display_error(message):
    print(f"[{RED}]{message}")

def highlight_find_results(src, text_to_highlight, reset_color=BLUE):
    return f"{src}".replace(text_to_highlight,
        f"[{RED}]{text_to_highlight}[{reset_color}]")

