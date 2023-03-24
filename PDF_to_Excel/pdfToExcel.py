import tabula

table = tabula.read_pdf("Table_and_Text.pdf", pages=1)

table[0].to_excel("output.xlsx", index=None)
