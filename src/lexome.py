
from finch import Finch

### TESTING ###
def run_op(str_dict: dict, finch: Finch) -> None:
    op: int = finch.lexome[finch.inst_h]
    exec(str(str_dict[op.to_bytes(1,'big')])+"(finch)")

def h_alloc(finch: Finch):
    print("h_alloc")

def h_search(finch: Finch):
    print("h_search")

def h_copy(finch: Finch):
    print("h_copy")

def if_label(finch: Finch):
    print("if_label")

def h_divide(finch: Finch):
    print("h_divide")

def nop_C(finch: Finch):
    print("nop_C")

def nop_A(finch: Finch):
    print("nop_A")

def nop_B(finch: Finch):
    print("nop_B")

def mov_head(finch: Finch):
    print("mov_head")




    
