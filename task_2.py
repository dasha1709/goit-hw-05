import re
def generator_numbers(text):
    matches = re.findall(r"\d+.\d+", text)
    for match in matches:
        yield match

def sum_profit(text, func):
    total_summ = 0
    for number in func(text):
        total_summ += float(number)
    
    return total_summ
 

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")