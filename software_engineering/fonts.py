import tkinter as tk

root = tk.Tk()
root.title("Example Form")

# Create labels
label1 = tk.Label(root, text="Name:")
label2 = tk.Label(root, text="Email:")
label3 = tk.Label(root, text="Phone:")

# Create entry fields
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry3 = tk.Entry(root)

# Add labels and entry fields to form
label1.grid(row=0, column=0)
entry1.grid(row=0, column=1)
label2.grid(row=1, column=0)
entry2.grid(row=1, column=1)
label3.grid(row=2, column=0)
entry3.grid(row=2, column=1)

# Create a button
submit_button = tk.Button(root, text="Submit")
submit_button.grid(row=3, column=0, columnspan=2)

root.mainloop()