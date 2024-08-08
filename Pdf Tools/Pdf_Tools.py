import PyPDF2
import pikepdf
from glob import glob
import pdf2image
import pdf2docx
import docx2pdf
from PyPDF2 import PdfReader, PdfWriter
import random
import string


# Required  :- Poppler Path / bin :- in 121 line - 8) Case Function
#              On That Same Path You Having "Split Pdfs" Named Folder
#              On That Same Path "Extract Images" Named Folder

# 1) Spliting Pdf

def split_pdf(file_path,save_path):

    old_pdf = pikepdf.Pdf.open(file_path)  # Open a Pdf

    s_path=save_path
    for n, page_content in enumerate(old_pdf.pages):  # Loop through all pages
        new_Pdf = pikepdf.Pdf.new()  # Make a new_pdf
        new_Pdf.pages.append(page_content)  # Add the page to the new_pdf
        new_Pdf.save(f"{s_path}/page{n+1}.pdf")  # Save the new_pdf page by page content.

    print("\nYour PDF has been split successfully")


# 2) Rotating Pdf

def Rotate(pdf_path,save_path):

    old_pdf=pikepdf.Pdf.open(pdf_path)                # Open The File

    rotate=int(input("How many Degree you want to rotate in multiple of 90: "))     # Give the rotation

    # print(old_pdf.pages)        # Print the no. of Pages

    for i in old_pdf.pages:       #  it iterates all the pages.
        i.Rotate=rotate           # It rotates all the pages
        old_pdf.save(save_path)      # It saves the pdf

    print("\nYour PDF has been rotated successfully")


# 3) Merge Pdf
def Merge(file_path,save_path):
    new_pdf=pikepdf.new()       # Make a new pdf

    for i in glob(file_path):                           # Here we use glob module in glob method which is take all the files which are end with .pdf on that path.
        old_pdf=pikepdf.open(i)                         # open all that pdf that are present on that directory.
        new_pdf.pages.extend(old_pdf.pages)             # Extend all the pdf files in new_pdf file

    new_pdf.save(save_path)   # Here we saved merged pdf file.

    print("\nYour PDF has been merged successfully")

# 4) Encrypting Pdf

# It Generates For Random Password. It Made only for 4) Part of this Pdf

def Password():

  list=[i for i in string.ascii_letters]
  list.extend(i for i in string.digits)
  list.extend(i for i in string.punctuation)

  length=int(input("Enter the length of password: "))

  l1=[]

  for i in range(length):
    Pass=random.choice(list)
    l1.append(Pass)

  random.shuffle(l1)

  password="".join(l1)

  return password

def Encrypted(pdf_path,save_path):

    old_pdf=pikepdf.Pdf.open(pdf_path)        # Open The Pdf

    no_extr=pikepdf.Permissions(extract=False)                              # Permission goes to false means not open the pdf.

    print("1) For Create Password\n2) For Random/Strong Password")
    x=int(input("Enter your Choice: "))
    if(x==1):
        password=input("Set a Password: ")               # Give the password
    elif(x==2):
        password=Password()
        print("Your Random Password has been generated successfully")
        print("Your Pdf Password is:",password)

    old_pdf.save(save_path,            # Save The Pdf
                encryption=pikepdf.Encryption(user=password,                       # user= password(What password you want)
                                              owner="Harsh",                       # who is the owner
                                              allow=no_extr))                      # Pemission allowed to open.

    print("\nYour PDF has been encrypted successfully")

# 5) OverlappingPdf

def Overlap(file_path1,file_path2,file1_page_no,file2_page_no,save_path):
    old_pdf1 = pikepdf.Pdf.open(file_path1)  # Open a Pdf 1
    old_pdf2 = pikepdf.Pdf.open(file_path2)  # Open a Pdf 2

    des_page = pikepdf.Page(old_pdf1.pages[file1_page_no])  # Get the first page of the old_pdf1
    sur_page = pikepdf.Page(old_pdf2.pages[file2_page_no])  # Get the fourth page of the old_pdf2

    des_page.add_overlay(sur_page, pikepdf.Rectangle(0, 0, 500, 500))  # Add the Overpap of sur_page to the des_page.

    old_pdf1.save(save_path)  # Save The Overlapped Pdf.

    print("\nYour PDF has been overlaid successfully")

