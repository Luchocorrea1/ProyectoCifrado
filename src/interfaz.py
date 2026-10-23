import tkinter as tk
from tkinter import messagebox
from src.logica import CifradorLogica


class CifradorApp:
    """Clase principal que gestiona la interfaz gráfica y la navegación de ventanas."""

    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación de Cifrado y Descifrado")
        self.root.geometry("450x350")
        self.root.resizable(False, False)

        # Configuración de estilo básico
        self.font_title = ("Helvetica", 14, "bold")
        self.font_text = ("Helvetica", 10)
        self.font_btn = ("Helvetica", 10, "bold")

        # Ventana principal por defecto
        self.crear_ventana_principal()

    def limpiar_ventana(self):
        """Elimina todos los widgets de la ventana actual."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def crear_ventana_principal(self):
        """Construye la Ventana Principal con información del estudiante y navegación."""
        self.limpiar_ventana()

        frame = tk.Frame(self.root)
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        lbl_titulo = tk.Label(
            frame,
            text="Sistema de Cifrado de Datos",
            font=self.font_title,
            fg="#1A365D",
        )
        lbl_titulo.pack(pady=(0, 15))

        lbl_autor = tk.Label(
            frame,
            text="Autor: Luis Norbey Correa Diaz\n"
            "Asignatura: Aplicaciones I\n"
            "Maestría en Inteligencia Artificial\n"
            "Universidad de La Salle",
            font=self.font_text,
            justify="center",
        )
        lbl_autor.pack(pady=(0, 25))

        btn_cifrar = tk.Button(
            frame,
            text="Ir a Cifrado de Datos",
            font=self.font_btn,
            bg="#2B6CB0",
            fg="white",
            width=25,
            height=2,
            command=self.crear_ventana_cifrado,
        )
        btn_cifrar.pack(pady=5)

        btn_descifrar = tk.Button(
            frame,
            text="Ir a Descifrado de Datos",
            font=self.font_btn,
            bg="#2C7A7B",
            fg="white",
            width=25,
            height=2,
            command=self.crear_ventana_descifrar,
        )
        btn_descifrar.pack(pady=5)

    def crear_ventana_cifrado(self):
        """Ventana para ingresar y cifrar un número de 6 dígitos."""
        self.limpiar_ventana()

        frame = tk.Frame(self.root)
        frame.pack(expand=True, fill="both", padx=20, pady=20)

        lbl_titulo = tk.Label(
            frame, text="Módulo de Cifrado", font=self.font_title, fg="#2B6CB0"
        )
        lbl_titulo.pack(pady=(0, 15))

        lbl_instruccion = tk.Label(
            frame,
            text="Ingrese un número entero de 6 dígitos:",
            font=self.font_text,
        )
        lbl_instruccion.pack(pady=5)

        entry_num = tk.Entry(frame, font=("Helvetica", 12), justify="center")
        entry_num.pack(pady=5)

        lbl_resultado = tk.Label(
            frame, text="Número cifrado: ---", font=("Helvetica", 11, "bold")
        )
        lbl_resultado.pack(pady=15)

        def procesar_cifrado():
            val = entry_num.get().strip()
            if len(val) == 6 and val.isdigit():
                res = CifradorLogica.cifrar_numero(val)
                lbl_resultado.config(
                    text=f"Número cifrado: {res}", fg="#2B6CB0"
                )
            else:
                messagebox.showerror(
                    "Error de Entrada",
                    "Debe ingresar exactamente un número entero de 6 dígitos.",
                )

        btn_procesar = tk.Button(
            frame,
            text="Cifrar",
            font=self.font_btn,
            bg="#2B6CB0",
            fg="white",
            width=15,
            command=procesar_cifrado,
        )
        btn_procesar.pack(pady=5)

        btn_volver = tk.Button(
            frame,
            text="Volver al Menú Principal",
            font=self.font_text,
            command=self.crear_ventana_principal,
        )
        btn_volver.pack(pady=(15, 0))

    def crear_ventana_descifrar(self):
        """Ventana para ingresar un número cifrado y recuperar el original."""
        self.limpiar_ventana()

        frame = tk.Frame(self.root)
        frame.pack(expand=True, fill="both", padx=20, pady=20)

        lbl_titulo = tk.Label(
            frame,
            text="Módulo de Descifrado",
            font=self.font_title,
            fg="#2C7A7B",
        )
        lbl_titulo.pack(pady=(0, 15))

        lbl_instruccion = tk.Label(
            frame, text="Ingrese el número cifrado (6 dígitos):", font=self.font_text
        )
        lbl_instruccion.pack(pady=5)

        entry_num = tk.Entry(frame, font=("Helvetica", 12), justify="center")
        entry_num.pack(pady=5)

        lbl_resultado = tk.Label(
            frame, text="Número original: ---", font=("Helvetica", 11, "bold")
        )
        lbl_resultado.pack(pady=15)

        def procesar_descifrado():
            val = entry_num.get().strip()
            if len(val) == 6 and val.isdigit():
                res = CifradorLogica.descifrar_numero(val)
                lbl_resultado.config(
                    text=f"Número original: {res}", fg="#2C7A7B"
                )
            else:
                messagebox.showerror(
                    "Error de Entrada",
                    "Debe ingresar exactamente un número entero de 6 dígitos.",
                )

        btn_procesar = tk.Button(
            frame,
            text="Descifrar",
            font=self.font_btn,
            bg="#2C7A7B",
            fg="white",
            width=15,
            command=procesar_descifrado,
        )
        btn_procesar.pack(pady=5)

        btn_volver = tk.Button(
            frame,
            text="Volver al Menú Principal",
            font=self.font_text,
            command=self.crear_ventana_principal,
        )
        btn_volver.pack(pady=(15, 0))