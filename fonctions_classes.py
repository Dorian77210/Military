#!/Python
# -*-coding:Utf-8-*
import pygame;
from pygame.locals import *;
from constantes import *;
import random;
global time;
time = 0;
global time2;
time2 = 0;
global tps;
tps = 0;
class Window:

	def __init__(self,img):

		self.img = pygame.image.load(img).convert();
		self.rect = self.img.get_rect();
		self.height = HEIGHT;
		self.width = WIDTH;

class Personnage:


	def __init__(self,bas,haut,gauche,droite,x,y,idi):

		self.bas = pygame.image.load(bas).convert_alpha();
		self.haut = pygame.image.load(haut).convert_alpha();
		self.droite = pygame.image.load(droite).convert_alpha();
		self.gauche = pygame.image.load(gauche).convert_alpha();
		self.img = self.bas;
		self.rect = self.img.get_rect();
		self.rect.center = ((x,y));
		self.munitions = MAX;
		self.id = idi;
		self.health = 5;
		self.mur = 4;

	def update_movements(self,touch,delta,liste):
		reveal = 0;
		if self.id == 1:
			p = Personnage("militaire1_bas.png","militaire1_haut.png","militaire1_gauche.png","militaire1_droite.png",self.rect.center[0],self.rect.center[1],self.id);
			v = 1;
			if touch == K_q:

				if self.rect.left > int(SPEED * delta):
					p.rect.left  -= int(SPEED * delta);

					for i in liste:

						if (type(i) is Element and p.rect.colliderect(i)) or (type(i) is Wall and \
							p.rect.colliderect(i)):			
							v = 0;

					if v:
						self.rect.left -= int(SPEED * delta);

						self.img = self.gauche;

			if touch == K_d:

				if self.rect.right < (WIDTH - int(SPEED * delta)):
					
					p.rect.x += int(SPEED * delta);
					for i in liste:

						if (type(i) is Element and p.rect.colliderect(i)) or (type(i) is Wall and \
							p.rect.colliderect(i)):	
							v = 0;
					if v:					
						self.rect.x += int(SPEED * delta);

						self.img = self.droite;

			if touch == K_s:
			
				if self.rect.bottom < (HEIGHT - int(SPEED * delta)):

					p.rect.bottom += int(SPEED * delta);

					for i in liste:

						if (type(i) is Element and p.rect.colliderect(i)) or (type(i) is Wall and \
							p.rect.colliderect(i)):	
							v = 0;
					if v:
						self.rect.bottom += int(SPEED * delta);

						self.img = self.bas;

			if touch == K_z:
			
				if self.rect.y > int(SPEED * delta):

					p.rect.y -= int(SPEED * delta);
					for i in liste:

						if (type(i) is Element and p.rect.colliderect(i)) or (type(i) is Wall and \
							p.rect.colliderect(i)):	
							v = 0;
					if v:
						self.rect.y -= int(SPEED * delta);
						self.img = self.haut;

			#gestion de l'apparition des points de vie
			for i in liste:

				if type(i) is Hearth and self.rect.colliderect(i):
					liste.remove(i);
					reveal = 1;
			if reveal:
				self.health = 5;
		else:

			p = Personnage("militaire1_bas.png","militaire1_haut.png","militaire1_gauche.png","militaire1_droite.png",self.rect.center[0],self.rect.center[1],self.id);
			v = 1;
			if touch == K_LEFT:

				if self.rect.left > int(SPEED * delta):
					p.rect.left  -= int(SPEED * delta);

					for i in liste:

						if (type(i) is Element and p.rect.colliderect(i)) or (type(i) is Wall and \
							p.rect.colliderect(i)):			
							v = 0;

					if v:
						self.rect.left -= int(SPEED * delta);

						self.img = self.gauche;

			if touch == K_RIGHT:

				if self.rect.right < (WIDTH - int(SPEED * delta)):
					
					p.rect.x += int(SPEED * delta);
					for i in liste:

						if (type(i) is Element and p.rect.colliderect(i)) or (type(i) is Wall and \
							p.rect.colliderect(i)):	
							v = 0;
					if v:					
						self.rect.x += int(SPEED * delta);

						self.img = self.droite;

			if touch == K_DOWN:
				
				if self.rect.bottom < (HEIGHT - int(SPEED * delta)):

					p.rect.bottom += int(SPEED * delta);

					for i in liste:

						if (type(i) is Element and p.rect.colliderect(i)) or (type(i) is Wall and \
							p.rect.colliderect(i)):	
							v = 0;
					if v:
						self.rect.bottom += int(SPEED * delta);

						self.img = self.bas;

			if touch == K_UP:
				
				if self.rect.y > int(SPEED * delta):

					p.rect.y -= int(SPEED * delta);
					for i in liste:

						if (type(i) is Element and p.rect.colliderect(i)) or (type(i) is Wall and \
							p.rect.colliderect(i)):	
							v = 0;
					if v:
						self.rect.y -= int(SPEED * delta);
						self.img = self.haut;

			for i in liste:

				if type(i) is Hearth and self.rect.colliderect(i):
					liste.remove(i);
					reveal = 1;
			if reveal:
				reveal = 0;
				self.health = 5;
	def military_attack(self,delta,liste):
		if self.munitions > 0:
			if self.img == self.bas:
				bullet = Bullet(self.rect.center,'bas',self.id);
			if self.img == self.haut:
				bullet = Bullet(self.rect.center,'haut',self.id);
			if self.img == self.gauche:
				bullet = Bullet(self.rect.center,'gauche',self.id);
			if self.img == self.droite:
				bullet = Bullet(self.rect.center,'droite',self.id);
			self.munitions -= 1;
			liste.append(bullet);

	def create_wall(self,liste):
		
		if self.mur > 0:
			v = 1;	#valeur de verification de pose de mur
			if self.img == self.droite:

				if self.rect.x < (WIDTH - SIZE_WALL):

					wall = Wall(self.rect.center[0] + SIZE_WALL,self.rect.center[1]);
					for i in liste:
						if (type(i) is Element and wall.rect.colliderect(i)) or (type(i) is Wall and wall.rect.colliderect(i)):
							v = 0;
							break;
					if v:
						liste.append(wall);
						self.mur -= 1;
			if self.img == self.gauche:

				if self.rect.x > SIZE_WALL:

					wall = Wall(self.rect.center[0] - SIZE_WALL,self.rect.center[1]);
					for i in liste:
						if (type(i) is Element and wall.rect.colliderect(i)) or (type(i) is Wall and wall.rect.colliderect(i)):
							v = 0;
							break;
					if v:
						liste.append(wall);
						self.mur -= 1;
			if self.img == self.bas:

				if self.rect.y < (HEIGHT - SIZE_WALL):

					wall = Wall(self.rect.center[0],self.rect.center[1] + SIZE_WALL);
					for i in liste:
						if (type(i) is Element and wall.rect.colliderect(i)) or (type(i) is Wall and wall.rect.colliderect(i)):
							v = 0;
							break;
					if v:
						liste.append(wall);
						self.mur -= 1;
			if self.img == self.haut:

				if self.rect.y > SIZE_WALL:

					wall = Wall(self.rect.center[0], self.rect.center[1] - SIZE_WALL);
					for i in liste:
						if (type(i) is Element and wall.rect.colliderect(i)) or (type(i) is Wall and wall.rect.colliderect(i)):
							v = 0;
							break;
					if v:
						liste.append(wall);
						self.mur -= 1;
	def reload(self,delta):
		global time;
		global time2;
		if self.id == 1:
			time += delta;
			if time > 3:
				self.munitions = 15;
				time = 0;
		else:
			time2 += delta;
			if time2 > 3:
				self.munitions = 15;
				time2 = 0;

