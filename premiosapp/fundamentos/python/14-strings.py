text = 'Ella sabe programar en Python'

'''
print('JavaScript' in text)
print('Python' in text)

if 'JS' in text:
    print('Elegiste bien!!')
else:
    print('Tambien elegiste bien')

'''

size = len(text)
print(size)

print(text)
print(text.upper()) # Mayuscula
print(text.lower()) # Minuscula
print(text.count('a')) # Contar

print(text.swapcase()) # Transformacion de | Mayuscula a Minuscula | y de | Minuscula a Mayuscula |
print(text.startswith('Ella')) # Ver si el texto inicia con esa palabra
print(text.endswith('Rust')) # Ver si el texto finaliza con esa palabra
print(text.replace('Python', 'Go')) # Remplaza un texto por otro texto

text_2 = 'este es un titulo'
print(text_2)
print(text_2.capitalize())  # Primera caracter en mayuscula
print(text_2.title()) # Primer caracter de cada palabra del texto en mayuscula
print(text_2.isdigit()) # Nos dice si el texto es un digito (Bolean)
print("398".isdigit())# A pesar de que es texto lo consdera un digito

# ? Extencion Better Comments
# ! Funciones presentes de Pythn
# * 1.	capitaliza      Cambia todas las letras a minúsculas menos la primera.
# * 2.	casefold        Utilizada para compara cadenas sin importar el tamaño de los caracteres.
# * 3.  center          Formaseta una cadena alineandola al centro
# * 4.  count           Cuenta las ocurrencias de una cadena
# * 5.  encode          Codifica una cadena según la codificación deseada.
# * 6.  endswith        Comprueba si la cadena termina con una cadena específica.
# * 7.  expandtabs      Convierte los tabuladores en espacios.
# * 8.  find            Devuelve el índice de la cadena buscada o -1 si no se encuentra.
# * 9.  format          Formatea una cadena de forma avanzada.
# * 10. format_map      Igual que format, pero sin hacer una copia de los parámetros.
# * 11. index           Devuelve el índice de una cadena de caracteres o ValueError.
# * 12. isalnum         Comprueba si la cadena es alfanumérica.
# * 13. isalpha         Comprueba si la cadena es alfabética.
# * 14. isascci         Comprueba si la cadena es ASCII.
# * 15. isdecimal       Comprueba si la cadena es un decimal.
# * 16. isdigit         Comprueba si la cadena es un dígito.
# * 17. isidentifier    Comprueba si la cadena es un identificador.
# * 18. islower         Comprueba si todos los caracteres son minúsculos.
# * 19. isnumeric       Comprueba si la cadena es numérica.
# * 20. isprintable     Comprueba si la cadena es imprimible.
# * 21. isspace         Comprueba si la cadena solo contiene espacios.
# * 22. istitle         Comprueba si la cadena tiene formato de título.
# * 23. isupper         Comprueba si todos los caracteres son mayúsculas.
# * 24. join            Une todos los elementos de un iterador en una cadena.
# * 25. ljust           Justifica la cadena a la izquierda.
# * 26. lower           Convierte la cadena a minúsculas.
# * 27. lstrip          Elimina los caracteres de espacio de la izquierda.
# * 28. maketrans       Crea una tabla de traducción para translate.
# * 29. partition       Crea particiones de una cadena usando un separador.
# * 30. replace         Reemplaza en la misma cadena un carácter por otro.
# * 31. removeprefix    Devuelve una nueva cadena con el prefijo especificado como argumento eliminado si se encuentra en la cadena origina.
# * 32. removesuffix    Devuelve una nueva cadena con el sufijo especificado
# * 33. rfin            Devuelve el índice de la cadena como parámetro buscando por la derecha o -1 si no se encuentra.
# * 34. rindex          Devuelve el índice de la cadena como parámetro buscando por la derecha o ValueError.
# * 35. rjust           Justifica la cadena a la derecha.
# * 36. rpartition      Crea particiones de una cadena usando un separador y comenzando por la derecha.
# * 37. rsplit          Devuelve una lista de cadenas al separar la original por un separador buscando por la derecha.
# * 38. rstrip          Devuelve una lista de cadenas separando la original por saltos de línea.
# * 39. split           Devuelve una lista de cadenas al separar la original por un separador.
# * 40. splitlines      Devuelve una lista de cadenas separando la original por saltos de línea.
# * 41. startswith      Comprueba si la cadena comienza con una cadena específica.
# * 42. strip           Elimina los espacios iniciales y finales de la cadena.
# * 43. swapcase        Cambia el tamaño de cada letra de minúsculas a Mayúsculas y las que estan en Mayúsculas a minúsculas.
# * 44. title           Convierte la cadena a formato título.
# * 45. translate       Reemplaza cada carácter por otro siguiendo una tabla de traducciones.
# * 46. upper           Convierte la cadena a mayúsculas.
# * 47. zfill           Añade ceros a la izquierda a una cadena numérica.