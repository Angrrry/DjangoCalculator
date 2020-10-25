import math
failed = []
for func in dir(math):
    try:
        attrs = getattr(math, func).__text_signature__
        print(func,attrs)
    except:
        failed.append(func)
print('-'*10)
print(failed)
