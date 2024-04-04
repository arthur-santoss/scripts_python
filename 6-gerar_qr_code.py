import qrcode

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=1,  # Tamanho do quadrado
        border=1,
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_code = qr.make_image(fill_color="black", back_color="white")
    qr_text = qr_code.get_image().convert('1')

    qr_ascii = ''
    for y in range(qr_text.size[1]):
        for x in range(qr_text.size[0]):
            if qr_text.getpixel((x, y)):
                qr_ascii += '  '  # Quadrado branco
            else:
                qr_ascii += '██'  # Quadrado preto
        qr_ascii += '\n'

    return qr_ascii

if __name__ == "__main__":
    data = input("Digite os dados que deseja codificar no QR Code: ")

    qr_ascii = generate_qr_code(data)
    print("\nQR Code gerado:")
    print(qr_ascii)
