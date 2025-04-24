def NejdelsiSlovo(text):
    slova = text.split()
    print (slova)
    

NejdelsiSlovo("fg jkgkdj   ff f       f 55 5f5 555")


def NejdelsiSlovo_2(text):
    slova = text.split()

    if not slova:
        return ""
    
    return max(slova, key=len)

print(NejdelsiSlovo_2("sdn fdf kkkk d kd kdkfkk d "))