class Wall:

	def __init__(self,x,y):

		self.img = pygame.image.load("barrel.png").convert_alpha();
		self.rect = self.img.get_rect();
		self.rect.center = ((x,y));

	def explose(self,perso1,perso2):

		p_centerX = self.rect.center[0];
		p_centerY = self.rect.center[1];
		p_perso_oneX = perso1.rect.center[0];
		p_perso_oneY = perso1.rect.center[1];

		p_perso_twoX = perso2.rect.center[0];
		p_perso_twoY = perso2.rect.center[1];
		if ((p_perso_oneX < p_centerX + 60) and (p_perso_oneX > p_centerX - 60)) \
		and ((p_perso_oneY < p_centerY + 60) and (p_perso_oneY > p_centerY - 60)):
			perso1.health -= 1;

		if ((p_perso_twoX < p_centerX + 60) and (p_perso_twoX > p_centerX - 60)) and ((p_perso_twoY < p_centerY + 60) and (p_perso_twoY > p_centerY - 60)):
			perso2.health -= 1;

class Bullet:

	def __init__(self,center,direction,idi):

		self.img = pygame.image.load("bubulet.png").convert_alpha();
		self.rect = self.img.get_rect();
		self.rect.center = center;
		self.update = 1;
		self.direction = direction;
		self.id = idi;

	def verifCollide(self,p_liste,perso,opponent):

			for i in p_liste:

				if type(i) is Element and self.rect.colliderect(i):
					p_liste.remove(self);
				if type(i) is Wall and self.rect.colliderect(i):
					i.explose(perso,opponent);
					p_liste.remove(i);

			if self.rect.colliderect(opponent.rect):

				p_liste.remove(self);
				opponent.health -= 1;

	def update_bullet(self,delta,liste,perso,opponent,p_screen):
		if self.id == 1:
			if self.direction == 'bas':

				self.rect.y += int(SPEED * delta * 3.5);
				if self.rect.y > HEIGHT:

					liste.remove(self);
			if self.direction == 'haut':

				self.rect.y -= int(SPEED * delta * 3.5);

				if self.rect.y < 0:
					liste.remove(self);
			if self.direction == 'droite':

				self.rect.x += int(SPEED * delta * 3.5);

				if self.rect.x > WIDTH:
					liste.remove(self);

			if self.direction == 'gauche':

				self.rect.x -= int(SPEED * delta * 3.5);

				if self.rect.x < 0:
					liste.remove(self);
			self.verifCollide(liste,perso,opponent);

		if self.id == 2:
			if self.direction == 'bas':

				self.rect.y += int(SPEED * delta * 3.5);
				if self.rect.y > HEIGHT:
					liste.remove(self);

			if self.direction == 'haut':

				self.rect.y -= int(SPEED * delta * 3.5);

				if self.rect.y < 0:
					liste.remove(self);
					
			if self.direction == 'droite':

				self.rect.x += int(SPEED * delta * 3.5);

				if self.rect.x > WIDTH:
					
					liste.remove(self);

			if self.direction == 'gauche':

				self.rect.x -= int(SPEED * delta * 3.5);

				if self.rect.x < 0:
					
					liste.remove(self);
			
			self.verifCollide(liste,perso,opponent);


