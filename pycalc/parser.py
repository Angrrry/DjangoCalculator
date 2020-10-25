import math
failed = []
for func in dir(math):
    try:
        attrs = getattr(math, func).__text_signature__
        # because __text_signature__ for log, hypot is None
        attrs = attrs.replace(' ','').split(',') if attrs else ['x']
        attrs = tuple(attr for attr in attrs if attr.isalpha())
        print(func,attrs)

        

    except:
        failed.append(func)
print('-'*10)
print(failed)
