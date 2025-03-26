import pulp as lp

class StockOption():
    '''
    This class holds the information for a single stock option
    '''

    def __init__(self, id, name, price_per_unit, expected_returns_per_unit, earnings_per_unit, category):
        '''
        This method initializes the stock options.

        Parameters
            id = int
                The stock's id
            name = str
                The stock's name
            price_per_unit : number
                The stock's price per unit
            expected_returns_per_unit : number
                The stock's expected returns per unit
            earnings_per_unit : number
                The stock's earnings per unit
        '''

        self.id = id
        self.name = name
        self.price_per_unit = price_per_unit
        self.expected_returns_per_unit = expected_returns_per_unit
        self.earnings_per_unit = earnings_per_unit
        self.category = category
        self.optimized_purchase_quantity = None

    def setOptimizedPurchaseQuantity(self, optimized_purchase_quantity):
        self.optimized_purchase_quantity = optimized_purchase_quantity

class InvestmentMaximization():
    '''
    This class attempts to maximize the portfolio's returns based on certain criteria
    '''
    column_names = ["Stock","Price/Unit","Expected Returns/Unit","Earnings/Unit","Category"]

    def __init__(self, stock_options = None, budget = 10000):
        '''
        This function initializes the investmentmaximization

        Parameters :
            stock_options : {"str":[]}, optional
                The stock options as a dictionary object (default dictionary of imaginary data is provided)
            budget : int
                The budget for the stock investments (default is $10,000)
        '''

        self.budget = budget
        self.loadStockOptions(stock_options=stock_options)
        self.total_optomized_expected_returns = None

    def loadStockOptions(self, stock_options):
        '''
        This function loads the stock options from the dictionary

        Parameters :
            stock_options : {"str":[]}
                The stock options as a dictionary object (default dictionary of imaginary data is provided)
        '''
        if stock_options == None:
            stock_options = self.getDefaultStockOptions()

        self.number_of_options = len(stock_options["Stock"])
        self.stock_options = []
        self.categories_set = set([])
        for i in range(0, self.number_of_options):
            stock_option = StockOption(id=i,name=stock_options[self.column_names[0]][i],price_per_unit=stock_options[self.column_names[1]][i],expected_returns_per_unit=stock_options[self.column_names[2]][i],earnings_per_unit=stock_options[self.column_names[3]][i],category=stock_options[self.column_names[4]][i])
            self.stock_options.append(stock_option)
            self.categories_set.add(stock_options[self.column_names[4]][i])
    
    def getDefaultStockOptions(self):
        '''
        This function returns the default stock options

        Returns :
            default_stock_options : {"str":[]}
                The dictionary containing the default stock options
        '''
        
        default_stock_options = {
            "Stock" : ["Microsoft","Apple","Pfizer","CVS","Coca-Cola","Disney"],
            "Price/Unit":[210,254,81.6,35,45,151],
            "Expected Returns/Unit":[19,28,4,2,6,4],
            "Earnings/Unit":[1.4,7.6,1.8,8,3.5,4],
            "Category":["Tech","Tech","Health","Health","Commodities","Commodities"]
        }
        return default_stock_options
        
    def getStockOptionsByCategory(self):
        '''
        This function returns the dictionary of categories with lists of each investion option inside

        Returns :
            categories : {"str":[StockOption]}
                The dictionary of the categories with their stock options
        '''

        categories = {
            category:[] for category in self.categories_set
        }
        for stock_option in self.stock_options:
            categories[stock_option.category].append(stock_option)
        return categories
    
    def calculateInvestmentMaximization(self):

        # the objective is to maximize the total expected return for the stock investment
        lpModel = lp.LpProblem('InvestmentMaximization', lp.LpMaximize)
        purchase_units = [ lp.LpVariable(f'x{stock.id}', 0, None) for stock in self.stock_options ] 
        lpModel += lp.lpSum([stock.expected_returns_per_unit*purchase_units[stock.id] for stock in self.stock_options])
        
        # the total cost of purchasing the units must be less than or equal to the budget
        lpModel += lp.lpSum([stock.price_per_unit*purchase_units[stock.id] for stock in self.stock_options]) <= self.budget
        
        # each category's purchase value should be between 1 / 2 * number_of_categories and 2 / number_of_categories of the budget
        stock_options_by_category = self.getStockOptionsByCategory()
        category_count = len(stock_options_by_category)
        for name,category in stock_options_by_category.items():
            lpModel += lp.lpSum([stock.price_per_unit*purchase_units[stock.id] for stock in category]) <= self.budget * (2 / category_count)
            lpModel += lp.lpSum([stock.price_per_unit*purchase_units[stock.id] for stock in category]) >= self.budget / (category_count * 2)

        # purchase price must be less that 15 * stock earnings
        lpModel += lp.lpSum([stock.price_per_unit*purchase_units[stock.id] for stock in self.stock_options]) <= 15 * lp.lpSum([stock.earnings_per_unit*purchase_units[stock.id] for stock in self.stock_options])
        
        lpModel.solve(lp.PULP_CBC_CMD(msg=False))

        for stock in self.stock_options:
            stock.optimized_purchase_quantity = purchase_units[stock.id].varValue
            print(f"{stock.id} : purchase {stock.optimized_purchase_quantity:.2f} units of {stock.name} at ${stock.price_per_unit} per unit for ${stock.optimized_purchase_quantity*stock.price_per_unit:.2f} total cost")
        self.total_optomized_expected_returns = lp.value(lpModel.objective)
        print(f"Total expected returns are ${self.total_optomized_expected_returns:.2f}")
    
if __name__ == '__main__':
    print("Loading Default Stocks")
    investment_maximization = InvestmentMaximization() 
    print("Maximizing Investment")
    investment_maximization.calculateInvestmentMaximization()