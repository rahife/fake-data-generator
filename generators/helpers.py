def decor(field):
    return ('"' + field + '"') if "," in field else field

