# MQTT Subscriber
# Code writter by MPAB
# Look at me on : 
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
# client_id = "puja_subscriber"
# keepalive = 300

broker = ""
port = ""
client_id = ""
keepalive = 3600

now = datetime.now()
dt_string = now.strftime("%d-%m-%Y %H:%M:%S")

logger = []
file_logger = " subscriber.csv"
file_name = str(dt_string) + str(file_logger)

berlangganan = []
berlangganan2 = [
    "pcr/puja/huruf/1",
    "pcr/puja/huruf/2",
    "pcr/puja/huruf/3",
    "pcr/puja/huruf/4",
    "pcr/puja/huruf/5",
    "pcr/puja/pesan",
    "pcr/puja/lampu/cerah",
    "pcr/puja/lampu/redup",
    "pcr/puja/lampu/hidup",
    "pcr/puja/lampu/mati",
    "pcr/puja/gambar/senyum",
    "pcr/puja/gambar/sedih",
    "pcr/puja/gambar/indonesia",
    "pcr/puja/gambar/pelangi",
    "pcr/puja/gambar/heart",
    "pcr/puja/animasi/heartbeat",
    "pcr/puja/animasi/heartbreak",
    "pcr/puja/animasi/pacman",
    "pcr/puja/animasi/uburubur",
    "pcr/puja/sensor/suhu",
    "pcr/puja/sensor/tekanan",
    "pcr/puja/sensor/kelembaban",
    "pcr/puja/joystick/atas",
    "pcr/puja/joystick/bawah",
    "pcr/puja/joystick/kanan",
    "pcr/puja/joystick/kiri",
    "pcr/puja/joystick/tengah",
    "pcr/puja/bersihkan"
]
    
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
    
    client = connect_mqtt(broker, port, client_id, keepalive)
    
    menu(client)

def connect_mqtt(broker, port, client_id, keepalive):
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("")
            print("Berhasil terhubung MQTT Broker!")
            print("")
        else:
            print("")
            print("Koneksi gagal, code error %d\n", rc)
            print("")
            
    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port, keepalive)
    
    return client
    
