import tkinter as tk
from conexion import conectar

class ContadorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contador")
        self.root.attributes("-topmost", True)
        self.root.geometry("200x100")
        self.root.resizable(False, False)

        self.conexion =conectar()
        if self.conexion is None:
            print("Error de conexión")
            self.root.destroy()
            return
        
        self.cursor = self.conexion.cursor()
        self.numero = self.obtener_numero()

        self.label = tk.Label(root, text=f"{self.numero}", font=("Arial", 24))
        self.label.pack(pady=5)

        self.boton_incrementar = tk.Button(root, text ="▶", command=self.incrementar, font=("Arial", 14))
        self.boton_incrementar.pack()
    
    def obtener_numero(self):
        self.cursor.execute("SELECT numero FROM contador ORDER BY ID DESC LIMIT 1")
        resultado = self.cursor.fetchone()
        return resultado[0] if resultado else 0
    
    def incrementar(self):
        self.numero += 1
        self.label.config(text=f"{self.numero}")
        self.cursor.execute("UPDATE contador SET numero = %s ORDER BY ID DESC LIMIT 1", (self.numero,))
        self.conexion.commit()

if __name__ == "__main__":
    root = tk.Tk()
    app = ContadorApp(root)
    root.mainloop()