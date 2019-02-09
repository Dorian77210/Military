#!/Python
# -*-coding:Utf-8-*
import pygame;

from random import *;
from pygame.locals import *;
from constantes import *;
from fonctions_classes import *;
def create_actors(file,fond,p_liste):
	global liste_objet;
	liste_objet = [];
	global screen;
	screen = Window(fond);
	liste_objet.append(screen);
	global perso1;
	if p_liste[0] == "m1":
		perso1 = Personnage("militaire1_bas.png","militaire1_haut.png","militaire1_gauche.png","militaire1_droite.png",P1_X,P1_Y,1);
	if p_liste[0] == "m2":
		perso1 = Personnage("militaire2_bas.png","militaire2_haut.png","militaire2_gauche.png","militaire2_droite.png",P1_X,P1_Y,1);
	if p_liste[0] == "r1":
		perso1 = Personnage("r1_bas.png","r1_haut.png","r1_gauche.png","r1_droite.png",P1_X,P1_Y,1);
	if p_liste[0] == "s1":
		perso1 = Personnage("s1_bas.png","s1_haut.png","s1_gauche.png","s1_droite.png",P1_X,P1_Y,1);
	if p_liste[0] == "s2":
		perso1 = Personnage("s2_bas.png","s2_haut.png","s2_gauche.png","s2_droite.png",P1_X,P1_Y,1);
	if p_liste[0] == "s3":
		perso1 = Personnage("s3_bas.png","s3_haut.png","s3_gauche.png","s3_droite.png",P1_X,P1_Y,1);
	if p_liste[0] == "s4":
		perso1 = Personnage("s4_bas.png","s4_haut.png","s4_gauche.png","s4_droite.png",P1_X,P1_Y,1);
	if p_liste[0] == "s5":
		perso1 = Personnage("s5_bas.png","s5_haut.png","s5_gauche.png","s5_droite.png",P1_X,P1_Y,1);
	liste_objet.append(perso1);


	global perso2;
	if p_liste[1] == "m2":
		perso2 = Personnage("militaire2_bas.png","militaire2_haut.png","militaire2_gauche.png","militaire2_droite.png", P2_X,P2_Y,2);
	if p_liste[1] == "m1":
		perso2 = Personnage("militaire1_bas.png","militaire1_haut.png","militaire1_gauche.png","militaire1_droite.png",P2_X,P2_Y,2);
	if p_liste[1] == "r1":
		perso2 = Personnage("r1_bas.png","r1_haut.png","r1_gauche.png","r1_droite.png",P2_X,P2_Y,2);
	if p_liste[1] == "s1":
		perso2 = Personnage("s1_bas.png","s1_haut.png","s1_gauche.png","s1_droite.png",P2_X,P2_Y,2);
	if p_liste[1] == "s2":
		perso2 = Personnage("s2_bas.png","s2_haut.png","s2_gauche.png","s2_droite.png",P2_X,P2_Y,2);
	if p_liste[1] == "s3":
		perso2 = Personnage("s3_bas.png","s3_haut.png","s3_gauche.png","s3_droite.png",P2_X,P2_Y,2);
	if p_liste[1] == "s4":
		perso2 = Personnage("s4_bas.png","s4_haut.png","s4_gauche.png","s4_droite.png",P2_X,P2_Y,2);
	if p_liste[1] == "s5":
		perso2 = Personnage("s5_bas.png","s5_haut.png","s5_gauche.png","s5_droite.png",P2_X,P2_Y,2);
	liste_objet.append(perso2);

	global niveau;
	if type(file) is str:
		niveau = Niveau(file);
		niveau.generer();
		niveau.afficher(liste_objet);
	elif type(file) is int:
		if file == 2:
			niveau = Niveau('n1');
			niveau.afficher2(liste_objet);
def update_render(game_screen,liste):

	for elt in liste:
		if type(elt) is Bullet and elt.id == 1:
			elt.update_bullet(delta_s,liste_objet,perso1,perso2,game_screen);
		elif type(elt) is Bullet and elt.id == 2:
			elt.update_bullet(delta_s,liste_objet,perso2,perso1,game_screen);
		game_screen.blit(elt.img, elt.rect);
	render_health_and_ammo(game_screen,perso1,perso2);

	pygame.display.flip();

