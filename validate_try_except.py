def validate(a,b):
    try:
        a/b
    except ValueError:
        return (ValueError)
    except ZeroDivisionError:
        return (ZeroDivisionError)
    except TypeError:
        return (TypeError)
    else:
        return a/int(b)

print(validate(1,'2'))