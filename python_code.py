def main():
    print("Keep it logically awesome.")
    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()
    print("there is quotes", quotes)

if __name__ == '__main__':
    main()
