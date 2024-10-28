from phone.contact import Contact  # Asegúrate de que la ruta sea correcta según tu estructura de carpetas

class Directory:
    """
    Clase Directorio que gestiona los contactos.
    """

    def __init__(self):
        # Inicializa la matriz con el encabezado
        self.contactos = [
            ["Nombre", "Apellido", "Organización", "Teléfono", "Dirección"]
        ]

    def add_contact(self, nombre, apellido, organizacion, telefono, direccion):
        """Agrega un nuevo contacto a la matriz."""
        nuevo_contacto = Contact(nombre, apellido, organizacion, telefono, direccion)
        self.contactos.append(nuevo_contacto.obtener_datos())

    def list_contacts(self):
        """Muestra todos los contactos en la matriz, incluyendo el encabezado."""
        for fila in self.contactos:
            print("|", " | ".join(fila), "|")
        print("|" + "----------|" * len(self.contactos[0]))
