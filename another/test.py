/var/www/html/smghendi/test-project/venv/bin/python3
import xlrd
import pymysql

# Open the workbook and define the worksheet
book = xlrd.open_workbook("all_14AA0001_01.xlsx")
sheet = book.sheet_by_name("Report 1")

# Establish a MySQL connection
database =  pymysql.connect (host="10.208.56.6", user = "webuser", passwd = "webuser123", db = "simon_pims_stg")

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

# Create the INSERT INTO sql query
query = """INSERT INTO `pims+_monthly_expenditure_test_copy1` (functional_area_key, functional_area_text, grant_key, grant_text, cost_center_key, cost_center_text, funded_program_key, funded_program_text, wbs_element_key, wbs_element_text, fiscal_year_key, fiscal_year_text, total_expenditures, consumable_budget, precommitment, commitment, consumed_budget, actual) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

# Create a For loop to iterate through each row in the XLS file, starting at row 5 to skip the headers
for r in range(4, sheet.nrows):
		functionalkey	= sheet.cell(r,2).value
		functionaltext	= sheet.cell(r,3).value
		grantkey	= sheet.cell(r,5).value
		granttext	= sheet.cell(r,6).value
		cckey		= sheet.cell(r,15).value
		cctext		= sheet.cell(r,16).value
		fpkey		= sheet.cell(r,17).value
		fptext		= sheet.cell(r,18).value
		wbskey		= sheet.cell(r,19).value
		wbstext		= sheet.cell(r,20).value
		fykey		= sheet.cell(r,21).value
		fytext		= sheet.cell(r,22).value
		texp		= sheet.cell(r,23).value
		consumable	= sheet.cell(r,24).value
		precommitment	= sheet.cell(r,25).value
		commitment	= sheet.cell(r,26).value
		consumed	= sheet.cell(r,27).value
		actual		= sheet.cell(r,28).value


		# Assign values from each row
		values = (functionalkey, functionaltext, grantkey, granttext, cckey, cctext, fpkey, fptext, wbskey, wbstext, fykey, fytext, texp, consumable, precommitment, commitment, consumed, actual)

		# Execute sql Query
		cursor.execute(query, values)

# Close the cursor
cursor.close()

# Commit the transaction
database.commit()

# Close the database connection
database.close()

# Print results
print ("")
print ("All Done.")
print ("")
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print ("Imported " + columns + " columns and " + rows + " rows to PIMS.")