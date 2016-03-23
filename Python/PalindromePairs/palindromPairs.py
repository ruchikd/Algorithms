class Solution:
	def palindromePairs(self, words):
		"""
		:type words: List[str]
		:rtype: List[List[int]]
		"""
		if words is None:
			return

		d = dict()
		palindromePairList = []
		for word1 in words:
			for word2 in words:
				wordStraight = word1+word2
				if wordStraight == wordStraight[::-1]:
					word1Pos = words.index(word1)
					word2Pos = words.index(word2)
					if (word1Pos != word2Pos):
						addWord = str(word1Pos) + "," + str(word2Pos)
						if addWord not in d.keys():
							d[addWord] = True
							palindromePairList.append([word1Pos, word2Pos])
				else:
					wordRev = word2+word1
					if wordStraight != wordRev:
						if wordRev == wordRev[::-1]:
							word1Pos = words.index(word1)
							word2Pos = words.index(word2)
							if (word1Pos != word2Pos):
								addWord = str(word2Pos) + "," + str(word1Pos)
								if addWord not in d.keys():
									d[addWord] = True
									palindromePairList.append([word2Pos, word1Pos])

		print palindromePairList


def main():
	words = ["abcd", "dcba", "lls", "s", "sssll"]

	sol = Solution()
	sol.palindromePairs(words)
	sol.palindromePairs(None)

	words = ["bat", "tab", "cat"]
	sol.palindromePairs(words)

	complexWord = ["deeabafjjegeajaajjc","head","bg","gfjadiheadidhb","ejhadfdbbf","gfgjjcheijghhbgi","bd","gj","faebidibahheheajhdad","cgfbbijhchgiagdjg","heegfahdei","afajcfbgbjcehjbajgch","fhdgf","fhfbidiehbd","acicifaaiaeda","egdcghfgiede","ihj","aieegchdhjggbaf","ahfaea","bfjjaei","iiahcdbddhhabhfa","fhdhifbhfijfjdhhaec","jjcaab","fgejaeicgcdb","ijeifhfaagbbhbgd","djgbh","bchbghbdhj","ihibdbede","aaieeg","bedidgaijhjffi","cii","bbfiehhaejhaihg","ebcfedjifefhaaich","dbhaebibchdai","gaeeabjeeefeba","feaiahffifhbjbjc","aibficccdgebha","caijihcaijbjdgh","fa","jajdhdgciciabf","jggijggefe","hieagiifgeiggcbda","hbdjhccf","bcifgjid","abidejifhfgagcbj","eie","dhgfcadbgi","ggbdadafdgdjaijbff","aafbefjjich","hhgjffdbhjjce","dccacijd","edaabga","jghcciedjeheecafjafi","hajhfbeade","ai","chehhhjbadd","higihhbia","h","daaffhigihffgib","hdchgcjfhehbdchjbfee","iehahgbd","hhbbhecee","hicchaicbcdcbghgbcb","ggehfjiacca","bicbj","iddagad","egjjajjfijicddghgjbd","fgdj","fdhadabhegefhiaaffj","jjdgd","jigefcbhfbah","fegif","edacai","chchigjif","ihdc","iichejea","ifeahhec","iicb","chhgjifbidccjh","jdbhjffj","dgghdhdhgjh","ggijbj","hac","gabch","acge","ihjdi","afbefigffcgg","jcdghaegagffiaa","fchbdbfgdgihgcbbf","afhehifegdggai","dhejd","bcdjaid","bfhacfgifgfbeiiadbj","cbjaiafefbiaha","fjdggbbdjfhggggi","adadhijfeddcfhcffcf","eebfbhjcfebfbiiii","bddjcheg","bbhbccagghhccbcadii","jjbdjhbi","aadicc","igigjecd","aigg","headbfabhi","aggf","gdibgfgdjf","ddejhdgaie","feigiedidjafibiiabeg","ihejc","dbhjdgceiajac","jgaddec","decf","jeahifda","ei","ceicjagifdajdaggbei","jdfegeagefjjd","ffjgej","abigcgfegii","cbia","ddbccgeiicad","ddjcedidfehhggjifcdc","djahchfjiaabcdfcghc","jd","egfhjgcdabgbijiaif","ebfagijiec","e","i","fdjechdehbg","hibdd","gcdcajhiiahgjebdef","cgebjdfeficigcbajeeg","fegihdbbgceeieja","fcfdeadbfgbg","idgb","feej","caefiaadhaeedfahjjg","gcjhgjajdjbacadiab","ceeahgafc","giidhhaedbhi","gfi","hggigegffeedd","bjaajbdecc","dcegegdigidghbfg","gdaehaagehc","ebcfe","hbihiaehibajbh","dd","chbddebaffaechfiafe","jgdabdhbae","ejffgfdehicgadjaada","ifih","ad","djjdifjgjjhdiaajefae","dfjabaihc","bdbgeefihdc","eijcghaccghehjheiife","hbd","ejhfehagcfdjfjc","gfiejeeeihfhhdfbga","agjiidgihh","gfhfhghccfjjd","ajg","jefebffddehjdgbjhece","jfgbecahdgheeeigbbbd","gcjgeaefb","geacffib","fbabhiag","hcdhdjh","eegaef","cbgd","fajjfgfeafbicic","cfcec","cjidg","c","becfafc","ceaifhebjcihifchccge","acjgbfb","eehfcdibhhdeaahghg","iajh","eh","dcbfgafj","fjfccjjd","jhgiga","cgddbjigg","ifdfhgddebjbhbdebceg","ghaaddiabgc","hhebbhcedi","gjji","hgjaaicfecdbhiaeeejf","ahdfechfgacaadgb","hegdcfffeghfbdaiah","jadegiij","behdhffcedh","jfagjgjabfggdebbgfbj","cffi","ggchfb","gf","afj","gdajgfjdeehcihbcbfc","bha","aifihgjehhji","jhbhagdcbebgedjib","dddgbcdfgcbcfh","bdcccdfiifaigg","eegbjdad","bijfhidcc","jfgdcbgbeidfbich","diacigecbeagij","ae","jeffgeccdjdfhchbfghb","eedjaejjaefdjbgae","jbj","hfajiiadb","ebce","difedbfejcaj","chbg","feidai","gjeihhc","afcbcdi","cgbhhaeahgh","eacejccfigche","iacbfjjag","iibhcgeidba","acjeie","cjejadcdiiiiie","jf","bdaegihihadedjbfjja","bheaefhedifefgcj","gjhehj","igbcedd","iiaebdgegiagi","jghjeghabfba","bddehbggjbgghbc","fbiidhjjg","jgdhhef","djbdcbciijbife","iaiajhjih","gbjcebdacaeg","ijbjjaahedhibjacjid","hfehjb","bfjejdfjedgbdccch","gcie","jbaahgidgbdbcjgccc","hgffjhgagabgdbjij","ecefhcgebh","da","acaajajfahf","gcghhjbiedghj","becgfjdbeicaiihfh","aadhhcjebagabeicjbdh","ieaahaej","g","hfeijjhfbidhbif","efbgbejjhiifbb","ajj","ciabaaadiagfjeaegg","jehcgdbbcdhc","d","fjeefeaffjj","edhb","jdg","bebacedgbjfdf","bhbfbdh","f","ebghcfdjgfdefjdffgdj","hecbeihfhehbgefhc","eibdacjdbha","jfehaibbagj","igaebgbdbjaehegjgdf","cjaiacffcjfadaahjgib","biajafegbgeeagafb","hgdgjcjigjgajfc","icebffehbfbdfb","aiibhdffaiebih","fgiffg","beffciih","eejibbd","dffhajefgibdbhcgjc","jbjbdaide","ihjfg","iga","ficacgiibich","chjehcgdaehb","gjibc","afigghidejad","heghbeddc","iib","dedbec","igdiaachjibbi","jjbdbbdifabdj","hegegcfbchedebgehg","bedhjddaiefgbjhgacb","eefiff","ijgebgdbii","cjffegfdcibgg","dggcacegag","jecaaed","ijffabbe","hhbfgbcaaifbdfii","dbiffejgjhab","bjdi","ibae","fddfacaicjgi","gcccjgdc","ejgbdddacidiejhf","fbebihdgagdcbibd","bdaef","eibbagafbjjcecb","eiihbggfddhaiabjbfb","hgheehaajggfjaij","cjhieife","cajabidhg","fdg","fgch","deggbid","dcbeaehjjige","hhbfjaifgd","geci","ahhfjfdihjjjceabedab","ibghbfdgfebfgdch","deaaachf","eic","dcdd","fgcjiciebcghgdejfj","igiiadcfdfcfiegfiaci","a","j","ciiaggebcdcfgejcjf","jibicii","cae","ejbg","dccagjaadceggh","dbd","hcjicggcjjfgebfgfdee","cjfcbiahajhb","edifbfhhjdaidhg","bhccbajifabehecaibhf","fidjjhecih","ehi","fibgg","hjeibehifibichbibeg","dbeacjdebe","egcg","hedadiidgacfhgh","jfccgcfhfajjbg","fbejjabchbbdcidfce","jb","ificfdf","afhdfefiedhfc","hidc","iaiafehddcg","fifijfjhhddeceeid","ghdecdfdbhdaf","aabafccbdiebjeffg","fhgeagdibbfab","igaighcjfaeffdeg","hfjijbfedbabebiebgd","bibbdbagibbhge","ghgcccdddijeafdbha","fdhfjfbfjhhhiahaeh","hhdbfdechadjbihd","bbaaabbihgc","fdddcgegcfjbdcfeidh","dggich","ebjgcff","fj","cha","ebajffdbj","efeiddggjdidadib","acbjbbah","addeaeaedh","eiehdjdiji","ffcgcghfeeg","eccjeheedecjiihhhj","gejhfcda","abj","fbbcfghghheabej","ijdiegbf","fg","fjgcgecgahhjhh","bcece","jhjidbjddeec","jfjfjfgefhh","eaggijiahffdihc","cfaaciegcefghd","afddbedfg","bigeagdicegh","djedccg","gaeeea","bajegadgii","ejibciihdeabdjbhai","eabhjieafedibcijbjg","aajggcigfhbhj","ccgjah","hfdih","ebgdgcfbeacgf","iibeehje","ibeeedjgdhbidaefa","bidjcijieeh","dahbeaajfeiidgi","dea","ggjigagch","fb","dghh","dbiefbihaieiaffbadc","gdhhf","hfeaicjeecfibhb","jbdahgghge","ebje","edhfbihhgegbhbfbidhh","bejdjjcj","bdjffgjdef","jchgidcff","edhccejjfbchiiabga","cegafghbdbaceiiaab","gddedgeefg","ieff","fgcddedaijahijcab","gichdibdhddh","gabfagfhd","jcfigahdchjaed","ic","dhhcfaajbabaij","hdgdjdce","djhg","eejfbcajhheaghbdaddf","jbajah","chjf","aaij","gagdhiiiacaiagib","hghdea","fedjiiahgiegbaiaibj","ahchacd","cacbddaafgee","cbfahb","fijfjbiecjc","ieddfiahjfaefcdhih","checfbejdhehjeaeaghh","gbiigiajehbghegaideg","bgh"]
	sol.palindromePairs(complexWord)

if __name__ == '__main__':
	main()