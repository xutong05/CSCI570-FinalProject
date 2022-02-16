import sys
# read input from input.txt
def Read_input():
    file = sys.argv[1]
    f = open(file, "r")
    # f = open("input.txt", "r")
    string_list = []
    num1 = []
    num2 = []
    is_second = True
    for line in f.readlines():
        line = line.strip()
        if not line.isnumeric():
            string_list.append(line)
            if len(string_list) == 2:
                is_second = False
        else:
            if is_second:
                num1.append(int(line))
            else:
                num2.append(int(line))
    f.close()
    return string_list, num1, num2


# return a list of two generated strings
def String_generator():
    string_list, num1, num2 = Read_input()
    result = []
    index = 0
    string = string_list[0]
    while index < len(num1):
        string = string[0:num1[index]+1] + string + string[num1[index]+1 :]
        index += 1
    result.append(string)
    
    index = 0
    string = string_list[1]
    while index < len(num2):
        string = string[0:num2[index]+1] + string + string[num2[index]+1 :]
        index += 1
    result.append(string)
        
    return result

# write output.txt file consist of two generated strings
# return a list of two generated strings
def write_output():
    result = String_generator()
    f = open("String_generator.txt", 'wt')
    f.write('\n'.join(result))
    f.close()
    return result

write_output()

