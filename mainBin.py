from solver2 import Solver
import api,math,threading

api_key = "6762a10e-d948-4746-4558-08dab2e5ba74"   # TODO: Your api key here
# The different map names can be found on considition.com/rules
# TODO: You map choice here. Unless changed, the map "Suburbia" will be selected.
map_name = "Suburbia"
# TODO: You bag type choice here. Unless changed, the bag type 1 will be selected.
bag_type = 2
orderMax=[0 for i in range(31)]
orderIndex=0
scoreForIndex=-math.inf

data={}


def main(orderMax):
    print("\n\n\nStarting game...")
    scores = []
    response = api.mapInfo(api_key, map_name)
    # print(response)
    days = 31 if map_name == "Suburbia" or map_name == "Fancyville" else 365
    solver = Solver(game_info=response)
    solution = solver.Solve(bag_type, days,orderMax)

    submit_game_response = api.submit_game(api_key, map_name, solution)
    score = submit_game_response["score"]
    temp = submit_game_response["dailys"]
    for i in temp:
        scores.append(i["negativeCustomerScore"]+i["positiveCustomerScore"]-i["c02"])
    # print(submit_game_response)
    print("for orderMax: ",orderMax)
    print("Score: " + str(score))
    print("Daily scores: " + str(scores))
    return score,scores

# def callNRecord(orderList):
#     for i in range(10):
#         th = threading.Thread(target=main,name=str(orderList)+": i", args=(orderList,))
#         th.start()



def binS(a,b):
    if a==b:
        orderMax[orderIndex]=a+1
        return
    temp=orderMax
    temp[orderIndex]=a
    _t,scoreA=main(temp)
    temp[orderIndex]=b
    _t,scoreB=main(temp)
    if scoreA==scoreB:
        binS(b,b*2)
    else:
        mid=(a+b)//2
        temp[orderIndex]=mid
        _t,scoreMid=main(temp)
        if scoreMid>scoreA and scoreMid==scoreB:
            binS(a,mid)
        elif scoreMid>scoreA and scoreMid<scoreB:
            binS(mid+1,b)
        elif scoreMid==scoreA and scoreMid<scoreB:
            binS(mid+1,b)
            
            # if scoreMid>scoreA:
            #     a=mid
            # else:
            #     b=mid
    #     orderMax[orderIndex]=a
    #     orderIndex+=1
    #     binS(0,1)

    # if a==b:
    #     return a
    # mid=(a+b)//2
    # if scores[mid]>scores[mid+1]:
    #     return binS(scores,a,mid)
    # else:
    #     return binS(scores,mid+1,b)

if __name__ == "__main__":
    for i in range(31):
        binS(0,100)
        orderIndex+=1
        print(orderMax)
        # print(i)