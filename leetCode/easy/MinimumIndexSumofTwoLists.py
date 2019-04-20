import sys


class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        res = []
        for item in list1:
            if item in list2:
                res.append(item)

        dres = {}
        for i in res:
            s = list1.index(i) + list2.index(i)
            dres[i] = s

        c = min(dres, key=dres.get)
        d = []
        for k, v in dres.items():
            if v == dres[c]:
                d.append(k)
        return d


if __name__ == "__main__":
    # list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    # list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    # list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    # list2 = ["KFC", "Shogun", "Burger King"]
    # list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    # list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    # so = Solution()
    # c = so.findRestaurant(list1, list2)
    print(sys.maxsize)


"""
        dictionary = {}
        ans = []
        minimum = sys.maxint
        
        for i in range(0, len(list1)) :
            dictionary[list1[i]] = i
        
        for i in range(0, len(list2)) :
            if list2[i] in dictionary :
                if i + dictionary[list2[i]] == minimum :
                    ans.append(list2[i])
                elif i + dictionary[list2[i]] < minimum :
                    ans = []
                    minimum = i + dictionary[list2[i]]
                    ans.append(list2[i])
        
        return ans
"""