# Actividad 3: Aplicación de Escritorio para Cifrado y Descifrado de Datos

---

## 📌 Información del Proyecto

* **Universidad:** Universidad de La Salle
* **Programa:** Maestría en Inteligencia Artificial
* **Asignatura:** Aplicaciones I
* **Estudiante:** Luis Norbey Correa Diaz
* **Docente:** Cristian Duney Bermúdez Quintero
* **Fecha:** Octubre de 2026

---

## 📝 Descripción General

Este proyecto consiste en el desarrollo de una aplicación de escritorio nativa en **Python** utilizando el framework gráfico **Tkinter**. La herramienta ofrece una interfaz intuitiva para el cifrado y descifrado seguro de datos numéricos de 6 dígitos mediante la combinación de operaciones aritméticas modulares y permutaciones posicionales.

El desarrollo fue diseñado siguiendo una arquitectura modular que separa la lógica de negocio de la capa de presentación (GUI), garantizando la mantenibilidad, escalabilidad y adherencia a los estándares de desarrollo profesional (PEP 8).

---

## 🏗️ Estructura Modular del Proyecto

En cumplimiento de las buenas prácticas de desarrollo de software y los requerimientos de la asignatura, el código se encuentra estructurado en módulos independientes dentro de una arquitectura limpia:

```text
ProyectoCifrado/
│
├── src/
│   ├── __pycache__          # Inicializador de paquetes de Python
│   ├── logica.py            # Algoritmos de cifrado y descifrado (Lógica de Negocio)
│   └── interfaz.py          # Interfaz gráfica de usuario y navegación (GUI)
│
├── app.py                  # Punto de entrada principal de la aplicación
└── README.md                # Documentación general del proyecto
```

---

## 💻 Requisitos del Sistema (Requirements)

A continuación se detallan los requerimientos de software necesarios para la ejecución del proyecto:

| Componente | Requisito Mínimo | Descripción |
| :--- | :--- | :--- |
| **Lenguaje** | Python `3.8+` | Entorno de ejecución principal |
| **Librería GUI** | Tkinter | Incluida de forma nativa en la biblioteca estándar de Python |
| **Sistema Operativo**| Windows 10/11, macOS, Linux | Plataforma cruzada compatible |


## 🚀 Guía de Instalación y Ejecución

Siga estos pasos para clonar, configurar el entorno virtual e iniciar la aplicación:

### 1. Clonar o descargar el repositorio
```bash
git clone https://github.com/Luchocorrea1/ProyectoCifrado.git
cd ProyectoCifrado
```

### 2. Crear y activar el Entorno Virtual (`venv`)

* **En Windows (PowerShell / CMD):**
  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```

* **En macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```


### 3. Ejecutar la aplicación
```bash
py [Version python] app.py

Ejemplo:

py -3.13 app.py
```

---

## 🔐 Descripción del Algoritmo

El sistema procesa estrictamente cadenas numéricas de 6 dígitos ($d_0, d_1, d_2, d_3, d_4, d_5$).

### 1. Cifrado
1. **Sustitución Aritmética Modular:** A cada dígito individual se le suma 7 y se calcula el residuo de la división entre 10:
   $$d_i' = (d_i + 7) \pmod{10}$$
2. **Permutación Posicional:** Se intercambian las posiciones de los dígitos según el siguiente patrón:
   * Posición $0 \longleftrightarrow$ Posición $2$
   * Posición $1 \longleftrightarrow$ Posición $3$
   * Posición $4 \longleftrightarrow$ Posición $5$

### 2. Descifrado
1. **Inversión de Permutación:** Se restauran las posiciones originales realizando los mismos intercambios ($0 \leftrightarrow 2$, $1 \leftrightarrow 3$, $4 \leftrightarrow 5$).
2. **Inversión Aritmética Modular:** Se aplica la operación aritmética inversa para recuperar los dígitos originales:
   $$d_i = (d_i' + 3) \pmod{10}$$

---

## ✨ Buenas Prácticas Aplicadas

* **Guía de Estilo PEP 8:** Convención de nombres (*snake_case* para métodos y variables, *PascalCase* para clases), tabulación consistente a 4 espacios y documentación mediante *docstrings*.
* **Programación Orientada a Objetos (POO):** Encapsulamiento de la lógica en la clase `CifradorLogica` e interfaz gestionada dinámicamente mediante `CifradorApp`.
* **Aislamiento de Entorno:** Uso de entornos virtuales para evitar la contaminación del entorno global de Python.
* **Manejo de Excepciones y Validaciones:** Validación de entradas de usuario para asegurar longitud y tipo de datos numéricos con alertas claras mediante cuadros de diálogo (`messagebox`).