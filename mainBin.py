from solver2 import Solver
import api,math,threading,time

api_key = "6762a10e-d948-4746-4558-08dab2e5ba74"   # TODO: Your api key here
# The different map names can be found on considition.com/rules
# TODO: You map choice here. Unless changed, the map "Suburbia" will be selected.
map_name = "Sky Scrape City"
# TODO: You bag type choice here. Unless changed, the bag type 1 will be selected.
bag_type = 2
orderMax=[0 for i in range(365)]
orderIndex=0
scoreForIndex=-math.inf

data={}

def getScoreAt(i):
    try:
        temp=orderMax.copy()
        temp[orderIndex]=i
        _s,d=main(temp)
        return(d[orderIndex])
    except:
        pass

def main(orderMax):
    try:
        st="".join([str(i) for i in orderMax])
        if st in data:
            return data[st][0],data[st][1]
        print("\n\n\nStarting game...")
        scores = []
        response = api.mapInfo(api_key, map_name)
        days = 31 if map_name == "Suburbia" or map_name == "Fancyville" else 365
        solver = Solver(game_info=response)
        solution = solver.Solve(bag_type, days,orderMax)

        submit_game_response = api.submit_game(api_key, map_name, solution)
        if submit_game_response != None:
            score = submit_game_response["score"]
            temp = submit_game_response["dailys"]
            for i in temp:
                scores.append(i["negativeCustomerScore"]+i["positiveCustomerScore"])
            print("for orderMax: ",orderMax)
            print("Score: " + str(score))
            print("Daily scores: " + str(scores))
            data[st]=(score,scores)
            return score,scores
    except:
        pass

def binS(a,b):
    try:
        scoreA = getScoreAt(a)
        scoreB = getScoreAt(b)
        scoreMid = getScoreAt((a+b)//2)
        if a+1==b:
            if scoreA>scoreB:
                orderMax[orderIndex]=a
            else:
                orderMax[orderIndex]=b
            return
        if scoreA==scoreMid and scoreMid==scoreB:
            orderMax[orderIndex]=a
            return
        if scoreA==scoreMid and scoreMid<scoreB:
            binS((a+b)//2,b)
            return
        if scoreA<scoreMid and scoreMid==scoreB:
            binS(a,(a+b)//2)
            return
        if scoreA<scoreMid and scoreMid<scoreB:
            if (a+b)//2==b-1:
                orderMax[orderIndex]=b
                return
            binS((a+b)//2,b)
            return
    except:
        pass
if __name__ == "__main__":
    t=time.time()
    orderIndex=0
    for i in range(365):
        binS(0,100)
        orderIndex+=1
        print(orderMax)
    print(time.time()-t)
