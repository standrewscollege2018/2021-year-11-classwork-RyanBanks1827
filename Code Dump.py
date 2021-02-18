def docheck(variable):
    try:
        int(variable)
        return False

    except ValueError:
        return True