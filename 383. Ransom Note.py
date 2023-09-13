class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        a=[]
        b=[]
        check=0
        for i in ransomNote:
            a.append(i)
        for i in magazine:
            b.append(i)

        for i in a:
            if i in b:
                b.remove(i)
            else:
                check=1
                return False
                break
        if check==0:
            return True
