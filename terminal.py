def main() -> None:
    runInterface()

# Option to run the simulation
def run_sim() -> None:
    str_orgs, str_lexome = list[list[str]],list[str]
    str_orgs, str_lexome = preprocessor.pre_process()

    # Converts lexemes to binary
    binary_dict: dict = lexome.to_dict(str_lexome)
    # Converts binary to lexemes
    str_dict: dict = dict(zip(binary_dict.values(),binary_dict.keys())) 

    print(binary_dict)
    print(str_dict)

    binary_orgs: list[bytearray] = []
    binary_lexome: bytearray = lexome.translate_to_binary(str_lexome,binary_dict)

    # Testing
    for o in str_orgs:
        binary_orgs.append(lexome.translate_to_binary(o,binary_dict))
    
    # Testing
    for o in binary_orgs:
        print(lexome.translate_to_str(o,str_dict))

    # Testing
    for b in binary_orgs[0]:
        lexome.run_op(b.to_bytes(1,'big'), str_dict, 0)
    quit()

# Startup interface
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

# Handles the display menus - easily updateable.
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

# Option to display About.
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
    import lexome
    import finch
    main()