# 6) Converting pdf to docx
def pdf2doc(file_path,save_path):

    old_pdf = file_path
    new_doc = save_path

    obj = pdf2docx.Converter(old_pdf)
    obj.convert(new_doc)
    obj.close

    print("\nYour PDF File has been converted successfully in Docx File")

# 7) Doc To Pdf Convert
def doc2pdf(file_path,save_path):

    doc_path=file_path
    pdf_path=save_path
    docx2pdf.convert(doc_path, pdf_path)

    print("\nYour Docx File has been converted successfully in PDF File")

# 8) Extract Pdf to Images

def pdf2img(file_path,save_path):

    # Download Poppler From link:- https://github.com/oschwartz10612/poppler-windows/releases/
    Poppler_path = "C:/Users\harsh\Desktop\Python_Projects\Pdf Tools\poppler-24.07.0\Library/bin"   # Enter a path of a poppler-bin
    poppler_path = Poppler_path.replace("\\", "/")

    old_pdf = pdf2image.convert_from_path(f"{file_path}", poppler_path=poppler_path)

    s_path=save_path
    for i in range(len(old_pdf)):
      # print(i)
      old_pdf[i].save(f"{s_path}/page{i+1}.jpg", "JPEG")

    print("\nYour PDF File has been converted successfully in Image File")


# 9) Compressing Pdf
def pdfCompressor(path):

    file_name = input("Enter a file name: ")  # File Name:- What's your PDF file Name
    file_path = f"{path}/{file_name}.pdf"

    reader = PdfReader(file_path)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.add_metadata(reader.metadata)

    with open(f"{path}/Compressed.pdf", "wb") as fp:
        writer.write(fp)

    print("\nYour PDF File has been compressed successfully")


# 10) Extracting Images In Pdf

def ExtractImages(file_path,save_path):

    old_pdf=pikepdf.Pdf.open(file_path)

    a=(len(old_pdf.pages))

    k=1

    for i in range(a):
        page=old_pdf.pages[i]
        l1=list(page.images.keys())
        # print(l1)
        for k,j in enumerate(l1):
            raw_image=page.images[j]
            pdf_image=pikepdf.PdfImage(raw_image)
            pdf_image.extract_to(fileprefix=f"{save_path}/Extract Images/image{i+1}{k+1}.png")

    print("\nAll Images have been extracted successfully")

# 11) Scaling Pdf

def scalePdf(path,save_path):

    file_name = input("Enter a file name: ")  # File Name:- What's your PDF file Name
    file_path = f"{path}/{file_name}.pdf"

    reader = PdfReader(file_path)
    writer = PdfWriter()

    # ****Scale****
    scale = int(input("Enter a scale value: "))

    for page in reader.pages:
        page.scale_by(scale)
        writer.add_page(page)

    with open(save_path, 'wb') as fp:
        writer.write(fp)

    print("\nYour PDF File has been scaled successfully")



# 12) Reverse Pdf
def reverse(file_path,save_path):

    old_pdf=pikepdf.Pdf.open(file_path)

    old_pdf.pages.reverse()
    old_pdf.save(save_path)

    print("\nYour PDF File has been reversed successfully")


# 13) Swapping Pdf  # It can't properly swap pages

def swapPages(file_path,save_path):

    old_pdf = pikepdf.Pdf.open(file_path)
    old_pdf1 = pikepdf.Pdf.open(file_path)
    x = int(input("Enter the page number 1: "))-1
    y = int(input("Enter the page number 2: "))-1
    old_pdf.pages[y]=old_pdf.pages[x]
    old_pdf.pages[x]=old_pdf1.pages[x]

    old_pdf.save(save_path)

# 14) Delete Pages
def delete_pages(file_path,save_path):

    old_pdf = pikepdf.Pdf.open(file_path)

    x=int(input("Enter the Delete Page No.: "))-1

    del old_pdf.pages[x]
    old_pdf.save(save_path)


