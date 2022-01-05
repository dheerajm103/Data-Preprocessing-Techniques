# Q1 	Create a string “Grow Gratitude

string1 = "Grow Gratitude" 

string1[0] # a) access the letter “G” of “Growth

len(string1)  # b) length of the string

string1.count("G")  # c) times “G” is in the string

# Q2  Create a string “Being aware of a single shortcoming within yourself is far more useful than being aware of a thousand in someone else.”

string2 = "Being aware of a single shortcoming within yourself is far more useful than being aware of a thousand in someone else."   
 
len(string2)  # a) 	Count the number of characters in the string
space = string2.count(' ')
space
char = len(string2) - space
char

# Q3) Create a string "Idealistic as it may sound, altruism should be the driving force in business, not just competition and a desire for wealth"

string3 = "Idealistic as it may sound, altruism should be the driving force in business, not just competition and a desire for wealth"

newstring = string3.split()  # a) one char of the word
newstring
newstring[0]

string3[0:3] # b) first three char

string3[-3:]  # c) last three char

# Q4)  create a string "stay positive and optimistic

string4 = "stay positive and optimistic"

string4.startswith("H") # a) string starts with “H”

string4.endswith("d")   # b)  string ends with  “d”

string4.endswith("c")   # c) string ends with “c”

# Q5) print " 🪐 " one hundred and eight times

print("🪐" * 108)

# Q6) to print " o " one hundred and eight times

print("o" * 108)

# Q7) 7.	Create a string “Grow Gratitude

string5 = "Grow Gratitude"

string5.replace( "Grow","Growth of")  #  Replace “Grow” with “Growth of”

# Q8) story was printed in a pdf

string6 = ".elgnujehtotniffo deps mehtfohtoB .eerfnoilehttesotseporeht no dewangdnanar eh ,ylkciuQ .elbuortninoilehtdecitondnatsapdeklawesuomeht ,nooS .repmihwotdetratsdnatuotegotgnilggurts saw noilehT .eert a tsniagapumihdeityehT .mehthtiwnoilehtkootdnatserofehtotniemacsretnuhwef a ,yad enO .ogmihteldnaecnedifnocs’esuomeht ta dehgualnoilehT ”.emevasuoy fi yademosuoyotplehtaergfo eb lliw I ,uoyesimorp I“ .eerfmihtesotnoilehtdetseuqeryletarepsedesuomehtnehwesuomehttaeottuoba saw eH .yrgnaetiuqpuekow eh dna ,peels s’noilehtdebrutsidsihT .nufroftsujydobsihnwoddnapugninnurdetratsesuom a nehwelgnujehtnignipeelsecno saw noil A"

mystring = string6[::-1] # reversing to get meaningful sentence
mystring
