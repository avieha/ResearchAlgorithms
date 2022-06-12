import sys


def doc_to_html(module_name, output_html):
    m_name = module_name[:-3]
    module = __import__(m_name)
    func_names = []
    documentation = {}
    annotations = {}
    i = 0
    for name in dir(module):
        if name[0] != "_":
            func_names.append(name)
            func_attr = module.__getattribute__(name)
            annotations[name] = func_attr.__annotations__
            documentation[name] = func_attr.__doc__
            i += 1

    output = open(output_html, "w")

    # Adding input data to the HTML file
    output.write("<html>\n<head>\n<title>\n" +
                 "</title>\n</head> <body><h1>" + "Module name: " + module.__name__ + "\n" + "Documentation:" + module.__doc__)
    for func_name in func_names:
        output.writelines("Func name: " + func_name + "\n Doc: " + str(documentation[func_name])+"\n")
        output.writelines("Annotations: " + str(annotations[func_name]) + "\n")
    output.write("</h1>\n \
                   </body></html>")

    # Saving the data into the HTML file
    output.close()


if __name__ == '__main__':
    arguments = sys.argv
    # doc_to_html(arguments[1], arguments[2])
    # PATH: C:\Users\Aviem\PycharmProjects\ResearchAlgo\Ex2
    # COMMAND: python doc_to_html.py mymodule.py mydoc.html
    # doc_to_html("mymodule.py", "mydoc.html")
    # doc_to_html("mymodule2.py", "mydoc2.html")
