def search(ws, line_pos, char_pos, seq, ignore_pos, total, origin_line_pos, origin_char_pos):
    xmas = ['X', 'M', 'A', 'S']

    ignore = ignore_pos

    new_total = total
    
    for i in range(line_pos-1, line_pos+1):
        for j in range(char_pos-1, char_pos+1):
            print(f"Checking {(j, i)}")
            if((j, i) in ignore):
               continue

            if(ws[j][i] == xmas[seq]):

                if(seq==3):
                    total+=1
                    seq = 0
                    search(ws, i, j, seq, ignore, new_total, origin_line_pos, origin_char_pos)


                print(xmas[seq])
                ignore.add((j, i))
                search(ws, i, j, seq+1, ignore, new_total, origin_line_pos, origin_char_pos)

    return new_total

            

    

with open("4-small.txt") as file:
    
    ws = []

    line_counter = 0
    char_counter = 0
    for line in file:
        char_counter = 0
        char_array = []
        for char in line:
            if(char=="\n"):
               continue
            char_array.append(char)
            char_counter+=1

        ws.append(char_array)
        line_counter+=1

    line_counter = 0
    char_counter = 0

    ignore_pos = set()

    for line in ws:
        for char in line:
            char_counter+=1
            search(ws, line_counter, char_counter, 0, ignore_pos, 0, line_counter, char_counter)
        line_counter+=1


