def cerrar_ticket(tickets, ticket_id):
    for ticket in tickets:

        if ticket["id"] == ticket_id:

            if ticket["estado"] == "Abierto":
                ticket["estado"] = "Cerrado"
                print("✅ Ticket cerrado correctamente")

            else:
                print("⚠️ El ticket ya estaba cerrado")

            return

    print("❌ Ticket no encontrado")


def reporte(tickets):
    abiertos = 0
    cerrados = 0

    for ticket in tickets:

        if ticket["estado"] == "Abierto":
            abiertos += 1

        elif ticket["estado"] == "Cerrado":
            cerrados += 1

    total = abiertos + cerrados

    print("\n📊 REPORTE DE TICKETS")
    print(f"Tickets abiertos: {abiertos}")
    print(f"Tickets cerrados: {cerrados}")
    print(f"Total tickets: {total}")
