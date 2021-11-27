from collections import Counter


def find_the_most_tweeted(arr):
    final_res_list = []
    for lists in arr:
        res_list = []
        unique_names = [pref_names.split()[0] for
                        pref_names in lists]
        times = Counter(unique_names)
        repeat = times.values()

        for ele in set(repeat):
            duplicate_value = ([(key, value) for
                                key, value in sorted(times.items()) if
                                value == ele])

            if len(duplicate_value) > 1:
                for key, value in duplicate_value:
                    res_list.append(f"{key} {value}")

            max_value = max(times.values())
            temp_max_result = [(key, value) for
                               key, value in sorted(times.items()) if
                               value == max_value]

            if temp_max_result != duplicate_value:
                for (key, value) in temp_max_result:
                    res_list.append(f"{key} {value}")

        final_res_list.append(res_list)
    return final_res_list


def num_of_each_test_cases(num):
    tweet_names = []
    for n in range(1, test_cases + 1):
        tweet_names_n = []
        num_of_test_case = int(input())

        for i in range(num_of_test_case):
            while num_of_test_case > 0:
                try:
                    names = input()
                    name, id = names.split(" ")
                    if id is not None:
                        tweet_names_n.append(f"{name}")
                    num_of_test_case = num_of_test_case - 1
                except Exception:
                    print('Invalid Input. Try again')

        tweet_names.append(tweet_names_n)
    return tweet_names


def print_res(arr):
    for a in list(arr):
        print(a)


if __name__ == '__main__':
    print("Input:")
    test_cases = int(input())
    list_of_tweet_names = num_of_each_test_cases(test_cases)
    res = find_the_most_tweeted(list_of_tweet_names)
    print("Output:")
    i = 1
    for r in res:
        print_res(set(r))
        i += 1
