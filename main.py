#Author: Jack Olesen.
#Results, such as the comparison plot are published in the following research paper:  http://www.acs.pollub.pl/pdf/v16n4/2.pdf

#The python code calculate optimal lot-sizing for the deterministic time-varying inventory optimization problem.
#It implements the Wagner-whitin model (the optimal), the Silver-meal(heuristic), and EOQ model (typical industrially used lot-sizing formula)


####### The initialization ###### Should be adjusted with your inputs. Examples are given here ##########3

# The model is initialized with the following data:
#       - Demand data as a list. Each item in the list represent the demand in that period.
#       - Ordering cost per order. For every period, that an order is placed, this cost is incurred. It is independent of the order size.
#       - Holding cost per product, per period. (How much the holding/carrying cost is for the product in 1 period)

#Different examples of demands. Each entry in the list, represent the demand for the period: [demand_period_1, demand_period_2, ...]

listDemandInitial2 = [85432.06, 94609.26, 98335.82, 87760.15, 122816.35, 121015.34, 91501.71, 123453.46]
# listDemandInitial2 = [85432.06, 94609.26, 98335.82, 37760.15, 122816.35, 131015.34, 93501.71, 133453.46]
# listDemandInitial2 = [1202, 12131, 324, 8932, 123, 902342, 438923, 5892023, 43890853, 2323, 48921, 4289, 342323.04, 48922, 42153, 59900, 89890]
# listDemandInitial2 = [120202, 12131, 324, 8932, 123, 902342, 438923, 5892023, 43890853, 2323, 48921, 4289, 342323.04, 48922, 42153, 59900, 89890]
# listDemandInitial2 = [120202, 12131, 12324, 843932, 86123, 902342, 438923, 58023, 438853, 2323]


# listDemandInitial2 = [78.1, 78.909, 79.92, 80.043, 79.397, 78.283, 79.982, 82.04, 79.661, 84.318, 83.848, 85.334]

# Ordering cost per order. For every period, that an order is placed, this cost is incurred. It is independent of the order size.
orderingCost = 750
# orderingCost = 764

#Holding cost per product, per period. (How much the holding/carrying cost is for the product in 1 period)
holdingCost = 0.002076923
# holdingCost = 0.9






####### The simulation ###### Should not be changed ##########3
A = orderingCost
H = holdingCost

totalDemandVsOrderList = []

import math
import copy
import matplotlib.pyplot as plt


# demandListSizes = [8, 12, 25] #actual number of periods considered
demandListSizes = [len(listDemandInitial2)] #for the purpose of showing it graphically later, it is desired to only use the same number of periods throughout!

AllOrdersListEOQ = []
AllOrdersListSM = []
AllOrdersListSMadjusted = []
AllOrdersListWW = []

totalInventoryCostListSM = []
totalInventoryCostListSMadjusted = []
totalInventoryCostListEOQ = []
totalInventoryCostListWW = []


adjustmentVariableList = []
averageList = []


#for WW
demandInFocus = []
listOrdersInTuples = []
listOfListOrders = []
totalInventoryCostList = []
bestPerformingList = []

listDemandInitial = listDemandInitial2[0:len(listDemandInitial2)]
print(listDemandInitial)

listWithAllListDemand = []
AllVarianceList = []

averageDemand = sum(listDemandInitial) / len(listDemandInitial)

for adjustmentVariable in range(-100, 301):  # -100, 301
    adjustmentVariableList.append(adjustmentVariable)
    adjustmentVariable = adjustmentVariable / 100
    adjustedListDemand = []
    adjustedListDemand2 = []
    for demand in listDemandInitial:
        demandAdjusted = ((demand - averageDemand) * adjustmentVariable) + demand
        if demandAdjusted > 0:
            adjustedListDemand.append(demandAdjusted)
        else:
            adjustedListDemand.append(0)
    averageDemandOfAdjusted = sum(adjustedListDemand)/len(adjustedListDemand)
    x = averageDemand / averageDemandOfAdjusted
    for i in adjustedListDemand:
        adjustedListDemand2.append(x*i)
    listWithAllListDemand.append(adjustedListDemand2)
    print("adj: ", adjustmentVariable, " and listDemand: ", adjustedListDemand)
    listMedVariancePunkter = []
    averageAfDataPunkter = sum(adjustedListDemand) / len(adjustedListDemand)
    for entry in adjustedListDemand:
        variancePunkt = (entry - averageAfDataPunkter) * (entry - averageAfDataPunkter)
        listMedVariancePunkter.append(variancePunkt)
    testVariance = (1 / (len(adjustedListDemand))) * sum(listMedVariancePunkter)
    AllVarianceList.append(testVariance)
    adjustedListDemand = []



