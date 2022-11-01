from solver import Solver
import api

api_key = ""   # TODO: Your api key here
# The different map names can be found on considition.com/rules
# TODO: You map choice here. Unless changed, the map "Suburbia" will be selected.
map_name = "Suburbia"
# TODO: You bag type choice here. Unless changed, the bag type 1 will be selected.
bag_type = 1

def main():
	print("Starting game...")
	response = api.mapInfo(api_key, map_name)

	days = 31 if map_name == "Suburbia" or map_name == "Fancyville" else 365

	solver = Solver(game_info=response)
	solution = solver.Solve(bag_type, days)

	submit_game_response = api.submit_game(api_key, map_name, solution)
	print(submit_game_response)

if __name__ == "__main__":
	main()