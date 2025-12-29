from purchase_analyzer import *


def main():
    out_path = "report.txt"
    write_report(my_dict, mistake_list, cnt_mistakes, spent, sum_of_category, top_n, out_path)


if __name__ == "__main__":
    main()
