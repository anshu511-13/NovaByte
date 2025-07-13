import tkinter as tk
import random

# Set-up

login=tk.Tk()
login.title("Login Area")
login.geometry("300x300")
score=0
score=0
cursor_upgrade_cost=10
helper_upgrade_cost=15
clone_upgrade_cost=50
click_power=1
click=0
upgrade=0

pass_label=tk.Label(login, text="Enter the password")
pass_label.pack()

pass_entry=tk.Entry(login)
pass_entry.pack()

area_label=tk.Label(login, text="Enter your Continent")
area_label.pack(pady=10)

area = tk.StringVar()
area.set("Asia")

area_input=tk.OptionMenu(login, area,
                         "Asia", 
                         "Africa", 
                         "North america", 
                         "South america", 
                         "Antarctica", 
                         "Europe", 
                         "Oceania")
area_input.pack()

def check_user_input():
    password=pass_entry.get()

    if password=="nova_123":
        window=tk.Tk()
        window.title("NovaByte")
        window.geometry("400x200")
        

        # Cookie Clicker

        def Cookie_Clicker():
            cookie_window=tk.Tk()
            cookie_window.title("Clicker Game")
            cookie_window.geometry("300x200")

            score=0
            cursor_upgrade_cost=10
            helper_upgrade_cost=15
            clone_upgrade_cost=50
            click_power=1
            upgrade=0
            click=0

            def change():
                global score, click_power, click
                score += click_power
                click +=1
                label.config(text=f"{score}")
                click_score_label.config(text=f"clicks(manually):{click}")

            def cursor_upgrade():
                global score, cursor_upgrade_cost, click_power, upgrade

                if score >= cursor_upgrade_cost:
                    score -= cursor_upgrade_cost
                    click_power += 1
                    cursor_upgrade_cost += 1
                    upgrade+=1
                    cursor_upgrade_button.config(text=f"cursor:{cursor_upgrade_cost}")
                    cpc_label.config(text=f"cpc(cookies per click):{click_power}")
                    upgrade_label.config(text=f"Upgrades bought:{upgrade}")
                    
            def helper_upgrade():
                global helper_upgrade_cost, score, click_power, upgrade

                if score >= helper_upgrade_cost:
                    score -= helper_upgrade_cost
                    click_power += 5
                    helper_upgrade_cost +=10
                    upgrade+=1
                    helper_upgrade_button.config(text=f"helper:{helper_upgrade_cost}")
                    cpc_label.config(text=f"cpc(cookies per click):{click_power}")
                    upgrade_label.config(text=f"Upgrades bought:{upgrade}")

            def clone_upgrade():
                global clone_upgrade_cost, score, click_power, upgrade

                if score >= clone_upgrade_cost:
                    score -= clone_upgrade_cost
                    click_power *= 2
                    clone_upgrade_cost += 100
                    upgrade+=1
                    clone_upgrade_button.config(text=f"Clone:{clone_upgrade_cost}")
                    cpc_label.config(text=f"cpc(cookies per click):{click_power}")
                    upgrade_label.config(text=f"Upgrades bought:{upgrade}")


            intro_cookie_label=tk.Label(cookie_window, text="Cookie Clicker")
            intro_cookie_label.pack(pady=(20,10))

            label=tk.Label(cookie_window, text="0")
            label.pack(pady=(20,10))

            button=tk.Button(cookie_window, text="🍪" , command=change)
            button.pack(pady=(40,40))

            li_label=tk.Label(cookie_window, text="Stats:-")
            li_label.place(relx=0.2, rely=0.5, anchor="center", x=-20, y=-20)

            click_score_label=tk.Label(cookie_window, text="clicks(manually):0")
            click_score_label.place(relx=0.2, rely=0.5, anchor="center", x=10, y=0)

            cpc_label=tk.Label(cookie_window, text="cpc(cookies per click):1")
            cpc_label.place(relx=0.2, rely=0.5, anchor="center", x=25, y=20)

            upgrade_label=tk.Label(cookie_window, text="Upgrades bought:0")
            upgrade_label.place(relx=0.2, rely=0.5, anchor="center", x=15, y=40)

            he_label=tk.Label(cookie_window, text="Upgrades:-")
            he_label.place(relx=1.0, rely=1.0, anchor="se", x=-20, y=-120)

            cursor_upgrade_button=tk.Button(cookie_window, text="cursor:10", command=cursor_upgrade)
            cursor_upgrade_button.place(relx=1.0, rely=1.0, anchor="se", x=-20, y=-90)

            helper_upgrade_button=tk.Button(cookie_window, text="helper:20", command=helper_upgrade)
            helper_upgrade_button.place(relx=1.0, rely=1.0, anchor="se", x=-20, y=-60)

            clone_upgrade_button=tk.Button(cookie_window, text="Clone:50", command=clone_upgrade)
            clone_upgrade_button.place(relx=1.0, rely=1.0, anchor="se", x=-20, y=-30)

        # Russian Roulette

        def Russian_Roulete():
            global choice, you, computer, comp_choice, user_choice
            
            russ_window=tk.Tk()
            russ_window.title("Russian Roulette")
            russ_window.geometry("325x250")
            choice = ["Blank", "Active"]
            you = 0
            computer=0
            comp_choice = random.choice(choice)
            user_choice=0

            def check():
                global score, user_choice, comp_choice, you, computer
                user_choice = etry.get()
                comp_choice = random.choice(choice)
                

                if (user_choice == "user" and comp_choice == "Blank") or (user_choice == "computer" and comp_choice == "Active"):
                
                    you += 1
                else:
                    computer += 1

                score_label.config(text=f"You: {you} | Computer: {computer}")
            
            intro_label=tk.Label(russ_window, text="Welcome to Russian Roulette")
            intro_label.pack(pady=20)

            ques_label=tk.Label(russ_window, text="Points towards the: (user/computer)")
            ques_label.pack(pady=10)

            etry=tk.Entry(russ_window)
            etry.pack()

            score_label = tk.Label(russ_window, text=("You: 0 | Computer: 0"), font=("Arial", 12))
            score_label.pack()

            submit=tk.Button(russ_window, text="Submit", command=check)
            submit.pack(pady=20)

        # Number Quest

        def no_quest():
            
            no=tk.Tk()
            no.title("Number Quest")
            no.geometry("300x200")
            
            def check_no():
                
                global no_choice
                no_ans = int(no_entry.get())
                no_choice=random.randint(1, 10)

                if no_ans > no_choice:
                    feed_no.config(text="Lower!")
                elif no_ans < no_choice:
                    feed_no.config(text="Higher!")
                else:
                    feed_no.config(text="Its perfect!")

            no_label=tk.Label(no, text="Enter a no.")
            no_label.pack(pady=10)

            no_entry=tk.Entry(no)
            no_entry.pack(pady=5)

            no_submit=tk.Button(no, text="Submit", command=check_no)
            no_submit.pack(pady=5)

            feed_no=tk.Label(no, text="")
            feed_no.pack(pady=5)

        # Novabyte Widgets

        label=tk.Label(window, text="NovaByte", font=("Helvetica",20))
        label.pack(pady=10)
                                         
        cook_Butt=tk.Button(window, text="Cookie Clicker", command=Cookie_Clicker)
        cook_Butt.pack(side="left", padx=30)

        russ_Butt=tk.Button(window, text="Russian Roulette", command=Russian_Roulete)
        russ_Butt.pack(side="right", padx=30)

        no_butt=tk.Button(window, text="Number Quest", command=no_quest).pack(pady=60)

login_butt=tk.Button(login, text="Submit", command=check_user_input).pack(pady=20)

login.mainloop()

