import os
import re
import sys

TERM_REGEX = re.compile(
    r"^(?P<type>xterm)(([-](?P<color_variant>256color|truecolor))?)$", re.I
)
COLORTERM_REGEX = re.compile(r"^(?P<type>truecolor)$", re.I)


up = "\x1b[Am"
reset = "\x1b[0m"
rewind = "\r"

bg_truecolor = "\x1b[1;48;2;195;36;84m"
fg_truecolor = "\x1b[1;38;2;255;255;255m"

bg_256color = "\x1b[1;48;5;197m"
fg_256color = "\x1b[1;38;5;255m"

bg_base_color = "\x1b[1;31m"
fg_base_color = "\x1b[1;37m"

reset_up_and_rewind = f"{reset}{up}{rewind}"


def show_info_truecolor(message):
    sys.stderr.write(f"{bg_truecolor}{fg_truecolor}{message}{reset}")


def show_info_256_color(message):
    sys.stderr.write(f"{bg_256color}{fg_256color}{message}{reset}")


def show_info_base_color(message):
    sys.stderr.write(f"{bg_base_color}{fg_base_color}{message}{reset}")


def show_info(*args, **kw):
    term_var = (os.getenv("TERM") or "").lower()
    colorterm_var = (os.getenv("COLORTERM") or "").lower()
    term = TERM_REGEX.search(term_var)
    colorterm = COLORTERM_REGEX.search(colorterm_var)

    sys.stderr.write(f"{reset_up_and_rewind}")
    sys.stderr.flush()

    if "truecolor" in colorterm_var:
        show_info_truecolor(*args, **kw)
    elif "256color" in term_var:
        show_info_256_color(*args, **kw)
    else:
        show_info_basecolors(*args, **kw)
