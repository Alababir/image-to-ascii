from PIL import Image
def asciiConvert(image, type, saveas, scale):
    scale = 2

    # Abre e pega o tamanho
    img = Image.open(image)
    w,h = img.size

    # resize da imagem (reduz)
    img.resize((w//scale * 4, h//scale)).save("resized.%s" % type)

    # Abre a imagem
    img = Image.open("resized.%s" % type)
    w, h = img.size # get new width and height 


    # Lista com altura e largura
    grid = []
    for i in range(h):
        grid.append(["X"] * w)

    pix = img.load()


    for y in range(h):
        for x in range(w):
            if sum(pix[x,y]) == 0:
                grid[y][x] = "%"
            elif sum(pix[x,y]) in range(1,100):
                grid[y][x] = "X"
            elif sum(pix[x,y]) in range(100,200):
                grid[y][x] = "#"
            elif sum(pix[x,y]) in range(200,300):
                grid[y][x] = "i"
            elif sum(pix[x,y]) in range(300,400):
                grid[y][x] = ")"
            elif sum(pix[x,y]) in range(400,500):
                grid[y][x] = "/"
            elif sum(pix[x,y]) in range(500,600):
                grid[y][x] = "+"
            elif sum(pix[x,y]) in range(600,700):
                grid[y][x] = "*"
            elif sum(pix[x,y]) in range(700,750):
                grid[y][x] = "'"
            else:
                grid[y][x] = " "
                
    art = open(saveas, "w")

    for row in grid:
        art.write("".join(row)+"\n")

    art.close()

if __name__ == '__main__':
    asciiConvert("perfil.jpeg", "jpeg", "output.txt", "1")



