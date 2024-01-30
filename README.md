# Inventory-Optimization-Deterministic-Time-Varying-Demand
This Python repository applies the inventory optimization including:
- Wagner–Whitin (the Optimal Dynamic lot-size model)
- Economic Order Quantity (EOQ)
- Silver-Meal (SM).

Additionally, the simulations allow users to explore the impact of demand variability on total inventory costs, comparing different ordering policies.

The model is initialized with the following data:
- Demand data as a list. Each item in the list represent the demand in that period.
 - Ordering cost per order. For every period, that an order is placed, this cost is incurred. It is independent of the order size.
- Holding cost per product, per period. (How much the holding/carrying cost is for the product in 1 period)

Results, such as the comparison plot are published in the following research paper:
- https://www.researchgate.net/publication/348607949_JOINT_EFFECT_OF_FORECASTING_AND_LOT-SIZING_METHOD_ON_COST_MINIMIZATION_OBJECTIVE_OF_A_MANUFACTURER_A_CASE_STUDY
- http://www.acs.pollub.pl/pdf/v16n4/2.pdf

**Author: Jack Olesen**



## Theoretical formulaes included in the deterministic inventory optimization
# Wagner Whitin Algorithm (Dynamic Lot-Sizing Model)

The Wagner Whitin algorithm is a dynamic lot-sizing model used in inventory management. It aims to determine the optimal production or order quantities over a planning horizon, considering variable demand and production costs. The algorithm minimizes the total costs associated with ordering and holding inventory.

**Key Features:**

- **Dynamic Approach:** Considers variable demand and production costs over time.
- **Optimal Lot Sizes:** Computes the optimal production or order quantities for each period.
- **Total Cost Minimization:** Aims to minimize the total costs associated with inventory, including ordering and holding costs.

**Usage:**

- Commonly applied in manufacturing and supply chain management to optimize production scheduling and inventory levels.
- Suitable for scenarios with fluctuating demand and variable production costs.

---

# Silver Meal Model

The Silver Meal model is a heuristic used for inventory management, particularly in production planning. It provides a simple approach to determine when to place orders or initiate production to minimize total costs.

**Key Features:**

- **Heuristic Method:** Offers a rule-of-thumb approach for order placement.
- **Cost Minimization:** Aims to minimize total costs, considering ordering and holding costs.
- **Single-Period Model:** Primarily applied to situations with a single product and a single production facility.

**Usage:**

- Widely used in industries where the cost of holding inventory is relatively low compared to the cost of placing orders or initiating production.

---

# Economic Order Quantity (EOQ) Model

The Economic Order Quantity (EOQ) model is a classical inventory management approach that determines the optimal order quantity to minimize total inventory costs. It assumes a constant demand rate and a known order cost.

**Key Features:**

- **Constant Demand:** Assumes a stable and known demand rate.
- **Ordering Cost vs. Holding Cost:** Balances the costs of placing orders with the costs of holding inventory.
- **Optimal Order Quantity:** Calculates the order quantity that minimizes total costs.

**Usage:**

- Commonly applied in various industries to determine the most cost-effective order quantity for replenishing inventory.
- Assumption of constant demand makes it suitable for products with relatively stable sales patterns.


Results, such as the comparison plot are published in the following research paper:
- https://www.researchgate.net/publication/348607949_JOINT_EFFECT_OF_FORECASTING_AND_LOT-SIZING_METHOD_ON_COST_MINIMIZATION_OBJECTIVE_OF_A_MANUFACTURER_A_CASE_STUDY
- http://www.acs.pollub.pl/pdf/v16n4/2.pdf

**Author: Jack Olesen**
