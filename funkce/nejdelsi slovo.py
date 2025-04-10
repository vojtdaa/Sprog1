def NejdelsiSlovo(text):
    nejdelsi_slovo = ""
    number = 0
    max_number = 0
    seznam_slov = []
    for i in text:
        if i != "":
            nejdelsi_slovo += i

        else:
            seznam_slov.append(nejdelsi_slovo)
            nejdelsi_slovo = ""
    return seznam_slov






print(NejdelsiSlovo("tect dhfh klfkdkf kdfk kdfk dkkfkfk")) 