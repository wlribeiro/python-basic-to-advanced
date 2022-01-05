import PyPDF2
import os
from  localpath import localpath


caminho_dos_pdfs = localpath() + '\\pdf'

novo_pdf = PyPDF2.PdfFileMerger()

for root, dirs, files in os.walk(caminho_dos_pdfs):
    for file_ in files :
        caminho_completo = os.path.join(root, file_)

        arquivo_pdf = open(caminho_completo, 'rb')
        novo_pdf.append(arquivo_pdf)

with open(f'{localpath()}\\output\\out.pdf', 'wb') as meu_novo_pdf :
    novo_pdf.write(meu_novo_pdf)

arquivo_pdf.close()




with open(localpath() + '\\output\\out.pdf', 'rb') as arquivo_pdf:
    leitor = PyPDF2.PdfFileReader(arquivo_pdf)
    num_paginas = leitor.getNumPages()
    # print(num_paginas)

    for num_pagina in range(num_paginas):
        escritor = PyPDF2.PdfFileWriter()
        pagina_atual = leitor.getPage(num_pagina)
        escritor.addPage(pagina_atual)

        with open(f'{localpath()}\\output\\{num_pagina}.pdf', 'wb') as novo_pdf:
            escritor.write(novo_pdf)
