# textul inițial
var_string = "Inquisitor și Varric sunt la Skyhold pentru cursul de Python."

# lista cu patch-uri (perechi de tipul: vechi, nou)
patches = [
    ("Inquisitor", "Conquistador"),
    ("Varric", "King"),
    ("Skyhold", "Palace")
]

# aplicarea înlocuirilor
for old, new in patches:
    var_string = var_string.replace(old, new)

print(var_string)