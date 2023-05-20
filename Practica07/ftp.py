from ftplib import FTP
import os

def connect_ftp(hostname, username, password):
    ftp = FTP(hostname)
    ftp.login(username, password)
    return ftp

def create_txt_folder(ftp):
    folder_name = "TXT"
    ftp.mkd(folder_name)
    return folder_name

def search_text_files(ftp, current_directory, txt_folder):
    file_list = []
    ftp.cwd(current_directory)
    ftp.retrlines('NLST', file_list.append)

    for file in file_list:
        if file.endswith(('.txt', '.msg', 'README')):
            copy_file_to_folder(ftp, file, txt_folder)

def copy_file_to_folder(ftp, file_name, txt_folder):
    with open(file_name, 'wb') as file:
        ftp.retrbinary('RETR ' + file_name, file.write)
    ftp.storbinary('STOR ' + os.path.join(txt_folder, file_name), open(file_name, 'rb'))
    os.remove(file_name)

def process_ftp(hostname, username, password):
    ftp = connect_ftp(hostname, username, password)
    txt_folder = create_txt_folder(ftp)
    search_text_files(ftp, '/', txt_folder)
    ftp.quit()

# Configuración del servidor FTP
hostname = 'example.com'
username = 'your_username'
password = 'your_password'

# Procesar el servidor FTP
process_ftp(hostname, username, password)

