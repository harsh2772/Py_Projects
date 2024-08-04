import pikepdf
from glob import glob
import pdf2image
import pdf2docx
import docx2pdf


# Rotating Pdf

def Rotate(pdf_path,save_path):

    old_pdf=pikepdf.Pdf.open(pdf_path)                # Open The File

    rotate=int(input("How many Degree you want to rotate in multiple of 90: "))     # Give the rotation

    # print(old_pdf.pages)        # Print the no. of Pages

    for i in old_pdf.pages:       #  it iterates all the pages.
        i.Rotate=rotate           # It rotates all the pages
        old_pdf.save(save_path)      # It saves the pdf


# Pdf Merge
def Merge():
    new_pdf=pikepdf.new()       # Make a new pdf

    for i in glob("C:/Users/harsh/Desktop/Python_Projects/Source Files/*.pdf"):      # Here we use glob module in glob method which is take all the files which are end with .pdf on that path.
        old_pdf=pikepdf.open(i)                         # open all that pdf that are present on that directory.
        new_pdf.pages.extend(old_pdf.pages)             # Extend all the pdf files in new_pdf file

    new_pdf.save("C:/Users/harsh/Desktop/Python_Projects/Source Files/Merged.pdf")   # Here we saved merged pdf file.


# Encrypting Pdf

def Encrypted(pdf_path,save_path):

    old_pdf=pikepdf.Pdf.open("C:/Users/harsh/Desktop/Python_Projects/Source Files/Photoshop.pdf")        # Open The Pdf

    no_extr=pikepdf.Permissions(extract=False)                              # Permission goes to false means not open the pdf.

    password=input("Set a Password: ")       # Give the password

    old_pdf.save("C:/Users/harsh/Desktop/Python_Projects/Source Files/Encrypted.pdf",            # Save The Pdf
                                    encryption=pikepdf.Encryption(user=password,                       # user= password(What password you want)
                                                                  owner="Harsh",                       # who is the owner
                                                                  allow=no_extr))                      # Pemission allowed to open.


if __name__=="__main__":
    pdf_path="C:/Users/harsh/Desktop/Python_Projects/Source Files/Photoshop.pdf"
    save_path="C:/Users/harsh/Desktop/Python_Projects/Source Files/Rotated.pdf"
    Rotate(pdf_path,save_path)


    pdf_path="C:/Users/harsh/Desktop/Python_Projects/Source Files/Photoshop.pdf"
    save_path="C:/Users/harsh/Desktop/Python_Projects/Source Files/Encrypted.pdf"
    Encrypted(pdf_path,save_path)


# Spliting Pdf

def split_pdf(file_path,save_path):

    old_pdf = pikepdf.Pdf.open(file_path)  # Open a Pdf

    for n, page_content in enumerate(old_pdf.pages):  # Loop through all pages
        new_Pdf = pikepdf.Pdf.new()  # Make a new_pdf
        new_Pdf.pages.append(page_content)  # Add the page to the new_pdf
        new_Pdf.save(f"page{n+1}.pdf")  # Save the new_pdf page by page content.

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


file_path="C:/Users/harsh/Desktop/Python_Projects/Source Files/Photoshop.pdf"
save_path="C:/Users/harsh/Desktop/Python_Projects/Source Files/Split Pdfs/"
split_pdf(file_path,save_path)