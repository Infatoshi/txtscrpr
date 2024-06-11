import os
import pdfplumber

def extract_text_from_pdf(pdf_path):
    """Extract text from a single PDF file."""
    text = ''
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text()
    except Exception as e:
        print(f"Failed to extract text from {pdf_path}: {e}")
    return text


def save_text_to_file(text, output_path):
    """Save extracted text to a text file."""
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(text)
    except Exception as e:
        print(f"Failed to write to {output_path}: {e}")


def process_directory(directory):
    """Process all PDF files in the directory recursively."""
    for root, dirs, files in os.walk(directory):
        print(f"Processing {root}")
        for file in files:
            if file.endswith(".pdf"):
                print(f"Processing {file}")
                pdf_path = os.path.join(root, file)
                text = extract_text_from_pdf(pdf_path)
                if text:
                    output_path = pdf_path.replace('.pdf', '.txt')
                    save_text_to_file(text, output_path)
                    print(f"Extracted and saved text from {pdf_path}")
            else:
                print(f"Skipping {file}")

if __name__ == "__main__":
    # base_directory = input("Enter the path to the directory: ")
    base_directory = "/Users/elliotarledge/Desktop/05-04-2024/a long long time ago in a galaxy far far away/txtbooks/topics"
    process_directory(base_directory)

