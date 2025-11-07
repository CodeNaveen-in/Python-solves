import pyttsx3
import PyPDF2

def pdf_to_speech(pdf_path):
    # Initialize text-to-speech engine
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech

    # Open and read PDF
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        print(f"🔍 Reading {num_pages} pages from {pdf_path}...")

        for page_num in range(num_pages):
            text = reader.pages[page_num].extract_text()
            if text:
                print(f"📄 Speaking page {page_num + 1}...")
                engine.say(text)
                engine.runAndWait()

    print("✅ Done converting PDF to speech.")

# Example usage
if __name__ == "__main__":
    pdf_path = "sample.pdf"  # Replace with your PDF file path
    pdf_to_speech(pdf_path)