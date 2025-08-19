class Room:
    def __init__(self, numar):
        self.numar = numar
        self.dispon = True
    def __str__(self):
        status = "Libera" if self.dispon else "Ocupata"
        return f"Camera {self.numar} - {status}"

class Hotel:
    def __init__(self):
        self.camere = []

    def add_room(self, numar):
        if isinstance(numar, Room):
            self.camere.append(numar)

    def check_in(self, numar_camera):
        for room in self.camere:
            if room.numar == numar_camera:
                if room.dispon:
                    room.dispon = False
                    print(f"Checkin complet pentru camera  {numar_camera}.")
                else:
                    print(f"Camera {numar_camera} este deja ocupata.")
                return
        print(f"Camera {numar_camera} nu exista in hotel.")

    def check_out(self, numar_camera):
        for room in self.camere:
            if room.numar == numar_camera:
                if not room.dispon:
                    room.dispon = True
                    print(f"Checkout complet pentru camera  {numar_camera}.")
                else:
                    print(f"Camera {numar_camera} este deja libera.")
                return
        print(f"Camera {numar_camera} nu existe in hotel.")

    def camere_dispon(self):
        disponibile = [room for room in self.camere if room.dispon]
        if not disponibile:
            print("Camera disponibile nu existe in hotel.")
        else:
            print("Camere disponibile:")
            for room in disponibile:
                print(f" - {room}")

if __name__ == "__main__":
    room1 = Room(1)
    room2 = Room(2)
    room3 = Room(3)

    hotel = Hotel()
    hotel.add_room(room1)
    hotel.add_room(room2)
    hotel.add_room(room3)

    hotel.camere_dispon()

    hotel.check_in(1)

    hotel.camere_dispon()




