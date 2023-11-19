import inspect

triplets = [
    ['t','u','p'],
    ['w','h','i'],
    ['t','s','u'],
    ['a','t','s'],
    ['h','a','p'],
    ['t','i','s'],
    ['w','h','s']
]


def recoverSecret(triplets):
    # Create a graph
    graph = {}
    for triplet in triplets:
        for char in triplet:
            if char not in graph:
                graph[char] = set()
    print(graph)
    # Add edges to the graph
    for triplet in triplets:
        graph[triplet[0]].add(triplet[1])
        graph[triplet[1]].add(triplet[2])
    print(graph)
    # Perform topological sort
    visited = set()
    result = []

    def visit(node, depth=0):
        print_stack_count()
        print(f"{tabWriter(depth)}Now visiting {node} ")
        if node not in visited:
            visited.add(node)
            for neighbour in graph[node]:
                print(f"{tabWriter(depth)}about to visit {neighbour}")
                visit(neighbour)
                depth += 1

            print(f"{tabWriter(depth)}prepending neighbor {node} to result.")
            result.insert(0, node)
            print(f"{tabWriter(depth)}Now exiting node {node}")
            print(result)
            print_stack_count()

    def tabWriter(numberOfTabs):
        return "*\t"*numberOfTabs

    def print_stack_count():
        # Count the number of frames in the current stack
        stack_count = len(inspect.stack())
        # print(f"Number of frames on the stack: stack count: {stack_count} node:")

    def example_function():
        # Call the function to print stack count from within another function
        print_stack_count()

    # Calling the function
    example_function()

    for node in graph:
        visit(node)
    print(visited)
    print(result)
    return ''.join(result)

print(recoverSecret(triplets))