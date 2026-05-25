import PyPDF2
import os

pdf_files = [
    "DSC602 2025-2026 - 01 Introduction.pdf",
    "DSC602 2025-2026 - 02 Data Abstraction and Representation.pdf",
    "DSC602_LECT03_04 (1).pdf"
]

for pdf_file in pdf_files:
    if os.path.exists(pdf_file):
        print(f"\n{'='*80}")
        print(f"FILE: {pdf_file}")
        print('='*80)
        
        with open(pdf_file, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            print(f"Total Pages: {len(reader.pages)}\n")
            
            for i, page in enumerate(reader.pages):
                text = page.extract_text()
                print(f"--- PAGE {i+1} ---")
                print(text)
                print()
    else:
        print(f"File not found: {pdf_file}")
