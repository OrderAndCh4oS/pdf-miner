from pathlib import Path
import re
from pdfminer.high_level import extract_text
from pdfminer.layout import LAParams
import pickle

longChainOfNumbersRegex = r"\d{20}"

if __name__ == '__main__':
    path = Path("./documents/Heinz-computational_nature_phonological_generalizations-2016.pdf")
    text = extract_text(path, laparams=LAParams(char_margin=5))
    lines = text.split('\n')
    paragraphs = []
    i = 0
    skipped_lines = 0
    skipped_chars = 0
    selected_lines = 0
    selected_chars = 0
    while i < len(lines):
        paragraph = ''
        processed_lines = 0
        while True:
            current_line = lines[i]
            paragraph += f" {current_line.strip()}"
            if i == len(lines) - 1 or not len(lines[i + 1].strip()):
                break
            i += 1
            processed_lines += 1
        cleanParagraph = paragraph.strip()
        if len(cleanParagraph) >= 140 and not re.search(r'\d{20}', cleanParagraph):
            paragraphs.append(cleanParagraph)
            selected_lines += processed_lines
            selected_chars += len(cleanParagraph)
        else:
            skipped_lines += processed_lines
            skipped_chars += len(paragraph)
        i += 1

    result = {
        "total_lines": len(lines),
        "total_chars": len(text),
        "skipped_lines": skipped_lines,
        "skipped_chars": skipped_chars,
        "selected_lines": selected_lines,
        "selected_chars": selected_chars,
        "paragraphs": paragraphs
    }

    with open(f'results/{path.stem}.pickle', 'wb') as handle:
        pickle.dump(result, handle, protocol=pickle.HIGHEST_PROTOCOL)

    with open(f'results/{path.stem}.pickle', 'rb') as handle:
        stored_result = pickle.load(handle)

    print(stored_result)
