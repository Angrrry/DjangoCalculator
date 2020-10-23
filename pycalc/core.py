# Wile with all logic. Later it will be refactored or deleted.
class Oper():
    """
    Defines how to represent symbols in input string.
    """
    def add(a, b):
        """returns sum of numeric a and b
        >>> Oper.add(1,3)
        4
        >>> Oper.add(2.0,19)
        21.0
        """
        return a+b

    def sub(a, b):
        """returns a -b for numeric a and b

        Args:
            a ([int]): number2
            b ([int]): number2

        >>> Oper.sub(1,4)
        -3
        >>> Oper.sub(1.0,-4)
        5.0
        """
        return a - b

    def mul(a, b):
        """multiplies a and b
        >>> Oper.mul(2,3)
        6
        >>> Oper.mul(0.5,2)
        1.0
        """
        return a * b

    def div(a, b):
        """returns a // b
        >>> Oper.div(2,3)
        0
        >>> Oper.div(3.0,2)
        1.0
        """
        return a // b

    def divide(a, b):
        """returns a / b
        >>> Oper.divide(3.0,2)
        1.5
        >>> Oper.divide(2,3)
        0.6666666666666666
        """
        return a / b

    def rem(a, b):
        """return a % b
        >>> Oper.rem(1,3)
        1
        >>> Oper.rem(6,3)
        0
        """
        return a % b

    def pow(a, b):
        """returns a**b
        >>> Oper.pow(3,2)
        9
        >>> Oper.pow(3,0.5)
        1.7320508075688772
        """
        return a ** b



if __name__ =="__main__":
    pass