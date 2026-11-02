import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def generate_codes(root, code, huffman_codes):
    if root is None:
        return

    if root.char is not None:
        huffman_codes[root.char] = code if code else "0"
        return

    generate_codes(root.left, code + "0", huffman_codes)
    generate_codes(root.right, code + "1", huffman_codes)

n = int(input("Enter number of characters: "))

heap = []

for i in range(n):
    char = input("Enter character: ")
    freq = int(input("Enter frequency: "))
    heapq.heappush(heap, Node(char, freq))

while len(heap) > 1:
    left = heapq.heappop(heap)
    right = heapq.heappop(heap)

    new_node = Node(None, left.freq + right.freq)
    new_node.left = left
    new_node.right = right

    heapq.heappush(heap, new_node)

if heap:
    root = heap[0]
    huffman_codes = {}
    generate_codes(root, "", huffman_codes)

    print("\nHuffman Codes:")
    for char, code in huffman_codes.items():
        print(f"{char} : {code}")
else:
    print("No characters to encode.")