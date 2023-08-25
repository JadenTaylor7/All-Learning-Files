#testing exceptions
import pandas as pd
import random
import plotly
import plotly.graph_objects as go
from datetime import datetime

def investOnce():
    proceed = False
    while proceed == False:
        try:
            money = int(input("What will be your initial investment?: $")) #money
        except ValueError:
            print("ERROR: Please enter a valid number")
            continue #prevents proceed from turning True
        else:
            #print("successful input")
            proceed = True
        finally:
            pass
            #print("I'mma always run, run, run no matter what")


    proceed = False
    while proceed == False:
        try: 
            years = int(input("How many years do you want your money to grow?: ")) #years
        except ValueError:
            print("ERROR: Please enter a valid number.")
            continue #prevents proceed from turning True
        proceed = True

    print("\n\n\nCalculating value based on 4%, 7% and 12% compounded monthly...")
    count = datetime.now().year
    money4 = money
    money7 = money
    yearList7 = [[count, money4, money7]]
    for i in range(years):
        count += 1
        money4 = money4 * (1 + .04/12)**(12)
        money4 = round(money4,2) #round to two decimal places
        money7 = money7 * (1 + .07/12)**(12)
        money7 = round(money7,2) #round to two decimal places
        yearList7.append([count, money4, money7])
        #print(self.money) #for testing

    #print(self.yearList4[0][1]) #for testing. prints out the initial value
    #print("In {} years, your ${} will grow to an average of ${:1.2f}".format(years, yearList7[0][1], money))
    print("If you invested ${} today and left it alone, you would have ${:1.2f} in the year {}".format(yearList7[0][1], money7, count))
    # try:
    #     for i in range(len(yearList7)):
    #         yearList7[i][1] = str(yearList7[i][1])
    #     for i in range(len(yearList7)):
    #         yearList7[i][1] = "${}".format(yearList7[i][1])
    # except:
    #     print("didn't work")
    # else:
    #     pass
    #     #print("successful conversion")
    


    df = pd.DataFrame(yearList7, columns=["Years", "Balance 4%", "Balance 7%"]) #columns is the titles for your columns
    #print(df)
    df.to_csv('balanceByYear.csv', index=False)
    
    #TODO this section needs some work
    # df1 = pd.pivot_table(df, values= ['Balance 4%', 'Balance 7%'], index='Years')
    # print(df1)
    # trace0 = go.Scatter(
    #     x = df1.index,
    #     y = df1.values[:][0],
    #     mode = "lines",
    #     name = "4%",
    # )
    # trace1 = go.Scatter(
    # x = df1.index,
    # y = df1.values[:][1],
    # mode = "lines",
    # name = "7%",
    # )

    # data = [trace0,trace1]
    # layout = go.Layout(title= "Investment balance over time")
    # figure = go.Figure(data = data, layout = layout)
    # figure.show()
    # input("pause")

    #used when reading from a file
    # csvFile = 'balanceByyear.csv'
    # dataToGraph = pd.read_csv(csvFile)
    # data = [go.Scatter( x=dataToGraph['Years'], y=dataToGraph['Balance'] )]
    # fig = go.Figure(data)
    # fig.show()
    #end used when reading from a file




    print("\nSelect an option")
    print("1: display graph\n2: display and save graph as html")
    userInput = input("Select an action 1-2 or quit: ")
    validInput = ["1","2","quit"]
    while userInput not in validInput:
        print("\nBruh, that's not an answer")
        print("\nSelect an option")
        print("1: display graph\n2: display and save graph as html")
        userInput = input("Select an action 1-2 or quit: ")
    if userInput == "1":
        data = [go.Scatter( x=df['Years'], y=df['Balance 4%'])]
        fig = go.Figure(data)
        fig.show()
    elif userInput == "2":
        data = [go.Scatter( x=df['Years'], y=df['Balance 4%'] )]
        fig = go.Figure(data)
        plotly.offline.plot(fig, filename="InvestmentGraph.html")
    else:
        print("Fine then, have it your way.")
        print("\t\t\t\t\t\t\tNPC has left the chat")




def howOld():
    try:
        age = int(input("How old are you? (enter age as int) "))
    except:
        print("That's not an appropriate age. Assigning you an age.")
        age = random.randint(3,99)
    else:
        print("Thanks for entering your age!")
    finally:
        input("\n(press enter to continue)")
        print("\n\nYou are {} years old.".format(age))
        input("\n(press enter to continue)")

if __name__ == '__main__':
    #howOld()
    investOnce()
