import pygame

def displayText(txt: str, screen: pygame.display.set_mode):
    fonte = pygame.font.Font(None, 74)
    white = (255, 255, 255) # branco
    rendered_text = fonte.render(txt, True, white)

    txt_rect = rendered_text.get_rect(center = (100, 700))

    screen.blit(rendered_text, txt_rect)