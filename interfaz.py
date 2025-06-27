# Archivo: interfaz.py

import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

from hamming                import cotaHamming,             cotaHammingInversa,             cotaHammingCheck
from singleton              import cotaSingleton,           cotaSingletonInversa,           cotaSingletonCheck
from plotkin                import cotaPlotkin,             cotaPlotkinInversa,             cotaPlotkinCheck
from elias                  import cotaElias,               cotaEliasInversa,               cotaEliasCheck
from gilbert                import cotaGilbert,             cotaGilbertCheck
from johnsonRestringida     import cotaJohnsonRestringida,  cotaJohnsonRestringidaInversa,  cotaJohnsonRestringidaCheck
from johnsonNoRestringida   import cotaJohnsonNoRestringida,cotaJohnsonNoRestringidaInversa,cotaJohnsonNoRestringidaCheck


from validarParametros import validar

import sys, os



def resource_path(relative_path):
    """Ruta absoluta a un recurso, compatible con PyInstaller."""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)



def calcular():
    # Reinicia el color del resultado para cada intento
    label_resultado.config(fg="black")

    try:
        modo  = combo_opcion.get()
        cota  = combo_cota.get()
        n     = int(entry_n.get())
        q     = int(entry_q.get())

        # Lee d, M y w sólo cuando tocan
        d = M = w = None
        if modo in ("Calcular M", "Verificar código"):
            d = int(entry_d.get())
        if modo in ("Calcular d", "Verificar código"):
            M = int(entry_M.get())
        if cota in ("Johnson restringida", "Johnson no restringida"):
            w = int(entry_w.get())

        # --- validación común de parámetros -----------------
        validar(n=n, d=d, M=M, q=q)   # w se validará dentro de la rutina Johnson en el futuro


        if cota == "Comparación":
            if modo != "Calcular M":
                resultado.set("Para Comparación usa ‘Calcular M’")
                return

            valores = []
            # Hamming
            valores.append(("Hamming", cotaHamming(n, d, q)))
            # Singleton
            valores.append(("Singleton", cotaSingleton(n, d, q)))
            # Plotkin
            valores.append(("Plotkin", cotaPlotkin(n, d, q)))
            # Elias–Bassalygo
            valores.append(("Elias–Bassalygo", cotaElias(n, d, q)))
            # (Gilbert–Varshamov se omite)

            # sustituye None por +∞ para ordenar y filtrar luego
            valores = [(nom, val if val is not None else float("inf"))
                       for nom, val in valores]
            valores.sort(key=lambda x: x[1])

            texto = "\n".join(f"{nom}: {Mmax}" for nom, Mmax in valores
                              if Mmax != float("inf"))
            resultado.set(texto)
            return

        if cota == "Hamming":
            if modo == "Calcular M":
                Mmax = cotaHamming(n, d, q)
                resultado.set(f"M ≤ {Mmax}")
            elif modo == "Calcular d":
                dmax = cotaHammingInversa(n, M, q)
                resultado.set(f"d ≤ {dmax}")
            else:
                cumple, Mmax = cotaHammingCheck(n, d, q, M)
                resultado.set(f"M ≤ {Mmax}.\n Código tiene M = {M} {' no excede la cota.' if cumple else ' excede la cota.'}")

        elif cota == "Singleton":
            if modo == "Calcular M":
                Mmax = cotaSingleton(n, d, q)
                resultado.set(f"M ≤ {Mmax}")
            elif modo == "Calcular d":
                dmax = cotaSingletonInversa(n, M, q)
                resultado.set(f"d ≤ {dmax}")
            else:
                cumple, Mmax = cotaSingletonCheck(n, d, q, M)
                resultado.set(f"M ≤ {Mmax}.\n Código tiene M = {M} {' no excede la cota.' if cumple else ' excede la cota.'}")

        elif cota == "Plotkin":
            if modo == "Calcular M":
                Mmax = cotaPlotkin(n, d, q)
                resultado.set(f"M ≤ {Mmax}")
            elif modo == "Calcular d":
                dmax = cotaPlotkinInversa(n, M, q)
                resultado.set(f"d ≤ {dmax}")
            else:
                cumple, Mmax = cotaPlotkinCheck(n, d, q, M)
                resultado.set(f"M ≤ {Mmax}.\n Código tiene M = {M} {' no excede la cota.' if cumple else ' excede la cota.'}")

        elif cota == "Elias":
            if modo == "Calcular M":
                Mmax = cotaElias(n, d, q)
                resultado.set(f"M ≤ {Mmax}")
            elif modo == "Calcular d":
                dmax = cotaEliasInversa(n, M, q)
                resultado.set(f"d ≤ {dmax}")
            else:
                cumple, Mmax = cotaEliasCheck(n, d, q, M)
                resultado.set(f"M ≤ {Mmax}.\n Código tiene M = {M} {' no excede la cota.' if cumple else ' excede la cota.'}")
        
        elif cota == "Johnson restringida":
            if modo == "Calcular M":
                Mmax = cotaJohnsonRestringida(n, d, w, q)
                resultado.set(f"M ≤ {Mmax}")
            elif modo == "Calcular d":
                dmax = cotaJohnsonRestringidaInversa(n, M, w, q)
                resultado.set(f"d ≤ {dmax}")
            else:
                cumple, Mmax = cotaJohnsonRestringidaCheck(n, d, w, q, M)
                resultado.set(f"M ≤ {Mmax}.\n Código tiene M = {M} {' no excede la cota.' if cumple else ' excede la cota.'}")
                
        elif cota == "Johnson no restringida":
            if modo == "Calcular M":
                Mmax = cotaJohnsonNoRestringida(n, d, w, q)
                resultado.set(f"M ≤ {Mmax}")
            elif modo == "Calcular d":
                dmax = cotaJohnsonNoRestringidaInversa(n, M, w, q)
                resultado.set(f"d ≤ {dmax}")
            else:
                cumple, Mmax = cotaJohnsonNoRestringidaCheck(n, d, w, q, M)
                resultado.set(f"M ≤ {Mmax}.\n Código tiene M = {M} {' no excede la cota.' if cumple else ' excede la cota.'}")

        # --- Johnson (sólo mensaje por ahora) ----------------
        elif cota in ("Johnson general"):
            resultado.set("Cota Johnson aún no implementada")

        else:
            resultado.set("Cota aún no implementada")


    except ValueError as e:
        resultado.set(str(e))
        label_resultado.config(fg="red")
        # messagebox.showerror("Error", str(e))  # opcional



