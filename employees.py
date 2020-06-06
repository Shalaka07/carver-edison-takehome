# Import modules

import pandas as pd
from dateutil.parser import parse
from datetime import datetime
from datetime import timedelta

def filter(filters):
	Emp = pd.read_csv('takehome.csv')

	# Data exploration and cleaning
	# Renaming 'Hire Date' column to prevent future conflicts because of having a sapce in the column name
	Emp = Emp.rename({'Hire Date':'HireDate'}, axis=1)  
	res = Emp
	
	if filters["Languages"]:
		res = Emp[:0]
		for lang in filters["Languages"]:
			lang=Emp.Language.str.contains(lang)
			res = res.append(Emp[lang])
	
	if filters["Salary"]:
		res_sal = Emp[:0]
		
		if isinstance(filters["Salary"], dict):
			#JSON Objects get converted to type dict in Python while JSON Arrays/Lists get converted to type list.
			if filters["Salary"]["max"]:
				res = res[res.Salary <= filters["Salary"]["max"]]
			if filters["Salary"]["min"]:
				res = res[res.Salary >= filters["Salary"]["min"]]
		else:
			#For JSON Arrays or int
			for sal in filters["Salary"]:
				#print(sal)
				res_sal = res_sal.append(res[res.Salary==sal])
				res=res_sal
	
	if filters["Date"]:
		max_years = filters["Date"]["max"]
		min_years = filters["Date"]["min"]
		# Converting to from series to datetime. 
		res["HireDate"] = pd.to_datetime(res["HireDate"])
		date_col = res.HireDate.dt.year
		now = 2020 # Setting current year
		date_col = now-date_col
		df1 = pd.DataFrame(data=date_col)
		res = res.assign(HireDate=df1['HireDate'])
		res = res[res.HireDate <= max_years]
		res = res[res.HireDate >= min_years]
		
	# Modifying dataframe for final response
	res["Name"] = res["First"] + " " + res["Last"]
	res = res.drop(columns=["First", "Last"])
	res = res.to_json(orient='records')
	
	return res
