# MQTT Publisher
# Code writter by MPAB
# Look at me : 
# LinkedIn : mpujaalifbudiman1998

from datetime import datetime
from paho.mqtt import client as mqtt_client
from sense_emu import SenseHat

import csv
import numpy as np
import random
import time

sense = SenseHat()

# broker = "broker.emqx.io"
# port = 1883
# client_id = "puja_publisher"
# keepalive = 3600

broker = ""
port = ""
client_id = ""
keepalive = ""

now = datetime.now()
dt_string = now.strftime("%d-%m-%Y %H:%M:%S")

logger = []
file_logger = " publisher.csv"
file_name = str(dt_string) + str(file_logger)
    
def run():
    print("Nama : M. Puja Alif Budiman")
    print("NIM : 2256102021")
    print("Kelas : 22-MTTK-B")
    print("Mata Kuliah : MT501 - Advanced Programming")
    print("")
    
    print("Data broker MQTT")
    broker = input("Broker : ")
    port = int(input("Port : "))
    client_id = input("Client ID : ")
    keepalive = int(input("Keepalive : "))
    
    client = connect_mqtt(broker, port, client_id, keepalive)
    
    menu(client)

def connect_mqtt(broker, port, client_id, keepalive):
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("")
            print("Berhasil terhubung MQTT Broker!")
        else:
            print("")
            print("Koneksi gagal, code error %d\n", rc)
            
    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port, keepalive)
    
    return client
    
def publish(client, topik, pesan):
    kirim = client.publish(topik, pesan)
    status = kirim[0]
    
    if status == 0:
        aksi = "mengirim"
        
        logger.append([dt_string, broker, port, client_id, aksi, topik, pesan])
        
        print("")
        print("Mengirimkan", pesan, "ke topik", topik)
        print("Harap tunggu, anda akan kembali ke menu dalam 3 detik!")
        
        time.sleep(3)
        menu(client)
    else:
        aksi = "gagal mengirim"
        
        logger.append([dt_string, broker, port, client_id, aksi, topik, pesan])
        
        print("")
        print("Gagal mengirimkan", pesan, "ke topik", topik)
        print("Harap tunggu, anda akan kembali ke menu dalam 3 detik!")
        
        time.sleep(3)
        menu(client)

def publish1(client, topik, pesan):
    kirim = client.publish(topik, pesan)
    status = kirim[0]
    
    if status == 0:
        aksi = "mengirim"
        
        logger.append([dt_string, broker, port, client_id, aksi, topik, pesan])
        
        print("")
        print("Mengirimkan", pesan, "ke topik", topik)
        print("Harap tunggu, anda akan kembali ke menu dalam 3 detik!")
        
        time.sleep(3)
        return
    else:
        aksi = "gagal mengirim"
        
        logger.append([dt_string, broker, port, client_id, aksi, topik, pesan])
        
        print("")
        print("Gagal mengirimkan", pesan, "ke topik", topik)
        print("Harap tunggu, anda akan kembali ke menu dalam 3 detik!")
        
        time.sleep(3)
        menu(client)

def publish2(client, topik, pesan, pilihan_menu):
    kirim = client.publish(topik, pesan)
    status = kirim[0]
    
    if status == 0:
        aksi = "mengirim"
        
        logger.append([dt_string, broker, port, client_id, aksi, topik, pesan])
        
        print("")
        print("Mengirimkan", pesan, "ke topik", topik)
        
        if topik == "pcr/puja/joystick/tengah":
            print("Harap tunggu, anda akan kembali ke menu dalam 3 detik!")
        
            time.sleep(3)
            menu(client)
        else:
            mqttTopic7(client, pilihan_menu)

    else:
        aksi = "gagal mengirim"
        
        logger.append([dt_string, broker, port, client_id, aksi, topik, pesan])
        
        print("")
        print("Gagal mengirimkan", pesan, "ke topik", topik)
        print("Harap tunggu, anda akan kembali ke menu dalam 3 detik!")
        
        time.sleep(3)
        menu(client)

