nro_ejercicio = input("\nNro. de ejercicio a ejecutar ( 1 - 10): ")
while not nro_ejercicio.isdigit() or not (int(nro_ejercicio) >= 1 and int(nro_ejercicio) <= 10):  
    nro_ejercicio= input("Nro. de ejercicio a ejecutar (1 - 10): ")

match nro_ejercicio: 
    case "1":

        print(f"\nEjercicio #1:\n")
        print("""\n""")
    case "2":

        print(f"\nEjercicio #2:\n")
        print("""\n""")
    case "3":
        
        print(f"\nEjercicio #3:\n")
        print("""\n""")
    case "4":

        print(f"\nEjercicio #4:\n")
        print("""\n""")
    case "5":

        print(f"\nEjercicio #5:\n")
        print("""\n""")
    case "6":
        
        print(f"\nEjercicio #6:\n")
        print("""\n""")
    case "7":

        print(f"\nEjercicio #7:\n")
        print("""\n""")
    case "8":
        
        print(f"\nEjercicio #8:\n")
        print("""\n""")
    case "9":
        
        print(f"\nEjercicio #9:\n")
        print("""\n""")
    case _:
        
        print(f"\nEjercicio #10:\n")
        print("""\n""")