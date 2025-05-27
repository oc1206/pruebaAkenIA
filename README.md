# pruebaAkenIA
Desarrollo de prueba técnica con AkenIA, traducción de un json y conversión de Ids.

Traductor Automático de texto en español a ingles en formato JSON
Este script traduce todas las claves y valores de un archivo JSON al inglés, excepto aquellas palabras que ya están en inglés o que se encuentran en una lista de exclusión (por ejemplo, identificadores como id). Utiliza la librería deep-translator para realizar la traducción automática y emplea caché para evitar traducciones repetidas, optimizando el proceso.

Requisitos
Python 3.x
Librería deep-translator

Instala la librería necesaria ejecutando:
pip install deep-translator

Uso
Coloca tu archivo original (por ejemplo, Prueba_Junior.json) en el mismo directorio que el script traductor.py.

Ejecuta el script en la terminal:
python traductor.py

Resultado:
Se generará un archivo llamado Prueba_Junior_en.json con todas las claves y valores traducidos al inglés (excepto los que están en la lista de exclusión).
Personalización

Puedes agregar más palabras a la lista palabras_ingles dentro del script para que no se traduzcan (por ejemplo, otros identificadores o palabras técnicas).
El script funciona con cualquier estructura de JSON, incluyendo listas y diccionarios anidados.

Ejemplo de estructura de archivos
/tu_carpeta/
│
├── traductor.py
├── Prueba_Junior.json
└── Prueba_Junior_en.json  # (se genera automáticamente)

Notas
Si tu archivo JSON es muy grande, la traducción puede tardar algunos minutos, ya que utiliza un traductor en línea.
El script utiliza caché para no traducir dos veces la misma palabra o frase, acelerando el proceso y reduciendo el consumo de la API.

Créditos
Traducción automática realizada con deep-translator.
