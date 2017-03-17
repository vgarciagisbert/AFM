#get all the pictures inside the folder you drop the Pictures_to_pdf.py file and create a pdf with all of them
#You must have latex installed in order to work

#Python 3.7
#Latex required
#Windows version

import glob, os

for filename in os.listdir("."):
    new_filename=filename.replace(' ','_')
    os.rename(filename, new_filename)
image_files=[]
for file in glob.glob("*.jpg"):
    print(file)
    image_files.append(file)
for file in glob.glob("*.bmp"):
    print(file)
    image_files.append(file)
for file in glob.glob("*.jpeg"):
    print(file)
    image_files.append(file)
for file in glob.glob("*.png"):
    print(file)
    image_files.append(file)
             

print(image_files)

print(sorted(image_files))

print('------------------------------------------------')
print('---------------Converting images----------------')
print('------------------------------------------------')

text_file = open("Output.tex", "w")

text_file.write(r"""\documentclass[a4paper,12pt]{article}
\usepackage{incgraph,tikz}

\begin{document}
""")
option=2
for name in image_files:
    if(option==1):
        text_file.write(r"""\incgraph[documentpaper]
          [width=\paperwidth,height=\paperheight]{"""+name+"""}
        """)
    else:    
        text_file.write(r"""\incgraph[
      ]{"""+name+"""}""")

    text_file.write(r"""


    """)



text_file.write(r"""\end{document}""")

text_file.close()

os.system("pdflatex Output.tex")

os.remove('Output.tex')
os.remove('Output.aux')
os.remove('Output.log')

os.system('start "" /max "Output.pdf"')


