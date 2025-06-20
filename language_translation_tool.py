from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator
import pyttsx3

root = Tk()
root.title("Language Translation Tool")
root.geometry("800x600")
root.resizable(False, False)
root.configure(bg="#282c34")

translator = Translator()

languages = {
    'English': 'en',
    'French': 'fr',
    'German': 'de',
    'Spanish': 'es',
    'Hindi': 'hi',
    'Chinese': 'zh-cn',
    'Japanese': 'ja',
    'Russian': 'ru',
    'Arabic': 'ar'
}

def translate_text():
    try:
        input_text = input_text_box.get("1.0", END).strip()
        src_lang = source_lang_var.get()
        tgt_lang = target_lang_var.get()

        if input_text == "":
            messagebox.showerror("Error", "Please enter text to translate!")
            return

        translated = translator.translate(input_text, src=languages[src_lang], dest=languages[tgt_lang])
        output_text_box.delete("1.0", END)
        output_text_box.insert(END, translated.text)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def copy_text():
    output = output_text_box.get("1.0", END)
    root.clipboard_clear()
    root.clipboard_append(output)
    messagebox.showinfo("Copied", "Translated text copied to clipboard!")

def speak_text():
    output = output_text_box.get("1.0", "end-1c").strip()
    if output == "":
        messagebox.showerror("Error", "No translated text to speak!")
        return
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.say(output)
        engine.runAndWait()
    except Exception as e:
        messagebox.showerror("Error", f"Text-to-Speech error:\n{str(e)}")


def clear_text():
    input_text_box.delete("1.0", END)
    output_text_box.delete("1.0", END)

Label(root, text="Language Translation Tool", font=("Helvetica", 18, "bold"), bg="#282c34", fg="white").pack(pady=10)

frame = Frame(root, bg="#282c34")
frame.pack(pady=10)

Label(frame, text="Input Text", bg="#282c34", fg="white").grid(row=0, column=0, padx=10, pady=5)
Label(frame, text="Translated Text", bg="#282c34", fg="white").grid(row=0, column=1, padx=10, pady=5)

input_text_box = Text(frame, height=10, width=40, font=("Helvetica", 12))
input_text_box.grid(row=1, column=0, padx=10, pady=5)

output_text_box = Text(frame, height=10, width=40, font=("Helvetica", 12))
output_text_box.grid(row=1, column=1, padx=10, pady=5)

lang_frame = Frame(root, bg="#282c34")
lang_frame.pack(pady=10)

Label(lang_frame, text="Source Language", bg="#282c34", fg="white").grid(row=0, column=0, padx=20)
Label(lang_frame, text="Target Language", bg="#282c34", fg="white").grid(row=0, column=1, padx=20)

source_lang_var = StringVar()
source_lang_dropdown = ttk.Combobox(lang_frame, textvariable=source_lang_var, values=list(languages.keys()), state='readonly', font=("Helvetica", 12))
source_lang_dropdown.current(0)
source_lang_dropdown.grid(row=1, column=0, padx=20)

target_lang_var = StringVar()
target_lang_dropdown = ttk.Combobox(lang_frame, textvariable=target_lang_var, values=list(languages.keys()), state='readonly', font=("Helvetica", 12))
target_lang_dropdown.current(1)
target_lang_dropdown.grid(row=1, column=1, padx=20)

btn_frame = Frame(root, bg="#282c34")
btn_frame.pack(pady=10)

translate_btn = Button(btn_frame, text="Translate", command=translate_text, width=20, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
translate_btn.grid(row=0, column=0, padx=10, pady=5)

copy_btn = Button(btn_frame, text="Copy Translated Text", command=copy_text, width=20, bg="#2196F3", fg="white", font=("Helvetica", 12, "bold"))
copy_btn.grid(row=0, column=1, padx=10, pady=5)

speak_btn = Button(btn_frame, text="Speak Translated Text", command=speak_text, width=20, bg="#FF9800", fg="white", font=("Helvetica", 12, "bold"))
speak_btn.grid(row=1, column=0, padx=10, pady=5)

clear_btn = Button(btn_frame, text="Clear", command=clear_text, width=20, bg="#f44336", fg="white", font=("Helvetica", 12, "bold"))
clear_btn.grid(row=1, column=1, padx=10, pady=5)

root.mainloop()
