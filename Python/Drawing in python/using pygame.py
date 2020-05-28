import pygame
pygame.init()
white = (255,255,255,255)
green = (0,255,0)
blue = (0,0,128)
black = ( 0,0,0)
red = (255,0,0)

x= 400
y= 400

display_surface = pygame.display.set_mode((x,y))
pygame.display.set_caption("Drawing")
display_surface.fill(white)

pygame.draw.polygon(display_surface, blue,[(146,0),(291,106),(236,277),(56,277),(0,166)])

pygame.draw.line(display_surface, green,(60,300),(120,300),4)
pygame.draw.circle(display_surface, green,(300,50),20,0)
pygame.draw.ellipse(display_surface, black,(300,250,40,80),1)
pygame.draw.rect(display_surface, black,(150,300,100,50))

#infinite loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()
