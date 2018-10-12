import re

_unum_re = re.compile("[0-9]+[ ]*[-]?") #(@"^\d$");

def sanoqu(esli):
	oqughan = esli
	oqughan = _unum_re.sub(_numstr2str, esli)
	return oqughan

def _numstr2str(mg):
	isninchi = False
	innumstr= mg.group(0)
	numstr = innumstr.strip()
	if innumstr.endswith("-"):
		numstr = innumstr[0:-1].strip()
		isninchi = True
	slen = len(numstr)
	if slen > 18:
		return "xane sani on sekkizdin yuqiri bolmisun"
	if numstr == "0":
		return "nöl"

	strstr = ""
	i = 0


	while i < slen:
		digit = numstr[i]
		if (slen - i) % 3 == 0 or (slen - i) % 3 == 1:
			if digit == '1':
				strstr = strstr + "bir "
			elif digit == '2':
				strstr = strstr + "ikki "
			elif digit == '3':
				strstr = strstr + "üch "
			elif digit == '4':
				strstr = strstr + "töt "
			elif digit == '5':
				strstr = strstr + "besh "
			elif digit == '6':
				strstr = strstr + "alte "
			elif digit == '7':
				strstr = strstr + "yette "
			elif digit == '8':
				strstr = strstr + "sekkiz "
			elif digit == '9':
				strstr = strstr + "toqquz "
			elif digit == '0':
				pass
			else:
				return "sandin bashqa herp belgilerni kirgüzmeng!"
		if (slen - i) % 3 == 2:
			if digit == '1':
				strstr = strstr + "on "
			elif digit == '2':
				strstr = strstr + "yigirme "
			elif digit == '3':
				strstr = strstr + "ottuz "
			elif digit == '4':
				strstr = strstr + "qiriq "
			elif digit == '5':
				strstr = strstr + "ellik "
			elif digit == '6':
				strstr = strstr + "atmish "
			elif digit == '7':
				strstr = strstr + "yetmish "
			elif digit == '8':
				strstr = strstr + "seksen "
			elif digit == '9':
				strstr = strstr + "toqsan "
			elif digit == '0':
				pass
			else:
				return "sandin bashqa herp belgilerni kirgüzmeng!"
		if (slen - i) % 3 == 0 and numstr[i] != '0':
			strstr = strstr + "yüz "
		if (slen - i) / 16 == 1 and (slen - i) % 16 == 0:
			if numstr[slen - 16] == '0' and numstr[slen - 17] == '0' and numstr[slen - 18] == '0':
				continue
			else:
				strstr = strstr + "tirliyarda "
		if (slen - i) / 13 == 1 and (slen - i) % 13 == 0:
			if numstr[slen - 13] == '0' and numstr[slen - 14] == '0' and numstr[slen - 15] == '0':
				continue
			else:
				strstr = strstr + "tirliyun "
		if (slen - i) / 10 == 1 and (slen - i) % 10 == 0:
			if numstr[slen - 10] == '0' and numstr[slen - 11] == '0' and numstr[slen - 12] == '0':
				continue
			else:
				strstr = strstr + "miliyard "
		if (slen - i) / 7 == 1 and (slen - i) % 7 == 0:
			if numstr[slen - 7] == '0' and numstr[slen - 8] == '0' and numstr[slen - 9] == '0':
				continue
			else:
				strstr = strstr + "miliyun "
		if (slen - i) / 4 == 1 and (slen - i) % 4 == 0:
			if numstr[slen - 4] == '0' and numstr[slen - 5] == '0' and numstr[slen - 6] == '0':
				continue
			else:
				strstr = strstr + "ming "
		i += 1
	if isninchi:
		strstr = strstr.strip()
		if strstr.endswith("i") or strstr.endswith("e"):
			strstr = strstr[0:- 1]
		strstr = strstr + "inchi "
	return strstr


if __name__ == '__main__':
    esli ="119276-yili 12 -ayning 25 - küni. 12 yashliq kichik bala, 105-qewettiki öyide kitab oqup olturatti."
    oqulghan = sanoqu(esli)
    print(esli)
    print(oqulghan)
