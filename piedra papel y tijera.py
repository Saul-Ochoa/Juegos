import random
while True:
    aleatorio=random.randrange(1,3)
    elije_pc=""
    print("Piedra=1")
    print("Tijera=2")
    print("Papel=3")
    opcion=int(input("Elige una opcion :"))
    
    
    if opcion==1:
        usuario_elije="Piedra"
    elif opcion==2:
        usuario_elije="Papel"
    elif opcion==3:
        usuario_elije="Tijera"
    print("Elegiste :",usuario_elije)
    
    if aleatorio==1:
        elije_pc="Piedra"
    elif aleatorio==2:
        elije_pc="Papel"
    elif aleatorio==3:
        elije_pc="Tijera"
    print("La maquina eligio :",elije_pc)
    
    if elije_pc=="Piedra" and usuario_elije=="Papel":
        print("Ganastes")
    if elije_pc=="Papel" and usuario_elije=="Tijera":
        print("Ganastes")
    if elije_pc=="Tijeras" and usuario_elije=="Piedra":
        print("Ganastes")
    if elije_pc=="Papel" and usuario_elije=="Piedra":
        print("Perdistes")
    if elije_pc=="Tijera" and usuario_elije=="Papel":
        print("Perdistes")
    if elije_pc=="Piedra" and usuario_elije=="Tijera":
        print("Perdistes")
    if elije_pc==usuario_elije:
        print("Empate")
    
    jugar_denuevo=input("Quieres jugar otra vez (si/no):")
    if jugar_denuevo.lower()!="si":
        break