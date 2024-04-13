import datetime

hora_atual = datetime.datetime.now().hour

if hora_atual < 12:
    print("Bom dia!")

elif hora_atual < 18:
    print("Boa tarde!")

else:
    print("Boa noite!")