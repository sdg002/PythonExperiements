"""
Simples example of generator
"""
def generate_sequential(n:int):
    for idx in range(n):
        print(f"Inside generator, {idx=}")
        yield idx


if __name__ =="__main__":
    gen1=generate_sequential(7)
    print(f"Type of gen1 is {type(gen1)}")
    print("Going to print the contents")
    print(list(gen1))
