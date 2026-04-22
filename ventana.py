import tkinter as tk
from tkinter import messagebox
from conexion import conectar

INTERVALO_REFRESCO_MS = 1000  # Refresca cada 1 segundo


class ContadorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Turno actual")
        self.root.attributes("-topmost", True)
        self.root.geometry("260x160")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2e")

        self.conexion = conectar()
        if self.conexion is None:
            messagebox.showerror(
                "Error de conexión",
                "No se pudo conectar a la base de datos.\nVerificá el archivo .env"
            )
            self.root.destroy()
            return

        self.cursor = self.conexion.cursor()
        self._construir_ui()
        self._refrescar()

    def _construir_ui(self):
        # Etiqueta "Turno"
        tk.Label(
            self.root, text="TURNO", font=("Arial", 11, "bold"),
            bg="#1e1e2e", fg="#888899"
        ).pack(pady=(14, 0))

        # Número grande
        self.label_numero = tk.Label(
            self.root, text="—", font=("Arial", 52, "bold"),
            bg="#1e1e2e", fg="#ffffff", width=4
        )
        self.label_numero.pack()

        # Fila de botones
        frame_botones = tk.Frame(self.root, bg="#1e1e2e")
        frame_botones.pack(pady=(0, 10))

        btn_cfg = {"font": ("Arial", 14), "width": 3, "relief": "flat", "cursor": "hand2"}

        tk.Button(
            frame_botones, text="◀", bg="#3a3a5c", fg="#ffffff",
            command=self.retroceder, **btn_cfg
        ).grid(row=0, column=0, padx=6)

        tk.Button(
            frame_botones, text="▶", bg="#5865f2", fg="#ffffff",
            command=self.avanzar, **btn_cfg
        ).grid(row=0, column=1, padx=6)

        tk.Button(
            frame_botones, text="↺", bg="#3a3a5c", fg="#ffaa44",
            command=self.confirmar_reset, **btn_cfg
        ).grid(row=0, column=2, padx=6)

    def _obtener_numero(self):
        try:
            self.conexion.ping(reconnect=True)
            self.cursor = self.conexion.cursor()
            self.cursor.execute("SELECT numero FROM contador ORDER BY id DESC LIMIT 1")
            resultado = self.cursor.fetchone()
            return resultado[0] if resultado else 0
        except Exception as e:
            print(f"Error al leer: {e}")
            return None

    def _refrescar(self):
        numero = self._obtener_numero()
        if numero is not None:
            self.label_numero.config(text=str(numero))
        self.root.after(INTERVALO_REFRESCO_MS, self._refrescar)

    def _actualizar_numero(self, nuevo_numero):
        try:
            self.conexion.ping(reconnect=True)
            self.cursor = self.conexion.cursor()
            self.cursor.execute(
                "UPDATE contador SET numero = %s ORDER BY id DESC LIMIT 1",
                (nuevo_numero,)
            )
            self.conexion.commit()
            self.label_numero.config(text=str(nuevo_numero))
        except Exception as e:
            print(f"Error al actualizar: {e}")
            messagebox.showerror("Error", f"No se pudo actualizar el número:\n{e}")

    def avanzar(self):
        numero_actual = self._obtener_numero()
        if numero_actual is not None:
            self._actualizar_numero(numero_actual + 1)

    def retroceder(self):
        numero_actual = self._obtener_numero()
        if numero_actual is not None and numero_actual > 0:
            self._actualizar_numero(numero_actual - 1)

    def confirmar_reset(self):
        confirmado = messagebox.askyesno(
            "Resetear turno",
            "¿Reiniciar el contador a 0?\nEsto afecta a todas las PCs."
        )
        if confirmado:
            self._actualizar_numero(0)


if __name__ == "__main__":
    root = tk.Tk()
    app = ContadorApp(root)
    root.mainloop()
