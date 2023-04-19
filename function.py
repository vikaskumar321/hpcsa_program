def my_logic(source,destination,fare,discount_rate):
    return f"Fare from{ source } to { destination } is { fare- (fare*discount_rate/100)} INR with has a applied discount of { discount_rate}%"

def my_print(string_value):
    print("Hello User !!!!")
    print(string_value)