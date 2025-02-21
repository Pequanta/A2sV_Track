# Problem: Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/

class ProductOfNumbers:

    def __init__(self):
        self.pre_product = [1]
        self.temp_val = 1


    def add(self, num: int) -> None:
        if num == 0:
            self.pre_product = [1]
            self.temp_val = 1
        else:
            self.temp_val *= num
            self.pre_product.append(self.temp_val)


    def getProduct(self, k: int) -> int:
        if k + 1> len(self.pre_product):
            return 0
        return self.pre_product[-1] // self.pre_product[-(k + 1)]

        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)