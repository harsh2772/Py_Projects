import pikepdf

# 13) Swapping Pdf  # It can't properly swap pages

def swapPages(file_path,save_path):

    old_pdf = pikepdf.Pdf.open(file_path)
    old_pdf1 = pikepdf.Pdf.open(file_path)
    x = int(input("Enter the page number 1: "))-1
    y = int(input("Enter the page number 2: "))-1
    old_pdf.pages[y]=old_pdf.pages[x]
    old_pdf.pages[x]=old_pdf1.pages[x]

    old_pdf.save(save_path)


if __name__=="__main__":

    Path = input("Enter the path of your PDF file: ")  # Path Like:- C:\Users\harsh\Desktop\Python_Projects\Pdf Tools
    path = Path.replace("\\", "/")
    file_name = input("Enter a file name: ")  # File Name:- What's your PDF file Name
    file_path = f"{path}/{file_name}.pdf"

    save_path = f"{path}/Swapped.pdf"
    swapPages(file_path, save_path)