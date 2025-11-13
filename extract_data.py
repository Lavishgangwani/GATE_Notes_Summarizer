import pdfplumber
import re
import json
from crewai.tools import tool


def clean_text(t):
    """Clean and normalize text"""
    t = t.replace("\n", " ")
    t = re.sub(r"\s+", " ", t)
    return t.strip()


def split_topics(text):
    """Split text into individual topics"""
    text = text.replace("[", "").replace("]", "")
    text = text.replace(";", ",")
    parts = [p.strip().rstrip(".") for p in text.split(",") if p.strip()]
    return parts


def extract_syllabus_pdf(pdf_path):
    """Extract syllabus sections and topics from PDF"""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            full_text = "\n".join(page.extract_text() or "" for page in pdf.pages)

        full_text = full_text.replace("\xa0", " ")
        heading_pattern = re.compile(r"([A-Z][A-Za-z /&()]+?):")

        sections = {}
        matches = list(heading_pattern.finditer(full_text))

        for i, match in enumerate(matches):
            heading = match.group(1).strip()
            start = match.end()
            end = matches[i + 1].start() if i + 1 < len(matches) else len(full_text)
            content = clean_text(full_text[start:end])
            topics = split_topics(content)
            sections[heading] = topics

        return sections
    except Exception as e:
        print(f"Error extracting PDF: {str(e)}")
        return {}