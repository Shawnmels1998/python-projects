def main():
    print("Currency converter")
    print()
    
    dollars = eval(input('Enter Amount in dollars: '))
    
    dollars = convert_to_shillings(dollars)
    
    print('That is', dollars, 'shillings')
    
convert_to_shillings = lambda dollars: dollars * 3708.16

main()