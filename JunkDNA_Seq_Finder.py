
class BP:
	str name = ""
	bool found = false


class Sequence:
	BP base_pairs = [] 
	int num_found = 0
	int size = 0

	all_found = false



#variables
S = Sequence()
G = []
min_junk_size = 5
num_bp_ins 
x = 0
y = 0


#import sequences
# S - sample being looked for
# G - seq being looked through

search_seq_size = G.size

while x < search_seq_size and S.num_found != S.size
	
	# if these two bases match
	if G[x] == S.base_pairs[y].name:

		# and there have been enough bases inserted between these two bases to have come from  "junk DNA"
		if min_junk_size < num_bp_ins:
			
			#say we found it, start checking the next base in the sequence being searched for, increase the tally of bases matching
			# then reset the counter determining validity of spaces between potential matches
			S.base_pairs[y].found = TRUE
			y = y + 1
			S.num_found = S.num_found + 1
			num_bp_ins = 0
		
		#otherwise, increase the number of bases in between matches
		else:		
			num_bp_ins = num_bp_ins + 1

	#if they've all been found, make note of it
	if S.num_found == S.size:
		S.all_found = TRUE

	#increase the counter
	x = x + 1
	






