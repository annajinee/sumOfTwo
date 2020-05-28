import sys, getopt

def main(argv):

    FILE_NAME = argv[0]
    I = 0
    J = 0
    SUM = 0

    try:
        opts, etc_args = getopt.getopt(argv[1:], "i:j:")

    except getopt.GetoptError:
        print(FILE_NAME, '-i <num1> -j <num2>')
        sys.exit(2)

    for opt, arg in opts:

        if opt == "-i":
            I = int(arg)

        elif opt == "-j":
            J = int(arg)

    SUM = I + J 
    print("SUM:", SUM)

if __name__ == "__main__":
    main(sys.argv)
