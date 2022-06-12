import gspread


def read_write_to_sheet(url):
    account = gspread.service_account()

    # Open spreadsheet by url:
    spreadsheet = account.open_by_url(url)

    # Open sheet by name:
    input_sheet = spreadsheet.worksheet("Input")
    try:
        output_sheet = spreadsheet.worksheet("Output")
    except:
        spreadsheet.add_worksheet("Output", input_sheet.row_count, input_sheet.col_count)
        output_sheet = spreadsheet.worksheet("Output")
    # cleaning from previous outputs
    output_sheet.clear()

    three_agents = False
    if input_sheet.acell("D1").value is not None:
        three_agents = True
    goods = {}
    char_count = 97
    for i in range(2, input_sheet.row_count):
        if input_sheet.cell(i, 2).value is None:
            break
        goods[chr(char_count)] = int(input_sheet.cell(i, 2).value)
        char_count += 1
    first_name = input_sheet.acell('B1').value
    second_name = input_sheet.acell('C1').value
    Alice = agents.AdditiveAgent(goods, name=first_name)
    George = agents.AdditiveAgent(goods, name=second_name)
    item_names = [chr(i) for i in range(97, char_count)]
    if three_agents:
        third_name = input_sheet.acell('D1').value
        Bob = agents.AdditiveAgent(goods, name=third_name)
        allocation = items.three_agents_IAV([Alice, George, Bob], item_names)
        third_bundle = allocation.get_bundles()[2]
        output_sheet.update("C1", third_name)
        output_sheet.update("C2", str(third_bundle))
        output_sheet.update("C3", "value:" + str(allocation.agents[0].value(third_bundle)))
    else:
        allocation = items.two_agents_ef1([Alice, George], item_names)
    first_bundle = allocation.get_bundles()[0]
    second_bundle = allocation.get_bundles()[1]
    agent = allocation.agents[0]
    output_sheet.update("A1:B1", [[first_name, second_name]])
    output_sheet.update("A2:B2", [[str(first_bundle), str(second_bundle)]])
    output_sheet.update("A3:B3",
                        [["value:" + str(agent.value(first_bundle)), "value:" + str(agent.value(second_bundle))]])


if __name__ == '__main__':
    read_write_to_sheet()
