#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    lista = dir(hidden_4)
    for c in sorted(lista):
        if c[0] != "_" and c[1] != "_":
            print(f"{c}")
