common = ['34', '.0000000011']
rare = ['22', '.0000000016']
epic = ['10', '.0000000022']
legendary = ['5', '.0000000044']
multiplier = .30
time = 1

c = int(common[0]) * float(common[1]) * time * multiplier
r = int(rare[0]) * float(rare[1]) * time * multiplier
e = int(epic[0]) * float(epic[1]) * time * multiplier
l = int(legendary[0]) * float(legendary[1]) * time * multiplier
print ("{:.11f}".format(c) )
print ("{:.11f}".format(r) )
print ("{:.11f}".format(e) )
print ("{:.11f}".format(l) )

print ("{:.11f}".format((c+r+e+l) * 60 *60) )