import xlsxwriter
def escribir():
    n="si"
    while n=="si":
        x=str(input("Fila con Columna"))
        y=str(input("Palabra"))
        workbook = xlsxwriter.Workbook('C.ONE.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.write(x,y)
        workbook.close()
        n=str(input("desea repetir Si o No"))
