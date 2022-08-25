from fpdf import FPDF
import os

# Primero, extraemos todos los nombres de las imágenes contenidas en una carpeta

f = []
for (dirpath, dirnames, filenames) in walk("Aqui va la ruta de la carpeta que contiene todas las imágenes separando con \\"):
    f.extend(filenames)
    break

# Después, con el ciclo for iteramos a través de todos los nombres de archivos que extraimos para generar para cada imagen su respectivo pdf

for image in sorted(f):
    pdf = FPDF()
    pdf.add_page()
    pdf.image("Ruta de la carpeta donde deseamos guardar los pdf separando con \\" + image, w=190, h=240)
    nombre=image+".pdf"
    pdf.output(nombre, "F")
