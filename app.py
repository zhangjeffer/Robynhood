from aws_boto3 import *
from stocks import *
from InvalidRequest import InvalidRequest


def msg_handler(phone_number, msg):
    split_msg = msg.split()
    return_msg = ""
    try: 
        if len(split_msg) == 1:
            return_msg = one_arg_handler(phone_number, split_msg[0])
        elif len(split_msg) == 2:
            return_msg = two_arg_handler(phone_number, split_msg)
        else:
            raise InvalidRequest
    except InvalidRequest:
        return_msg = "Invalid request"
    return return_msg


def one_arg_handler(phone_number, arg):
    return_msg = ""
    if arg[0] == "$":
        ticker = arg[1:]
        return_msg = retrieve_stock_text(ticker)
    elif arg == "Show":
        return_msg = show_handler(phone_number)
    else:
        raise InvalidRequest
    return return_msg


def two_arg_handler(phone_number, arg):
    user_request = arg[0]
    request_info = arg[1]
    return_msg = ""
    if user_request == "Show":
        return_msg = show_handler(phone_number)
    elif user_request == "Add" and request_info[0] == "$":
        return_msg = add_handler(phone_number, request_info[1:])
    elif user_request == "Remove" and request_info[0] == "$":
        return_msg = remove_handler(phone_number, request_info[1:])
    else:
        raise InvalidRequest
    return return_msg


def add_handler(phone_number, msg):
    print(phone_number)
    stock_info = price(msg)
    if not stock_info:
        raise InvalidRequest
    update_add(phone_number, msg)
    return "Added ${} to your watchlist".format(msg)


def remove_handler(phone_number, msg):
    remove(phone_number, msg)
    return "Removed ${} to your watchlist".format(msg)


def show_handler(phone_number):
    watchlist_printout = ""
    watchlist = retrieve(phone_number)
    if not watchlist:
        return "Nothing in watchlist."
    for stock in watchlist:
        watchlist_printout += retrieve_stock_text(stock) + "\n"
    return watchlist_printout


def retrieve_stock_text(ticker):
    stock_info = price(ticker)
    msg = ""
    if not stock_info:
        msg = "Invalid request"
    else:
        msg = "${}: Ask: ${}, Bid: ${}".format(ticker, stock_info[0], stock_info[1])
    return msg
