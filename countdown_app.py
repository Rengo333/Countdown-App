import time
from tkinter import *
from tkinter import messagebox


def main():
    # creating app
    app = Tk()
    app.geometry("300x250")
    app.title("Countdown App")

    # declaration of variables
    hour = StringVar()
    minute = StringVar()
    second = StringVar()

    # setting the default value as 0
    hour.set("00")
    minute.set("00")
    second.set("00")

    # creating entry field to get inputs
    hour_entry = Entry(app, width=3, font=("Arial", 18, ""), textvariable=hour)
    hour_entry.place(x=80, y=20)

    minute_entry = Entry(app, width=3, font=("Arial", 18, ""), textvariable=minute)
    minute_entry.place(x=130, y=20)

    second_entry = Entry(app, width=3, font=("Arial", 18, ""), textvariable=second)
    second_entry.place(x=180, y=20)


    def timer():

        try:
            # input from a user in seconds
            temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())

        except:
            print("Please input the right value")

        while temp > -1:

            # converting input to mins and seconds
            mins, secs = divmod(temp, 60)

            # converting the input entered in mins. or secs. to hours, mins. ,secs.
            hours = 0
            if mins > 60:
                hours, mins = divmod(mins, 60)

            # using format () method to store the value up to two decimal places
            hour.set("{0:2d}".format(hours))
            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))

            # updating the timer after decrementing the temp value every time
            app.update()
            time.sleep(1)

            # if temp value = 0 then a messagebox pops up
            if temp == 0:
                messagebox.showinfo("Countdown", "Time is up ")

            # decrementing 1 every second
            temp -= 1

    # creating button
    btn = Button(app, text='Set Time Countdown', bd='5', command=timer)
    btn.place(x=70, y=120)

    # infinite loop
    app.mainloop()


if __name__ == "__main__":
    main()
