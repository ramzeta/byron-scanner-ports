
#https://fsymbols.com/es/generadores/

print()
print("  ")
print("  ██████╗░██╗░░░██╗██████╗░░█████╗░███╗░░██╗░██████╗░█████╗░░█████╗░███╗░░██╗███╗░░██╗███████╗██████╗░")
print("  ██╔══██╗╚██╗░██╔╝██╔══██╗██╔══██╗████╗░██║██╔════╝██╔══██╗██╔══██╗████╗░██║████╗░██║██╔════╝██╔══██╗")
print("  ██████╦╝░╚████╔╝░██████╔╝██║░░██║██╔██╗██║╚█████╗░██║░░╚═╝███████║██╔██╗██║██╔██╗██║█████╗░░██████╔╝")
print("  ██╔══██╗░░╚██╔╝░░██╔══██╗██║░░██║██║╚████║░╚═══██╗██║░░██╗██╔══██║██║╚████║██║╚████║██╔══╝░░██╔══██╗")
print("  ██████╦╝░░░██║░░░██║░░██║╚█████╔╝██║░╚███║██████╔╝╚█████╔╝██║░░██║██║░╚███║██║░╚███║███████╗██║░░██║")
print("  ╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝")
print()

print("[Info] Herramienta para escanear los puertos abiertos en una dirección IP")




import nmap3
nmap = nmap3.Nmap()
ip=input("[+] IP Objetivo ==> ")
# Esto es equivalente a nmap -oX - nmmapper.com -O
os_results = nmap.nmap_os_detection(ip) # Ejecutar como administrador
print(os_results)