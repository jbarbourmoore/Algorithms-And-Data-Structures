import unittest
from UsingPolynomialMultiplication_FFT import *
import time
from random import randint
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from HelperClasses.GenerateArrays import generate_random_array

class UsingPolynomialMultiplication_FFT_UnitTests(unittest.TestCase):
    '''
    This class contains basic unit tests for the binary search algorithms
    '''

    def setUp(self):
        pass

    def test_true_with_5_elements(self):
        '''
        This method tests that the binary search algorithm functions properly with an item smaller than the smallest 
        '''

        a_set = set([4, 7, 12, 14, 15])
        b_set = set([2, 4, 6, 8, 10])

        c_set = set([1, 2, 5, 13, 25])

        result_brute_force = checkForSum(a_set=a_set, b_set=b_set, c_set=c_set)
        self.assertEqual(result_brute_force, True)

        result = checkForSum_FFTPolynomialMultiplication(a_set=a_set, b_set=b_set, c_set=c_set)
        self.assertEqual(result, True)

    
    def test_false_with_5_elements(self):
        '''
        This method tests that a sum of a value in a and a value in b is not in set_c with 5 elements in each set
        '''

        a_set = set([4, 7, 12, 14, 15])
        b_set = set([2, 4, 6, 8, 10])

        c_set = set([1, 2, 5, 3, 26])

        result_brute_force = checkForSum(a_set=a_set, b_set=b_set, c_set=c_set)
        self.assertEqual(result_brute_force, False)

        result = checkForSum_FFTPolynomialMultiplication(a_set=a_set, b_set=b_set, c_set=c_set)
        self.assertEqual(result, False)


    def test_false_with_10_elements(self):
        '''
        This method tests that a sum of a value in a and a value in b is not in set_c with 10 elements in each set
        '''
    
        a_set = set([15, 3, 2, 1, 20, 29, 22, 20, 10, 26])
        b_set = set([1, 7, 20, 28, 11, 11, 8, 11, 14, 19])

        c_set = set([1, 5, 6, 7, 19, 25, 32, 44, 47, 51])

        result_brute_force = checkForSum(a_set=a_set, b_set=b_set, c_set=c_set)
        self.assertEqual(result_brute_force, False)

        result = checkForSum_FFTPolynomialMultiplication(a_set=a_set, b_set=b_set, c_set=c_set)
        self.assertEqual(result, False)


    def test_false_with_50_elements(self):
        '''
        This method tests that a sum of a value in a and a value in b is not in set_c with 50 elements in each set
        '''
    
        a_set = set([17, 70, 124, 147, 142, 60, 128, 73, 15, 86, 73, 123, 134, 28, 16, 49, 7, 70, 12, 146, 78, 11, 100, 132, 42, 4, 12, 139, 117, 12, 99, 131, 119, 136, 135, 97, 119, 33, 32, 100, 99, 44, 53, 99, 134, 29, 33, 137, 57, 21])
        b_set = set([114, 33, 14, 148, 37, 124, 113, 41, 21, 88, 86, 14, 134, 85, 138, 49, 84, 126, 135, 54, 139, 21, 50, 138, 2, 112, 13, 17, 61, 28, 13, 17, 144, 136, 92, 98, 18, 70, 123, 79, 33, 100, 92, 36, 116, 1, 30, 135, 30, 103])

        c_set = set([1, 2, 3, 4, 7, 10, 11, 15, 27, 288, 289, 292, 293, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332])

        duration_check, duration_check_fft = self.generate_results(a_set, b_set, c_set, False)
        print(f"Brute Force Method Duration:{duration_check:.2} seconds \nFFT Polynomial Method Duration:{duration_check_fft:.2} seconds")



    def test_false_with_1000_elements(self):
        '''
        This method tests that a sum of a value in a and a value in b is not in set_c with 1000 elements in each set
        '''
         
        a_set, b_set, c_set = self.get_sets_not_including_sum(set_length=1000)
        
        duration_check, duration_check_fft = self.generate_results(a_set, b_set, c_set, False)

        print(f"Brute Force Method Duration:{duration_check:.2} seconds \nFFT Polynomial Method Duration:{duration_check_fft:.2} seconds")
        self.assertGreater(duration_check,duration_check_fft)

    def test_true_with_1000_elements(self):
        '''
        This method tests that a sum of a value in a and a value in b is  in set_c with 1000 elements in each set
        '''

        a_set, b_set, c_set = self.get_sets_including_sum(set_length=1000)
        
        duration_check, duration_check_fft = self.generate_results(a_set, b_set, c_set, True)

        print(f"Brute Force Method Duration:{duration_check:.2} seconds \nFFT Polynomial Method Duration:{duration_check_fft:.2} seconds")
        self.assertGreater(duration_check,duration_check_fft)

    def test_increasing_size_arrays_durations(self):
        starting_size = 50
        increase_quantity = 50
        attempts_per_count = 10
        size_increases = 19

        set_sizes = []
        brute_force_durations = []
        fft_durations = []
        includes_list = []
        method_list = []
        durations = []
        doubled_sizes = []

        for j in range(0,2):
            if j == 0:
                includes = False
            else:
                includes = True

            for i in range(0,size_increases):
                set_size = starting_size+increase_quantity*i

                for _ in range(0,attempts_per_count):

                    if includes:
                        a_set, b_set, c_set = self.get_sets_including_sum(set_length=set_size)
                    else:
                        a_set, b_set, c_set = self.get_sets_not_including_sum(set_length=set_size)

                    
                    duration_check, duration_check_fft = self.generate_results(a_set, b_set, c_set, includes)

                    print(f"Array Size: {set_size} Including: {includes}")
                    print(f"Brute Force Method Duration:{duration_check:.2} seconds \nFFT Polynomial Method Duration:{duration_check_fft:.2} seconds")

                    set_sizes.append(set_size)
                    brute_force_durations.append(duration_check)
                    fft_durations.append(duration_check_fft)
                    includes_list.append(includes)
                    doubled_sizes.append(set_size)
                    method_list.append("Brute Force")
                    durations.append(duration_check)
                    doubled_sizes.append(set_size)
                    method_list.append("FFT")
                    durations.append(duration_check_fft)

        result_dictionary = {
            "Array Length":set_sizes,
            "Brute Force Method Duration":brute_force_durations,
            "FFT Method Duration":fft_durations,
            "Includes Sum":includes_list
        }

        all_results_dict = {
           "Array Length":doubled_sizes,
           "Duration":durations,
           "Method":method_list
        }

        dataframe = pd.DataFrame.from_dict(result_dictionary)
        all_dataframe = pd.DataFrame.from_dict(all_results_dict)

        fig, axes = plt.subplots(nrows=2, ncols=2, sharey=False)
        fig.set_figwidth(10)
        fig.set_figheight(8)

        bright_palette = sns.hls_palette(h=.5)

        sns.set_theme(style="whitegrid", palette=bright_palette)
        sns.lineplot(data=dataframe, x="Array Length", y="Brute Force Method Duration", ax=axes[0,0], hue="Includes Sum", palette=bright_palette[2:4])
        sns.scatterplot(data=dataframe, x="Array Length", y="Brute Force Method Duration", ax=axes[0,0], hue="Includes Sum", palette=bright_palette[2:4])
        sns.lineplot(data=dataframe, x="Array Length", y="FFT Method Duration", ax=axes[0,1], hue="Includes Sum", palette=bright_palette[0:2])
        sns.scatterplot(data=dataframe, x="Array Length", y="FFT Method Duration", ax=axes[0,1], hue="Includes Sum", palette=bright_palette[0:2])
        sns.scatterplot(data=all_dataframe, x="Array Length", y="Duration", ax=axes[1,0], hue="Method", palette=bright_palette[0:3:2])
        sns.lineplot(data=all_dataframe, x="Array Length", y="Duration", ax=axes[1,0], hue="Method", palette=bright_palette[0:3:2])
        sns.stripplot(data=all_dataframe, x="Array Length", y="Duration", ax=axes[1,1], hue="Method", palette=bright_palette[0:3:2],
        dodge=True, alpha=.25, zorder=1, legend=False)

        sns.pointplot(data=all_dataframe, x="Array Length", y="Duration", ax=axes[1,1], hue="Method",
    dodge=.8 - .8 / 3, palette=bright_palette[0:3:2], errorbar=None,
    markers="d", markersize=4, linestyle="none",
)

        fig.canvas.manager.set_window_title('FFT amd Brute Force Durations By Array Length')

        plt.tight_layout()
        plt.show()


    def generate_results(self, a_set, b_set, c_set, expected_result):
        start_check = time.time()
        result_brute_force = checkForSum(a_set=a_set, b_set=b_set, c_set=c_set)
        duration_check = time.time() - start_check

        self.assertEqual(result_brute_force, expected_result)

        start_check_fft = time.time()
        result = checkForSum_FFTPolynomialMultiplication(a_set=a_set, b_set=b_set, c_set=c_set)
        duration_check_fft = time.time() - start_check_fft

        self.assertEqual(result, expected_result)
        return duration_check,duration_check_fft

    def get_sets_not_including_sum(self, set_length):
        a_set = generate_random_array(array_length=set_length, min_value=1,max_value=set_length*3)
        b_set = generate_random_array(array_length=set_length, min_value=1,max_value=set_length*3)

        sums_a_b = []
        for a in a_set:
            for b in b_set:
                sums_a_b.append(a+b)

        c_set = []
        i = 1
        while len(c_set) < set_length :
            if i not in sums_a_b:
                c_set.append(i)
            i += 1

        return a_set,b_set,c_set
    
    def get_sets_including_sum(self, set_length):
        a_set, b_set, c_set = self.get_sets_not_including_sum(set_length=set_length)
        
        c_set[randint(1,set_length-1)] = a_set[randint(1,set_length-1)] + b_set[randint(1,set_length-1)]

        return a_set,b_set,c_set

if __name__ == '__main__':
    unittest.main()