def subscribe (client: mqtt_client, topik):    
    def on_message(client, userdata, msg): 
        aksi = "menerima"
        data = str(msg.payload)
        
        print("Menerima topik", msg.topic, "dengan nilai", data)
        
        logger.append([aksi, topik, data])
               
        if msg.topic == "pcr/puja/huruf/1":
            pesan = msg.payload.decode("utf-8")
            
            black = (0, 0, 0)
            white = (255, 255, 255)
        
            sense.show_message(pesan, text_colour=black, back_colour=white, scroll_speed=0.05)
        
        if msg.topic == "pcr/puja/huruf/2":
            pesan = msg.payload.decode("utf-8")
            
            black = (0, 0, 0)
            white = (255, 255, 255)
        
            sense.show_message(pesan, text_colour=black, back_colour=white, scroll_speed=0.05)
            
        if msg.topic == "pcr/puja/huruf/3":
            pesan = msg.payload.decode("utf-8")
            
            black = (0, 0, 0)
            white = (255, 255, 255)
        
            sense.show_message(pesan, text_colour=black, back_colour=white, scroll_speed=0.05)
            
        if msg.topic == "pcr/puja/huruf/4":
            pesan = msg.payload.decode("utf-8")
            
            white = (255, 255, 255)
            warna1 = (255, 255, 255)
            warna2 = (255, 0, 0)
            warna3 = (0, 255, 0)
            warna4 = (0, 0, 255)
            warna5 = (255, 255, 0)
            warna6 = (0, 255, 255)
            warna7 = (255, 0, 255)
            warna8 = (192, 192, 192)
            warna9 = (128, 128, 128)
            warna10 = (128, 0, 0)
            
            # for element in range(len(pesan)):
                # a = pesan[element]
                # b = "warna"
                # c = element + 1
                # d = b + str(c)
                
                # print(a, b, c, d)
                
            white = (255, 255, 255)
            black = (0, 0, 0)
            red = (255, 0, 0)
            lime = (0, 255, 0)
            blue = (0, 0, 255)
            yellow = (255, 255, 0)
            aqua = (0, 255, 255)
            magenta = (255, 0, 255)
            silver = (192, 192, 192)
            gray = (128, 128, 128)
            maroon = (128, 0, 0)
        
            sense.show_message("P", text_colour=black, back_colour=white, scroll_speed=0.05)
            sense.show_message("C", text_colour=red, back_colour=white, scroll_speed=0.05)
            sense.show_message("R", text_colour=lime, back_colour=white, scroll_speed=0.05)
            sense.show_message("2", text_colour=blue, back_colour=white, scroll_speed=0.05)
            sense.show_message("0", text_colour=yellow, back_colour=white, scroll_speed=0.05)
            sense.show_message("T", text_colour=aqua, back_colour=white, scroll_speed=0.05)
            sense.show_message("a", text_colour=magenta, back_colour=white, scroll_speed=0.05)
            sense.show_message("h", text_colour=silver, back_colour=white, scroll_speed=0.05)
            sense.show_message("u", text_colour=gray, back_colour=white, scroll_speed=0.05)
            sense.show_message("n", text_colour=maroon, back_colour=white, scroll_speed=0.05)
        
        if msg.topic == "pcr/puja/huruf/5":
            pesan = msg.payload.decode("utf-8")
            
            white = (255, 255, 255)
        
            color = list(np.random.choice(range(256), size=3))
            sense.show_message("P", text_colour=color, back_colour=white, scroll_speed=0.05)
            
            color = list(np.random.choice(range(256), size=3))
            sense.show_message("o", text_colour=color, back_colour=white, scroll_speed=0.05)
            
            color = list(np.random.choice(range(256), size=3))
            sense.show_message("l", text_colour=color, back_colour=white, scroll_speed=0.05)
            
            color = list(np.random.choice(range(256), size=3))
            sense.show_message("i", text_colour=color, back_colour=white, scroll_speed=0.05)
            
            color = list(np.random.choice(range(256), size=3))
            sense.show_message("t", text_colour=color, back_colour=white, scroll_speed=0.05)
            
            color = list(np.random.choice(range(256), size=3))
            sense.show_message("e", text_colour=color, back_colour=white, scroll_speed=0.05)
            
            color = list(np.random.choice(range(256), size=3))
            sense.show_message("k", text_colour=color, back_colour=white, scroll_speed=0.05)
            
            color = list(np.random.choice(range(256), size=3))
            sense.show_message("n", text_colour=color, back_colour=white, scroll_speed=0.05)
            
            color = list(np.random.choice(range(256), size=3))
            sense.show_message("i", text_colour=color, back_colour=white, scroll_speed=0.05)
            
            color = list(np.random.choice(range(256), size=3))
            sense.show_message("k", text_colour=color, back_colour=white, scroll_speed=0.05)
            
            color = list(np.random.choice(range(256), size=3))
            sense.show_message("C", text_colour=color, back_colour=white, scroll_speed=0.05)
            
            color = list(np.random.choice(range(256), size=3))
            sense.show_message("a", text_colour=color, back_colour=white, scroll_speed=0.05)
            
            color = list(np.random.choice(range(256), size=3))
            sense.show_message("l", text_colour=color, back_colour=white, scroll_speed=0.05)
            
            color = list(np.random.choice(range(256), size=3))
            sense.show_message("t", text_colour=color, back_colour=white, scroll_speed=0.05)
            
            color = list(np.random.choice(range(256), size=3))
            sense.show_message("e", text_colour=color, back_colour=white, scroll_speed=0.05)
            
            color = list(np.random.choice(range(256), size=3))
            sense.show_message("x", text_colour=color, back_colour=white, scroll_speed=0.05)
            
            color = list(np.random.choice(range(256), size=3))
            sense.show_message("R", text_colour=color, back_colour=white, scroll_speed=0.05)
            
            color = list(np.random.choice(range(256), size=3))
            sense.show_message("i", text_colour=color, back_colour=white, scroll_speed=0.05)
            
            color = list(np.random.choice(range(256), size=3))
            sense.show_message("a", text_colour=color, back_colour=white, scroll_speed=0.05)
            
            color = list(np.random.choice(range(256), size=3))
            sense.show_message("u", text_colour=color, back_colour=white, scroll_speed=0.05)
        
        if msg.topic == "pcr/puja/pesan":
            pesan = msg.payload.decode("utf-8")
            
            black = (0, 0, 0)
            white = (255, 255, 255)
        
            sense.show_message(pesan, text_colour=black, back_colour=white, scroll_speed=0.05)
        
        if msg.topic == "pcr/puja/lampu/cerah":
            w = (255, 255, 255)
        
            image = [
                w, w, w, w, w, w, w, w,
                w, w, w, w, w, w, w, w,
                w, w, w, w, w, w, w, w,
                w, w, w, w, w, w, w, w,
                w, w, w, w, w, w, w, w,
                w, w, w, w, w, w, w, w,
                w, w, w, w, w, w, w, w,
                w, w, w, w, w, w, w, w
            ]

            sense.set_pixels(image)
            
        if msg.topic == "pcr/puja/lampu/redup":
            g = (128, 128, 128)
        
            image = [
                g, g, g, g, g, g, g, g,
                g, g, g, g, g, g, g, g,
                g, g, g, g, g, g, g, g,
                g, g, g, g, g, g, g, g,
                g, g, g, g, g, g, g, g,
                g, g, g, g, g, g, g, g,
                g, g, g, g, g, g, g, g,
                g, g, g, g, g, g, g, g
            ]

            sense.set_pixels(image)
            
        if msg.topic == "pcr/puja/lampu/hidup":
            w = (255, 255, 255)
            b = (0, 0, 0)
        
            image = [
                w, b, b, b, b, b, b, b,
                b, b, b, b, b, b, b, b,
                b, b, b, b, b, b, b, b,
                b, b, b, b, b, b, b, b,
                b, b, b, b, b, b, b, b,
                b, b, b, b, b, b, b, b,
                b, b, b, b, b, b, b, b,
                b, b, b, b, b, b, b, b
            ]

            sense.set_pixels(image)
        
        if msg.topic == "pcr/puja/lampu/mati":
            w = (255, 255, 255)
            b = (0, 0, 0)
        
            image = [
                b, b, b, b, b, b, b, b,
                b, b, b, b, b, b, b, b,
                b, b, b, b, b, b, b, b,
                b, b, b, b, b, b, b, b,
                b, b, b, b, b, b, b, b,
                b, b, b, b, b, b, b, b,
                b, b, b, b, b, b, b, b,
                b, b, b, b, b, b, b, b
            ]

            sense.set_pixels(image)
            
        if msg.topic == "pcr/puja/gambar/senyum":
            m = (128, 0, 0)
            y = (255, 255, 0)
            b = (0, 0, 0)

            image = [
                b, y, y, y, y, y, y, b,
                y, y, m, y, y, m, y, y,
                y, y, m, y, y, m, y, y,
                y, y, y, y, y, y, y, y,
                y, y, y, y, y, y, y, y,
                y, m, m, m, m, m, m, y,
                y, y, m, m, m, m, y, y,
                b, y, y, y, y, y, y, b
]
            sense.set_pixels(image)
            
        if msg.topic == "pcr/puja/gambar/sedih":
            m = (128, 0, 0)
            y = (255, 255, 0)
            b = (0, 0, 0)

            image = [
                b, y, y, y, y, y, y, b,
                y, y, m, y, y, m, y, y,
                y, y, m, y, y, m, y, y,
                y, y, y, y, y, y, y, y,
                y, y, y, y, y, y, y, y,
                y, y, m, m, m, m, y, y,
                y, m, m, m, m, m, m, y,
                b, y, y, y, y, y, y, b
            ]

            sense.set_pixels(image)
            
        if msg.topic == "pcr/puja/gambar/indonesia":
            r = (255, 0, 0)
            w = (255, 255, 255)
    
            image = [
                r, r, r, r, r, r, r, r,
                r, r, r, r, r, r, r, r,
                r, r, r, r, r, r, r, r,
                r, r, r, r, r, r, r, r,
                w, w, w, w, w, w, w, w,
                w, w, w, w, w, w, w, w,
                w, w, w, w, w, w, w, w,
                w, w, w, w, w, w, w, w
            ]
        
            sense.set_pixels(image)
        
        if msg.topic == "pcr/puja/gambar/pelangi":
            r = (255, 0, 0)
            o = (255, 127, 0)
            y = (255, 255, 0)
            g = (0, 255, 0)
            b = (0, 0, 255)
            i = (75, 0, 130)
            v = (148, 0, 211)
    
            image = [
                r, r, r, r, r, r, r, r,
                r, r, r, r, r, r, r, r,
                o, o, o, o, o, o, o, o,
                y, y, y, y, y, y, y, y,
                g, g, g, g, g, g, g, g,
                b, b, b, b, b, b, b, b,
                i, i, i, i, i, i, i, i,
                v, v, v, v, v, v, v, v
            ]
        
            sense.set_pixels(image)
        
        if msg.topic == "pcr/puja/gambar/heart":
            r = (255, 0, 0)
            w = (255, 255, 255)

            image = [
                w, r, r, w, w, r, r, w,
                r, r, r, r, r, r, r, r,
                r, r, r, r, r, r, r, r,
                r, r, r, r, r, r, r, r,
                r, r, r, r, r, r, r, r,
                w, r, r, r, r, r, r, w,
                w, w, r, r, r, r, w, w,
                w, w, w, r, r, w, w, w
            ]
            
            sense.set_pixels(image)
            
        if msg.topic == "pcr/puja/animasi/heartbeat":
            r = (255, 0, 0)
            w = (255, 255, 255)
            b = (0, 0, 0)

            image = [
                b, b, b, b, b, b, b, b,
                b, r, r, b, b, r, r, b,
                r, r, w, w, r, r, r, r,
                r, w, r, r, r, r, r, r,
                b, r, r, r, r, r, r, b,
                b, b, r, r, r, r, b, b,
                b, b, b, r, r, b, b, b,
                b, b, b, b, b, b, b, b
            ]

            image2 = [
                b, b, b, b, b, b, b, b,
                b, b, b, b, b, b, b, b,
                b, b, r, b, b, r, b, b,
                b, r, r, w, r, r, r, b,
                b, b, r, r, r, r, b, b,
                b, b, b, r, r, b, b, b,
                b, b, b, b, b, b, b, b,
                b, b, b, b, b, b, b, b
            ]

            for ulangi in range(1, 11):
                sense.set_pixels(image)
                time.sleep(0.45)
            
                sense.set_pixels(image2)
                time.sleep(0.40)
        
        if msg.topic == "pcr/puja/animasi/heartbreak":
            r = (255, 0, 0)
            w = (255, 255, 255)
            b = (0, 0, 0)

            image = [
                w, r, r, w, w, r, r, w,
                r, r, r, r, r, r, r, r,
                r, r, r, r, r, r, r, r,
                r, r, r, r, r, r, r, r,
                r, r, r, r, r, r, r, r,
                w, r, r, r, r, r, r, w,
                w, w, r, r, r, r, w, w,
                w, w, w, r, r, w, w, w
            ]

            image2 = [
                w, r, r, w, w, r, r, w,
                r, r, r, r, b, r, r, r,
                r, r, r, b, r, r, r, r,
                r, r, r, b, r, r, r, r,
                r, r, b, r, r, r, r, r,
                w, r, r, b, r, r, r, w,
                w, w, r, r, b, r, w, w,
                w, w, w, r, b, w, w, w
            ]

            for ulangi in range(1, 11):
                sense.set_pixels(image)
                time.sleep(2)
            
                sense.set_pixels(image2)
                time.sleep(2)
        
        if msg.topic == "pcr/puja/animasi/pacman":
            y = (255, 255, 0)
            r = (255, 0, 0)
            w = (255, 255, 255)

            image = [
                w, w, w, y, y, y, y, y,
                w, y, y, r, r, y, y, y,
                y, y, y, r, r, y, y, w,
                y, y, y, y, y, y, w, w,
                y, y, y, y, y, w, w, w,
                y, y, y, y, y, y, w, w,
                w, y, y, y, y, y, y, w,
                w, w, y, y, y, y, y, y
            ]
            
            image2 = [
                w, w, w, y, y, y, w, w,
                w, y, y, r, r, y, y, w,
                y, y, y, r, r, y, y, y,
                y, y, y, y, y, w, w, w,
                y, y, y, y, w, w, w, w,
                y, y, y, y, y, w, w, w,
                w, y, y, y, y, y, y, y,
                w, w, y, y, y, y, w, w
            ]

            image3 = [
                w, w, w, y, y, y, w, w,
                w, y, y, r, r, y, y, w,
                y, y, y, r, r, y, y, y,
                y, y, y, y, y, y, y, y,
                y, y, y, y, w, w, w, w,
                y, y, y, y, y, y, y, y,
                w, y, y, y, y, y, y, y,
                w, w, y, y, y, y, w, w
            ]

            image4 = [
                w, w, w, y, y, y, w, w,
                w, y, y, r, r, y, y, w,
                y, y, y, r, r, y, y, y,
                y, y, y, y, y, y, y, y,
                y, y, y, y, y, y, y, y,
                y, y, y, y, y, y, y, w,
                w, y, y, y, y, y, y, w,
                w, w, y, y, y, y, w, w
            ]

            for ulangi in range(1, 11):
                sense.set_pixels(image)
                time.sleep(0.25)
    
                sense.set_pixels(image2)
                time.sleep(0.25)
    
                sense.set_pixels(image3)
                time.sleep(0.25)
    
                sense.set_pixels(image4)
                time.sleep(0.25)
                
        if msg.topic == "pcr/puja/animasi/uburubur":
            b = (0, 0, 0)
            v = (148, 0, 211)
            w = (255, 255, 255)
            a = (0, 255, 255)

            image = [
                b, b, v, v, v, v, b, b,
                b, v, v, v, v, v, v, b,
                v, v, w, w, v, w, w, v,
                v, v, w, a, v, w, a, v,
                v, v, v, v, v, v, v, v,
                v, v, v, v, v, v, v, v,
                v, b, v, b, v, b, v, v,
                v, b, v, b, v, b, v, v
            ]

            image2 = [
                b, b, v, v, v, v, b, b,
                b, v, v, v, v, v, v, b,
                v, v, w, w, v, w, w, v,
                v, v, a, w, v, a, w, v,
                v, v, v, v, v, v, v, v,
                v, v, v, v, v, v, v, v,
                v, v, b, v, b, v, b, v,
                v, v, b, v, b, v, b, v
            ]

            image3 = [
                b, b, v, v, v, v, b, b,
                b, v, v, v, v, v, v, b,
                v, v, a, w, v, a, w, v,
                v, v, w, w, v, w, w, v,
                v, v, v, v, v, v, v, v,
                v, v, v, v, v, v, v, v,
                v, b, v, b, v, b, v, v,
                v, b, v, b, v, b, v, v
            ]

            image4 = [
                b, b, v, v, v, v, b, b,
                b, v, v, v, v, v, v, b,
                v, v, w, a, v, w, a, v,
                v, v, w, w, v, w, w, v,
                v, v, v, v, v, v, v, v,
                v, v, v, v, v, v, v, v,
                v, v, b, v, b, v, b, v,
                v, v, b, v, b, v, b, v
            ]

            for ulangi in range(1, 11):
                sense.set_pixels(image)
                time.sleep(0.25)
    
                sense.set_pixels(image2)
                time.sleep(0.25)
    
                sense.set_pixels(image3)
                time.sleep(0.25)
    
                sense.set_pixels(image4)
                time.sleep(0.25)
        
        if msg.topic == "pcr/puja/sensor/suhu":
            data = float(msg.payload)
            pesan = "Suhu : "
            cetak = pesan + str(data)
    
            if data < 24:
                latar = (0, 0, 255)
            elif data > 32:
                latar = (255, 0, 0)
            else:
                latar = (0, 255, 0)
            
            white = (255, 255, 255)
            
            sense.show_message(cetak, text_colour=white, back_colour=latar, scroll_speed=0.05)
        
        if msg.topic == "pcr/puja/sensor/tekanan":
            data = float(msg.payload)
            pesan = "Tekanan : "
            cetak = pesan + str(data)
    
            if data < 400:
                latar = (0, 0, 255)
            elif data > 800:
                latar = (255, 0, 0)
            else:
                latar = (0, 255, 0)
            
            white = (255, 255, 255)
            
            sense.show_message(cetak, text_colour=white, back_colour=latar, scroll_speed=0.05)
        
        if msg.topic == "pcr/puja/sensor/kelembaban":
            data = float(msg.payload)
            pesan = "Kelembaban : "
            cetak = pesan + str(data)
    
            if data < 45:
                latar = (0, 0, 255)
            elif data > 65:
                latar = (255, 0, 0)
            else:
                latar = (0, 255, 0)
            
            white = (255, 255, 255)
            
            sense.show_message(cetak, text_colour=white, back_colour=latar, scroll_speed=0.05)
            
        if msg.topic == "pcr/puja/joystick/atas":
            w = (255, 255, 255)
            r = (255, 0, 0)

            image = [
                w, w, w, r, r, w, w, w,
                w, w, r, r, r, r, w, w,
                w, r, r, r, r, r, r, w,
                r, r, r, r, r, r, r, r,
                r, r, r, r, r, r, r, r,
                w, w, r, r, r, r, w, w,
                w, w, r, r, r, r, w, w,
                w, w, r, r, r, r, w, w
            ]
        
            sense.set_pixels(image)
        
        if msg.topic == "pcr/puja/joystick/bawah":
            w = (255, 255, 255)
            b = (0, 0, 255)

            image = [
                w, w, b, b, b, b, w, w,
                w, w, b, b, b, b, w, w,
                w, w, b, b, b, b, w, w,
                b, b, b, b, b, b, b, b,
                b, b, b, b, b, b, b, b,
                w, b, b, b, b, b, b, w,
                w, w, b, b, b, b, w, w,
                w, w, w, b, b, w, w, w
            ]
        
            sense.set_pixels(image)
            
        if msg.topic == "pcr/puja/joystick/kanan":
            w = (255, 255, 255)
            y = (255, 255, 0)
    
            image = [
                w, w, w, y, y, w, w, w,
                w, w, w, y, y, y, w, w,
                y, y, y, y, y, y, y, w,
                y, y, y, y, y, y, y, y,
                y, y, y, y, y, y, y, y,
                y, y, y, y, y, y, y, w,
                w, w, w, y, y, y, w, w,
                w, w, w, y, y, w, w, w
            ]
        
            sense.set_pixels(image)
        
        if msg.topic == "pcr/puja/joystick/kiri":
            w = (255, 255, 255)
            g = (0, 255, 0)

            image = [
                w, w, w, g, g, w, w, w,
                w, w, g, g, g, w, w, w,
                w, g, g, g, g, g, g, g,
                g, g, g, g, g, g, g, g,
                g, g, g, g, g, g, g, g,
                w, g, g, g, g, g, g, g,
                w, w, g, g, g, w, w, w,
                w, w, w, g, g, w, w, w
            ]
        
            sense.set_pixels(image)
        
        if msg.topic == "pcr/puja/joystick/tengah":
            sense.clear()
    
        if msg.topic == "pcr/puja/bersihkan":
            sense.clear()
        
    client.subscribe(topik)
    client.on_message = on_message
    
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
    print("97. Berlangganan Semua Topik")
    print("98. Logger")
    print("99. Eksekusi")
    print("0. Bersihkan")
    print("")
    print("Langganan : ", berlangganan)
    print("")
    
    pilihan_menu = int(input("Pilih : "))
    
    submenu(client, pilihan_menu)

