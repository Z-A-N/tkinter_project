import mysql.connector

connect = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="PennyPlan"
)

# Memastikan koneksi berhasil
if connect.is_connected():
    print("Koneksi ke database berhasil!")
    db_info = connect.get_server_info()
    print(f"Server MySQL versi: {db_info}")

# Menutup koneksi
connect.close()