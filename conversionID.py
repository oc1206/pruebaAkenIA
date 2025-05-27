import json
import random
import string
import re

# Cargar el archivo JSON original
with open('Prueba_Junior.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Diccionario para mapear id original a nuevo id
id_map = {}

def generar_id_50():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=50))

def mapear_id(id_original):
    if id_original not in id_map:
        id_map[id_original] = generar_id_50()
    return id_map[id_original]

def reemplazar_ids(obj):
    if isinstance(obj, dict):
        nuevo = {}
        for k, v in obj.items():
            # Si la clave es 'id', reemplazar el valor
            if k == "id" and isinstance(v, str):
                nuevo[k] = mapear_id(v)
            # Si el valor es string y parece una referencia a un id, reemplazarlo
            elif isinstance(v, str):
                # Busca patrones como "Salta a: <id>" y reemplaza solo el id
                match = re.match(r"(Salta a: )([a-f0-9\-]{36})", v)
                if match:
                    nuevo[k] = match.group(1) + mapear_id(match.group(2))
                else:
                    nuevo[k] = v
            else:
                nuevo[k] = reemplazar_ids(v)
        return nuevo
    elif isinstance(obj, list):
        return [reemplazar_ids(item) for item in obj]
    else:
        return obj

# Procesar el JSON
data_nuevo = reemplazar_ids(data)

# Guardar el resultado en un nuevo archivo
with open('Prueba_Junior_ids50.json', 'w', encoding='utf-8') as f:
    json.dump(data_nuevo, f, ensure_ascii=False, indent=2)

print("IDs convertidos y referenciados correctamente. Archivo guardado como Prueba_Junior_ids50.json")
