def secure_input(chaine):
    result = 0
    ok = False
    try:
        result = int(chaine)
        ok = True
    except:
        result = -1
    return result, ok
        