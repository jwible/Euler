def calc(p100=0, p50=0, p20=0, p10=0, p5=0, p2=0, p1=0):
	#print (p100, p50, p20, p10, p5, p2, p1)
	return (p100*100 + p50*50 + p20*20 + p10*10 + p5*5 + p2*2 + p1*1)



solutions = 1
for p100 in range (2, -1, -1):
	if calc(p100)== 200:
		solutions+=1
	if calc (p100) < 200:
		for p50 in range (4, -1, -1):
			if calc(p100,p50) == 200:
				solutions+=1
			if calc(p100,p50) < 200:
				for p20 in range (10, -1, -1):
					if calc(p100,p50,p20) == 200:
						solutions+=1
					if calc(p100,p50,p20) <200:
						for p10 in range (20,-1,-1):
							if calc(p100,p50,p20,p10) == 200:
								solutions+=1
							if calc(p100,p50,p20,p10) <200:
								for p5 in range (40,-1,-1):
									if calc(p100,p50,p20,p10,p5) == 200:
										solutions+=1
									if calc(p100,p50,p20,p10,p5) <200:
										for p2 in range (100,-1,-1):
											if calc(p100,p50,p20,p10,p5,p2) == 200:
												solutions+=1
											if calc(p100,p50,p20,p10,p5,p2) <200:
												for p1 in range (200,-1,-1):
													if calc(p100,p50,p20,p10,p5,p2,p1) == 200:
														solutions+=1

print (solutions)
