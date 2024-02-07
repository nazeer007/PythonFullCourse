customer = {
    "name": "Nazeer",
    "age": 21,
    "is_verified":True
}
customer["birthdate"] = "Jan 1 2000"
customer["name"] = "Syed"
print(customer["name"])
print(customer.get("gender", "male"))