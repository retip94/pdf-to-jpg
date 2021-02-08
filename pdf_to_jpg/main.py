import glob
import ghostscript
import locale


def main():
    pdfs = get_all_pdfs()
    for pdf in pdfs:
        name = pdf.split('.p')[0]
        pdf_to_jpg(
            pdf,
            f'{name}.jpeg'
        )


def pdf_to_jpg(pdf_input_path, jpeg_output_path):
    args = ["pdf2jpeg",  # actual value doesn't matter
            "-dNOPAUSE",
            "-sDEVICE=jpeg",
            "-r300",
            "-sOutputFile=" + jpeg_output_path,
            pdf_input_path]
    encoding = locale.getpreferredencoding()
    args = [a.encode(encoding) for a in args]
    ghostscript.Ghostscript(*args)


def get_all_pdfs():
    pdf_files = glob.glob("*.pdf")
    return pdf_files


if __name__ == '__main__':
    main()
