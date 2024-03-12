import turtle

def draw_tree(branch_length, t, level):
    """
    Рекурсивно малює дерево Піфагора.

    :param branch_length: Довжина гілки.
    :param t: Екземпляр Turtle для малювання.
    :param level: Рівень рекурсії.
    """
    if level > 0:
        t.forward(branch_length)
        t.right(45)
        draw_tree(branch_length - 10, t, level - 1)
        t.left(90)
        draw_tree(branch_length - 10, t, level - 1)
        t.right(45)
        t.backward(branch_length)

def main():
    """
    Основна функція для малювання дерева Піфагора за допомогою Turtle.
    """
    level = int(input("Введіть рівень рекурсії (більше 0): "))
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    draw_tree(75, t, level)
    my_win.exitonclick()

if __name__ == "__main__":
    main()
