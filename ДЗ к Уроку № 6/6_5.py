class Stationary:

    def __init__(self, title="Something that can draw"):
        self.title = title

    def draw(self):
        print(f'Just start drawing! {self.title}')


class Pen(Stationary):
    def draw(self):
        print(f'Just start drawing with Pen! {self.title}')


class Pencil(Stationary):
    def draw(self):
        print(f'Just start drawing with Pencil! {self.title}')


class Handle(Stationary):
    def draw(self):
        print(f'Just start drawing with Handle! {self.title}')

stat = Stationary()
stat.draw()

pen = Pen()
pencil = Pencil()
handle = Handle()

pen.draw()
pencil.draw()
handle.draw()
