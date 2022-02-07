def main() -> None:
    runInterface()

def run_sim() -> None:
    orgs, lexome = list[list[str]],list[str]
    orgs, lexome = preprocessor.pre_process()
    lexome_dict: dict = binary.to_dict(lexome)
    print(lexome_dict)
    lexome_orgs: list[bytearray] = []
    quit()

def runInterface() -> None:
    buffer: str = ""
    title_buffer: str =  "-"*23 + "\n"
    title_buffer +=      "PYFINCH - ALPHA BUILD\n"
    title_buffer +=      "-"*23
    for i, (option,_) in enumerate(optionHandler(get=True)):
        buffer += "[" + str(i) +  "]: " + option + "\n"
    while True:
        pretty("HEADER",title_buffer)
        pretty("BOLD",buffer)
        action: list[(str,str)] = optionHandler(input())
        if action[0][0] == "NOP":
            print("Invalid Action")
        else:
            exec(action[1])

def optionHandler(option: str = None, get: bool=False) -> list[(str,str)]:
    options: list[(str,str)] = []
    options.append(("Run Simulation - Run a preset simulation","run_sim()"))
    options.append(("About - Information about PYFINCH","about()"))
    options.append(("Quit - Quit PYFINCH","quit()"))
    if get:
        return options
    try:
        choice: int = int(option)
    except:
        return [("NOP","NOP")]
    if choice >= len(options) or choice < 0:
        return [("NOP","NOP")]
    return options[choice]

def about() -> None:
    try:
        with open("about.txt",'r',encoding='utf-8') as f:
            lines = f.read()
        print(lines)
    except:
        pretty("WARNING","The file (about.txt) could not be found in top level directory")
    

if __name__ == "__main__":
    import preprocessor
    from visual import pretty
    import binary
    main()