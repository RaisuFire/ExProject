# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates



class Solution(object):

    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """



        def getbyid(id):
            for em in employees:
                if em.id == id:
                    return em
        em = getbyid(id)
        imp = em.importance
        if len(em.subordinates) == 0:
            pass
        print(em.subordinates)
        for i in em.subordinates:
            imp += self.getImportance(employees, i)
        return imp


if __name__ == "__main__":
    nums = [[1,5,[2,3]],[2,3,[]],[3,3,[]]]
    id = 1
    employees = []
    for i in nums:
        em = Employee(i[0], i[1], i[2])
        employees.append(em)
    # so = Solution()
    # imp = so.getImportance(employees, id)
    # print(imp)
