import csv
from tkinter import *
import monobit_test, frequency_within_block_test, runs_test, longest_run_ones_in_a_block_test, binary_matrix_rank_test
import dft_test, non_overlapping_template_matching_test, overlapping_template_matching_test
import maurers_universal_test, linear_complexity_test, serial_test, approximate_entropy_test
import cumulative_sums_test, random_excursion_test, random_excursion_variant_test

testFunc = [monobit_test, frequency_within_block_test, runs_test, longest_run_ones_in_a_block_test,
            binary_matrix_rank_test
    , dft_test, non_overlapping_template_matching_test, overlapping_template_matching_test
    , maurers_universal_test, linear_complexity_test, serial_test, approximate_entropy_test
    , cumulative_sums_test, random_excursion_test, random_excursion_variant_test]
testlist = [
    'monobit_test', 'frequency_within_block_test', 'runs_test', 'longest_run_ones_in_a_block_test',
    'binary_matrix_rank_test',
    'dft_test', 'non_overlapping_template_matching_test', 'overlapping_template_matching_test',
    'maurers_universal_test', 'linear_complexity_test', 'serial_test', 'approximate_entropy_test',
    'cumulative_sums_test', 'random_excursion_test', 'random_excursion_variant_test']


def main():
    global v
    Input = "input.txt"  # input file containing bit strings

    NUM_TEST = 15

    # Write output to csv files
    fieldnames = [None] * NUM_TEST  # fieldnames associating with outputs of each test
    fieldnames[0] = ['n', 'zeroes count', 'ones count', 'abs(ones-zeroes)', 'p-value', 'success']
    fieldnames[1] = ['n', 'chi_sq', 'p-value', 'success']
    fieldnames[2] = ['n', 'zeroes count', 'ones count', 'one_prop', 'vobs', 'p-value', 'success']
    fieldnames[3] = ['n', 'chi_sq', 'p-value', 'success']
    fieldnames[4] = ['n', 'M', 'Q', 'N', 'FM', "FMM", 'chi_sq', 'p-value', 'success']
    fieldnames[5] = ['n', 'N0', 'N1', 'd', 'p-value', 'success']
    fieldnames[6] = ['n', 'mu', 'sigma', 'chi_sq', 'p-value', 'success']
    fieldnames[7] = ['n', 'template', 'M', 'N', 'K', 'model', 'v', 'lambda', 'eta', 'chi_sq', 'p-value', 'success']
    fieldnames[8] = ['n', '#blocks', 'L', 'K', 'Q', 'sigma', 'p-value', 'success']
    fieldnames[9] = ['n', 'M', 'N', 'K', 'v', 'mu', 'chi_sq', 'p-value', 'success']
    fieldnames[10] = ['n', 'psi_sq_m', 'psi_sq_mm1', 'psi_sq_mm2', 'delta1', 'delta2', 'p1', 'p2', 'p_average',
                      'success']
    fieldnames[11] = ['n', 'appen_m', 'chi_sq', 'p-value', 'success']
    fieldnames[12] = ['n', 'p_forward', 'p_backward', 'success']
    fieldnames[13] = ['n', 'J', 'chi_sq', 'p-value', 'p_average', 'success']
    fieldnames[14] = ['n', 'J', 'count', 'p-value', 'p_average', 'success']

    fo = [None] * NUM_TEST  # list of output file

    output = [None] * NUM_TEST  # output file name
    writer = [None] * NUM_TEST  # writers of csv file

    source = [None] * NUM_TEST

    for i in range(NUM_TEST):
        if i < 9:
            output[i] = "result/result_0" + str(i + 1) + "_" + testlist[i] + ".csv"
        else:
            output[i] = "result/result_" + str(i + 1) + "_" + testlist[i] + ".csv"

        if fieldnames[i] != None:
            fo[i] = open(output[i], mode="w")
            writer[i] = csv.DictWriter(fo[i], fieldnames=fieldnames[i])
            writer[i].writeheader()

    fi = open(Input, "r+")  # input file

    result = [None] * NUM_TEST

    # for i in range(NUM_TEST):
    i = v.get()
    i -= 1
    if (i >= 0):

        total_count = 0
        success_count = 0
        p_average = 0.0
        fi = open(Input, "r+")  # input file

        '''
        Handle special cases: concatenate multiple lines into one to obtain 
        input with enough bit length for each test
        '''
        # binary_matrix_rank_test
        if i == 4:
            # count = 0
            bits = ''
            for line in fi:
                if len(bits) < 38912 * 2:
                    bits += line[:-1]
                else:
                    total_count += 1
                    x = testFunc[i].test(bits, len(bits))

                    p_average += x[len(x) - 2]

                    if x[len(x) - 1]:
                        success_count += 1

                    writeDict = {}

                    for j in range(len(x)):
                        writeDict[fieldnames[i][j]] = x[j]

                    writer[i].writerow(writeDict)
                    bits = ''

        # overlapping_template_matching_test            
        elif i == 7:
            bits = ''
            for line in fi:
                if len(bits) < 1028016 * 2:
                    bits += line[:-1]
                else:
                    total_count += 1
                    x = testFunc[i].test(bits, len(bits))

                    p_average += x[len(x) - 2]

                    if x[len(x) - 1]:
                        success_count += 1

                    writeDict = {}

                    for j in range(len(x)):
                        writeDict[fieldnames[i][j]] = x[j]

                    writer[i].writerow(writeDict)
                    bits = ''

        # maurers_universal_test
        elif i == 8:
            bits = ''
            for line in fi:
                if len(bits) < 387840 * 2:
                    bits += line[:-1]
                else:
                    total_count += 1
                    x = testFunc[i].test(bits, len(bits))

                    p_average += x[len(x) - 2]

                    if x[len(x) - 1]:
                        success_count += 1

                    writeDict = {}

                    for j in range(len(x)):
                        writeDict[fieldnames[i][j]] = x[j]

                    writer[i].writerow(writeDict)
                    bits = ''
        # linear_complexity_test
        elif i == 9:

            bits = ''
            for line in fi:
                if len(bits) < 1000000:
                    bits += line[:-1]
                else:
                    total_count += 1
                    x = testFunc[i].test(bits, len(bits))

                    p_average += x[len(x) - 2]

                    if x[len(x) - 1]:
                        success_count += 1

                    writeDict = {}

                    for j in range(len(x)):
                        writeDict[fieldnames[i][j]] = x[j]

                    writer[i].writerow(writeDict)
                    bits = ''
        # random_excursion_test and random_excursion_variant_test
        elif i == 13 or i == 14:
            bits = ''
            for line in fi:
                if len(bits) < 1000000 * 2:
                    bits += line[:-1]
                else:
                    total_count += 1
                    x = testFunc[i].test(bits, len(bits))

                    p_average += x[len(x) - 2]

                    if x[len(x) - 1]:
                        success_count += 1

                    if x[1] < 500:
                        x[len(x) - 1] = str(x[len(x) - 1]) + " NOT RELIABLE: J < 500"

                    writeDict = {}

                    for j in range(len(x)):
                        writeDict[fieldnames[i][j]] = x[j]

                    writer[i].writerow(writeDict)
                    bits = ''
        else:
            for line in fi:
                total_count += 1
                if fieldnames[i] is not None:

                    x = testFunc[i].test(line[:-1], len(line[:-1]))

                    p_average += x[len(x) - 2]

                    if x[len(x) - 1]:
                        success_count += 1

                    writeDict = {}

                    writeDict[fieldnames[i][0]] = len(line[:-1])

                    for j in range(len(x)):
                        writeDict[fieldnames[i][j + 1]] = x[j]

                    writer[i].writerow(writeDict)

        writeDict = {fieldnames[i][len(fieldnames[i]) - 1]: float(success_count) / total_count,
                     fieldnames[i][len(fieldnames[i]) - 2]: p_average / total_count}
        writer[i].writerow(writeDict)

        root2 = Toplevel(asli)
        root2.title(testlist[i])
        p_a = "p_average = " + str(p_average / total_count)
        p_p = "passed percentage = " + str(float(success_count) / total_count)
        p_n = "Test " + str(i + 1) + ": " + testlist[i] + " finished!"
        Label(root2, text=p_a).grid(row=0, column=0, columnspan=3)
        Label(root2, text=p_p).grid(row=1, column=0, columnspan=3)
        Label(root2, text=p_n).grid(row=2, column=0, columnspan=3)
        Label(root2, text=""" """).grid(row=3, column=0)
        root2.mainloop()
        # print("p_average = " + str(p_average / total_count))
        # print("passed percentage = " + str(float(success_count) / total_count))
        # print("Test " + str(i + 1) + ": " + testlist[i] + " finished!")


if __name__ == "__main__":
    asli = Tk()
    root = Toplevel(asli)
    root.title('NIST Statistical Test')
    asli.geometry("5x5")
    Label(root, text="""Enter test number :""").grid(row=0, column=0)
    Label(root, text=""" """).grid(row=1, column=0)
    v = IntVar()
    v.set(1)
    counter = 0
    for t in testlist:
        Radiobutton(root, text=t, variable=v, value=counter + 1).grid(row=2 + int(counter / 4), column=counter % 4)
        counter += 1
        Label(root, text=""" """).grid(row=4, column=0)
    Button(root, text='run', command=main, height=1, width=10).grid(row=10, columnspan=2, padx=10, column=2, sticky=E)
    root.mainloop()
