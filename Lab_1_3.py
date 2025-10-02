import tkinter as tk
import sys
from tkinter.filedialog import askopenfilename

file_path = ""  

def getfile():
    global file_path
    filename = askopenfilename(filetypes=[("FASTA files", "*.fasta *.fa *.txt"), ("All files", "*.*")])
    file_path = filename
    if file_path:
        status_label.config(text=f"Selected: {file_path}")
        
def reset():
     output_box.delete("1.0", tk.END)

def processfile():
    if not file_path:
        status_label.config(text="No file selected.")
        return

    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
            seq = ''.join(line.strip() for line in lines[1:])

        freq = []
        alph = []

        for i in seq:
            if i not in alph:
                alph.append(i)
                freq.append(1)
            else:
                freq[alph.index(i)] += 1

        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, "Unique characters (alphabet):\n")
        output_box.insert(tk.END, ", ".join(alph) + "\n\n")
        output_box.insert(tk.END, "Relative frequencies:\n")

        for j in freq:
            output_box.insert(tk.END, str(j / len(seq)) + "\n")

    except Exception as e:
        status_label.config(text=f"Error: {str(e)}")

def main() -> int:
    global output_box, status_label

    app = tk.Tk()
    app.title("FASTA File Alphabet Frequency")
    app.geometry("600x400")

    pick_button = tk.Button(app, text='Pick File', width=25, command=getfile)
    pick_button.pack(pady=5)

    process_button = tk.Button(app, text='Process File', width=25, command=processfile)
    process_button.pack(pady=5)
    
    process_button = tk.Button(app, text='Reset', width=25, command=reset)
    process_button.pack(pady=5)

    status_label = tk.Label(app, text="No file selected.")
    status_label.pack(pady=5)

    output_box = tk.Text(app, height=15, width=70)
    output_box.pack(padx=10, pady=10)

    app.mainloop()
    return 0

if __name__ == '__main__':
    sys.exit(main())
