import math

def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))

# En lugar de factorint, usar is_prime


n = 352189612438784047320754903106372002809877965719588610950180565262740960705788381566578345723325074804073747981488556714699194183628557150903839852453543700776971896448650422022044960974232637963499485064773137220336653165714273408753468196975611814144214482908258123395290626550717602601895666745644709508591571302894106487383195731091217527995774179358090943421864881850666765491934935419093710096767868514339375941764521600704560564724716373816013966194185050357691082654919969371044174479415710416530800029987261822155401485231590655607419352265580910531638967882492680615189164541617995862933344817766381378089

#firstnumber = 2**128
firstnumber = 340282366920938463463374607435568211456
checkpoints = firstnumber
cont = 0
while firstnumber < 2**129:
	if firstnumber == checkpoints:
		print("Checkpoint", firstnumber)
		checkpoints = firstnumber + 100000000
	if n % firstnumber == 0:
		cont += 1
		print("First prime", firstnumber)
		if cont == 16:
			break
	firstnumber += 1
	
