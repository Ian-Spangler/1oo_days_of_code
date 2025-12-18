# Couldn't install gcloud, so used gTTS module instead 
from PyPDF2 import PdfReader
from gtts import gTTS
import os

PDF_FILE = "input.pdf"
OUTPUT_AUDIO = "audiobook.mp3"

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text


def text_to_speech(text, output_file):
    tts = gTTS(text=text, lang="en")
    tts.save(output_file)


def main():
    if not os.path.exists(PDF_FILE):
        print("❌ PDF file not found.")
        return

    print("📄 Extracting text from PDF...")
    text = extract_text_from_pdf(PDF_FILE)

    if not text.strip():
        print("❌ No text found in PDF.")
        return

    print("🔊 Converting text to speech...")
    text_to_speech(text, OUTPUT_AUDIO)

    print(f"✅ Audiobook created: {OUTPUT_AUDIO}")


if __name__ == "__main__":
    main()
