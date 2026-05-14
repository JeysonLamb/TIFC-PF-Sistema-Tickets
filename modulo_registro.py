tickets = {}

def registrar_ticket(descripcion, prioridad):

    # Validar descripción
    if descripcion.strip() == "":
        print("La descripción no puede estar vacía")
        return

    # Generar ID automático
    numero = len(tickets) + 1
    id_ticket = f"T-{numero:03}"

    # Crear ticket
    ticket = {
        "descripcion": descripcion,
        "prioridad": prioridad,
        "estado": "Abierto"
    }

    # Guardar en el diccionario
    tickets[id_ticket] = ticket

    print("Ticket registrado:", id_ticket)
   