class Niveau:

	def __init__(self,file):

		self.elements = 5;
		self.structure = 0;
		self.file = file;

	def generer(self):
		
		with open(self.file,"r") as fichier:

			liste_fichier = [];

			for ligne in fichier:

				liste_ligne = [];

				for sprite in ligne:

					if sprite != '\n':

						liste_ligne.append(sprite);
				liste_fichier.append(liste_ligne);

			self.structure = liste_fichier;

	def afficher(self,liste):

		if self.file != 'n1':
			i = 0;

			for ligne in self.structure:

				j = 0;

				for sprite in ligne:

					x = j * 30;
					y = i * 30;
					if sprite == 'm':
					
						element = Element("caisse.png",x + 15,y + 15);
						liste.append(element);

					if sprite == 'n':

						element = Element("wall.png",x + 15,y + 15);
						liste.append(element);

					if sprite == 'b':

						element = Element("bed_jail.png",x + 10,y + 20);
						liste.append(element);

					if sprite == 'c':

						element = Element("bed_jail2.png", x + 10, y + 15);
						liste.append(element);

					if sprite == 't':

						element = Element("toilet.png", x + 15, y + 15);
						liste.append(element);

					if sprite == 's':

						element = Element("toilet2.png",x+15,y+15);
						liste.append(element);

					if sprite == 'd':

						element = Element("computers1.png",x+15,y+15);
						liste.append(element);

					if sprite == 'e':

						element = Element("computers2.png",x+15,y+15);
						liste.append(element);

					if sprite == 'f':

						element = Element("door.png",x+15,y+8);
						liste.append(element);

					if sprite == 'a':

						element = Element("tree.png",x+15,y+15);
						liste.append(element);

					if sprite == 'j':

						element = Element("bush.png",x+15,y+15);
						liste.append(element);
					j += 1;

				i += 1;

	def afficher2(self,liste):

		#on cree tout les objets qui nous interesse
		voiture1 = Element("car3.png",345,370);
		voiture2 = Element("car4.png",30,210);
		voiture3 = Element("car1.png",390,270);
		tank1 = Element("tank.png",330,125);
		house1 = Element("house_japan1.png",135,155);
		house2 = Element("house_japan1.png",225,155);
		wall1 = Element("stone_wall.png",14,180);
		wall3 = Element("stone_wall.png",50,180);

		liste.append(voiture1);
		liste.append(voiture2);
		liste.append(voiture3);
		liste.append(tank1);
		liste.append(house1);
		liste.append(house2);
		liste.append(wall1);
		liste.append(wall3);

class Element:

	def __init__(self,img,x,y):

		self.img = pygame.image.load(img).convert_alpha();
		self.rect = self.img.get_rect();
		self.rect.center = ((x,y));

class Hearth(Element):

	def __init__(self):

		Element.__init__(self,"health.png",(WIDTH/2),(HEIGHT/2));
		
