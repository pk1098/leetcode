class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        product = 0
        ans = 0
        last_product_negative= 0
        flag = 0
        negative_count = 0
        negative_value = []
        index = 0
        for value in nums:
            index = index + 1
            if value<0 and flag==0:
                flag = 1
                negative_count += 1
                last_product_negative = product
                negative_value.append(last_product_negative)
                if ans < last_product_negative:
                    ans = last_product_negative
                product = 0
            elif value<0 and flag==1:
                flag = 0
                negative_count += 1
                last_product_negative = product + 2 + last_product_negative
                negative_value.append(last_product_negative-1)
                if ans < last_product_negative:
                    ans = last_product_negative
                product = last_product_negative
            elif value>0:
                product = product + 1
                if ans < product:
                    ans = product
            elif value == 0 and index!=(len(nums)):
                if flag==1 and ((negative_count-1)>0 and (negative_count-1)%2==0):
                    ans = last_product_negative + product - negative_value[0] if (last_product_negative + product - negative_value[0])>ans else ans
                product = 0
                last_product_negative= 0
                flag = 0
                negative_count = 0
                negative_value.clear()
                
        # print(negative_value)
        if flag==1 and ((negative_count-1)>0 and (negative_count-1)%2==0):
            ans = last_product_negative + product - negative_value[0] if (last_product_negative + product - negative_value[0])>ans else ans
        return ans
                
        
                
            
        