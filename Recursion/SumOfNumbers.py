def sum_of_n(num):
    if num == 0:
        return 0
    else:
        return sum_of_n(num-1) + num

def main():
    print(sum_of_n(25))
    
if __name__ == "__main__":
    main()