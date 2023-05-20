#!/bin/bash

# Verificar si se proporcionó un argumento de ruta al archivo
if [ $# -eq 0 ]; then
    echo "Debe proporcionar la ruta relativa del archivo de texto como argumento."
    exit 1
fi

# Verificar si el comando "mail" está disponible en el sistema
if ! command -v mail &> /dev/null; then
    echo "El programa 'mail' no está instalado en el sistema."
    echo "Por favor, instale el programa 'mail' para enviar correos electrónicos."
    exit 1
fi

# Ruta relativa del archivo de texto que contiene las direcciones de correo electrónico
archivo_correos="$1"

# Configuración del correo electrónico
remite="tucorreo@example.com"
asunto="Asunto del correo"
mensaje="Cuerpo del correo"

# Función para enviar el correo electrónico
function enviar_correo() {
    destinatario="$1"
    echo "Enviando correo a: $destinatario"
    echo "$mensaje" | mail -s "$asunto" -r "$remite" "$destinatario"
}

# Verificar si el archivo existe
if [ -f "$archivo_correos" ]; then
    # Leer cada línea del archivo
    while IFS= read -r linea; do
        # Verificar si la línea contiene una dirección de correo válida
        if [[ "$linea" =~ ^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$ ]]; then
            enviar_correo "$linea"
        fi
    done < "$archivo_correos"
else
    echo "El archivo $archivo_correos no existe."
fi
