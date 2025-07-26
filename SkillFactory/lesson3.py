class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)


root = TreeNode("C:")

documents = TreeNode("Documents")
root.add_child(documents)
documents.add_child(TreeNode("Homework.docx"))
documents.add_child(TreeNode("Report.docx"))

pictures = TreeNode("Pictures")
root.add_child(pictures)
pictures.add_child(TreeNode("Summer.jpg"))
pictures.add_child(TreeNode("Winter.jpg"))

root.add_child(TreeNode('secret.key'))


def print_file_system(node, indent=""):
    print(indent + node.name + ("/" if (not node.children else "\\"))
    if node.children:
        for
    child in node.children:
    print_file_system(child, indent + "  ")

    print_file_system(root)