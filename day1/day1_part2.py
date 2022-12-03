f = open("inputs","r")
chunked_input = f.read().split('\n\n')
for x in range(len(chunked_input)):
    chunked_input[x] = chunked_input[x].split('\n')

# removing last entry as its null
chunked_input.pop(-1)

total_input = chunked_input

for x in range(len(chunked_input)):
    sub_total_input = 0
    for y in chunked_input[x]:
            sub_total_input += int(y)
    total_input[x] = sub_total_input

# This worked in the repl but in the script it leads to a null array, unsure why
# final_answer = total_input.sort()
# print(final_answer[-1])

final_answer = sorted(total_input)
print(final_answer[-1] + final_answer[-2] + final_answer[-3])
