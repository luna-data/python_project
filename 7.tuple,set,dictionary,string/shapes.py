import turtle
turtle.speed(0)
turtle.bgcolor('black')

# 딕셔너리로 좌표 정보 저장

shapes = {'triangle': [(0, 100), (-100, -100), (100, -100)],
          'square': [(-50, 50), (-50, -50), (50, -50), (50, 50)],
          'pentagon': [(0, 100), (-95, 30), (-58, -80), (58, -80), (95, 30)],
          'hexagon': [(-60, 90), (-90, 30), (-60, -30), (60, -30), (90, 30), (60, 90)]
}

def draw_shape(shape_name):
    turtle.color('white')
    turtle.penup()
    coords = shapes[shape_name]
    turtle.goto(coords[0])
    turtle.pendown() 
    for coord in coords[1:]:
        turtle.goto(coord)
    turtle.goto(coords[0])

def draw_all_shapes():
    for shape_name in shapes :
        draw_shape(shape_name)
        turtle.penup()
        turtle.forward(150)
        turtle.pendown()

draw_all_shapes()
turtle.mainloop()