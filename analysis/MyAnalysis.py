class MyAnalysis :
    def mix(self,m1,m2,x1,x2,y1,y2,z1,z2):
        if ((y1 == 'NO') | (y2 == 'NO')) & ((z1 == 'NO') | (z2 == 'NO')) :
            all = m1 + m2 + x1 + x2
            you2 = 'NO'
            you3 = 'NO'
        elif ((y1 != 'NO') & (y2 != 'NO')) & ((z1 == 'NO') | (z2 == 'NO')) :
            all = m1 + m2 + x1 + x2 + y1 + y2
            you2 = y1 + y2
            you3 = 'NO'
        elif ((y1 == 'NO') | (y2 == 'NO')) & ((z1 != 'NO') | (z2 != 'NO')) :
            all = m1 + m2 + x1 + x2 + z1 + z2
            you2 = 'NO'
            you3 = z1 + z2
        else :
            all = m1 + m2 + x1 + x2 + y1 + y2 + z1 + z2
            you2 = y1 + y2
            you3 = z1 + z2

        e = all.count('E')
        i = all.count('I')

        a = all.count('A')
        c = all.count('C')

        o = all.count('O')
        s = all.count('S')

        l = all.count('L')
        h = all.count('H')

        new = ''
        if e > i :
            new = 'E'
        elif e < i :
            new = 'I'
        else :
            new = m1[0]

        if a > c :
            new = new + 'A'
        elif a < c :
            new = new + 'C'
        else :
            new = new + m1[1]

        if o > s :
            new = new + 'O'
        elif o < s :
            new = new + 'S'
        else :
            new = new + m2[0]

        if l > h :
            new = new + 'L'
        elif l < h :
            new = new + 'H'
        else :
            new = new + m2[1]

        result = {
            'my': m1+m2,
            'you1': x1+x2,
            'you2': you2,
            'you3': you3,
            'we': new
        }
        return result

if __name__ == '__main__' :
    MyAnalysis().mix('EC','OL','IC','OL');