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

map_name = "Sky Scrape City"

choices = [11, 48, 28, 95, 14, 21, 65, 87, 57, 66, 84, 57, 84, 7, 32, 39, 3, 62, 98, 48, 69, 54, 32, 22, 36, 75, 54, 71, 46, 82, 82, 37, 56, 15, 35, 10, 37, 15, 21, 92, 29, 21, 88, 59, 56, 4, 94, 88, 43, 6, 97, 75, 40, 27, 45, 99, 36, 41, 67, 16, 71, 74, 5, 54, 26, 28, 42, 82, 1, 10, 39, 3, 95, 92, 6, 73, 59, 45, 73, 74, 63, 7, 86, 10, 73, 47, 77, 19, 42, 36, 89, 19, 2, 99, 18, 3, 43, 62, 59, 58, 19, 51, 81, 29, 91, 44, 92, 24, 90, 40, 57, 8, 75, 33, 83, 12, 63, 99, 89, 5, 4, 9, 78, 44, 47, 67, 94, 49, 74, 70, 100, 75, 14, 91, 63, 14, 0, 12, 3, 88, 29, 73, 40, 27, 61, 99, 79, 31, 85, 88, 2, 63, 70, 36, 84, 24, 81, 24, 65, 90, 80, 4, 67, 42, 68, 100, 70, 83, 74, 47, 49, 13, 48, 8, 31, 25, 50, 69, 1, 65, 74, 66, 84, 98, 54, 25, 96, 19, 19, 29, 16, 48, 35, 8, 28, 1, 58, 87, 93, 75, 29, 97, 97, 52, 81, 100, 19, 34, 30, 9, 40, 25, 11, 83, 8, 85, 81, 29, 36, 75, 9, 69, 96, 64, 62, 60, 47, 72, 43, 74, 15, 33, 61, 83, 24, 41, 22, 92, 35, 59, 50, 63, 74, 69, 63, 17, 7, 90, 84, 87, 4, 62, 19, 35, 66, 58, 16, 91, 2, 38, 2, 37, 6, 2, 9, 93, 64, 83, 53, 11, 20, 51, 91, 32, 9, 27, 56, 50, 1, 60, 99, 1, 65, 71, 16, 75, 8, 28, 25, 22, 28, 94, 30, 64, 63, 39, 83, 96, 2, 23, 96, 3, 27, 35, 5, 18, 99, 58, 50, 32, 41, 65, 8, 70, 68, 50, 22, 47, 32, 17, 1, 67, 87, 38, 39, 1, 7, 67, 32, 9, 5, 35, 50, 54, 37, 42, 1, 22, 97, 5, 99, 12, 52, 80, 53, 19, 43, 47, 89, 54, 25, 21, 9, 38, 22, 38, 4, 73, 70, 16, 4, 27, 66, 0, 15]
best_scores = []
best_scoresD = {}
maxScore=-inf
played_games=0
f = open(map_name+"NEW.csv", 'w')
writer = csv.writer(f)

maxVals=[0 for i in range(365)]
maxchoices=[]

header=["score","bag_type","recycleRefundChoice","refundAmountMultiplicationFactor","choices1","choices2","choices3","choices4","choices5","choices6","choices7","choices8","choices9","choices10","choices11","choices12","choices13","choices14","choices15","choices16","choices17","choices18","choices19","choices20","choices21","choices22","choices23","choices24","choices25","choices26","choices27","choices28","choices29","choices30","choices31"]
writer.writerow(header)
v = [0, 1, 2]

def main():
	# print("Starting game...")
	global played_games, best_scores, best_scoresD, map_name,maxScore,maxchoices

	while True:
		global choices
		c=choices.copy()
		# map_name = "Suburbia" if random.randint(0,2)==0 else "Fancyville"
		response = api.mapInfo(api_key, map_name)
		days = 31 if map_name == "Suburbia" or map_name == "Fancyville" else 365
		
		# random shit happens here x
		
		for i in range(days):
			c[i]+=random.randint(-1000,1000)
			if c[i]<0:
				c[i]=0
		
		bag_type = 3
		recycleRefundChoice = False
		refundAmountMultiplicationFactor = random.random()
		# best_scores.append(score)
		# best_scores.sort(reverse=True)
		# best_scores=best_scores[:10]
		# if score not in best_scoresD.keys():
		# 	best_scoresD[score]=submit_game_response

		try:
			solver = Solver(game_info=response)
			solution = solver.Solve(bag_type, days, c, recycleRefundChoice, refundAmountMultiplicationFactor)
			submit_game_response = api.submit_game(api_key, map_name, solution)
			score = submit_game_response["score"]
			row = [score,bag_type,recycleRefundChoice,refundAmountMultiplicationFactor]
			row.extend(c)
			writer.writerow(row)
			played_games+=1
			if score>maxScore:
				maxScore=score
				maxchoices=c
				choices=c

			
			print("Game #{}: Score: {}".format(played_games, maxScore))
			f2 = open(map_name+"result.txt", 'w')
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
