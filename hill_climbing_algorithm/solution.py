
from typing import *
import dijkstra as di


def main():
    with open("./input.txt") as f:
        counter = 0
        graph: di.Graph = di.Graph()
        start = ""
        end = ""
        lines = list(map(lambda x: x.strip("\n"),f.readlines()))
        grid = [] # y, x
        for line in lines:
            row = []
            for letter in line:
                if letter == "S":
                    start = "S" + str(counter)
                if letter == "E":
                    end = "E" + str(counter)
                row.append(letter + str(counter))
                counter +=1
            grid.append(row)
        for row in grid:
            graph = connect_row(graph, row)
        for i in range(len(grid)-1):
            row_now = grid[i]
            row_next = grid[i+1]
            graph = connect_rows(graph, row_now, row_next)
        dijkstra = di.DijkstraSPF(graph, start)
        #print(graph)
        path = dijkstra.get_path(end)
        print("PATH: ", path)
        print("PATH LEN: ", len(path)-1)

def connect_row(graph: di.Graph, row):
    for i in range(len(row)-1):
        node_a = row[i]
        node_b = row[i+1]
        letter_a = node_a[0]
        letter_b = node_b[0]
        if letter_a == "S":
            letter_a = "a"
        if letter_b == "S":
            letter_b = "a"
        if letter_a == "E":
            letter_a = "z"
        if letter_b == "E":
            letter_b = "z"
        val_a = ord(letter_a)
        val_b = ord(letter_b)
        weight = 1
        if val_a >= val_b:
            graph.add_edge(node_a, node_b, weight)
        if val_b >= val_a:
            graph.add_edge(node_b, node_a, weight)
        if abs(val_a-val_b)<=1:
            graph.add_edge(node_a, node_b, weight)
            graph.add_edge(node_b, node_a, weight)
    return graph

def connect_rows(graph: di.Graph, row_now, row_next):
    for i in range(len(row_now)):
        node_a = row_now[i]
        node_b = row_next[i]
        letter_a = node_a[0]
        letter_b = node_b[0]
        if letter_a == "S":
            letter_a = "a"
        if letter_b == "S":
            letter_b = "a"
        if letter_a == "E":
            letter_a = "z"
        if letter_b == "E":
            letter_b = "z"
        val_a = ord(letter_a)
        val_b = ord(letter_b)
        weight = 1
        if val_a >= val_b:
            graph.add_edge(node_a, node_b, weight)
        if val_b >= val_a:
            graph.add_edge(node_b, node_a, weight)
        if abs(val_a-val_b)<=1:
            graph.add_edge(node_a, node_b, weight)
            graph.add_edge(node_b, node_a, weight)
        
    return graph


if __name__ == "__main__":
    main()