def submenu(client, pilihan_menu):
    if pilihan_menu == 1:
        print("")
        print("Selamat Datang di Proyek UAS")
        print(dt_string)
        print("Menu 1. Huruf :")
        print("")
        print("1. Gulung")
        print("2. Gulung 1")
        print("3. Gulung 2")
        print("4. Huruf Pasti")
        print("5. Huruf Acak")
        print("0. Menu")
        print("")
        print("Langganan : ", berlangganan)
        print("")
        
        pilihan_submenu = int(input("Pilih : "))
        
        cek(client, pilihan_menu, pilihan_submenu)

    if pilihan_menu == 2:
        pilihan_submenu = 0
        
        cek(client, pilihan_menu, pilihan_submenu)
        
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
        print("0. Menu")
        print("")
        
        pilihan_submenu = int(input("Pilih : "))
        
        cek(client, pilihan_menu, pilihan_submenu)
    
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
        print("0. Menu")
        print("")
        
        pilihan_submenu = int(input("Pilih : "))
        
        cek(client, pilihan_menu, pilihan_submenu)
    
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
        print("0. Menu")
        print("")
        
        pilihan_submenu = int(input("Pilih : "))
        
        cek(client, pilihan_menu, pilihan_submenu)
        
    if pilihan_menu == 6:
        print("")
        print("Selamat Datang di Proyek UAS")
        print(dt_string)
        print("Menu 6. Sensor :")
        print("")
        print("1. Suhu")
        print("2. Tekanan")
        print("3. Kelembaban")
        print("0. Menu")
        print("")
        
        pilihan_submenu = int(input("Pilih : "))
        
        cek(client, pilihan_menu, pilihan_submenu)
    
    if pilihan_menu == 7:
        print("")
        print("Selamat Datang di Proyek UAS")
        print(dt_string)
        print("Menu 7. Joystick :")
        print("")
        print("1. Atas")
        print("2. Bawah")
        print("3. Kanan")
        print("4. Kiri")
        print("5. Tengah")
        print("0. Menu")
        print("")
        
        pilihan_submenu = int(input("Pilih : "))
        
        cek(client, pilihan_menu, pilihan_submenu)
    
    if pilihan_menu == 97:
        eksekusi1(client)
    
    if pilihan_menu == 98:
        unduh(client)
    
    if pilihan_menu == 99:
        eksekusi(client)
    
    if pilihan_menu == 0:
        pilihan_submenu = 0

        cek(client, pilihan_menu, pilihan_submenu)
        
