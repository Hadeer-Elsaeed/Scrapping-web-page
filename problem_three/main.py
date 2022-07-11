from generate_qr import GenerateQr

def main():
    make_qr = GenerateQr()
    make_qr.generate_code()
    make_qr.zip_output_pdfs()

if __name__ == "__main__":
    main()