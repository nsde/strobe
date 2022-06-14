import os
import sys
import os.path
import webbrowser

def replacer(text: str, dictionary: dict) -> str:
    for k, v in dictionary.items():
        text = text.replace(k, v)
    return text

def lazy(path, ext):
    if not '.' in path:
        path = f'{path}.{ext}'
    return path

def render(inp: str, outp: str) -> None:
    inp = lazy(inp, 'dish')
    outp = lazy(outp, 'html')
    
    dish = open(inp).read()
    
    dish = replacer(dish, {
        '{': '<a href="',
        '|': '"><button>',
        '}': '</button></a>'
    })
    
    open(outp, 'w').write(dish)

def main():
    arg = sys.argv[1:]
    
    if not '--' in arg[0] and not '--' in arg[1]:
        render(arg[0], arg[1])
    
    if '--show' in arg:
        output_file = arg[1] if len(arg) == 3 else arg[0]
        output_path = os.path.join(os.path.dirname(__file__), lazy(output_file, 'html'))
        webbrowser.open(output_path)
        
        if '--temp' in arg:
            os.remove(output_path)

if __name__ == '__main__':
    main()