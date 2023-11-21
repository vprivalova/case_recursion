import turtle


def color_tree(depth, size):
  turtle.colormode(255)
  cg = 255 - int(depth * (250/6)) % 255
  turtle.color(0, cg, 0)
  if depth == 0:
    turtle.forward(size)
  else:
    turtle.forward(size)
    turtle.right(45)
    color_tree(depth - 1, size / 2)
    turtle.left(90)
    color_tree(depth - 1, size / 2)
    turtle.right(45)
    turtle.backward(size)


turtle.left(90)
color_tree(6, 100)
turtle.done()
