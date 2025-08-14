def file_type(file_name):
    extensions = {
        'jpg': 'imagine',
        'jpeg': 'imagine',
        'png': 'imagine',
        'gif': 'imagine',
        'bmp': 'imagine',
        'txt': 'text',
        'pdf': 'text',
        'doc': 'text',
        'docx': 'text',
        'mp3': 'muzica'
    }
    if "." not in file_name:
        return "Fara extensie"
    ext = file_name.rsplit(".", 1)[-1].lower()
    return extensions.get(ext, "Fara extensie")


if __name__ == "__main__":
    print(file_type("imagine.png"))
    print(file_type("text.txt"))
    print(file_type("fisier"))
    print(file_type("music_20221107.mp3"))

