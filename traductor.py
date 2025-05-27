import json
from deep_translator import GoogleTranslator
import re

# Palabras clave que NO se deben traducir (puedes agregar más si lo necesitas)
palabras_ingles = {"id", "isExpanded", "null"}

# Diccionarios para cachear traducciones
cache_claves = {}
cache_valores = {}

def es_ingles(texto):
    # Considera que ya está en inglés si solo tiene letras inglesas y espacios
    return bool(re.fullmatch(r"[A-Za-z0-9 _\-]+", texto))

def traducir_clave(clave):
    if clave in palabras_ingles:
        return clave
    if clave in cache_claves:
        return cache_claves[clave]
    traduccion = GoogleTranslator(source='auto', target='en').translate(clave)
    cache_claves[clave] = traduccion
    return traduccion

def traducir_valor(valor):
    if valor in palabras_ingles or es_ingles(valor):
        return valor
    if valor in cache_valores:
        return cache_valores[valor]
    traduccion = GoogleTranslator(source='auto', target='en').translate(valor)
    cache_valores[valor] = traduccion
    return traduccion

def traducir_json(obj):
    if isinstance(obj, dict):
        nuevo = {}
        for k, v in obj.items():
            nueva_k = traducir_clave(k)
            nuevo[nueva_k] = traducir_json(v)
        return nuevo
    elif isinstance(obj, list):
        return [traducir_json(item) for item in obj]
    elif isinstance(obj, str):
        return traducir_valor(obj)
    else:
        return obj

# Cargar el archivo JSON original
with open('Prueba_Junior.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Traducir el JSON
data_traducido = traducir_json(data)

# Guardar el resultado en un nuevo archivo
with open('Prueba_Junior_en.json', 'w', encoding='utf-8') as f:
    json.dump(data_traducido, f, ensure_ascii=False, indent=2)

print("Traducción completada. Archivo guardado como Prueba_Junior_en.json")