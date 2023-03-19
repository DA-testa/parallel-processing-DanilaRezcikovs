# python3
import heapq

def parallel_processing(n, m, data):
    heap = [(0, i) for i in range(n)]
    output = []
    for i in range(m):
        t = data[i]
        start_time, thread_index = heapq.heappop(heap)
        output.append((thread_index, start_time))
        start_time += t
        heapq.heappush(heap, (start_time, thread_index))
    return output



def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result = parallel_processing(n, m, data)
    for thread_index, start_time in result:
        print(thread_index, start_time)



if __name__ == "__main__":
    main()
