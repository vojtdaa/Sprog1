def obrat(s):
    novy = ""

    def obracej(s, novy):
        if len(s) == 0:
            return novy
        
        novy += s[-1]

        return obracej(s[:-1], novy)

    return obracej(s, novy)

print(obrat(''))        # → ''
print(obrat('a'))       # → 'a'
print(obrat('ahoj'))    # → 'joha'
print(obrat('python'))  # → 'nohtyp'