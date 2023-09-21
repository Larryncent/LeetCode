def maxArea2(height) -> int:
    _max = 0
    n = len(height)
    s = set(height)
    rev_height = height.copy()
    rev_height.reverse()
    while len(s) > 0:
        max_height = max(s)
        print('max_height: ', max_height)
        if len([i >= max_height for i in height]) >= 2:
            for i in range(n):
                if height[i] >= max_height:
                    left_index = i
                    break
            for j in range(n - 1, 0, -1):
                if height[j] >= max_height:
                    right_index = j
                    break
            print('left_index:', left_index, 'right_index: ', right_index)
            width = right_index - left_index
            water = width*max_height
            print("width*max_height: ", water)
            if water > _max:
                _max = width*max_height
        s.remove(max_height)
    return _max
        
    
