# DHCP Starvation Attack – Scapy

## 👨‍🎓 Autor
Nombre: Stephan Cedano Sanchez
Matrícula: 2024-1404  

---

## Video demostrativo

[Ver video demostrativo] 

---

## 🎯 Objetivo

Crear un programa en Python usando la librería Scapy que permita simular, dentro de un laboratorio controlado, un ataque de tipo DHCP Starvation. El objetivo es evidenciar cómo un atacante puede consumir todas las direcciones IP disponibles del servidor DHCP hasta dejarlo sin capacidad de asignarlas a los clientes legítimos.

---

## 🖥 Topología del Laboratorio 

- Router: R1  
- Switch: SW1  
- Host Atacante: Ubuntu Server  
- Host Víctima: Windows 10  
- Red basada en matrícula  

Red utilizada:  
202.4.14.0/24 

--- 

### Direccionamiento 

- Default gateway 202.4.14.1
- PC ubuntu server 202.4.14.2
- PC Window 202.4.14.3

  ---

### Diagrama de Topología
![Diagrama de Topología] (Topologia.png)






---

## ⚙ Requisitos

- Python 3  
- Scapy  
- Permisos root  
- Entorno virtualizado (VMware / PnetLab)  

---

## 🔧 Instalación de Scapy

```bash
pip install scapy
```

---

## 🚀 Ejecución del Script

Desde la máquina atacante (Kali Linux):

```bash
sudo python3 starvation.py 
```

---

## 🔍 Funcionamiento del Script

El script genera múltiples direcciones MAC aleatorias y envía paquetes DHCP Discover al servidor DHCP.

Cada solicitud simula un cliente diferente dentro de la red.

El servidor DHCP responde asignando direcciones IP hasta que el pool disponible se agota.

Cuando el pool se llena, los dispositivos legítimos ya no pueden obtener una dirección IP válida, provocando una denegación de servicio (DoS).

---

## 📊 Resultados Obtenidos

- Se enviaron múltiples solicitudes DHCP Discover.
- El servidor asignó direcciones IP a clientes falsos.
- El pool DHCP se saturó.
- El equipo víctima no pudo obtener dirección IP.

---

## 🛡 Medidas de Mitigación

Para prevenir este tipo de ataque se pueden implementar:

- DHCP Snooping
- Port Security en switches
- Limitación de solicitudes DHCP por puerto
- Monitoreo de tráfico anómalo
- Segmentación de red

---

⚠ Este laboratorio fue realizado únicamente en un entorno controlado con fines académicos.