def cek(client, pilihan_menu, pilihan_submenu):
    if pilihan_menu == 1:
        if pilihan_submenu == 1:
            topik = "pcr/puja/huruf/1"
                
        if pilihan_submenu == 2:
            topik = "pcr/puja/huruf/2"
            
        if pilihan_submenu == 3:
            topik = "pcr/puja/huruf/3"
            
        if pilihan_submenu == 4:
            topik = "pcr/puja/huruf/4"
            
        if pilihan_submenu == 5:
            topik = "pcr/puja/huruf/5"
            
        if pilihan_submenu == 0:
            menu(client)
            
    if pilihan_menu == 2:
        topik = "pcr/puja/pesan"
    
    if pilihan_menu == 3:
        if pilihan_submenu == 1:
            topik = "pcr/puja/lampu/cerah"
            
        if pilihan_submenu == 2:
            topik = "pcr/puja/lampu/redup"
            
        if pilihan_submenu == 3:
            topik = "pcr/puja/lampu/hidup"
            
        if pilihan_submenu == 4:
            topik = "pcr/puja/lampu/mati"
            
        if pilihan_submenu == 0:
            menu(client)
    
    if pilihan_menu == 4:
        if pilihan_submenu == 1:
            topik = "pcr/puja/gambar/senyum"
            
        if pilihan_submenu == 2:
            topik = "pcr/puja/gambar/sedih"
        
        if pilihan_submenu == 3:
            topik = "pcr/puja/gambar/indonesia"
        
        if pilihan_submenu == 4:
            topik = "pcr/puja/gambar/pelangi"
        
        if pilihan_submenu == 5:
            topik = "pcr/puja/gambar/heart"
            
        if pilihan_submenu == 0:
            menu(client)
    
    if pilihan_menu == 5:
        if pilihan_submenu == 1:
            topik = "pcr/puja/animasi/heartbeat"
        
        if pilihan_submenu == 2:
            topik = "pcr/puja/animasi/heartbreak"
            
        if pilihan_submenu == 3:
            topik = "pcr/puja/animasi/pacman"
        
        if pilihan_submenu == 4:
            topik = "pcr/puja/animasi/uburubur"
            
        if pilihan_submenu == 0:
            menu(client)
            
    if pilihan_menu == 6:
        if pilihan_submenu == 1:
            topik = "pcr/puja/sensor/suhu"
            
        if pilihan_submenu == 2:
            topik = "pcr/puja/sensor/tekanan"
            
        if pilihan_submenu == 3:
            topik = "pcr/puja/sensor/kelembaban"
            
        if pilihan_submenu == 0:
            menu(client)
    
    if pilihan_menu == 7:
        if pilihan_submenu == 1:
            topik = "pcr/puja/joystick/atas"
        
        if pilihan_submenu == 2:
            topik = "pcr/puja/joystick/bawah"
        
        if pilihan_submenu == 3:
            topik = "pcr/puja/joystick/kanan"
        
        if pilihan_submenu == 4:
            topik = "pcr/puja/joystick/kiri"
        
        if pilihan_submenu == 5:
            topik = "pcr/puja/joystick/tengah"
            
        if pilihan_submenu == 0:
            menu(client)
    
    if pilihan_menu == 0:
        topik = "pcr/puja/bersihkan"
    
    simpan(client, topik)
        
def simpan(client, topik):
    if topik not in berlangganan:        
        aksi = "berlangganan"
        pesan = "none"
        
        berlangganan.append(topik)
        logger.append([aksi, topik, pesan])
        
        print("")
        print("Berhasil berlangganan topik", topik)
        print("Harap tunggu, anda akan kembali ke menu dalam 3 detik!")
        
        time.sleep(3)
        menu(client)
    else:
        print("")
        print("Anda sebelumnya sudah berlangganan topik ini", topik)
        print("Harap tunggu, anda akan kembali ke menu dalam 3 detik!")
        
        time.sleep(3)
        menu(client)

def unduh(client):
    with open(file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Aksi', 'Topik', 'Pesan'])
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
        
def eksekusi(client):
    for langganan in berlangganan:
        topik = langganan
        subscribe(client, topik)
    
    client.loop_forever()
    
def eksekusi1(client):
    for langganan in berlangganan2:
        topik = langganan
        subscribe(client, topik)
    
    client.loop_forever()
     
if __name__ == '__main__':
    run()
