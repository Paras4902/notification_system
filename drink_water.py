import win10toast  # pip install win10toast
import time

if __name__ == '__main__':
    toaster = win10toast.ToastNotifier()
    while True:
        toaster.show_toast("Drink Water", "The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for women.", duration=10)
        time.sleep(3600)

# to add this to bg process write: pythonw .\drink_water.py