# 15) Crop Pdf

def crop_pdf(file_path,save_path):

    reader = PdfReader(file_path)
    writer = PdfWriter()

    x = int(input("Enter The Upper_Left x-aixs: "))
    y = int(input("Enter The Upper_Left y-aixs: "))
    xx = int(input("Enter The Upper_Right x-aixs: "))
    yy = int(input("Enter The Upper_Right y-aixs: "))
    for page in reader.pages:
        page.cropbox.upper_left = (x, y)
        page.cropbox.lower_right = (xx, yy)
        writer.add_page(page)

    with open(save_path, 'wb') as fp:
        writer.write(fp)



if __name__=="__main__":

    while True:
        print("""*****Welcome to Harsh Pdf Tools App*****
    What You Want To Do With Use This App
    choice:-1) Split PDF
            2) Rotate PDF
            3) Merge PDF
            4) Encrypted Pdf
            5) Overlapping Pdf
            6) Pdf to Docx
            7) Docx to PDF
            8) Pdf to Image
            9) Compress Pdf
           10) Extracting Images From Pdf 
           11) Scaling Pdf
           12) Reverse Pdf
           13) Swap Pages **
           14) Delete Pages
           15) Crop Pdf
           !!!!!Enter Any Other No. For Quit!!!!!""")

        x=int(input("Enter your choice: "))
        match x:
            case 1:
                Path=input("Enter the path of your PDF file: ")         # Path Like:- C:\Users\harsh\Desktop\Python_Projects\Pdf Tools
                path=Path.replace("\\","/")
                file_name=input("Enter a file name: ")                  # File Name:- What's your PDF file Name
                file_path=f"{path}/{file_name}.pdf"

                save_path=f"{path}/Split Pdfs"                          # Make Sure You Create a "Split Pdfs" named folder in your path.
                split_pdf(file_path,save_path)

            case 2:
                Path = input("Enter the path of your PDF file: ")       # Path Like:- C:\Users\harsh\Desktop\Python_Projects\Pdf Tools
                path = Path.replace("\\", "/")
                file_name = input("Enter a file name: ")                # File Name:- What's your PDF file Name
                file_path = f"{path}/{file_name}.pdf"

                save_path = f"{path}/Rotated.pdf"
                Rotate(file_path,save_path)

            case 3:
                Path = input("Enter the path of your PDF file: ")       # Path Like:- C:\Users\harsh\Desktop\Python_Projects\Pdf Tools
                path = Path.replace("\\", "/")
                file_path = f"{path}/*.pdf"

                save_path = f"{path}/Merged.pdf"
                Merge(file_path,save_path)

            case 4:
                Path = input("Enter the path of your PDF file: ")       # Path Like:- C:\Users\harsh\Desktop\Python_Projects\Pdf Tools
                path = Path.replace("\\", "/")
                file_name = input("Enter a file name: ")                # File Name:- What's your PDF file Name
                file_path = f"{path}/{file_name}.pdf"
                save_path = f"{path}/Encrypted.pdf"
                Encrypted(file_path,save_path)

            case 5:
                Path = input("Enter the path of your PDF file: ")       # Path Like:- C:\Users\harsh\Desktop\Python_Projects\Pdf Tools
                path = Path.replace("\\", "/")
                file_name = input("Enter a file name: ")                # File Name:- What's your PDF file Name
                file_path1 = f"{path}/{file_name}.pdf"

                file_name2 = input("Enter a file name: ")               # File Name:- What's your PDF file Name
                file_path2 = f"{path}/{file_name2}.pdf"

                file1_page_no=int(input("Enter the page no of your PDF file: "))-1              # Enter a Page no. On That page you want overlapping a data.
                file2_page_no=int(input("Enter the page no of your PDF file: "))-1              # Here you Enter That Page No. Which Data You Want to overlap on the above file.

                save_path=f"{path}/Overlaped.pdf"
                Overlap(file_path1,file_path2,file1_page_no,file2_page_no,save_path)

            case 6:
                Path = input("Enter the path of your PDF file: ")               # Path Like:- C:\Users\harsh\Desktop\Python_Projects\Pdf Tools
                path = Path.replace("\\", "/")
                file_name = input("Enter a file name: ")                        # File Name:- What's your PDF file Name
                file_path = f"{path}/{file_name}.pdf"

                save_path = f"{path}/pdf2doc.docx"
                pdf2doc(file_path,save_path)

            case 7:
                Path = input("Enter the path of your Docx file: ")      # Path Like:- C:\Users\harsh\Desktop\Python_Projects\Pdf Tools
                path = Path.replace("\\", "/")
                file_name = input("Enter a file name: ")                # File Name:- What's your Docx file Name
                file_path = f"{path}/{file_name}.docx"

                save_path = f"{path}/doc2pdf.pdf"
                doc2pdf(file_path,save_path)

            case 8:
                Path = input("Enter the path of your Pdf file: ")       # Path Like:- C:\Users\harsh\Desktop\Python_Projects\Pdf Tools
                path = Path.replace("\\", "/")
                file_name = input("Enter a file name: ")                # File Name:- What's your PDF file Name
                file_path = f"{path}/{file_name}.pdf"

                save_path = f"{path}/Extract Images"                    # Mae Sure You Have a "Extract Images" Folder named in your path.
                pdf2img(file_path,save_path)

            case 9:
                Path = input("Enter the path of your Pdf file: ")  # Path Like:- C:\Users\harsh\Desktop\Python_Projects\Pdf Tools
                path = Path.replace("\\", "/")

                pdfCompressor(path)


            case 10:
                Path = input("Enter the path of your Pdf file: ")  # Path Like:- C:\Users\harsh\Desktop\Python_Projects\Pdf Tools
                path = Path.replace("\\", "/")
                file_name = input("Enter a file name: ")  # File Name:- What's your PDF file Name
                file_path = f"{path}/{file_name}.pdf"

                ExtractImages(file_path,path)


            case 11:
                Path = input("Enter the path of your Pdf file: ")  # Path Like:- C:\Users\harsh\Desktop\Python_Projects\Pdf Tools
                path = Path.replace("\\", "/")

                save_path = f"{path}/Scaled.pdf"
                scalePdf(path,save_path)

            case 12:
                Path = input("Enter the path of your PDF file: ")  # Path Like:- C:\Users\harsh\Desktop\Python_Projects\Pdf Tools
                path = Path.replace("\\", "/")
                file_name = input("Enter a file name: ")            # File Name:- What's your PDF file Name
                file_path = f"{path}/{file_name}.pdf"

                save_path = f"{path}/Reversed.pdf"
                reverse(file_path, save_path)

            case 13:
                Path = input("Enter the path of your PDF file: ")  # Path Like:- C:\Users\harsh\Desktop\Python_Projects\Pdf Tools
                path = Path.replace("\\", "/")
                file_name = input("Enter a file name: ")            # File Name:- What's your PDF file Name
                file_path = f"{path}/{file_name}.pdf"

                save_path = f"{path}/Swapped.pdf"
                swapPages(file_path, save_path)

            case 14:
                Path = input("Enter the path of your PDF file: ")  # Path Like:- C:\Users\harsh\Desktop\Python_Projects\Pdf Tools
                path = Path.replace("\\", "/")
                file_name = input("Enter a file name: ")            # File Name:- What's your PDF file Name
                file_path = f"{path}/{file_name}.pdf"

                save_path = f"{path}/Updated.pdf"
                delete_pages(file_path, save_path)

            case 15:
                Path = input("Enter the path of your PDF file: ")   # Path Like:- C:\Users\harsh\Desktop\Python_Projects\Pdf Tools
                path = Path.replace("\\", "/")
                file_name = input("Enter a file name: ")            # File Name:- What's your PDF file Name
                file_path = f"{path}/{file_name}.pdf"

                save_path = f"{path}/Cropped.pdf"
                crop_pdf(file_path, save_path)

            case _:
                print("!!!!!!!!!!!EXIT!!!!!!!!!!")
                break