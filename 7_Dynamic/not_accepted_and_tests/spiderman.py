



def get_order(arr, heights, directions):
    heights = [None] * len(arr)
    directions = [None] * len(arr)
    heights[0] = arr[0]
    heights[-1] = 0
    directions[0] = 1
    directions[-1] = -1

    for i in range(1, len(arr)):
        if arr[i] >= heights[i - 1]:
            directions[i] = -1
            heights[i] = heights[i - 1] - arr[i]
        else:
            directions[i] = 1
            heights[i] = heights[i-1] + arr[i]

        if i == len(arr) - 1:
            if heights[i] == 0:
                return directions
            else:
                pass

