import pylightxl

ws = "Variáveis comuns"

sheet = list(pylightxl.readxl("input.xlsx").ws(ws).rows)

name_to_format = {
    "uint32_t": "I",
    "uint16_t": "H",
    "uint8_t": "B",
    "float": "f",
}

sheet = sheet[9 if ws == "Variáveis FBP" else 5 :]
json_conversion = {}
for row in sheet:
    if row[2] not in ["N/A", ""]:
        try:
            json_conversion[row[3]] = {
                "addr": row[1],
                "format": name_to_format[row[2]],
                "size": row[5],
                "egu": row[7],
            }
        except KeyError:
            pass

print(json_conversion)
