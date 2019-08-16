with open('square.in') as f:
    # txt = f.read()
    # print(txt)
    x1, y1, x2, y2 = map(int, f.readline().split())
    x3, y3, x4, y4 = map(int, f.readline().split())
    max_x_ans = max(x1, x2, x3, x4)
    min_x_ans = min(x1, x2, x3, x4)
    min_y_ans = min(y1, y2, y3, y4)
    max_y_ans = max(y1, y2, y3, y4)
    ans = max((max_y_ans - min_y_ans), (max_x_ans - min_x_ans))
    print(ans**2)
    pw = open('square.out', 'w')
    pw.write(str(ans**2))
    pw.close()