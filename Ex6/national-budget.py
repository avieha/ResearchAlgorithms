import pandas as pd


def education_budget(year: int) -> int:
    filtered_budget = pd.read_csv("national-budget.csv", index_col=["שנה", "שם רמה 2"])
    temp = filtered_budget.loc[year, "חינוך"]
    education_budget_by_year = temp["הוצאה נטו"].sum()
    return education_budget_by_year


def security_budget_ratio(year: int) -> float:
    filtered_info = pd.read_csv("national-budget.csv", index_col=["שנה", "שם רמה 2"])
    temp = filtered_info.loc[year, "בטחון"]
    total_security_budget_by_year = temp["הוצאה נטו"].sum()
    filtered_info = pd.read_csv("national-budget.csv", index_col=["שנה"])
    total_budget_by_year = filtered_info.loc[year]["הוצאה נטו"].sum()
    ratio = total_security_budget_by_year / total_budget_by_year
    return ratio


def largest_budget_year(office: str) -> int:
    pass


def something():
    pass


if __name__ == '__main__':
    # print(education_budget(2016))
    print(security_budget_ratio(2016))
    # df = pd.read_csv("national-budget.csv", encoding='UTF-8')
    # counter = 0
    # print(df.info())
    # print(df.head(20))
    # for i in range(975975):
    #     print(df.iloc(i)['שנה'])
    #     # counter += 1
    # print(counter)
