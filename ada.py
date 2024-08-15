def ada():
    first_name = "AdA"
    last_name = "LoVeLAce"

# Convertimos el nombre y el apellido a minúsculas
    full_name_lowercase = f"{first_name.lower()} {last_name.lower()}"

# Convertimos el nombre y el apellido a capitalizado (primera letra en mayúscula)
    full_name_capitalized = f"{first_name.capitalize()} {last_name.capitalize()}"

# Convertimos el nombre y el apellido a mayúsculas
    full_name_uppercase = f"{first_name.upper()} {last_name.upper()}"

# Output final con las cuatro formas
    output = f"""{full_name_lowercase} 
    {full_name_capitalized} 
    {full_name_uppercase}  
    \t{full_name_lowercase}"""

    print(output)

