import PyPDF2
import os

pdf_files = [
    "DSC602 2025-2026 - 01 Introduction.pdf",
    "DSC602 2025-2026 - 02 Data Abstraction and Representation.pdf",
    "DSC602_LECT03_04 (1).pdf"
]

output_file = "pdf_extraction_full.txt"

with open(output_file, 'w', encoding='utf-8') as out:
    for pdf_file in pdf_files:
        if os.path.exists(pdf_file):
            out.write(f"\n{'='*80}\n")
            out.write(f"FILE: {pdf_file}\n")
            out.write('='*80 + "\n\n")
            
            with open(pdf_file, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                out.write(f"Total Pages: {len(reader.pages)}\n\n")
                
                for i, page in enumerate(reader.pages):
                    text = page.extract_text()
                    out.write(f"--- PAGE {i+1} ---\n")
                    out.write(text)
                    out.write("\n\n")
        else:
            out.write(f"File not found: {pdf_file}\n")

print(f"Extraction complete. Output written to {output_file}")
