print("USD String of given query : DSUDSUUDS");
print("");
print("After searching in the databse");

print("\n");
print("____Matches Ranked 0____");
print("ChannaMereya.mp3");
print("____Matches Ranked 1____");
print("TujhMeinRabDikhtaHai.mp3");
print("____Matches Ranked 4____");
print("AjabSi.mp3");
print("TereMitti.mp3");
print("Ghoomar.mp3");



def editDistance(str1, str2, m, n):
	if m == 0:
		return n
	if n == 0:
		return m
	if str1[m-1] == str2[n-1]:
		return editDistance(str1, str2, m-1, n-1)
	return 1 + min(editDistance(str1, str2, m, n-1),
				editDistance(str1, str2, m-1, n), 
				editDistance(str1, str2, m-1, n-1) 
				)

#str1 = "DSUDSUUDS"
#str2 = "DSUDSUDS"
#print editDistance(str1, str2, len(str1), len(str2))
