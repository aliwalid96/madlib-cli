import re

def read_template(path):
    try:
        file = open(path)
    except FileNotFoundError:
        print('File path is invalid')
        raise FileNotFoundError
    else:
        content = file.read()
        file.close()
        return content
        

def parse_template(content):
    parts = re.findall('{(.+?)}',content)
    
    for part in parts:
        content = re.sub(part, "", content)
    parts = tuple(parts)
    
    return  content, parts

def user_input(parts):
    user_inputs = []
    for part in parts:
      item  = input(f'Please type in {part}: ')
      user_inputs.append(item)
    return user_inputs
    
   

def merge(content,user_inputs):

    for item in user_inputs:
        result = content.format(*user_inputs)
        
        # print(result)
    return result


if __name__ == '__main__':
    print("its a game which ask you to enter a words then merge them togather with another paragraph")
    read = read_template('assets/user.txt')
    parse, words = parse_template(read)
    inputs  = user_input(words)
    finished = merge (parse,inputs)
    
    print(finished)
            

