#Importando modulos y declarando variables.

import requests, re, os, openpyxl
import  functions as fun
from googlesearch import search
from datetime import datetime

enlaces = []
enlacesLimpios = []
Phnumbers = []
emails = []
dates = []
images = []
cells = ['A1','F1','H1','J1', 'L1', 'O1', 'Q1']
cellFill = ['Links','PNumbers', 'Emails', 'Dates', 'Images', 'Lista desordenada', 'Lista ordenada']
cities = ['London', 'Monterrey', 'Paris', 'Uganda', 'Lima']
KelvinTemps = []

# Pidiendo la o las palabras clave al usuario.

pClave = input('Inserte la/las palabras clave de la búsqueda \n')

# Haciendo la búsqueda de las 15 palabras y agregándolas a una lista.

for enlace in search(pClave, tld='com', num=15, stop=15, pause=15):
    enlaces.append(enlace)

# Sacando el tiempo con datetime y estableciendo el formato deseado
# dia, mes, año, hora y minuto.

actual = datetime.now()
dateHour = actual.strftime("%d de %b del %Y a las %H;%M")

# Estableciendo el nombre del directorio a crear.

dirName = (pClave + ': ' + dateHour)

# Creando el directorio y sus respectivas exepciones
# (disponibles en la documentación del módulo).

try: 
    os.mkdir(dirName)
except FileExistsError:
    print("El directorio ya existe")
except FileNotFoundError:
    print("El Path no existe")


# Un guardado del path principal donde veremos todos los 
# intentos de search creados.
pathOG = os.getcwd()


# Aquí estamos metiendonos al directorio creado y hacemos sus
# respectivas excepciones.
# De igual forma las podemos encontrar en la documentación del módulo.

try:
    os.chdir(dirName)
except FileNotFoundError:
    print("El directorio solicitado no existe")
except PermissionError:
    print("No tienes los permisos adecuados para acceder a este directorio")
except NotADirectoryError:
    print("No es un directorio")

# Aquí hacemos un for para ir remplazando cada / con una | y así no tener el error
# de que os.mkdir quiera utilizar las páginas como rutas.

for i in range(0,len(enlaces)):
    enlacesLimpios += [enlaces[i].replace('/','|')]

# esto nos genera una copia del path que creamos para esta busqueda, ayudará más adelante

pathDentroDelTest = os.getcwd()

for i in range(0,len(enlacesLimpios)):
    try:
        # Creamos el path para los html, evitando así tener que entrar y salir constantemente de los directorios
        pathForHtml = (pathDentroDelTest + "/" + enlacesLimpios[i] + '/pagina.html')

        # Se hace el directorio respectivo de la página
        os.mkdir(enlacesLimpios[i])

        # Pedimos el html de las páginas y lo hacemos un archivo en la ruta creada pathForHtml
        page = requests.get(enlaces[i])

        # Creamos el archvio html
        with open(pathForHtml, 'w+') as wp:
            wp.write(page.text)
        # Añadimos a las listas su respectiva función de búsqueda         
        Phnumbers.append(fun.phoneNumbersRegEx(page.text))
        emails.append(fun.emailsRegex(page.text))
        dates.append(fun.datesRegEx(page.text))
        images.append(fun.imagesRegEx(page.text))
    except FileExistsError:
        print("El directorio ya existe")
    except FileNotFoundError:
        print("El Path no existe")

# Creamos el libro de excel y una hoja

book = openpyxl.Workbook()
sheet = book.active
sheet.title = 'Resultados del web scraping'

# Rellenamos la primera fila con las cosas que estamos buscando

for i in range(0,len(cells)):
    sheet[cells[i]] = cellFill[i]


# Empezamos a rellenar las columnas con el contenido de las listas

for i in range(0,len(enlaces)):
        pos = 'A' + str((i + 3))
        sheet[pos] = str(enlaces[i])

for i in range(0,len(Phnumbers)):
        pos = 'F' + str((i + 3))
        sheet[pos] = str(Phnumbers)
    
for i in range(0,len(emails)):
        pos = "H" + str((i + 3))
        sheet[pos] = str(emails[i])

for i in range(0,len(dates)):
        pos = "J" + str((i + 3))
        sheet[pos] = str(dates[i])

for i in range(0,len(images)):
        pos = "L" + str((i + 3))
        sheet[pos] = str(images[i])


#### Esto es para meter a la fuerza un método de ordenamiento y la API xd ####

for i in range(0,len(cities)):
    # Aquí estamos acomodando el link de la API para hacerlo "Modular"
    BaseUrl = "https://api.openweathermap.org/data/2.5/weather?appid=d1d9b16a6e2829afc00c3e538111d581&q="
    city = cities[i]
    url = BaseUrl + city
    # Está pidiendo la info a la api y la está pasando a JSON
    response = requests.get(url).json()
    # del diccionario creado con JSON queremos sacarle lo que esté en main, temp
    temp_kelvin = response['main']['temp']
    # le agregamos a la lista de kelvin temps lo que sacó de la API
    KelvinTemps.append(temp_kelvin)


# Pasamos la lista desordenada a el excel 
for i in range(0,len(KelvinTemps)):
        pos = "O" + str((i + 3))
        sheet[pos] = str(KelvinTemps[i])


# Ordenamos la lista
listaOrdenada = fun.sortM(KelvinTemps)

# Pasamos la lista ordenada al excel
for i in range(0,len(listaOrdenada)):
        pos = "Q" + str((i + 3))
        sheet[pos] = str(listaOrdenada[i])

# Guardamos el libro
book.save('Resultados.xlsx')


