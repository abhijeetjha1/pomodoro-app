from tkinter import  *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
Timer=None
# ---------------------------- TIMER RESET ------------------------------- #
def  reset_timer():
    window.after_cancel(Timer)
    canvas.itemconfig(time_txt, text= f"00:00")
    checkmark.config(text="")
    head.config(text="Timer" ,fg=GREEN)
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_count():
    global reps
    reps+=1
    if reps%8== 0 :
        count_down(LONG_BREAK_MIN*60)
        head.config(text="Break", fg=RED)

    elif reps%2==0:
        count_down(SHORT_BREAK_MIN*60)
        head.config(text="Break", fg=PINK)

    else :
        count_down(WORK_MIN*60)
        head.config(text="Work", fg=GREEN)





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    min=count//60
    sec=count%60
    # dynamic typing changing of variable during execution
    if sec<10:
        sec=f"0{sec}"
    if min<10 :
        min=f"0{min}"
    canvas.itemconfig(time_txt, text= f"{min}:{sec}")
    if count>0 :
        global Timer
        Timer=window.after(1,count_down, count-1)
    if count==0 :
        start_count()
        if reps==2 :
            checkmark.config(text="✓")
        elif reps==4 :
            checkmark.config(text="✓✓")
        elif reps==6 :
            checkmark.config(text="✓✓✓")
        elif reps==8 :
            checkmark.config(text="✓✓✓✓")

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)
# adding image to the file using canvas
canvas= Canvas(width=200,height=240)
canvas.config(bg=YELLOW,highlightthickness=0)
img=PhotoImage(file="tomato.png")
canvas.create_image(100,120,image=img)
time_txt=canvas.create_text(103,130 ,text="00:00" ,fill="white", font=(FONT_NAME,30,"bold"))
canvas.grid(row=1,column=1)


head=Label(text="Timer" , font=(FONT_NAME, 40 , "bold") , fg=GREEN ,bg=YELLOW)


head.grid(row=0,column=1)

start_button=Button(text="Start",highlightthickness=0 , command=start_count)
start_button.grid(row=2,column=0)

reset_button=Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2,column=2)

checkmark=Label(bg=YELLOW,fg=GREEN)

checkmark.grid(row=3,column=1)


window.mainloop()