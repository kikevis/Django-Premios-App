name = "Geovanny"
last_name = 'Villa'
print(name)
print(last_name)

full_name = name + " " + last_name
print(full_name)

quote = "I'm Geovanny"
print(quote)

quote2 = ' "Hello" '
print(quote2)

# format
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print('v1 ', template)

template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)

print('v2', template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print('v3', template)

# other format
name = "Geovanny"
last_name= "Villa"
age = 24

impresion = f"Hola {name} {last_name}, tu edad es {age}"
print(impresion)