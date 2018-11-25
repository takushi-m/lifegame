import pyxel

diff = [
    [-1,-1]
    ,[-1,0]
    ,[-1,1]
    ,[0,-1]
    ,[0,1]
    ,[1,-1]
    ,[1,0]
    ,[1,1]
]

class App:
    def __init__(self):
        self.w = 16
        self.h = 12
        self.is_run = False
        self.px = 0
        self.py = 0
        pyxel.init(self.w*10, self.h*10, fps=8)

        self.map = [[0 for _ in range(self.w)] for _ in range(self.h)]

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        elif not self.is_run:
            if pyxel.btnp(pyxel.KEY_DOWN):
                self.py = (self.py+1)%self.h
            elif pyxel.btnp(pyxel.KEY_UP):
                self.py = (self.py-1+self.h)%self.h
            elif pyxel.btnp(pyxel.KEY_RIGHT):
                self.px = (self.px+1)%self.w
            elif pyxel.btnp(pyxel.KEY_LEFT):
                self.px = (self.px-1+self.w)%self.w
            elif pyxel.btnp(pyxel.KEY_A):
                self.map[self.py][self.px] = 1
            elif pyxel.btnp(pyxel.KEY_R):
                self.is_run = True
        elif self.is_run:
            map = [[0 for _ in range(self.w)] for _ in range(self.h)]
            for hi in range(self.h):
                for wi in range(self.w):
                    s = 0
                    for d in diff:
                        if self.h>hi+d[0]>=0 and self.w>wi+d[1]>=0:
                            s += self.map[hi+d[0]][wi+d[1]]
                    if s>3:
                        map[hi][wi] = 0
                    elif s<2:
                        map[hi][wi] = 0
                    elif s==3:
                        map[hi][wi] = 1
                    elif s==2 and self.map[hi][wi]==1:
                        map[hi][wi] = 1
            self.map = map


    def draw(self):
        pyxel.cls(0)
        for hi in range(self.h+1):
            pyxel.line(0, 10*hi, self.w*10, 10*hi, 1)
        for wi in range(self.w):
            pyxel.line(10*wi, 0, 10*wi, self.h*10, 1)

        for hi in range(self.h):
            for wi in range(self.w):
                if self.map[hi][wi]==1:
                    pyxel.rect(wi*10, hi*10, (wi+1)*10, (hi+1)*10, 11)

        if not self.is_run:
            pyxel.rect(self.px*10, self.py*10, (self.px+1)*10, (self.py+1)*10, 8)

if __name__ == '__main__':
    App()
