import wbdata
import datetime

data_date = (datetime.datetime(2010, 1, 1), datetime.datetime(2011, 1, 1))
wbdata.get_incomelevel()
countries = [i['id'] for i in wbdata.get_country(incomelevel="HIC", display=False)]
indicators = {"IC.TAX.TOTL.CP.ZS": "Tax","NY.GDP.PCAP.PP.KD": "gdppc", "IC.REG.COST.PC.MA.ZS": "doing_business"}
df = wbdata.get_dataframe(indicators, country=countries, convert_date=True)

df.to_csv('econ.csv')