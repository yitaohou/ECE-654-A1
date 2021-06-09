import ast
import os

#getDepth function implement a method to output a list of layers of all the If/For/while... statements at
def getDepth(root, depth, list, parent=True):
    for child in ast.iter_child_nodes(root):
        if isinstance(child, ast.If) or isinstance(child, ast.While) or isinstance(child, ast.For) or isinstance(child, ast.AsyncFor) or isinstance(child,ast.With)  or isinstance(child, ast.AsyncWith):
            if parent:
                depth = 1
                list.append(depth)
            else:
                depth += 1
                list.append(depth)
            getDepth(child, depth,list, parent=False)
            depth = depth - 1

#class collectName is used to traverse all the nodes, and collect all associated identifier
class collectName(ast.NodeVisitor):
   def visit_Module(self, node):
     self.names = set()
     self.generic_visit(node)
     return self.names
     #print (self.names)
   def visit_Name(self, node):
     self.names.add(node.id)

def checkingFunction(testcode):
    list = [1]
    Satisfied = True

    tc_visit = collectName()
    # Parse the ast
    tc_ast = ast.parse(testcode)

    #Checking the nested structure
    getDepth(tc_ast,0,list)
    if max(list) >= 4:
        print("Failed: Nested structure greater than 4")
        Satisfied = False

    #Checking the length of identifiers
    identifier = tc_visit.visit(tc_ast)
    for ids in identifier:
        if len(ids) == 13:
            print("Failed: id with length of 13 detected")
            Satisfied = False
            break

    #If 2 passed 2 analysis, print the pass state
    if Satisfied == True:
        print("Passed the AST Analysis")


path = "./Tests"
files = os.listdir(path)
for f in files:
    print("File Name:",f)
    fileName = path + "/" + f
    file = open(fileName, "r")
    checkingFunction(file.read())
    print('')
