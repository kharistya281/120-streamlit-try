import pandas as pd 
import streamlit as st 

# data = pd.read_csv("tips.csv")

# st.title('Try Data Visualization')

# chart_data = plt.scatter(data['day'], data['tip'], c=data['size'],
#            s=data['total_bill'])

# st.line_chart


# def create_bar_plot(data):
#     plt.bar(data['day'], data['tip'])
#     plt.xlabel('Day')
#     plt.ylabel('Tip')
#     plt.title('Bar Chart')

# def create_line_chart(data):
#     plt.plot(data['tip'], data['size'])
#     plt.xlabel('Day')
#     plt.ylabel('Tip')

# def create_histogram(data):
#     plt.hist(data['total_bill'])

# def main():
#     st.title('Data Visualization of Tip Given by The Customer')

#     dataCsv = pd.read_csv("tips.csv")

#     st.write("Line Chart")
#     create_line_chart(dataCsv)
#     st.pyplot()

#     st.write("Bar Chart")
#     create_bar_plot(dataCsv)

#     st.write("Histogram")
#     create_histogram(dataCsv) 

st.title('Data Visualization of Tip Given by The Customer')

data = pd.read_csv("tips.csv")
st.write("Line Chart")
st.line_chart(data[['day', 'tip']])

st.write("Bar Chart")
st.bar_chart(data[['day', 'tip']])


