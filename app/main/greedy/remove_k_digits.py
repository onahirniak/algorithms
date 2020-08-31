class RemoveKDigits():
    def remove_digits(self, k, num):
        if k >= len(num):
            return '0'

        stack = []

        for digit in num:
            while stack and stack[-1] > digit and k > 0:
                stack.pop()
                k -= 1

            stack.append(digit)

        if k > 0:
            stack = stack[0:k * (-1)]

        return ''.join(stack).lstrip('0') or '0'