class Order:
    def __init__(self, qtty, customer):
        self.customer = customer
        self.qtty = qtty

    def print_order(self):
        print(f" Cliente: {self.get_customer()}")
        print(f" Cantidad: {self.get_qtty()}")
        print(" ------------")

    def get_qtty(self):
        return self.qtty

    def get_customer(self):
        return self.customer


class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

    def get_next(self):
        return self.next

    def set_next(self, next_node):
        self.next = next_node


class Queue:
    def __init__(self):
        self.top = None   #Cabeza de la cola
        self.tail = None  #Final de la cola
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def front(self):
        if self.is_empty():
            return None
        return self.top.info

    def enqueue(self, info):
        new_node = Node(info)
        if self.is_empty():
            self.top = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        
        info = self.top.info
        self.top = self.top.get_next()
        self._size -= 1
        
        if self.top is None:
            self.tail = None
            
        return info

    def print_info(self):
        print("------ QUEUE DUMP ------")
        print(f"Tamaño: {self.size()}")
        
        node = self.top
        count = 1
        while node is not None:
            print(f"* Elemento {count}")
            node.info.print_order()
            node = node.get_next()
            count += 1
            
        print("-----------------------")

    def get_nth(self, pos):
        if pos < 1 or pos > self.size():
            return None
            
        node = self.top
        for _ in range(1, pos):
            node = node.get_next()
            
        return node.info


#Probar el Queue 
if __name__ == "__main__":
    cola = Queue()

    print("--- Agregar 3 Pedidos ---")
    cola.enqueue(Order(20, "cust1"))
    cola.print_info()

    cola.enqueue(Order(30, "cust2"))
    cola.print_info()

    cola.enqueue(Order(40, "cust3"))
    cola.print_info()

    print("\n--- Probando el FRONT ---")
    frente = cola.front()
    if frente:
        print("Elemento en el frente:")
        frente.print_order()

    print("\n--- Probando el DEQUEUE ---")
    extraido = cola.dequeue()
    if extraido:
        print("Elemento extraído:")
        extraido.print_order()
    cola.print_info()

    print("\n--- Prueba de GET_NTH de 4 elementos ---")
    cola_nth = Queue()
    cola_nth.enqueue(Order(10, "cliente_A"))
    cola_nth.enqueue(Order(20, "cliente_B"))
    cola_nth.enqueue(Order(30, "cliente_C"))
    cola_nth.enqueue(Order(40, "cliente_D"))
    
    cola_nth.print_info()
    
    tercero = cola_nth.get_nth(3)
    if tercero:
        print("El tercer elemento es:")
        tercero.print_order()
    else:
        print("\nPosición no válida")