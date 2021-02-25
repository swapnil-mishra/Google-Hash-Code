from dataclasses import dataclass
from typing import *



@dataclass
class ipt:
    
    tms: dict

    pz: list

    @property
    def total_pz(self):
        return len(self.pz)

    @staticmethod
    def from_string(file_name):
        with open(file_name, 'r') as file_reader:
            list_of_line: List[str] = file_reader.readlines()
            
            _, num_tm_2, num_tm_3, num_tm_4 = [int(elem) for elem in list_of_line[0].strip().split(" ")]

            return ipt(
                tms= { 2: num_tm_2, 3: num_tm_3, 4: num_tm_4 },
                pz=[
                    set(line.strip().split(" ")[1:]) for idx, line in enumerate(list_of_line) if idx != 0
                ]
            )


@dataclass
class dlv:
    tm_card: int
    pz_rcvd: List[int]


@dataclass
class otpt:
    rcvs: List[dlv]

    def to_string(self):
        pz_card = len(self.rcvs)
        header = [str(pz_card)]
        rest = [" ".join([str(rcv.tm_card) ] + [str(pizza_id) for pizza_id in rcv.pz_rcvd]) for rcv in self.rcvs]
        return "\n".join(header + rest)


def pyt(filename):
    def decorator(solution):
        inp = ipt.from_string(filename)
        otpt = solution(inp).to_string()
        with open(filename+'.out.txt', 'w') as file_writer:
            file_writer.write(otpt)
    return decorator

