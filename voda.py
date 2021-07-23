import pygame

w = 1000
h = 500



pygame.init()
win = pygame.display.set_mode((w,h))

rects = []
piesky = []
voda = []

white = (255,255,255)
orange = (255, 165, 0)
blue = (173,216,230)

class Square:

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.rect = pygame.draw.rect(win, white, (10*x, 10*y, 10, 10))
		self.pos = [x-1, y-1]
		self.color = 'black'
		self.occupied_by = None


class Voda:
	def __init__(self, sqr):	
		self.sqr = sqr
		pygame.draw.rect(win, blue, self.sqr.rect)
		self.final = False

	def new_sqr(self, sqr):
		pygame.draw.rect(win, white, self.sqr.rect)
		self.sqr.occupied_by = None
		self.sqr = sqr
		self.sqr.occupied_by = 'voda'
		pygame.draw.rect(win, blue, self.sqr.rect)


	def check_neighbors(self):
			try:
				if rects[self.sqr.y+1][self.sqr.x].occupied_by!='piesok' and rects[self.sqr.y+1][self.sqr.x].occupied_by!='voda':
					self.new_sqr(rects[self.sqr.y+1][self.sqr.x])

					if rects[self.sqr.y+1][self.sqr.x].occupied_by!='piesok' and rects[self.sqr.y+1][self.sqr.x].occupied_by!='voda':
						self.new_sqr(rects[self.sqr.y+1][self.sqr.x])


				elif rects[self.sqr.y][self.sqr.x+1].occupied_by!='piesok' and rects[self.sqr.y][self.sqr.x+1].occupied_by!='voda':
					self.new_sqr(rects[self.sqr.y][self.sqr.x+1])


				elif rects[self.sqr.y][self.sqr.x-1].occupied_by!='piesok' and rects[self.sqr.y][self.sqr.x-1].occupied_by!='voda':
					self.new_sqr(rects[self.sqr.y][self.sqr.x-1])

				elif rects[self.sqr.y+1][self.sqr.x-1].occupied_by!='piesok' and rects[self.sqr.y+1][self.sqr.x-1].occupied_by!='voda':
					self.new_sqr(rects[self.sqr.y+1][self.sqr.x-1])	

				elif rects[self.sqr.y+1][self.sqr.x+1].occupied_by!='piesok' and rects[self.sqr.y+1][self.sqr.x+1].occupied_by!='voda':
					self.new_sqr(rects[self.sqr.y+1][self.sqr.x+1])	
			except:
				pass					
		



class Piesok:
	def __init__(self, sqr):
		self.sqr = sqr
		pygame.draw.rect(win, orange, sqr.rect)
		self.final = False

	def check_neighbors(self):
		if not self.final:
			try:
				if rects[self.sqr.y+1][self.sqr.x].occupied_by=='voda':
					old_sq = self.sqr
					voda.append(Voda(self.sqr))
					self.new_sqr(rects[self.sqr.y+1][self.sqr.x])
					old_sq.occupied_by = 'voda'
					for o in voda:
							if o.sqr == self.sqr:
								voda.remove(o)

				elif rects[self.sqr.y+1][self.sqr.x].occupied_by!='piesok':
					self.new_sqr(rects[self.sqr.y+1][self.sqr.x])

					if rects[self.sqr.y+1][self.sqr.x].occupied_by=='voda':
						old_sq = self.sqr
						voda.append(Voda(self.sqr))
						self.new_sqr(rects[self.sqr.y+1][self.sqr.x])
						old_sq.occupied_by = 'voda'
						for o in voda:
							if o.sqr == self.sqr:
								voda.remove(o)

					elif rects[self.sqr.y+1][self.sqr.x].occupied_by!='piesok':
						self.new_sqr(rects[self.sqr.y+1][self.sqr.x])
					 

				elif rects[self.sqr.y+1][self.sqr.x+1].occupied_by=='voda':
					old_sq = self.sqr
					voda.append(Voda(self.sqr))
					self.new_sqr(rects[self.sqr.y+1][self.sqr.x+1])
					old_sq.occupied_by = 'voda'
					for o in voda:
							if o.sqr == self.sqr:
								voda.remove(o)

				elif rects[self.sqr.y+1][self.sqr.x+1].occupied_by!='piesok':
					self.new_sqr(rects[self.sqr.y+1][self.sqr.x+1])

					if rects[self.sqr.y+1][self.sqr.x+1].occupied_by=='voda':
						old_sq = self.sqr
						voda.append(Voda(self.sqr))
						self.new_sqr(rects[self.sqr.y+1][self.sqr.x+1])
						old_sq.occupied_by = 'voda',
						for o in voda:
							if o.sqr == self.sqr:
								voda.remove(o)

					elif rects[self.sqr.y+1][self.sqr.x+1].occupied_by!='piesok':
						self.new_sqr(rects[self.sqr.y+1][self.sqr.x+1])

				elif rects[self.sqr.y+1][self.sqr.x-1].occupied_by=='voda':
					old_sq = self.sqr
					voda.append(Voda(self.sqr))
					self.new_sqr(rects[self.sqr.y+1][self.sqr.x-1])
					old_sq.occupied_by = 'voda'
					for o in voda:
						if o.sqr == self.sqr:
							voda.remove(o)


				elif rects[self.sqr.y+1][self.sqr.x-1].occupied_by!='piesok':
					self.new_sqr(rects[self.sqr.y+1][self.sqr.x-1])

					if rects[self.sqr.y+1][self.sqr.x-1].occupied_by=='voda':
						old_sq = self.sqr
						voda.append(Voda(self.sqr))
						self.new_sqr(rects[self.sqr.y+1][self.sqr.x-1])
						old_sq.occupied_by = 'voda'
						for o in voda:
							if o.sqr == self.sqr:
								voda.remove(o)

					elif rects[self.sqr.y+1][self.sqr.x-1].occupied_by!='piesok':
						self.new_sqr(rects[self.sqr.y+1][self.sqr.x-1])


			except IndexError:
				self.final = True

	def new_sqr(self, sqr):
		pygame.draw.rect(win, white, self.sqr.rect)
		self.sqr.occupied_by = None
		self.sqr = sqr
		self.sqr.occupied_by = 'piesok'
		pygame.draw.rect(win, orange, self.sqr.rect)







class Window:
	def __init__(self):
		for i in range(50):
			rects.append([])
			for j in range(100):
				rects[i].append(Square(j, i))



def OnClick1():
	event = pygame.mouse.get_pos()
	y = event[1]//10
	x = event[0]//10
	piesky.append(Piesok(rects[y][x]))
	rects[y][x].occupied_by = 'piesok'

def OnClick2():
	event = pygame.mouse.get_pos()
	y = event[1]//10
	x = event[0]//10
	voda.append(Voda(rects[y][x]))
	rects[y][x].occupied_by = 'voda'	
	





if __name__ == '__main__':
	wind = Window()
	running = True
	while running:
		mouse = pygame.mouse.get_pressed(3)
		if mouse[0]:
			OnClick1()
		if mouse[2]:
			OnClick2()


		everything = voda+piesky
		for p in everything:
			p.check_neighbors()
		pygame.display.update()

		for j in rects:
			for p in j:
				if p.occupied_by=='voda':
					pygame.draw.rect(win, blue, p.rect)
				elif p.occupied_by =='piesok':
					pygame.draw.rect(win, orange, p.rect)


		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				running = False
				break	