from solver import Solver
import api,random,threading,csv,itertools
from math import inf

api_key = "6762a10e-d948-4746-4558-08dab2e5ba74"   # TODO: Your api key here
# The different map names can be found on considition.com/rules
# TODO: You map choice here. Unless changed, the map "Suburbia" will be selected.
# map_name = "Suburbia" if random.randint(0,2)==0 else "Fancyville"
# TODO: You bag type choice here. Unless changed, the bag type 1 will be selected.
# bag_type = random.randint(1,5)
threads = 200

map_name = "Suburbia"


best_scores = []
best_scoresD = {}
maxScore=-inf
played_games=0
f = open(map_name+"RandNEW.csv", 'w')
writer = csv.writer(f)

maxVals=[0 for i in range(31)]
maxchoices=[]

header=["score","bag_type","recycleRefundChoice","refundAmountMultiplicationFactor","choices1","choices2","choices3","choices4","choices5","choices6","choices7","choices8","choices9","choices10","choices11","choices12","choices13","choices14","choices15","choices16","choices17","choices18","choices19","choices20","choices21","choices22","choices23","choices24","choices25","choices26","choices27","choices28","choices29","choices30","choices31"]
writer.writerow(header)
v = [0, 1, 2]

def main():
	# print("Starting game...")
	global played_games, best_scores, best_scoresD, map_name,maxScore,maxchoices

	while True:

		# map_name = "Suburbia" if random.randint(0,2)==0 else "Fancyville"
		response = api.mapInfo(api_key, map_name)
		days = 31 if map_name == "Suburbia" or map_name == "Fancyville" else 365

		ch=[0 for i in range(days)]
		# random shit happens here x
		for i in range(days):
			ch[i]=random.randint(0,10)
			if ch[i]<0:
				ch[i]=0
		
		bag_type = 2
		recycleRefundChoice = True
		refundAmountMultiplicationFactor = random.random()
		# best_scores.append(score)
		# best_scores.sort(reverse=True)
		# best_scores=best_scores[:10]
		# if score not in best_scoresD.keys():
		# 	best_scoresD[score]=submit_game_response

		try:
			solver = Solver(game_info=response)
			solution = solver.Solve(bag_type, days, ch, recycleRefundChoice, refundAmountMultiplicationFactor)
			submit_game_response = api.submit_game(api_key, map_name, solution)
			score = submit_game_response["score"]
			row = [score,bag_type,recycleRefundChoice,refundAmountMultiplicationFactor]
			row.extend(ch)
			writer.writerow(row)
			played_games+=1
			if score>maxScore:
				maxchoices=ch
				maxScore=score
			print("Game #{}: Score: {}".format(played_games, maxScore),ch)
			f2 = open(map_name+"resultRand.txt", 'w')
			f2.write("Game #{}: Score: {}\n".format(played_games, maxScore))
			# print(submit_game_response)
			f2.write(str(maxchoices))
			f2.close()

		except:
			pass

		# print("Game finished game "+str(played_games)+" with score: " + str(score))
		# print("\n\n\n\n\n\nBest scores: "+str(best_scores),"out of "+str(played_games)+" games")
		# print("Best score: "+str(best_scores[0])+" with "+str(best_scoresD[best_scores[0]]))

if __name__ == "__main__":
	for i in range(threads):
		threading.Thread(target=main).start()
