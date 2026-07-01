import os

folder_name = r"C:\Users\Administrator\Desktop\rag_pipline\data\txt_files"

chats = []
def chunker():
    
    for filename in os.listdir(folder_name):
        if filename.endswith(".txt"):
            
            full_path = os.path.join(folder_name, filename)
            
            with open(full_path, "r", encoding="utf-8") as file:
                context = file.read()
                chats.append(context)        

    
    return chats
    

"""

import os
import re
from app.config import chats_dir, chunk_max_chars, chunk_overlap_chars

# Filenames look like: chat_339_en.txt / chat_339_uz.txt / chat_339_ru.txt
FILENAME_RE = re.compile(r"chat_(\d+)_(\w+)\.txt$", re.IGNORECASE)

HEADER_PATTERNS = {
    "load_number": re.compile(r"^Load:\s*([^\|]+)", re.MULTILINE),
    "route": re.compile(r"Route:\s*(.+)$", re.MULTILINE),
    "driver": re.compile(r"^Driver:\s*([^\|]+)", re.MULTILINE),
    "operator": re.compile(r"^Operator:\s*(.+)$", re.MULTILINE),
    "date": re.compile(r"^Date:\s*(.+)$", re.MULTILINE),
    "company": re.compile(r"^Company:\s*(.+)$", re.MULTILINE),
}


def _parse_header(text: str) -> dict:
    meta = {}
    for key, pattern in HEADER_PATTERNS.items():
        match = pattern.search(text)
        meta[key] = match.group(1).strip() if match else None
    return meta


def _split_text(text: str, max_chars: int, overlap: int) -> list[str]:

    if len(text) <= max_chars:
        return [text]

    lines = text.split("\n")
    chunks: list[str] = []
    current: list[str] = []
    current_len = 0

    for line in lines:
        line_len = len(line) + 1
        if current_len + line_len > max_chars and current:
            chunk_text = "\n".join(current)
            chunks.append(chunk_text)

            # start next chunk with overlap (trailing lines of the previous chunk)
            overlap_lines: list[str] = []
            overlap_len = 0
            for prev_line in reversed(current):
                overlap_len += len(prev_line) + 1
                overlap_lines.insert(0, prev_line)
                if overlap_len >= overlap:
                    break
            current = overlap_lines
            current_len = sum(len(l) + 1 for l in current)

        current.append(line)
        current_len += line_len

    if current:
        chunks.append("\n".join(current))

    return chunks


def chunker(
    folder_name: str = None,
    max_chars: int = None,
    overlap: int = None,
) -> list[dict]:

    folder_name = folder_name or chats_dir
    max_chars = max_chars or chunk_max_chars
    overlap = overlap or chunk_overlap_chars

    if not os.path.isdir(folder_name):
        raise FileNotFoundError(f"Chat data folder not found: {folder_name}")

    all_chunks: list[dict] = []

    for filename in sorted(os.listdir(folder_name)):
        if not filename.endswith(".txt"):
            continue

        full_path = os.path.join(folder_name, filename)
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()

        fname_match = FILENAME_RE.search(filename)
        chat_id = fname_match.group(1) if fname_match else filename
        language = fname_match.group(2) if fname_match else "unknown"

        header = _parse_header(content)

        pieces = _split_text(content, max_chars=max_chars, overlap=overlap)

        for idx, piece in enumerate(pieces):
            all_chunks.append(
                {
                    "chat_id": chat_id,
                    "source_file": filename,
                    "language": language,
                    "load_number": header.get("load_number"),
                    "driver": header.get("driver"),
                    "operator": header.get("operator"),
                    "route": header.get("route"),
                    "chunk_index": idx,
                    "text": piece,
                }
            )

    return all_chunks

"""