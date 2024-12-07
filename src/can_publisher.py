#!/usr/bin/env python3
from pprint import pprint

import can
import rospy
from msg import Can_msg


def convert(bits):
    return bits.zfill(8)


def process_0x424(data):
    return {
        "Alerta_CintoC": bool(int(data[0][1])),
        "Alerta_CintoP": bool(int(data[0][0])),
        "Porta_Condutor": bool(int(data[2][6])),
        "Porta_Outras": bool(int(data[2][7])),
        "ParaBrisas_Frente": bool(int(data[1][4])),
        "ParaBrisas_Atras": bool(int(data[1][3])),
        "Pisca_Esq": bool(int(data[1][6])),
        "Pisca_Dir": bool(int(data[1][7])),
        "Medios": bool(int(data[1][1])),
        "Maximos": bool(int(data[1][2])),
    }


def process_0x3A4(data):
    return {
        "Temperatura_AC": int(data[0][7])
        + int(data[0][6]) * 2
        + int(data[0][5]) * 4
        + int(data[0][4]) * 8,
        "Intensidade_AC": int(data[1][7])
        + int(data[1][6]) * 2
        + int(data[1][5]) * 4
        + int(data[1][4]) * 8,
        "Btn_Tmax": bool(int(data[0][2])),
        "Btn_Solf": bool(int(data[0][1])),
        "Btn_Imax": bool(int(data[0][0])),
    }


def process_0x412(data):
    return {
        "Velocidade": data[1],
        "Contador_Km": (data[2] * 65536) + (data[3] * 256) + data[4],
    }


def process_0x418(data):
    mudanca_map = {0x50: "Park", 0x52: "Reverse", 0x4E: "Neutral", 0x44: "Foward"}
    return {"Mudanca": mudanca_map.get(data[0], "Nada")}


def process_0x346(data):
    return {"AutonomiaKm": data[7]}


def process_0x374(data):
    return {"AutonomiaPerc": (data[1] - 10) / 2}


def process_0x373(data):
    estado_bateria = (((data[2]) * 256) + (data[3] - 128) * 128) / 100
    return {"Carregador": estado_bateria < 0}


def main():
    bustype = "socketcan"
    channel = "can0"
    bitrate = 500000

    pub = rospy.Publisher("can_messages", Can_msg, queue_size=10)
    rospy.init_node("can_node", anonymous=True)

    process_map = {
        hex(0x424): process_0x424,
        hex(0x3A4): process_0x3A4,
        hex(0x412): process_0x412,
        hex(0x418): process_0x418,
        hex(0x346): process_0x346,
        hex(0x374): process_0x374,
        hex(0x373): process_0x373,
    }

    while not rospy.is_shutdown():
        try:
            bus = can.interface.Bus(channel=channel, interface=bustype, bitrate=bitrate)
            message = bus.recv()
            if message and len(message.data) > 0:
                id = hex(message.arbitration_id)
                data = [convert(bin(byte)[2:]) for byte in message.data]
                if id in process_map:
                    result = process_map[id](data)
                    pprint(result)

                    msg = Can_msg()
                    msg.autonomia_perc = int(result.get("AutonomiaPerc", 0))
                    msg.autonomia_km = int(result.get("AutonomiaKm", 0))
                    msg.contador_km = int(result.get("Contador_Km", 0))
                    msg.velocidade = int(result.get("Velocidade", 0))
                    msg.temperatura_ac = int(result.get("Temperatura_AC", 0))
                    msg.intensidade_ac = int(result.get("Intensidade_AC", 0))
                    msg.mudanca = str(result.get("Mudanca", "Nada"))
                    msg.porta_condutor = bool(result.get("Porta_Condutor", False))
                    msg.porta_outras = bool(result.get("Porta_Outras", False))
                    msg.parabrisas_frente = bool(result.get("ParaBrisas_Frente", False))
                    msg.parabrisas_atras = bool(result.get("ParaBrisas_Atras", False))
                    msg.btn_tmax = bool(result.get("Btn_Tmax", False))
                    msg.btn_imax = bool(result.get("Btn_Imax", False))
                    msg.alerta_cintop = bool(result.get("Alerta_CintoP", False))
                    msg.alerta_cintoc = bool(result.get("Alerta_CintoC", False))
                    msg.pisca_dir = bool(result.get("Pisca_Dir", False))
                    msg.pisca_esq = bool(result.get("Pisca_Esq", False))
                    msg.medios = bool(result.get("Medios", False))
                    msg.maximos = bool(result.get("Maximos", False))
                    msg.carregador = bool(result.get("Carregador", False))

                    pub.publish(msg)
        except Exception as e:
            rospy.logerr(f"Error: {e}")


if __name__ == "__main__":
    main()
