agenda=[
    ["Carlos","6181234567"],
    ["Alberto","668202092"],
    ["Marin","67758584849"]
    ]

for r in agenda:
    print(r)

for r in range(0,3):
    for c in range(0,2):
        print(agenda[r][c])

valores=""
for r in range(0,3):
    for c in range(0,2):
        valores+=f"[{agenda[r][c]}],"
    valores+=f"\n"
print(valores)

