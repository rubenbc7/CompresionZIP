import zipfile

files = ["words.txt", "words2.txt", "words3.txt", "vortice.mp4"]
archive = "archive.zip"
password = b"12345"

#Comprimir los archivos en formato zip
with zipfile.ZipFile(archive, "w") as zf:
    for file in files:
        zf.write(file)

    zf.setpassword(password)

#Leer archivo zip creado
with zipfile.ZipFile(archive, "r") as zf:
    crc_test = zf.testzip()
    if crc_test is not None:
        print("Algo sucedió o HEader incorrectos: {crc_test}")

    #Obtener la información en consola del zip creado
    info = zf.infolist()
    print(info)

    file = info[0]
    with zf.open(file) as f:
        print(f.read().decode())