class Rectangle:


	def __init__(self,x,y,color):

		self.x = x;
		self.y = y;
		self.color = color;
		self.width = 120;
		self.height = 40;
		self.move_y = 50;
		self.id = 0;
	def deplacer(self,direction):

		if direction == 'haut':

			if self.y > 70:

				self.y -= self.move_y;

				self.id -= 1;

		if direction == 'bas':

			if self.y < WIDTH - (self.move_y + 10):
				self.y += self.move_y;

				self.id += 1; 
		
		if direction == 'droite':

			self.x += (WIDTH / 2);
			self.y = 55;
			self.id = 0;
def update_actions(perso,perso2,delta,liste_key,liste):
	
	if liste_key[K_q]:

		perso.update_movements(K_q,delta,liste);

	if liste_key[K_d]:

		perso.update_movements(K_d,delta,liste);

	if liste_key[K_z]:

		perso.update_movements(K_z,delta,liste);

	if liste_key[K_s]:

		perso.update_movements(K_s,delta,liste);

	if liste_key[K_t]:

		perso.create_wall(liste);

	if liste_key[K_a]:

		perso.military_attack(delta,liste);

	if liste_key[K_e]:

		perso.reload(delta);

	if liste_key[K_RIGHT]:

		perso2.update_movements(K_RIGHT,delta,liste);

	if liste_key[K_LEFT]:

		perso2.update_movements(K_LEFT,delta,liste);

	if liste_key[K_UP]:

		perso2.update_movements(K_UP, delta,liste);

	if liste_key[K_DOWN]:

		perso2.update_movements(K_DOWN,delta,liste);

	if liste_key[K_KP0]:

		perso2.military_attack(delta,liste);

	if liste_key[K_KP1]:

		perso2.create_wall(liste);

def render_health_and_ammo(screen,perso1,perso2):

	hearth = pygame.image.load("health.png").convert_alpha();
	ammo = pygame.image.load("ammunition.png").convert_alpha();
	barrel = pygame.image.load("barrel2.png").convert_alpha();
	#rendu des points de vie des personnages
	for i in range(perso1.health):

		screen.blit(hearth, ((i*15), 0));

	i = perso2.health;
		
	while i > 0:

		screen.blit(hearth, ((i*15) + 350, 0));
		i -= 1;

	#rendue des munitions des personnages

	font = pygame.font.Font(None,20);
	mun_perso1 = font.render(":X" + str(perso1.munitions),1,(255,255,255));
	mun_perso2 = font.render(":X" + str(perso2.munitions),1,(255,255,255));
	mur_perso1 = font.render(":X" + str(perso1.mur),1,(255,255,255));
	mur_perso2 = font.render(":X" + str(perso2.mur),1,(255,255,255));

	screen.blit(ammo, (80,0));
	screen.blit(mun_perso1, (90,0));
	screen.blit(mur_perso1, (150,0));
	screen.blit(barrel, (135,0));


	screen.blit(ammo, (320,0));
	screen.blit(mun_perso2,(330,0));
	screen.blit(barrel,(275,0));
	screen.blit(mur_perso2,(290,0));
def render_end(screen,vainqueur):

	END = True;
	font = pygame.font.Font(None,30);
	if vainqueur.id == 1:
		texte = font.render("Le vainqueur est le joueur 1",1,(235,10,19));
	else:
		texte = font.render("Le vainqueur est le joueur 2",1,(235,10,19));

	texte2 = font.render("Press ESCAPE to go out...",1,(235,10,19));
	while END:
		for event in pygame.event.get():
			if event.type == KEYDOWN and event.key == K_ESCAPE:
				END = False;
			if event.type == QUIT:
				END = False;

		screen.blit(texte, (50,HEIGHT / 2 - 10));
		screen.blit(texte2,(50,HEIGHT / 2 + 10));
		pygame.display.flip();

	return 1;

