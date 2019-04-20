class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """

        def getdemain(cpd):
            dicm = {}
            a = cpd.split()
            b = a[1].split('.')
            k = ''
            for i in range(len(b) - 1, -1, -1):
                k = b[i] + '.' + k
                if k[-1] == '.':
                    k = k[:-1]
                dicm[k] = a[0]
            return dicm

        n = []
        for cpd in cpdomains:
            n.append(getdemain(cpd))
        ans = {}
        for i in n:
            for k, v in i.items():
                if k in ans.keys():
                    ans[k] = int(ans[k]) + int(v)
                else:
                    ans[k] = v
        anslist = []
        for k, v in ans.items():
            a = str(v) + ' ' + k
            anslist.append(a)
        return anslist


if __name__ == "__main__":
    cpd = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    so = Solution()
    a = so.subdomainVisits(cpd)
    print(a)

    # cpd = "900 google.mail.com"
    #
    #
    # def getdemain(cpd):
    #     dicm = {}
    #     a = cpd.split()
    #     b = a[1].split('.')
    #     k = ''
    #     for i in range(len(b) - 1, -1, -1):
    #         k = b[i] + '.' + k
    #         if k[-1] == '.':
    #             k = k[:-1]
    #         dicm[k] = a[0]
    #     return dicm
    #
    #
    # print(getdemain(cpd))


    '''
            dictionary = dict()
        for i in cpdomains:
            self.updateDict(i,dictionary)
        result = []
        for key,value in dictionary.items():
            result.append(str(value)+" "+key)
        return result
    
    def updateDict(self,info,dictionary):
        result = info.split(" ")
        times = int(result[0])
        domains = result[1].split(".")
        for i in range(len(domains)):
            tempDomain = ".".join(domains[i:])
            if(tempDomain in dictionary):
                dictionary[tempDomain]+=times
            else:
                dictionary[tempDomain] = times
    '''
