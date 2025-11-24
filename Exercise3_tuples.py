patient = ("John Doe", 45, "120/80", 72)

print(patient[1])
print(patient[3])

patient_list = list(patient)
patient_list[3] = 80
patient = tuple(patient_list)
print(patient)

patients = (
    ("John Doe", 45, "120/80", 72),
    ("Jane Roe", 50, "118/75", 70),
    ("Sam Kim", 39, "130/85", 78),
    ("Lucy Ann", 60, "140/90", 82),
    ("Mark Lee", 30, "110/70", 65)
)

names = [p[0] for p in patients]
print(names)