def wait_end(vainqueur):

	end = render_end(game_screen,vainqueur);
	if end:

		not game;

def check_life():

	if perso1.health == 0:

		wait_end(perso2);

	if perso2.health == 0:

		wait_end(perso1);

def main():

	pygame.init();
	pygame.display.set_caption("Military versus");
	running = True;
	global game;
	game = False;
	accueil = False;
	selection = False;
	time = 0;
	time2 = 0;
	tps = 0;
	son = pygame.mixer.Sound("Dragon_Ball_Super_AMV_-_Courtesy_Call.wav");
	tps_selection = 0;
	liste_selection = [];
	liste_perso = ["m1","m2","r1","s1","s2","s3","s4","s5"];
	p_liste = [];
	perso_selected = 0;
	global delta_s;
	delta_s = 0;
	global game_screen;
	game_screen = pygame.display.set_mode((WIDTH, HEIGHT));

	pygame.key.set_repeat(30,30);
	while running:

		son.play();

		v = 0;

		choix = 0;

		accueil = True;

		game = False;

		selection = True;

		rect = Rectangle(5,55,(255,255,255));

		while accueil:
			perso_selected = 0;
			liste_selection = [];
			tps = 0;
			tps_selection = 0;
			p_liste = [];
			time = 0;
			time2 = 0;
			pygame.time.Clock().tick(FPS);

			for event in pygame.event.get():

				if event.type == QUIT:
					accueil = False;
					running = False;
					selection = False;

				if event.type == KEYDOWN:

					if event.key == K_SPACE:
						accueil = False;
						running = False;

					if event.key == K_F1:

						game = True;
						accueil = False;
						choix = 2;

					if event.key == K_F2:

						game = True;
						accueil = False;
						choix = 'n2';

					if event.key == K_F3:

						game = True;
						accueil = False;
						choix = 'n3';

					if event.key == K_F4:

						game = True;
						accueil = False;
						choix = 'n4';

			update_accueil(game_screen);
			pygame.display.flip();
		while selection:

			delta_s = pygame.time.Clock().tick(FPS / 2) / 1000.0;

			for event in pygame.event.get():

				if event.type == QUIT:
					selection = False;
					running = False;
					game = False;
					pygame.quit();
				if event.type == KEYDOWN:

					if event.key == K_KP1: selection = False;

					if event.key == K_z:

						rect.deplacer('haut');

					if event.key == K_s:

						rect.deplacer('bas');

					if event.key == K_RETURN:

						drawValidation(rect,game_screen,liste_selection);
						perso_selected += 1;
						p_liste.append(liste_perso[rect.id]);
						rect.deplacer('droite');

					if event.key == K_ESCAPE:
						selection = False;
						accueil = True;
						game = False;
						choix = 0;

			if perso_selected == 2:
				tps_selection += delta_s;
				print(tps_selection);
				if tps_selection > 2.0: selection = False;
			update_selection(game_screen,rect);
			pygame.draw.rect(game_screen,rect.color,(rect.x,rect.y,rect.width,rect.height),1);
			pygame.draw.rect(game_screen,rect.color, (WIDTH / 2,0 , 1, HEIGHT), 1);
			pygame.draw.rect(game_screen,rect.color, (0,40,WIDTH,1),1);
			for i in liste_selection:
				game_screen.blit(i[0], i[1]);
			pygame.display.flip();
		if choix != 0:

			if choix == 2:

				create_actors(choix, "route.png",p_liste);

			if choix == 'n2':

				create_actors(choix, "fond.jpg",p_liste);

			if choix == 'n3':

				create_actors(choix,"fond.jpg",p_liste);

			if choix == 'n4':

				create_actors(choix,"floor.png",p_liste);

		while game:

			delta_s = pygame.time.Clock().tick(FPS) / 1000;
			liste_key = pygame.key.get_pressed();
			for event in pygame.event.get():
				if event.type == QUIT:
					running = False;
					game = False;
				if event.type == KEYDOWN and event.key == K_ESCAPE:
					game = False;

			check_reload(perso1,perso2,delta_s);
			check_life();
			update_render(game_screen,liste_objet);
			update_actions(perso1,perso2,delta_s,liste_key,liste_objet);
			tps += delta_s
			generate_hearth(liste_objet,tps);
	return 1;