listWithAllListDemand2 = copy.deepcopy(listWithAllListDemand)

for i in listWithAllListDemand:
    for kl in i:
        if kl < 0:
            print("den her: ", i)

# input("ok, stop")

for listDemand in listWithAllListDemand:
    print("demand xuxuxux ", listDemand)
    EOQ = math.sqrt((2 * sum(listDemand) / len(listDemand) * orderingCost) / holdingCost)
    listDemandCopy = copy.deepcopy(listDemand)
    print("demandcopy1: ", listDemandCopy)
    orderList = []
    averageList.append(sum(listDemand) / len(listDemand))

    while len(listDemand) != 0:
        sumDemand = 0
        cumDemand = []
        for demand in listDemand:
            sumDemand = sumDemand + demand
            cumDemand.append(sumDemand)

        differenceList = []
        for x in cumDemand:
            y = EOQ - x
            if y >= 0:
                differenceList.append(y)
            else:
                differenceList.append(y * -1)

        if len(orderList) == 0:
            orderList.append(1 + differenceList.index(min(differenceList)))
        else:
            orderList.append(orderList[-1] + 1 + differenceList.index(min(differenceList)))

        for x in range(differenceList.index(min(differenceList)) + 1):
            listDemand.pop(0)

    actualOrderList = []

    numberOfOrders = len(orderList)
    for x, count in zip(reversed(orderList), range(1, numberOfOrders + 1)):
        if len(orderList) > 1:
            while x != orderList[-2] + 1:
                x -= 1
        else:
            x = 1
        orderList.pop(-1)
        actualOrderList.append(x)

    actualOrderList.reverse()

    adjustedOrderList = [i - 1 for i in actualOrderList[:len(actualOrderList)]]
    adjustedOrderList.append(len(listDemandCopy))

    orderListWithLotSizes = []
    orderSizeList = []
    for order, listPlacement in zip(actualOrderList, adjustedOrderList[1:]):
        orderSize = sum(listDemandCopy[order - 1:listPlacement])
        orderSizeList.append(orderSize)
        orderListWithLotSizes.append((order, orderSize))

    AllOrdersListEOQ.append(orderListWithLotSizes)
    # print("den her: ", orderListWithLotSizes)
    # print(sum(listDemandCopy))
    # print(sum(orderSizeList))

    # if listDemandCopy == listDemandInitial:
    #     print("this one ", orderListWithLotSizes)
    #
    # if listDemandCopy == [85432.06, 94609.26, 98335.82, 87760.15, 122816.35, 121015.34, 91501.71, 123453.46]:
    #     print("this one8 ", orderListWithLotSizes)

    # WW
    demandInFocus.clear()
    for i in listDemandCopy:
        listOfListOrders.clear()
        listOrdersInTuples.clear()
        demandInFocus.append(i)
        listOfListOrders.append([(1, sum(demandInFocus))])
        if len(bestPerformingList) > 0:
            for bestPerformingOrderlist, count2 in zip(bestPerformingList, range(1, len(bestPerformingList) + 1)):
                bestPerformingOrderlist2 = copy.deepcopy(bestPerformingOrderlist)
                bestPerformingOrderlist2.append((bestPerformingOrderlist[0][0] + count2,
                                                 sum(demandInFocus[bestPerformingOrderlist[0][0] + count2 - 1:])))
                listOfListOrders.append(bestPerformingOrderlist2)
        totalInventoryCostList.clear()
        for listOrdersThroughTuples in listOfListOrders:
            listOrders = []
            lastPeriod = 0
            for k, number in zip(listOrdersThroughTuples, range(0, len(listOrdersThroughTuples))):
                while k[0] - 1 != lastPeriod:
                    listOrders.append(0)
                    lastPeriod += 1
                listOrders.append(k[1])
                lastPeriod = k[0]
            while len(listOrders) < len(demandInFocus):
                listOrders.append(0)
                if len(listOrders) == 50:
                    input("stop, over 50")
            holdingCostList = []
            inventoryOnHand = 0
            demandVsOrderList = []
            for entryDemandInFocus, entryOrder in zip(demandInFocus, listOrders):
                holdingCostList.append(
                    inventoryOnHand * holdingCost)  # holding cost calculated with beginning inventory for period instead of average
                inventoryOnHand = inventoryOnHand - entryDemandInFocus + entryOrder
            totalOrderingCost = len(listOrdersThroughTuples) * orderingCost
            totalInventoryCost = sum(holdingCostList) + totalOrderingCost
            totalInventoryCostList.append(totalInventoryCost)
        bestPerformingList.append(
            copy.deepcopy(listOfListOrders[totalInventoryCostList.index(min(totalInventoryCostList))]))
    AllOrdersListWW.append(copy.deepcopy(bestPerformingList[-1]))
    bestPerformingList.clear()

    # silver meal
    listDemand = copy.deepcopy(listDemandCopy)
    originalAmountOfPeriodsWithDemand = len(listDemand)

    while len(listDemand) != 0:
        holdingCostList = []
        formerAverageTotalCostPerPeriod = 0
        orderReceived = originalAmountOfPeriodsWithDemand + 1 - len(listDemand)
        for n, demand in zip(range(1, len(listDemand) + 1), listDemand):
            holdingCostList.append(demand * holdingCost * (n - 1))
            averageTotalCostPerPeriod = 1 / n * ((A) + sum(holdingCostList))
            # print(averageTotalCostPerPeriod)
            if formerAverageTotalCostPerPeriod == 0:
                formerAverageTotalCostPerPeriod = averageTotalCostPerPeriod
            elif averageTotalCostPerPeriod > formerAverageTotalCostPerPeriod:
                orderList.append((orderReceived, sum(listDemand[0:n - 1])))
                del listDemand[0:n - 1]
                break
            if len(listDemand) == n:
                orderList.append((orderReceived, sum(listDemand)))
                listDemand = []
                break
            formerAverageTotalCostPerPeriod = averageTotalCostPerPeriod
    AllOrdersListSM.append(copy.deepcopy(orderList))  # copy here or it get changed later :(
    holdingCostList.clear()
    if len(orderList) > 1:
        print("tester")
        lastOrder = orderList[-1][0]
        print(orderList[-1][0])
        secondLastOrder = orderList[-2][0]
        print(orderList[-2][0])
        print(listDemandInitial)
        holdingCostIncreasement = 0
        print("zxzx: ", listDemandInitial[lastOrder - 1:])
        for demand in listDemandInitial[lastOrder - 1:]:
            print("demand: ", demand)
            n = lastOrder - secondLastOrder + holdingCostIncreasement
            print("n: ", n)
            print("cost: ", demand * holdingCost * (n))
            holdingCostList.append(demand * holdingCost * (n))
            holdingCostIncreasement += 1
        print("sumholdingcostlist: ", sum(holdingCostList))
        if orderingCost > sum(holdingCostList):
            orderPlacement = orderList[-2][0]
            orderSize = orderList[-2][1] + orderList[-1][1]
            orderList.pop(-1)
            orderList.pop(-1)
            orderList.append((orderPlacement, orderSize))
    AllOrdersListSMadjusted.append(copy.deepcopy(orderList))
