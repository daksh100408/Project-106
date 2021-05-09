import plotly.express as px
import csv
import numpy as np 

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df, x ="Days Present", y = "Marks In Percentage")
        fig.show()

def getDataSource(data_path):
    markinpercentage = []
    days_present = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            markinpercentage.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))
    return {"x": markinpercentage, "y": days_present}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation in marks and percentage and days present: \n", correlation[0, 1])

def setup():
    data_path ="data/Student Marks vs Days Present.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()

    #with open("data/cups of coffee vs hours of sleep.csv")as f:
    #df = csv.DictReader(f)
    #fig = px.scatter(df,x="Coffee", y="sleep")
    #fig.show()