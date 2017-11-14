# Constants:
#MULTIPLIER1 = '3141592653589793238462643383279502884197169399375105820974944592'
#MULTIPLIER2 = '2718281828459045235360287471352662497757247093699959574966967627'


def multiply(n1, n2):
    print "n1 = %d and n2 = %d" % (n1, n2)
    sn1 = str(n1)
    sn2 = str(n2)
    ln1 = len(sn1)
    ln2 = len(sn2)
    if (ln1 % 2) != 0:
        print "Cannot validate odd number of digits"
        return 0
    m = max(ln1, ln2)/2
    B1 = pow(10, 2*m)
    B2 = pow(10, m)
    # import pdb
    # pdb.set_trace()

    if ln1 <= 3 or ln2 <= 3:
        print "Returning %s" % (n1*n2)
        return n1 * n2
    x1n1 = int(sn1[0:ln1/2])
    x2n1 = int(sn1[ln1/2:ln1])
    x1n2 = int(sn2[0:ln2/2])
    x2n2 = int(sn2[ln2/2:ln2])
    z1 = multiply(x1n1, x1n2)        # higher half
    z2 = multiply(x2n1, x2n2)        # lower half
    z0 = multiply((x1n1 + x2n1), (x1n2 + x2n2))
    zval = z0 - z1 - z2
    print "z1 = %d, z2 = %d, z0 = %d, zval = %d, B1 = %d, B2 = %d" % (z1, z2, z0, zval, B1, B2)
    res = (B1 * z1) + (B2 * zval) + z2
    print "res = %d" % res
    return res


if __name__ == '__main__':

    m1 = 3141592653589793238462643383279502884197169399375105820974944592
    m2 = 2718281828459045235360287471352662497757247093699959574966967627
    print "Multiplying %s and %s results in %s" % (m1, m2, multiply(m1, m2))


