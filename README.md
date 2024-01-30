# Inventory-Optimization-Deterministic-Time-Varying-Demand
This Python repository implements simulations for inventory optimization strategies, including Wagner–Whitin (the Optimal Dynamic lot-size model), Economic Order Quantity (EOQ), Silver-Meal (SM). The simulations allow users to explore the impact of demand variability on total inventory costs, comparing different ordering policies.



The model is initialized with the following data:
- Demand data as a list. Each item in the list represent the demand in that period.
 - Ordering cost per order. For every period, that an order is placed, this cost is incurred. It is independent of the order size.
- Holding cost per product, per period. (How much the holding/carrying cost is for the product in 1 period)


Results, such as the comparison plot are published in the following research paper:  
http://www.acs.pollub.pl/pdf/v16n4/2.pdf

Author: Jack Olesen
