depar = "SEOUL"
hub = "DAEGU"
dest = "YEOSU"
roads = [["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","DAEJEON"],["SEOUL","ULSAN"],["DAEJEON","DAEGU"],["GWANGJU","BUSAN"],["DAEGU","GWANGJU"],["DAEGU","BUSAN"],["ULSAN","DAEGU"],["GWANGJU","YEOSU"],["BUSAN","YEOSU"]]

def soultion(depar, hub, dest, roads):
    answer = 0
    next = "a"
    while(1):
        check = []
        arr = []
        for i in range(len(roads)):
            check.append(0)
        while(1):
            if next == dest:
                arr.append(dest)
                if hub not in arr:
                    continue
                else:
                    answer += 1
                break
            for i in range(len(roads)):
                if roads[i][0] == depar and check[i] == 0 and roads[i][1] not in arr:
                    check[i] = 1
                    arr.append(roads[i][0])
                    next = roads[i][1]
                    break
                if roads[i][0] == next and check[i] == 0 and roads[i][1] not in arr:
                    check[i] = 1
                    arr.append(roads[i][0])
                    next = roads[i][1]
                    break





    return answer

print(soultion(depar,hub,dest,roads))