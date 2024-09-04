class Solution(object):
  def maximumWealth(self, accounts):
    """
    :type accounts: List[List[int]]
    :rtype: int
    """
    max_wealth = 0
    for customer_accounts in accounts:
      customer_wealth = sum(customer_accounts)
      max_wealth = max(max_wealth, customer_wealth)
    return max_wealth