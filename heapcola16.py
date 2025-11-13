from heap import HeapMax

# Creamos la cola de impresión (cola de prioridad)
cola = HeapMax()

# Cargamos tres documentos de empleados (prioridad 1)
cola.arrive("Documento_empleado1", 1)
cola.arrive("Documento_empleado2", 1)
cola.arrive("Documento_empleado3", 1)

# Mostramos el contenido de la cola
print("Cola actual:")
print(cola.elements)

# Punto b. imprimir el primer documento de la cola (solo el nombre)
prioridad, doc = cola.elements[0]
print("El primer documento de la cola: ", doc)


# Punto c. carga dos documentos del staff de TI (prioridad 2)
cola.arrive("Documento_TI1", 2)
cola.arrive("Documento_TI2", 2)

print("Cola despues de agregar 2 documentos de staff TI")
print(cola.elements)

# punto d. carga un documento para gerente
cola.arrive("Documento_gerente1", 3)
print("Cola agregando un gerente: ")
print(cola.elements)

#punto e. imprime los dos primeros doc
print("primeros dos documentos de la cola")

if cola.size() > 0:
    prioridad1, doc1 = cola.elements[0]
    print("1-", doc1, " prioridad ", prioridad1)

if cola.size() > 1:
    prioridad2, doc2 = cola.elements[1]
    print("2-", doc2, " prioridad ", prioridad2)

# punto f. carga dos documentos de empleados y uno de gerente.
cola.arrive("Documento_empleado4", 1)
cola.arrive("Documento_empleado5", 1)
cola.arrive("Documento_gerente2", 3)

print("cola luego de agregar dos documentos de empleado y uno de gerente:")
print(cola.elements)

#punto g. imprime todos los documentos de la cola de impresión.
print("Todos los documentos en la cola de impresión:")
for prioridad, doc in cola.elements:
    print(" - ", doc, " prioridad ", prioridad)