# A recursive algorithm must have a base case
# A recursive algotithm must change its state and move towards the base case
# A recursive algorithm must call itself, recursively

def bottles_of_beer(bob):
    """ Prints 99 Bottles of Beer on the wall lyrics/
        :param bob: Must be a positive integer.
    """
    if bob < 1:
        print("""No more bottles of beer on the wall./
        no more bottles of beer""")
        return
    tmp = bob
    bob -= 1
    print("""{} bottles of beer on the wall. {} botles of beer./
    Take one down, pass it around, {} bottles of beer on the wall./
    """.format(tmp, tmp, bob))

    bottles_of_beer(bob)

bottles_of_beer(99)
