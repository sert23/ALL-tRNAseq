import sys,os

fileI = open(sys.argv[1],'r')
cabecera = fileI.readline()

totales = {}
for line in fileI:
	line = line.strip().split("\t")
	name = line[0].split("-")[1].split(":")[0]
	type = line[0].split(":")[1]

	try:
		values = totales[name]
	except:
		values = [0,0]

	RCadj = float(line[3])

	if type=="tRNA__mature3p_fl":
		RCfl = values[0]+RCadj
		RCtotal = values[1] + RCadj
	
	else:
		RCfl = values[0]
		RCtotal = values[1] + RCadj

	totales[name] = [RCfl,RCtotal]

outFile = open(sys.argv[2],'a')
cabecera = "tRNA\tFL_RC\tTotalRC\tPercentage\n"
outFile.write(cabecera)
for element in totales:
	percentage = str((totales[element][0])/(totales[element][1])*100)
	escribir = element+"\t"+str(totales[element][0])+"\t"+str(totales[element][1])+"\t"+percentage+"\n"
	outFile.write(escribir)


outFile.close()