root = tk.Tk()
root.title("Calculadora de cotas de códigos")
root.geometry("900x560")  # un poco más alta para el nuevo campo

main = tk.Frame(root)
main.pack(fill="both", expand=True)

# imagen lateral
img = Image.open(resource_path("logoPrograma.png"))
img = img.resize((300, 400), Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(img)
tk.Label(main, image=photo).grid(row=0, column=0, padx=20, pady=20)

# formulario
form = tk.Frame(main)
form.grid(row=0, column=1, sticky="n", padx=20, pady=20)

tk.Label(form, text="Selecciona una cota:").pack()
combo_cota = ttk.Combobox(
    form,
    values=[
        "Hamming",
        "Singleton",
        "Plotkin",
        "Elias–Bassalygo",
        "Gilbert–Varshamov",
        "Johnson restringida",
        "Johnson no restringida",
        "Johnson general",
        "Comparación",
    ],
)
combo_cota.set("Hamming")
combo_cota.pack(pady=5)

tk.Label(form, text="¿Qué deseas hacer?").pack()
combo_opcion = ttk.Combobox(
    form,
    values=[
        "Calcular M",
        "Calcular d",
        "Verificar código",
        "Comparación",  # fuerza el modo apropiado en la UI
    ],
)
combo_opcion.set("Calcular M")
combo_opcion.pack(pady=5)


def actualizar_campos(event=None):
    """Habilita o deshabilita M/d/w según la opción y la cota."""
    modo = combo_opcion.get()
    cota_act = combo_cota.get()

    # n y q siempre habilitados
    entry_n.config(state="normal")
    entry_q.config(state="normal")

    # --- d y M ------------------------------------------------
    entry_d.config(state="normal")
    entry_M.config(state="normal")
    if modo == "Calcular M":
        entry_M.delete(0, tk.END)
        entry_M.config(state="disabled")
    elif modo == "Calcular d":
        entry_d.delete(0, tk.END)
        entry_d.config(state="disabled")
    elif modo == "Comparación":
        entry_M.delete(0, tk.END)
        entry_M.config(state="disabled")

    # --- w ----------------------------------------------------
    if cota_act in ("Johnson restringida", "Johnson no restringida"):
        entry_w.config(state="normal")
    else:
        entry_w.delete(0, tk.END)
        entry_w.config(state="disabled")


# Activar la lógica tanto al cambiar “modo” como al cambiar “cota”
combo_opcion.bind("<<ComboboxSelected>>", actualizar_campos)
combo_cota.bind("<<ComboboxSelected>>", actualizar_campos)

# entradas de datos
tk.Label(form, text="n:").pack()
entry_n = tk.Entry(form)
entry_n.pack()

tk.Label(form, text="d:").pack()
entry_d = tk.Entry(form)
entry_d.pack()

tk.Label(form, text="q:").pack()
entry_q = tk.Entry(form)
entry_q.pack()

tk.Label(form, text="w:").pack()
entry_w = tk.Entry(form)
entry_w.pack()

tk.Label(form, text="M:").pack()
entry_M = tk.Entry(form)
entry_M.pack()

# botón y etiqueta de resultados
tk.Button(form, text="Calcular", command=calcular).pack(pady=10)
resultado = tk.StringVar()
label_resultado = tk.Label(form, textvariable=resultado, font=("Arial", 12), justify="left")
label_resultado.pack()

actualizar_campos()  # estado inicial de las entradas
root.mainloop()