def unduh(client):
    with open(file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Datetime', 'Broker', 'Port', 'ID Client', 'Aksi', 'Topik', 'Pesan'])
        writer.writerows(logger)
        
        if writer:
            print("")
            print(f"File {file_name} berhasil disimpan.")
            print("Harap tunggu, anda akan kembali ke menu dalam 3 detik!")
            
            time.sleep(3)
            menu(client)
        else:
            print("")
            print(f"File {file_name} gagal disimpan.")
            print("Harap tunggu, anda akan kembali ke menu dalam 3 detik!")
            
            time.sleep(3)
            menu(client)

def menu(client):
    print("")
    print("Selamat Datang di Proyek UAS")
    print(dt_string)
    print("")
    print("1. Huruf")
    print("2. Pesan")
    print("3. Lampu")
    print("4. Gambar")
    print("5. Animasi")
    print("6. Sensor")
    print("7. Joystick")
    print("98. Logger")
    print("0. Bersihkan")
    print("")
    
    pilihan_menu = int(input("Pilih : "))
    
    submenu(client, pilihan_menu)

def submenu(client, pilihan_menu):
    if pilihan_menu == 1:
        print("")
        print("Selamat Datang di Proyek UAS")
        print(dt_string)
        print("Menu 1. Huruf")
        print("")
        print("1. Gulung")
        print("2. Gulung 1")
        print("3. Gulung 2")
        print("4. Huruf Pasti")
        print("5. Huruf Acak")
        print("99. Tampilkan Semua")
        print("0. Menu")
        print("")
        
        pilihan_submenu = int(input("Pilih : "))
        
        mqttTopic1(client, pilihan_menu, pilihan_submenu)

    if pilihan_menu == 2:
        mqttTopic2(client, pilihan_menu)
        
    if pilihan_menu == 3:
        print("")
        print("Selamat Datang di Proyek UAS")
        print(dt_string)
        print("Menu 3. Lampu :")
        print("")
        print("1. Cerah")
        print("2. Redup")
        print("3. Hidup")
        print("4. Mati")
        print("99. Tampilkan Semua")
        print("0. Menu")
        print("")
        
        pilihan_submenu = int(input("Pilih : "))
        
        mqttTopic3(client, pilihan_menu, pilihan_submenu)
    
    if pilihan_menu == 4:
        print("")
        print("Selamat Datang di Proyek UAS")
        print(dt_string)
        print("Menu 4. Gambar :")
        print("")
        print("1. Senyum")
        print("2. Sedih")
        print("3. Indonesia")
        print("4. Pelangi")
        print("5. Heart")
        print("99. Tampilkan Semua")
        print("0. Menu")
        print("")
        
        pilihan_submenu = int(input("Pilih : "))
        
        mqttTopic4(client, pilihan_menu, pilihan_submenu)
    
    if pilihan_menu == 5:
        print("")
        print("Selamat Datang di Proyek UAS")
        print(dt_string)
        print("Menu 5. Animasi :")
        print("")
        print("1. Heartbeat")
        print("2. Heartbreak")
        print("3. Pacman")
        print("4. Ubur-ubur")
        print("99. Tampilkan Semua")
        print("0. Menu")
        print("")
        
        pilihan_submenu = int(input("Pilih : "))
        
        mqttTopic5(client, pilihan_menu, pilihan_submenu)
    
    if pilihan_menu == 6:
        print("")
        print("Selamat Datang di Proyek UAS")
        print(dt_string)
        print("Menu 6. Sensor :")
        print("")
        print("1. Suhu")
        print("2. Tekanan")
        print("3. Kelembaban")
        print("99. Tampilkan Semua")
        print("0. Menu")
        print("")
        
        pilihan_submenu = int(input("Pilih : "))

        mqttTopic6(client, pilihan_menu, pilihan_submenu)
    
    if pilihan_menu == 7:
        print("")
        print("Selamat Datang di Proyek UAS")
        print(dt_string)
        print("Menu 7. Joystick :")
        print("")
        print("Silakan gunakan joystick Sense HAT")
        print("Tekan enter pada joystick untuk kembali ke menu")
        print("")

        mqttTopic7(client, pilihan_menu)
    
    if pilihan_menu == 98:
        unduh(client)
    
    if pilihan_menu == 0:
        mqttTopic0(client, pilihan_menu)
    
def mqttTopic1(client, pilihan_menu, pilihan_submenu):
    def gulung(client, pilihan_menu, pilihan_submenu):
        topik = "pcr/puja/huruf/1"
        pesan = "Politeknik Caltex Riau"
        
        if pilihan_submenu == 99:
            publish1(client, topik, pesan)
        else: 
            publish(client, topik, pesan)
    
    def gulung1(client, pilihan_menu, pilihan_submenu):
        topik = "pcr/puja/huruf/2"
        pesan = "Selamat datang di PCR"
        
        if pilihan_submenu == 99:
            publish1(client, topik, pesan)
        else: 
            publish(client, topik, pesan)
        
    def gulung2(client, pilihan_menu, pilihan_submenu):
        topik = "pcr/puja/huruf/3"
        pesan = "Selamat datang Mahasiswa Baru angkatan 2021 (G21)"
        
        if pilihan_submenu == 99:
            publish1(client, topik, pesan)
        else: 
            publish(client, topik, pesan)
        
    def hurufpasti(client, pilihan_menu, pilihan_submenu):
        topik = "pcr/puja/huruf/4"
        pesan = "PCR20Tahun"
        
        if pilihan_submenu == 99:
            publish1(client, topik, pesan)
        else: 
            publish(client, topik, pesan)
    
    def hurufacak(client, pilihan_menu, pilihan_submenu):
        topik = "pcr/puja/huruf/5"
        pesan = "Politeknik Caltex Riau"
        
        publish(client, topik, pesan)
     
    if pilihan_menu == 1:
        if pilihan_submenu == 1:
            gulung(client, pilihan_menu, pilihan_submenu)

        if pilihan_submenu == 2:
            gulung1(client, pilihan_menu, pilihan_submenu)
    
        if pilihan_submenu == 3:
            gulung2(client, pilihan_menu, pilihan_submenu)
    
        if pilihan_submenu == 4:
            hurufpasti(client, pilihan_menu, pilihan_submenu)
    
        if pilihan_submenu == 5:
            hurufacak(client, pilihan_menu, pilihan_submenu)
    
        if pilihan_submenu == 99:
            gulung(client, pilihan_menu, pilihan_submenu)
            time.sleep(1)
        
            gulung1(client, pilihan_menu, pilihan_submenu)
            time.sleep(1)
        
            gulung2(client, pilihan_menu, pilihan_submenu)
            time.sleep(1)
        
            hurufpasti(client, pilihan_menu, pilihan_submenu)
            time.sleep(1)
        
            hurufacak(client, pilihan_menu, pilihan_submenu)
            time.sleep(1)
            
        if pilihan_submenu == 0:
            menu(client)

def mqttTopic2(client, pilihan_menu):
    topik = "pcr/puja/pesan"
    
    print("")
    pesan = input("Masukkan pesan : ")
    
    publish(client, topik, pesan)
    
def mqttTopic3(client, pilihan_menu, pilihan_submenu):
    def lampu_cerah(client, pilihan_menu, pilihan_submenu):
        topik = "pcr/puja/lampu/cerah"
        pesan = "Lampu cerah"
        
        if pilihan_submenu == 99:
            publish1(client, topik, pesan)
        else: 
            publish(client, topik, pesan)
    
    def lampu_redup(client, pilihan_menu, pilihan_submenu):
        topik = "pcr/puja/lampu/redup"
        pesan = "Lampu redup"
        
        if pilihan_submenu == 99:
            publish1(client, topik, pesan)
        else: 
            publish(client, topik, pesan)
    
    def lampu_hidup(client, pilihan_menu, pilihan_submenu):
        topik = "pcr/puja/lampu/hidup"
        pesan = "Lampu hidup"
        
        if pilihan_submenu == 99:
            publish1(client, topik, pesan)
        else: 
            publish(client, topik, pesan)
    
    def lampu_mati(client, pilihan_menu, pilihan_submenu):
        topik = "pcr/puja/lampu/mati"
        pesan = "Lampu mati"
        
        publish(client, topik, pesan)
    
    if pilihan_menu == 3:
        if pilihan_submenu == 1:
            lampu_cerah(client, pilihan_menu, pilihan_submenu)
    
        if pilihan_submenu == 2:
            lampu_redup(client, pilihan_menu, pilihan_submenu)
    
        if pilihan_submenu == 3:
            lampu_hidup(client, pilihan_menu, pilihan_submenu)
    
        if pilihan_submenu == 4:
            lampu_mati(client, pilihan_menu, pilihan_submenu)
            
        if pilihan_submenu == 99:
            lampu_cerah(client, pilihan_menu, pilihan_submenu)
            time.sleep(1)
        
            lampu_redup(client, pilihan_menu, pilihan_submenu)
            time.sleep(1)
        
            lampu_hidup(client, pilihan_menu, pilihan_submenu)
            time.sleep(1)
        
            lampu_mati(client, pilihan_menu, pilihan_submenu)
            time.sleep(1)
            
        if pilihan_submenu == 0:
            menu(client)

def mqttTopic4(client, pilihan_menu, pilihan_submenu):    
    def gambar_senyum(client, pilihan_menu, pilihan_submenu):
        topik = "pcr/puja/gambar/senyum"
        pesan = "Gambar senyum"
        
        if pilihan_submenu == 99:
            publish1(client, topik, pesan)
        else: 
            publish(client, topik, pesan)
        
    def gambar_sedih(client, pilihan_menu, pilihan_submenu):
        topik = "pcr/puja/gambar/sedih"
        pesan = "Gambar sedih"
        
        if pilihan_submenu == 99:
            publish1(client, topik, pesan)
        else: 
            publish(client, topik, pesan)
    
    def gambar_indonesia(client, pilihan_menu, pilihan_submenu):
        topik = "pcr/puja/gambar/indonesia"
        pesan = "Gambar Indonesia"
        
        if pilihan_submenu == 99:
            publish1(client, topik, pesan)
        else: 
            publish(client, topik, pesan)
        
    def gambar_pelangi(client, pilihan_menu, pilihan_submenu):
        topik = "pcr/puja/gambar/pelangi"
        pesan = "Gambar pelangi"
        
        if pilihan_submenu == 99:
            publish1(client, topik, pesan)
        else: 
            publish(client, topik, pesan)
    
    def gambar_heart(client, pilihan_menu, pilihan_submenu):
        topik = "pcr/puja/gambar/heart"
        pesan = "Gambar heart"
        
        publish(client, topik, pesan)
    
    if pilihan_menu == 4:
        if pilihan_submenu == 1:
            gambar_senyum(client, pilihan_menu, pilihan_submenu)
    
        if pilihan_submenu == 2:
            gambar_sedih(client, pilihan_menu, pilihan_submenu)
        
        if pilihan_submenu == 3:
            gambar_indonesia(client, pilihan_menu, pilihan_submenu)
            
        if pilihan_submenu == 4:
            gambar_pelangi(client, pilihan_menu, pilihan_submenu)
        
        if pilihan_submenu == 5:
            gambar_heart(client, pilihan_menu, pilihan_submenu)
        
        if pilihan_submenu == 99:
            gambar_senyum(client, pilihan_menu, pilihan_submenu)
            time.sleep(1)
        
            gambar_sedih(client, pilihan_menu, pilihan_submenu)
            time.sleep(1)
            
            gambar_indonesia(client, pilihan_menu, pilihan_submenu)
            time.sleep(1)
        
            gambar_pelangi(client, pilihan_menu, pilihan_submenu)
            time.sleep(1)
            
            gambar_heart(client, pilihan_menu, pilihan_submenu)
            time.sleep(1)
            
        if pilihan_submenu == 0:
            menu(client)
            
def mqttTopic5(client, pilihan_menu, pilihan_submenu):    
    def animasi_heartbeat(client, pilihan_menu, pilihan_submenu):
        topik = "pcr/puja/animasi/heartbeat"
        pesan = "Animasi heartbeat"
        
        if pilihan_submenu == 99:
            publish1(client, topik, pesan)
        else: 
            publish(client, topik, pesan)
    
    def animasi_heartbreak(client, pilihan_menu, pilihan_submenu):
        topik = "pcr/puja/animasi/heartbreak"
        pesan = "Animasi heartbreak"
        
        if pilihan_submenu == 99:
            publish1(client, topik, pesan)
        else: 
            publish(client, topik, pesan)
    
    def animasi_pacman(client, pilihan_menu, pilihan_submenu):
        topik = "pcr/puja/animasi/pacman"
        pesan = "Animasi pacman"
        
        if pilihan_submenu == 99:
            publish1(client, topik, pesan)
        else: 
            publish(client, topik, pesan)
    
    def animasi_uburubur(client, pilihan_menu, pilihan_submenu):
        topik = "pcr/puja/animasi/uburubur"
        pesan = "Animasi ubur-ubur"
        
        publish(client, topik, pesan)
    
    if pilihan_menu == 5:
        if pilihan_submenu == 1:
            animasi_heartbeat(client, pilihan_menu, pilihan_submenu)
            
        if pilihan_submenu == 2:
            animasi_heartbreak(client, pilihan_menu, pilihan_submenu)
            
        if pilihan_submenu == 3:
            animasi_pacman(client, pilihan_menu, pilihan_submenu)
            
        if pilihan_submenu == 4:
            animasi_uburubur(client, pilihan_menu, pilihan_submenu)
        
        if pilihan_submenu == 99:
            animasi_heartbeat(client, pilihan_menu, pilihan_submenu)
            time.sleep(1)
            
            animasi_heartbreak(client, pilihan_menu, pilihan_submenu)
            time.sleep(1)
            
            animasi_pacman(client, pilihan_menu, pilihan_submenu)
            time.sleep(1)
            
            animasi_uburubur(client, pilihan_menu, pilihan_submenu)
            time.sleep(1)
            
        if pilihan_submenu == 0:
            menu(client)

def mqttTopic6(client, pilihan_menu, pilihan_submenu):
    def sensor_suhu(client, pilihan_menu, pilihan_submenu):
        topik = "pcr/puja/sensor/suhu"
        suhu = sense.get_temperature()
        pesan = round(suhu, 2)
        
        if pilihan_submenu == 99:
            publish1(client, topik, pesan)
        else: 
            publish(client, topik, pesan)
        
    def sensor_tekanan(client, pilihan_menu, pilihan_submenu):
        topik = "pcr/puja/sensor/tekanan"
        tekanan = sense.get_pressure()
        pesan = round(tekanan, 2)
        
        if pilihan_submenu == 99:
            publish1(client, topik, pesan)
        else: 
            publish(client, topik, pesan)
        
    def sensor_kelembaban(client, pilihan_menu, pilihan_submenu):
        topik = "pcr/puja/sensor/kelembaban"
        kelembaban = sense.get_humidity()
        pesan = round(kelembaban, 2)
        
        publish(client, topik, pesan)
     
    if pilihan_menu == 6:
        if pilihan_submenu == 1:
            sensor_suhu(client, pilihan_menu, pilihan_submenu)

        if pilihan_submenu == 2:
            sensor_tekanan(client, pilihan_menu, pilihan_submenu)
    
        if pilihan_submenu == 3:
            sensor_kelembaban(client, pilihan_menu, pilihan_submenu)
    
        if pilihan_submenu == 99:
            sensor_suhu(client, pilihan_menu, pilihan_submenu)
            time.sleep(1)
        
            sensor_tekanan(client, pilihan_menu, pilihan_submenu)
            time.sleep(1)
        
            sensor_kelembaban(client, pilihan_menu, pilihan_submenu)
            time.sleep(1)
            
        if pilihan_submenu == 0:
            menu(client)

def mqttTopic7(client, pilihan_menu):
    def joystick_atas(client, pilihan_menu):
        topik = "pcr/puja/joystick/atas"
        pesan = "Joystick atas"
        
        publish2(client, topik, pesan, pilihan_menu)
        
    def joystick_bawah(client, pilihan_menu):
        topik = "pcr/puja/joystick/bawah"
        pesan = "Joystick bawah"
        
        publish2(client, topik, pesan, pilihan_menu)
    
    def joystick_kanan(client, pilihan_menu):
        topik = "pcr/puja/joystick/kanan"
        pesan = "Joystick kanan"
        
        publish2(client, topik, pesan, pilihan_menu)
    
    def joystick_kiri(client, pilihan_menu):
        topik = "pcr/puja/joystick/kiri"
        pesan = "Joystick kiri"
        
        publish2(client, topik, pesan, pilihan_menu)
    
    def joystick_tengah(client, pilihan_menu):
        topik = "pcr/puja/joystick/tengah"
        pesan = "Joystick tengah"
        
        publish2(client, topik, pesan, pilihan_menu)
    
    if pilihan_menu == 7:
        while True:
            for event in sense.stick.get_events():
                if event.action == "pressed":
                    if event.direction == "up":
                        joystick_atas(client, pilihan_menu)
                    
                    if event.direction == "down":
                        joystick_bawah(client, pilihan_menu)
                    
                    if event.direction == "right":
                        joystick_kanan(client, pilihan_menu)
                    
                    if event.direction == "left":
                        joystick_kiri(client, pilihan_menu)
                    
                    if event.direction == "middle":
                        joystick_tengah(client, pilihan_menu)
    
def mqttTopic0(client, pilihan_menu):
    topik = "pcr/puja/bersihkan"
    nilai = 0
    
    publish(client, topik, nilai)
    
if __name__ == '__main__':
    run()
