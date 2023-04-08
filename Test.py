from pygame import*
window = display.set_mode((700, 500))
display.set_caption("First project")
#character coordinates
x = 100
y = 395
#character and background image
img1 = transform.scale(image.load('monkey_001.png'), (100, 100))
background = transform.scale(image.load("cave.png"), (700,500))
#we place the images on the application window
window.blit(background,(0,0))
window.blit(img1,(x2,y2))
#refresh the window
display.update()
time.delay(5000)


#hjslhasijlhkhjalsdkhjaskkdhajsdhl