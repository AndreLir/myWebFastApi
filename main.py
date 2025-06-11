from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json
import os

app = FastAPI()

# Static files (CSS/JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Archivo JSON donde se guardan los libros
LIBROS_FILE = "libros.json"

# Leer libros desde el archivo JSON
def leer_libros():
    if not os.path.exists(LIBROS_FILE):
        return []
    with open(LIBROS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

# Guardar libros en el archivo JSON
def guardar_libros(libros):
    with open(LIBROS_FILE, "w", encoding="utf-8") as f:
        json.dump(libros, f, ensure_ascii=False, indent=2)

@app.get("/libros", response_class=HTMLResponse)
def formulario_libros(request: Request):
    libros = leer_libros()
    return templates.TemplateResponse("libros.html", {"request": request, "libros": libros})

@app.post("/libros", response_class=HTMLResponse)
def enviar_libro(request: Request, titulo: str = Form(...), autor: str = Form(...)):
    libros = leer_libros()
    nuevo_libro = {
        "id": len(libros) + 1,
        "titulo": titulo,
        "autor": autor
    }
    libros.append(nuevo_libro)
    guardar_libros(libros)
    return templates.TemplateResponse("libros.html", {"request": request, "libros": libros})
