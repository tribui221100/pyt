import turtle
import time

def say_hello():
    print("Hello World from greeter!")

def darling():
    # Setup screen
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("❤️ Trái tim tặng Anh Thư ❤️")

    # Setup turtle
    t = turtle.Turtle()
    t.speed(3)
    t.color("red", "pink")  # viền đỏ, fill hồng

    # Vẽ trái tim
    t.penup()
    t.goto(0, -100)
    t.pendown()

    t.begin_fill()
    t.left(50)
    t.forward(133)
    t.circle(50, 200)
    t.right(140)
    t.circle(50, 200)
    t.forward(133)
    t.end_fill()
    t.hideturtle()

    # Nhảy nhẹ (animation)
    for i in range(10):
        t.penup()
        t.goto(0, -100 + i*5)
        t.pendown()
        time.sleep(0.05)

    # Hiện chữ
    t.penup()
    t.goto(0, 150)
    t.color("pink")
    t.write("Tặng Anh Thư ^^^", align="center", font=("Comic Sans MS", 24, "bold"))

    # Giữ màn hình mở lâu hơn
    screen.update()
    print("Bấm Enter để thoát...")
    screen.mainloop()  # giữ cửa sổ mở cho đến khi đóng thủ công