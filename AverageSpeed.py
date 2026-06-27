# Average Speed Calculator 
import sys
import tkinter as tk

from tkinter import messagebox, simpledialog


def main():
    showWelcomeMessage()

    distance = getDistanceInput()
    time = getTimeInput()
    speedKmh = calculateAverageSpeed(distance, time)
    speedMs = convertKmhToMs(speedKmh)

    displayResults(distance, time, speedKmh, speedMs)

def showWelcomeMessage():
    print("===========================")
    print("Average Speed Calculator")
    print("===========================")
    print("Formula: V(avg) = distance / time")
    print("Results shown in km/h and m/s")
    print("============================")

def getDistanceInput():

    while True:
        input_str = simpledialog.askstring("Input", "Enter the total distance traveld (in km): ")
        if input_str is None:
            messagebox.showinfo("Information", "Program terminated by user.")
            sys.exit(0)

        input_str = input_str.strip()
        
        if not input_str:
            messagebox.showerror("Input Error", "Input cannot be empty! Please enter a number.")
            continue

        try:
            distance = float(input_str)
            if distance <= 0:
                messagebox.showerror("Input Error", "Distance must be greater than zero.")
            else:
                return distance
        except ValueError:
            messagebox.showerror("Input Error", "Invalid input! Please enter a valid number.")


def getTimeInput():
    while True:
        input_str = simpledialog.askstring("Input", "Enter the total time taken (in hrs): ")
        if input_str is None:
            messagebox.showinfo("Information", "Program terminated by user.")
            sys.exit(0)

        input_str = input_str.strip()

        if not input_str:
            messagebox.showerror("Input Error", "Input cannot be empty! Please enter a number.")
            continue

        try:
            time = float(input_str)
            if time <= 0:
                messagebox.showerror("Input Error", "Time must be greater than zero!")

            else:
                return time
        except ValueError:
            messagebox.showerror("Input Error", "Invalid input! Please enter a valid number.")


def calculateAverageSpeed(distance, time):
    return distance / time


def convertKmhToMs(speedKmh):
    return speedKmh * 1000.0 / 3600.0


def displayResults(distance, time, speedKmh, speedMs):
    print("\n ==================================")
    print("Calculation Results")
    print("=====================================")
    print(f"Distance: {distance} km")
    print(f"Time: {time} hrs")
    print(f"Average Speed: {speedKmh} km/h")
    print(f"Average Speed: {speedMs} m/s")
    print("======================================")

 # GUI Message Box (Replicates JOptionPane.showMessageDialog)
    resultText = (
        f"AVERAGE SPEED CALCULATION\n"
        f"==========================\n\n"
        f"Input Values:\n"
        f"• Distance: {distance} km\n"
        f"• Time: {time} hours\n\n"
        f"Calculation:\n"
        f"• Formula: Speed = Distance ÷ Time\n"
        f"• {distance} km ÷ {time} hours\n"
        f"• = {speedKmh:.4f} km/h\n\n"
        f"Conversion to m/s:\n"
        f"• {speedKmh:.4f} km/h × (1000 m ÷ 3600 s)\n"
        f"• = {speedKmh:.4f} km/h × {1000.0/3600.0:.4f}\n"
        f"• = {speedMs:.4f} m/s\n\n"
        f"Final Results:\n"
        f"• Average Speed: {speedKmh:.4f} km/h\n"
        f"• Average Speed: {speedMs:.4f} m/s"
        )
    
     # If we want a GUI window to stay open:
    root = tk.Tk()
    root.withdraw() # Hides the main tiny blank window if we are only using simpledialog/messagebox
    messagebox.showinfo("Average Results", resultText)
    
   
             
if __name__ == "__main__":
   
    
    main() # Runs the logic
    





