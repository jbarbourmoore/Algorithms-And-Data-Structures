import pulp as lp
import pandas as pd

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
    column_names = ["Stock","Price/Unit","Expected Returns/Unit","Earnings/Unit","Category","Units To Purchase","Total Purchase Price", "Expected Returns"]

    def __init__(self, stock_options = None, budget = 10000):
        '''
        This method initializes the investmentmaximization

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
        This method loads the stock options from the dictionary

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
        This method returns the default stock options

        Returns :
            default_stock_options : {"str":[]}
                The dictionary containing the default stock options
        '''

        default_stock_options = {
            self.column_names[0] : ["Ford","General Motors","Harley-Davidson","Microsoft","Apple","IBM","Pfizer","CVS","Coca-Cola","Disney"],
            self.column_names[1] : [10.30, 50.95, 25.96, 389.97,221.53,250.34,25.21,67.20,70.02,100.78],
            self.column_names[2] : [.0876*10.3, .0514*50.95, .0144*25.96, .024*389.97, 221.53*.0743,250.34*.0267,25.21*.0458,67.20*.0523,70.02*0.296,100.78*.0098],
            self.column_names[3] : [.038*10.3,.0192+50.95,.0093*25.96,.0084*389.97,221.53*.045,250.34*.0213,25.21*.0673,67.20*.04,70.02*.011,100.78*.0586],
            self.column_names[4] : ["Vehicles","Vehicles","Vehicles","Tech","Tech","Tech","Health","Health","Commodities","Commodities"]
        }
        return default_stock_options
        
    def getStockOptionsByCategory(self):
        '''
        This method returns the dictionary of categories with lists of each investion option inside

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
        '''
        This method calculates the optimal stock purchases to fit certain parameters
        '''

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
    
    def generateDataframe(self):
        '''
        This method returns a dataframe with all of the data on the stock options and current recommendations
        '''

        stock_names = []
        stock_prices = []
        stock_expected_returns = []
        stock_earnings_per_unit = []
        stock_categories = []
        if self.total_optomized_expected_returns!= None:
            stock_to_purchases = []
            stock_total_costs = []
            stock_total_expected_returns = []
        for stock in self.stock_options:
            stock_names.append(stock.name)
            stock_prices.append(stock.price_per_unit)
            stock_expected_returns.append(stock.expected_returns_per_unit)
            stock_earnings_per_unit.append(stock.earnings_per_unit)
            stock_categories.append(stock.category)
            if self.total_optomized_expected_returns!= None:
                stock_to_purchases.append(stock.optimized_purchase_quantity)
                stock_total_costs.append(stock.optimized_purchase_quantity*stock.price_per_unit)
                stock_total_expected_returns.append(stock.optimized_purchase_quantity*stock.earnings_per_unit)
        dictionary = {
            self.column_names[0] : stock_names,
            self.column_names[1] : stock_prices,
            self.column_names[2] : stock_expected_returns,
            self.column_names[3] : stock_earnings_per_unit,
            self.column_names[4] : stock_categories,
        }
        if self.total_optomized_expected_returns!= None:
            dictionary[self.column_names[5]] = stock_to_purchases
            dictionary[self.column_names[6]] = stock_total_costs
            dictionary[self.column_names[7]] = stock_total_expected_returns
        pd.options.display.float_format = '{:,.2f}'.format

        dataframe = pd.DataFrame.from_dict(dictionary)
        return dataframe

    
if __name__ == '__main__':
    print("- - - - - - - - - - - - - - - ")
    print("Loading Default Stocks")
    print("- - - - - - - - - - - - - - - ")
    investment_maximization = InvestmentMaximization() 
    print(investment_maximization.generateDataframe())
    print("- - - - - - - - - - - - - - - ")
    print("Maximizing Investment")
    print("- - - - - - - - - - - - - - - ")
    investment_maximization.calculateInvestmentMaximization()
    print("- - - - - - - - - - - - - - - ")
    print("Outputting The Data")
    print("- - - - - - - - - - - - - - - ")
    print(investment_maximization.generateDataframe())