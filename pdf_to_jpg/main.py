import glob
import ghostscript
import locale


def main():
    pdfs = get_all_pdfs()
    for pdf in pdfs:
        name = pdf.split('.pdf')[0]
        pdf_to_jpg(
            pdf,
            name
        )


def pdf_to_jpg(pdf_input_path, jpeg_name):
    args = ["pdf2jpeg",  # actual value doesn't matter
            "-dNOPAUSE",
            "-sDEVICE=jpeg",
            "-r300",
            f'-sOutputFile={jpeg_name}-%03d.jpg',
            pdf_input_path]
    encoding = locale.getpreferredencoding()
    args = [a.encode(encoding) for a in args]
    with ghostscript.Ghostscript(*args) as g:
        ghostscript.cleanup()



def get_all_pdfs():
    pdf_files = glob.glob("*.pdf")
    return pdf_files


if __name__ == '__main__':
    main()
