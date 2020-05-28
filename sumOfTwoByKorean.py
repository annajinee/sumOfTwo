import sys, getopt, math

numbers = [
    ("일", 1),
    ("이", 2),
    ("삼", 3),
    ("사", 4),
    ("오", 5),
    ("육", 6),
    ("칠", 7),
    ("팔", 8),
    ("구", 9),
    ("십", 10),
    ("백", 100),
    ("천", 1000),
    ("만", 10000),
    ("억", 100000000),
    ("조", 1000000000000)
]

def kodreanToNum(korean):
    decode_result = []
    result = 0
    num_result = 0
    index = 0

    while index < len(korean):
        for number, true_value in numbers:
            if index + len(number) <= len(korean):
                if korean[index:index + len(number)] == number:
                    decode_result.append((true_value, math.log10(true_value).is_integer()))
                    if len(number) == 2:
                        index += 1
                    break
        index += 1

    for index, (number, is_natural) in enumerate(decode_result):
        if is_natural:
            if math.log10(number) > 3 and (math.log10(number) - 4) % 4 == 0:
                result += num_result * number
                num_result = 0

            elif index - 1 >= 0:
                if not decode_result[index - 1][1]:
                    num_result += number * decode_result[index - 1][0]
                else:
                    num_result += number
            else:
                num_result += number

        else:
            if index + 1 == len(decode_result):
                num_result += number
            elif not decode_result[index + 1][1]:
                num_result += number
            elif math.log10(decode_result[index + 1][0]) > 3 and (math.log10(decode_result[index + 1][0]) - 4) % 4 == 0:
                num_result += number

    result += num_result

    return result

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
            I = kodreanToNum(arg)

        elif opt == "-j":
            J = kodreanToNum(arg)

    SUM = I + J
    print("SUM:", SUM)

if __name__ == "__main__":
    main(sys.argv)
