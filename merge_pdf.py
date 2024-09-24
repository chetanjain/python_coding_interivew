from pypdf import PdfWriter
import os

merger = PdfWriter()
path = "C://Users//ChJain//Downloads//Certificates//Extra Documents"
files = os.listdir("C://Users//ChJain//Downloads//Certificates//Extra Documents")
pdf_files = [file for file in files if file.endswith(".pdf")]

for pdf in pdf_files:
    final_path = path+'/'+pdf
    merger.append(final_path)

merger.write(f"{path}/mergerd-pdf.pdf")
merger.close()
