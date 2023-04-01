# Enter your code here. Read input from STDIN. Print output to STDOUT

def copy(string,start,stop):
    clip = string[start-1:stop]
    return clip


def cut(string,start,stop):
    clip = string[start-1:stop]

    if (start-1) == 0:
        string = string[(stop):]

    elif stop == len(string):
        string = string[:(start-1)]

    else:
        string = string[:(start-1)] + string[(stop):]

    return clip, string


def paste(string,start,clip):
    if (start-1) == 0:
        string = clip + string

    elif start >= len(string):
        string = string + clip

    else:
        string = string[:(start-1)] + clip + string[(start-1):]


    return string


clipboard = []
text_string = input()
operations = int(input())

for i in range(operations):
    command = input()

    if command[0:2] == "CO":

        clip = (copy(text_string,int(command[5]),int(command[7])))
        if clip != "":
            clipboard.append(clip)

    
    elif command[0:2] == "CU":

        clip, text_string = (cut(text_string,int(command[4]),int(command[6])))
        clipboard.append(clip)

    elif command[0:2] == "PA":

        clip = clipboard[-1]
        if len(clipboard) > 1:
            clipboard.pop()

        text_string = paste(text_string,int(command[6]),clip)



print(text_string)
