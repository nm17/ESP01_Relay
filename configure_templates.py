# noinspection PyUnresolvedReferences

from pathlib import Path
import glob

header_path = Path("include/templates.h")
templates = [Path(a) for a in glob.glob("templates/*.html")]

header_fd = header_path.open("w+")

header_fd.write("/// !!! WARNING !!! AUTO-GENERATED FILE, PLEASE DO NOT MODIFY IT AND USE\n\n\n")


for page_num, page in enumerate(templates):
    page_name = page.stem
    header_fd.write(f"const char template_{page_name}[]= (\n")
    page_txt = page.read_text()
    lines = page_txt.splitlines()
    lines_num = len(lines)
    for i, line in enumerate(lines):
        line = line.replace('"', r'\"')
        header_fd.write(rf'"{line}\n"' + (');' if lines_num - i - 1 == 0 else '') + '\n')
    header_fd.write(f"\nconst int template_{page_name}_length = {len(page_txt) + 1};\n\n\n")