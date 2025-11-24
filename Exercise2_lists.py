routes = [
    "Nairobi-Westlands",
    "Mombasa-Nyali",
    "Nakuru-Lanet",
    "Kisumu-CBD",
    "Eldoret-Naiberi",
    "Thika-Gatanga",
    "Nanyuki-Timau",
    "Nyeri-Kiganjo",
    "Malindi-Watamu",
    "Naivasha-Karati"
]

routes.append("Kajiado-Kitengela")
routes.remove("Kisumu-CBD")

routes.sort()
routes.reverse()

count_N = sum(route.startswith("N") for route in routes)
print(count_N)

long_routes = [route for route in routes if len(route) > 10]
print(long_routes)