def update_accueil(screen):

	font_versus = pygame.font.Font(None, 60);
	font_level = pygame.font.Font(None, 30);
	m1_gauche = pygame.image.load("militaire1_gauche.png").convert_alpha();
	m1_droite = pygame.image.load("militaire1_droite.png").convert_alpha();
	m2_gauche = pygame.image.load("militaire2_gauche.png").convert_alpha();
	m2_droite = pygame.image.load("militaire2_droite.png").convert_alpha();

	t1 = font_versus.render("VERSUS",1,(255,255,255));
	t2 = font_level.render("F1 : City",1,(255,255,255));
	t3 = font_level.render("F2 : Cargaisons",1,(255,255,255));
	t4 = font_level.render("F3 : Jail",1,(255,255,255));
	t5 = font_level.render("F4 : Forest",1,(255,255,255));
	screen.fill((141,39,32));
	screen.blit(m1_droite, (50,50));
	screen.blit(m2_gauche, (380,50));
	screen.blit(m2_droite, (50,380));
	screen.blit(m1_gauche,(380,380));
	screen.blit(t1,((WIDTH / 2) - 80, (HEIGHT / 2) - 30));
	screen.blit(t2,((WIDTH / 2) - 80, (HEIGHT / 2) + 20));
	screen.blit(t3, ((WIDTH / 2) - 80, (HEIGHT / 2) + 40));
	screen.blit(t4, ((WIDTH / 2) - 80, (HEIGHT / 2) + 60));
	screen.blit(t5, ((WIDTH / 2) - 80, (HEIGHT / 2) + 80));

def update_selection(p_screen,p_rect):
	#creation de tous les textes et autres
	font_choix = pygame.font.Font(None,25);
	text1 = font_choix.render("Joueur 1 : ",1,(255,255,255));
	text1bis = font_choix.render("Joueur 2 : ",1,(255,255,255));
	text2 = font_choix.render("Military 1",1,(255,255,255));
	text3 = font_choix.render("Military 2",1,(255,255,255));
	text4 = font_choix.render("Machine",1,(255,255,255));
	text5 = font_choix.render("Soldat 1",1,(255,255,255));
	text6 = font_choix.render("Soldat 2",1,(255,255,255));
	text7 = font_choix.render("Soldat 3",1,(255,255,255));
	text8 = font_choix.render("Soldat 4",1,(255,255,255));
	text9 = font_choix.render("Soldat 5",1,(255,255,255));
	m1 = pygame.image.load("militaire1_bas.png").convert_alpha();
	m2 = pygame.image.load("militaire2_bas.png").convert_alpha();
	r1 = pygame.image.load("r1_bas.png").convert_alpha();
	s1 = pygame.image.load("s1_bas.png").convert_alpha();
	s2 = pygame.image.load("s2_bas.png").convert_alpha();
	s3 = pygame.image.load("s3_bas.png").convert_alpha();
	s4 = pygame.image.load("s4_bas.png").convert_alpha();
	s5 = pygame.image.load("s5_bas.png").convert_alpha();

	p_screen.fill((141,39,32));
	p_screen.blit(text1,(10,20));
	p_screen.blit(text2, (40,65));
	p_screen.blit(m1,(10,60));
	p_screen.blit(text3, (40,115));
	p_screen.blit(m2,(10,110));
	p_screen.blit(text4,(40,165));
	p_screen.blit(r1,(10,160));
	p_screen.blit(text5,(40,215));
	p_screen.blit(s1,(10,210));
	p_screen.blit(text6,(40,265));
	p_screen.blit(s2,(10,260));
	p_screen.blit(text7,(40,315));
	p_screen.blit(s3,(10,310));
	p_screen.blit(text8,(40,365));
	p_screen.blit(s4,(10,360));
	p_screen.blit(text9,(40,415));
	p_screen.blit(s5,(10,410));


	p_screen.blit(text1bis,(WIDTH - 90,20));
	p_screen.blit(text2, (265,65));
	p_screen.blit(m1,(235,60));
	p_screen.blit(text3, (265,115));
	p_screen.blit(m2,(235,110));
	p_screen.blit(text4,(265,165));
	p_screen.blit(r1,(235,160));
	p_screen.blit(text5,(265,215));
	p_screen.blit(s1,(235,210));
	p_screen.blit(text6,(265,265));
	p_screen.blit(s2,(235,260));
	p_screen.blit(text7,(265,315));
	p_screen.blit(s3,(235,310));
	p_screen.blit(text8,(265,365));
	p_screen.blit(s4,(235,360));
	p_screen.blit(text9,(265,415));
	p_screen.blit(s5,(235,410));

def drawValidation(p_rect,p_screen,liste):

	f = pygame.font.Font(None,25);
	text1 = f.render("Ready",1,(0,255,0));
	coords = (text1,(p_rect.x + p_rect.width + 10, p_rect.y + 10));
	liste.append(coords);
def generate_hearth(liste,tps):

	if int(tps) % 15 == 0 and tps > 0:

		i = Hearth();
		liste.append(i);

def check_reload(perso1,perso2,delta_s):

	if perso1.munitions == 0:
		perso1.reload(delta_s);
	if perso2.munitions == 0:
		perso2.reload(delta_s);

def check_reload_mini_jeu(p,delta):

	if p.munitions == 0:
		p1.reload(delta);