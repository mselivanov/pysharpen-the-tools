"""
Module solves assignment from hackerrank

It's New Year's Day and everyone's in line for the Wonderland rollercoaster ride!
There are a number of people queued up, and each person wears a sticker indicating
their initial position in the queue.
Initial positions increment by  from  at the front of the line to  at the back.
Any person in the queue can bribe the person directly in front of them to swap positions.
If two people swap positions, they still wear the same sticker denoting their original
places in line.
One person can bribe at most two others.
Fascinated by this chaotic queue, you decide you must know the minimum number
of bribes that took place to get the queue into its current state!
"""

def bloom_filter(queue):
    "Function checks if queue re-arrange is possible"
    for current_idx, initial_idx in enumerate(queue):
        if ((current_idx + 1) - initial_idx) < -2:
            return False
    return True

def swap(queue, idx1, idx2):
    "Swaps elements in list"
    queue[idx1], queue[idx2] = queue[idx2], queue[idx1]

def make_move(queue, moves):
    "Function makes retrospective move along the queue"
    curr_idx = 0
    end_idx = len(queue)-1
    required_moves = 0
    while curr_idx < end_idx:
        if queue[curr_idx] > queue[curr_idx+1]:
            if queue[curr_idx] != curr_idx + 1:
                if moves[curr_idx] > 0:
                    swap(queue, curr_idx, curr_idx + 1)
                    required_moves += 1
                else:
                    raise ValueError('Too chaotic')
            else:
                raise ValueError('Too chaotic')
        curr_idx += 1
    return required_moves


def minimum_bribes(queue):
    "Calculate minimum bribes"
    if not bloom_filter(queue):
        print('Too chaotic')
        return
    required_bribes = 0
    moves = [2]*len(queue)
    current_queue = list(queue)
    while True:
        moves_made = 0
        try:
            moves_made = make_move(current_queue, moves)
            if moves_made == 0:
                break
            required_bribes += moves_made
        except ValueError:
            print('Too chaotic')
            return
    print(required_bribes)

def main():
    "Main function"
    minimum_bribes([1, 2, 5, 3, 7, 8, 6, 4])

if __name__ == '__main__':
    main()
#    t = int(input())
#
#    for t_itr in range(t):
#        n = int(input())
#        q = list(map(int, input().rstrip().split()))
#        minimumBribes(q)
