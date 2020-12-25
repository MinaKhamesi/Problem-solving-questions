def shortestPath(path):
    startWithSlash = path[0] == '/'
    tokens = list(filter(isImportant, path.split('/')))
    stack = []
    if startWithSlash:
        stack.append('')
    for token in tokens:
        if token == '..':
            if len(stack) == 0 or stack[-1] =='..':
                stack.append(token)
            elif stack[-1]!='':
                stack.pop()
        else:
            stack.append(token)
    if len(stack) == 1 and stack[-1] == '':
        return '/'
    return '/'.join(stack)

def isImportant(token):
    return token != '.' and len(token) > 0

