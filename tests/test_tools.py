from brain.tools import available_tools

tools = available_tools()

for name, description in tools.items():
    print(name)
    print(" -", description)
    print()