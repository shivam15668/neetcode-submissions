class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] > h:
                index = stack.pop()
                height = heights[index]
                if stack:
                  width = i- stack[-1] - 1
                else:
                  width = i
                area = height * width
                max_area = max(max_area, area)
            stack.append(i)
        return max_area