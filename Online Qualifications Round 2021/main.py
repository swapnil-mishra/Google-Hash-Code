import sys


class St:
    def __init__(self, text):
        self.start_Isec, self.end_Isec, self.name, self.time = text.split(' ')


class Isec:
    def __init__(self, id):
        self.id = id
        self.incoming_Sts = []

    def add_St(self, St):
        self.incoming_Sts.append(St)


class Car:
    def __init__(self, text):
        self.nbr_Sts, *self.text_Sts = text.split(' ')


def read_file(file_name):
    file = open(file_name, "r")
    lines = [line.rstrip() for line in file.readlines()]
    file.close()

    cmd = lines.pop(0)

    return cmd, lines


def main():
    cmd, lines = read_file(sys.argv[1])

    dur, Isecs_number, Sts_number, cars_number, score = cmd.split(' ')

    Sts = []
    Isecs = {}
    paths = []

    for i in range(0, int(Sts_number)):
        line = lines.pop(0)

        if not line.split(' ')[1] in Isecs.keys():
            Isecs[line.split(' ')[1]] = Isec(line.split(' ')[1])
            Isecs[line.split(' ')[1]].add_St(line.split(' ')[2])
        else:
            Isecs[line.split(' ')[1]].add_St(line.split(' ')[2])
        Sts.append(St(line))

    for i in range(0, int(cars_number)):
        paths.append(Car(lines.pop(0)))

    file = open("result-" + sys.argv[1], "w")

    file.write(str(len(Isecs.keys())) + "\n")
    for k, v in Isecs.items():
        file.write(v.id + "\n")
        file.write(str(len(v.incoming_Sts)) + "\n")
        for St in v.incoming_Sts:
            file.write(St + " 1" + "\n")

    file.close()


if __name__ == "__main__":
    main()
