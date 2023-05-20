import re, openpyxl

def phoneNumbersRegEx(html):
    phoneNumbers = re.compile(r'(\(\d{2}\)\s\d{4}-\d{4}|\d{2}\s\d{4}\s\d{4}|\d{2}\s\d{8}|\d{3}\s\d{3}\s{4}|\(\d{3}\)\s\d{3}\s\d{4}|\(\d{3}\)\s\d{3}-\d{4}|\+\d{2}\s\d{2}\s\d{4}\s\d{4}|\+\d{2}\s\d{2}\s\d{4}-\d{4}|\+\d{2}\s\(\d{2}\)\s\d{4}\s\d{4}|\+\d{2}\s\(\d{2}\)\s\d{4}-\d{4})')
    matches_phoneNumbers = phoneNumbers.findall(html)
    return matches_phoneNumbers
    
# (81) 8329-4000
# 12 3456 7890
# 93 92833298
# 983 398 9383
# (239) 983 0923
# +52 81 1234 1234
# +52 81 1234-1234
# +52 (81) 1234 1234

def emailsRegex(html):
    emails = re.compile(r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+|[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+)')
    matches_emails = emails.findall(html)
    return matches_emails

# contactouni@uanl.mx
# ejemplo@uanl.edu.mx

def datesRegEx(html):
    dates = re.compile(r'(\d{2}\s[EFMAJSONDefmajsond]\w+\s\d{4}|\d{1}\s[EFMAJSONDefmajsond]\w+\s\d{4}|[EFMAJSONDefmajsond]\w+\s\d{2}\s\d{4}|[EFMAJSONDefmajsond]\w+\s\d{1}\s\d{4})')
    matches_dates = dates.findall(html)
    return matches_dates

# 11 Enero 2022                 # 10 enero 2022             # 10 Ene 2022
# 10 ene 2022                   # 9 Enero 2022              # 9 enero 2022
# 9 Ene 2022                    # 9 ene 2022                # Enero 11 2022
# enero 11 2022                 # Ene 10 2022               # ene 10 2022
# Enero 9 2022                  # enero 9 2022              # Ene 9 2022
# ene 9 2022

def imagesRegEx(html):
    images = re.compile(r'(img\ssrc=\".+\.\w+\")')
    matches_images = images.findall(html)
    return matches_images

# img src="ejemplo.jpg"
# img src"*****.******"

def bSort(list):
    swapped = False
    for i in range(len(list)-1):
        for j in range(0, len(list)-i-1):
            if list[j] > list[j + 1]:
                swapped = True
                list[j], list[j + 1] = list[j + 1], list[j]
        if not swapped:
            return

def sortM(nordered):
    ordered = []
    i = 0
    lowest = nordered[0]
    while len(nordered) > 0:
        if  nordered[i] < lowest:
            lowest = nordered[i]
        i += 1
        if i == len(nordered):
            ordered.append(lowest)
            nordered.remove(lowest)
            if nordered:
                lowest = nordered[0]
            i = 0
    return ordered

# def cellFill(CellLetter,List):
#     for i in range(0,len(List)):
#         pos = CellLetter + str((i + 3))
#         sheet[pos] = str(List[i])