print("done")
print("demandcopy2: ", listDemandCopy)
print(AllOrdersListEOQ)
print(AllOrdersListSM)
print(AllOrdersListSMadjusted)

# calculaton of total inventory cost

# listDemand = [85432.06, 94609.26, 98335.82, 87760.15, 122816.35, 121015.34, 91501.71, 123453.46]

# listOrdersThroughTuples = [(1, 278377.14), (4, 210576.5), (6, 212517.05+123453.46)]

count = -1
for listOrdersThroughTuples in AllOrdersListSMadjusted + AllOrdersListSM + AllOrdersListEOQ + AllOrdersListWW:
    listOrders = []
    lastPeriod = 0
    # print("klklklkl: ", listOrdersThroughTuples)
    # input("lololo")
    for i, number in zip(listOrdersThroughTuples, range(0, len(listOrdersThroughTuples))):
        while i[0] - 1 != lastPeriod:
            listOrders.append(0)
            lastPeriod += 1
        listOrders.append(i[1])
        lastPeriod = i[0]
    while len(listOrders) != len(listDemandCopy):
        listOrders.append(0)

    # print("test: ", sum(listOrders), sum(listDemand))

    holdingCostList = []
    inventoryOnHand = 0
    demandVsOrderList = []
    for i, x in zip(listDemandCopy, listOrders):
        y = [i, x + inventoryOnHand]
        holdingCostList.append(
            inventoryOnHand * holdingCost)  # holding cost calculated with beginning inventory for period instead of average
        inventoryOnHand = inventoryOnHand - i + x
        demandVsOrderList.append(i * -1)
        demandVsOrderList.append(x)
    totalDemandVsOrderList.append(demandVsOrderList)

    # print("holdingCost: ", sum(holdingCostList))

    totalOrderingCost = len(listOrdersThroughTuples) * orderingCost
    # print("længde: ", len(listOrdersThroughTuples))
    # print("OrderingCost: ", totalOrderingCost)
    # print("leeennn", len(listOrdersThroughTuples))
    #
    totalInventoryCost = sum(holdingCostList) + totalOrderingCost
    # print("order ", listOrdersThroughTuples)
    # print("TC: ", totalInventoryCost)
    # print("oc: ", orderingCost)
    # print("hc: ", sum(holdingCostList))
    # input("sstop")

    count += 1
    if len(AllOrdersListSMadjusted) > count:
        # print("a")
        totalInventoryCostListSMadjusted.append(totalInventoryCost)
    elif len(AllOrdersListSMadjusted) + len(AllOrdersListSM) > count:
        # print("b ")
        totalInventoryCostListSM.append(totalInventoryCost)
    elif len(AllOrdersListSMadjusted) + len(AllOrdersListSM) + len(AllOrdersListEOQ) > count:
        # print("c ")
        totalInventoryCostListEOQ.append(totalInventoryCost)
    else:
        totalInventoryCostListWW.append(totalInventoryCost)



