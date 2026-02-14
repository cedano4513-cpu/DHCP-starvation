# DHCP Starvation Attack – Scapy

## 👨‍🎓 Autor
Nombre: Stephan Cedano Sanchez
Matrícula: 2024-1404  

---

## Video demostrativo

[Ver video demostrativo] (https://youtu.be/XlFxx-4FgPU)

---

## 🎯 Objetivo

Crear un programa en Python usando la librería Scapy que permita simular, dentro de un laboratorio controlado, un ataque de tipo DHCP Starvation. El objetivo es evidenciar cómo un atacante puede consumir todas las direcciones IP disponibles del servidor DHCP hasta dejarlo sin capacidad de asignarlas a los clientes legítimos.

---

## 🖥 Topología del Laboratorio 

- Router: R1  
- Switch: SW1  
- Host Atacante: Ubuntu Server  
- Host Víctima: router  
- Red basada en matrícula  

Red utilizada:  
202.4.14.0/24 

--- 

### Direccionamiento 

- Default gateway 202.4.14.1
- PC ubuntu server 202.4.14.2
- PC Window 202.4.14.3

  ---






---

## ⚙ Requisitos

- Python   
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

Desde la máquina atacante (ubuntu server):

```bash
sudo python dhcp_starvation.py 
```

---

## 🔍 Funcionamiento del Script

El programa crea varias direcciones MAC falsas de manera aleatoria y envía solicitudes DHCP Discover al servidor DHCP.
Cada petición aparenta provenir de un equipo distinto dentro de la red.
El servidor comienza a entregar direcciones IP a estas supuestas máquinas hasta que se terminan las disponibles en su rango de asignación.
Una vez agotado el pool, los equipos reales no logran recibir una IP válida, lo que ocasiona una interrupción del servicio (ataque de denegación de servicio o DoS).

---

## 📊 Resultados Obtenidos

-Se generaron numerosas peticiones DHCP Discover.

-El servidor comenzó a otorgar direcciones IP a equipos simulados.

-El rango de direcciones disponible en el DHCP se llenó.

-El equipo legítimo no consiguió recibir una dirección IP.

---

## 🛡 Medidas de Mitigación

Para evitar este tipo de incidente pueden aplicarse las siguientes prácticas:

-Activar DHCP Snooping.

-Configurar seguridad de puertos (Port Security) en los switches.

-Establecer un límite de solicitudes DHCP por cada puerto.

-Vigilar el tráfico en busca de comportamientos inusuales.


