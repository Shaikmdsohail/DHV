
"""
Name: Shaik Mohammed Sohail
Student ID: 22028788
Course: 7PAM2004-0901-2023 - Data Handling and Visualisation
University: Msc Data Science (SW) with Placement Year
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def readFile(filename):
    '''
    Parameters
    ----------
    filename: The filename is an argument parsed from the main function which name/path of the csv file

    Returns
    -------
    This function reads the csv file and filters the data and transpose it and returns the respective data frames
    '''
    
    db = pd.read_csv(filename,skiprows = 3)
    db.set_index('Country Name', inplace=True)
    
    db_f = db[db["Indicator Code"] == "ER.H2O.FWTL.ZS"]
    db_p = db[db["Indicator Code"] == "SP.POP.TOTL"]
    
    period = ["2000","2002","2004","2006","2008","2010","2012","2014","2016","2018"]
    
    db_fw = db_f[period]
    db_pg = db_p[period]
    
    db_fw = db_fw.loc[["United Kingdom", "China", "United States", "India"]]
    db_pg = db_pg.loc[["United Kingdom", "China", "United States", "India"]]
    
    db_fw_T = db_fw.transpose()
    db_pg_T = db_pg.transpose()
    
    
    return db_fw, db_fw_T, db_pg, db_pg_T

def Line(data, data1):
    '''
    Parameters
    ----------
    Parameters
    ----------
    data : The data is parsed argument from main fnction which should be the dataframe type..

    Returns
    -------
    The function return nothng but plots the Line graph for the parsed data frame.
    '''
    data.plot(kind="line", figsize=(10, 5))
    plt.title("Annual freshwater withdrawals, total (% of internal resources)")
    plt.xlabel("Year")
    plt.ylabel("Percentage of total withdrawl")
    plt.legend()
    plt.show()
    
    data1.plot(kind="line", figsize=(10, 5))
    plt.title("Total Population Growth")
    plt.xlabel("Year")
    plt.ylabel("Count Population Growth")
    plt.legend()
    plt.savefig("22028788.png", dpi=300)


def Bar(data,data1):
    '''

    Parameters
    ----------
    data : The data is parsed argument from main fnction which should be the dataframe type..

    Returns
    -------
    The function return nothng but plots the bar graph for the parsed data frame.

    '''
    data = data.loc[:,["2000","2006","2012","2018"]]
    data1 = data1.loc[:,["2000","2006","2012","2018"]]
    
    data.plot(kind="bar", figsize=(10, 5))
    plt.title("Annual freshwater withdrawals, total (% of internal resources)")
    plt.xlabel("Countries")
    plt.ylabel("Percentage of total withdrawl")
    plt.legend()
    plt.show()
    
    data1.plot(kind="bar", figsize=(10, 5))
    plt.title("Total Population Growth")
    plt.xlabel("Countries")
    plt.ylabel("Count Population Growth")
    plt.legend()
    plt.savefig("22028788.png", dpi=300)

#Main Function
file = "API_19_DS2_en_csv_v2_6183479.csv"
db_Fw, db_Fw_T, db_Pg, db_Pg_T = readFile(file)

Bar(db_Fw,db_Pg)
Line(db_Fw_T, db_Pg_T)


