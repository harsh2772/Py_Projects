import pikepdf
import pdf2image
import pdf2docx
import docx2pdf

# # Spliting Pdf

old_pdf = pikepdf.Pdf.open("C:/Users/harsh/Desktop/Python_Projects/Source Files/Photoshop.pdf")  # Open a Pdf

for n, page_content in enumerate(old_pdf.pages):  # Loop through all pages
    new_Pdf = pikepdf.Pdf.new()  # Make a new_pdf
    new_Pdf.pages.append(page_content)  # Add the page to the new_pdf
    new_Pdf.save(f"C:/Users/harsh/Desktop/Python_Projects/Source Files/Split Pdfs/page{n+1}.pdf")  # Save the new_pdf page by page content.

# OverlappingPdf

old_pdf1 = pikepdf.Pdf.open("C:/Users/harsh/Desktop/Python_Projects/Source Files/Photoshop.pdf")  # Open a Pdf 1
old_pdf2 = pikepdf.Pdf.open("C:/Users/harsh/Desktop/Python_Projects/Source Files/Photoshop.pdf")  # Open a Pdf 2

des_page = pikepdf.Page(old_pdf1.pages[0])  # Get the first page of the old_pdf1
sur_page = pikepdf.Page(old_pdf2.pages[3])  # Get the fourth page of the old_pdf2

des_page.add_overlay(sur_page, pikepdf.Rectangle(0, 0, 500, 500))  # Add the Overpap of sur_page to the des_page.

old_pdf1.save("C:/Users/harsh/Desktop/Python_Projects/Source Files/Overlaped.pdf")  # Save The Overlapped Pdf.

# Extract Pdf to Images -- It Shows Error

# old_pdf = pdf2image.convert_from_path(
#     "Photoshop.pdf", poppler_path=r"poppler-22.04.0/Library/bin")

# for i in range(len(old_pdf)):
#   print(i)
#   old_pdf[i].save(f"Extract Pdf to Images/page{i+1}.jpg", "JPEG")

# Converting pdf to docx

old_pdf = "C:/Users/harsh/Desktop/Python_Projects/Source Files/He.pdf"
new_doc = "C:/Users/harsh/Desktop/Python_Projects/Source Files/new.docx"

obj = pdf2docx.Converter(old_pdf)
obj.convert(new_doc)
obj.close

# Another Approch for convert pdf to docx
# pdf2docx.parse(old4_pdf, new1_doc)


# Converting docx to pdf

doc_path="C:/Users/harsh/Desktop/Python_Projects/Source Files/new.docx"
pdf_path="C:/Users/harsh/Desktop/Python_Projects/Source Files/Hell.pdf"
docx2pdf.convert(doc_path, pdf_path)
