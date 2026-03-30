import sys
from pypdf import PdfReader

def dump_pdf_text(pdf_path: str):
    try:
        reader = PdfReader(pdf_path)
        output_file = "debug_pdf_output.txt"

        with open(output_file, "w", encoding="utf-8") as f:
            for i, page in enumerate(reader.pages):
                text = page.extract_text()
                header = f"\n{'='*20} PAGE {i + 1} {'='*20}\n"

                print(header + (text if text else "[No text found]"))

                f.write(header)
                f.write(text if text else "[No text found]\n")

        print(f"\n[+] Dump complete. Full text also saved to {output_file}")
    except Exception as e:
        print(f"Error reading PDF '{pdf_path}': {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python debug_pdf.py <path_to_failing_pdf>")
    else:
        dump_pdf_text(sys.argv[1])