# print("skrrr")
# print(len(AllOrdersListEOQ))
# print(len(AllOrdersListSM))
# print(len(AllOrdersListSMadjusted))
#
# print(AllOrdersListEOQ)
# print(AllOrdersListSM)
# print(AllOrdersListSMadjusted)




# print(totalInventoryCostListEOQ)
# print(totalInventoryCostListSM)
# print(totalInventoryCostListSMadjusted)

EOQpenalty = []
SMpenalty = []
SMApenalty = []


for SMa, SM, EOQ, WW in zip(totalInventoryCostListSMadjusted, totalInventoryCostListSM, totalInventoryCostListEOQ, totalInventoryCostListWW):
    EOQpenalty.append(((EOQ/WW)-1)*100)
    SMpenalty.append(((SM/WW)-1)*100)
    SMApenalty.append(((SMa / WW) - 1) * 100)

print("sss")
print(min(EOQpenalty))
print(max(EOQpenalty))

print(EOQpenalty)

print(min(SMpenalty))
print(max(SMpenalty))

print(SMpenalty)



# line 1 points
x1 = adjustmentVariableList
y1 = EOQpenalty
# plotting the line 1 points
plt.plot(x1, y1, marker='o', color='skyblue', markerfacecolor='blue', label = "EOQ penalty")
# line 2 points
# x2 = [y for y in range(1, len(SMpenalty)+1)]
x2 = adjustmentVariableList
y2 = SMpenalty
# plotting the line 2 points
plt.plot(x2, y2, marker='o', color='olive', markerfacecolor='limegreen', label = "SM penalty")
#line 3 points
x3 = adjustmentVariableList
y3 = SMApenalty
# plotting the line 1 points
plt.plot(x3, y3, marker='o', color='red', markerfacecolor='tomato', label = "SMa penalty")
plt.xlabel('Variability of demand.\n -100 = no variability. 0 = demand unchanged. 0-infinity = increasing variability')
# Set the y axis label of the current axis.
plt.ylabel('Cost penalty')
# Set a title of the current axes.
plt.title('Comparison between total inventory cost of EOQ, SM, adjusted SM vs WW. \n (' + str(demandListSizes[0]) + ' periods)')
# show a legend on the plot
plt.legend()
# Display a figure.
plt.show()


# print(AllOrdersListSM)
# print(listWithAllListDemand2)
# print(totalInventoryCostListSM)
# print(totalInventoryCostListSMadjusted)


