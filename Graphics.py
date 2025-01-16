import tkinter
from tkinter.filedialog import askopenfile
from tkinter import messagebox
import pikepdf
from pypdf import PdfReader, PdfWriter
from core.Showing import *
import sys

start_again = True


class Program(tkinter.Tk):
    def __init__(self):
        global start_again
        super().__init__()

        self.stop_status = False

        self.title('𝓟𝔂 𝓟𝓓𝓕 𝓒𝓻𝓪𝓬𝓴𝓮𝓻 v𝟐.𝟏')
        self.geometry('880x600')
        self.resizable(False, False)
        self.config(bg="Black")

        self.text = tkinter.Label(master=self,
                                  text="Hello USER This is PY PDF CRACKER Graphically !!!!\nLet's Go Please Give Me A "
                                       "PDF File To Cracking Password of The \nPDF File And Find Password.", font=(
                "Consolas", 14), bg="Black", fg="White")
        self.text.pack()

        self.b = tkinter.Button(master=self, text="Browse", font=("Consolas", 15),
                                command=lambda: self.ask_file_and_show_file_directory(textbox=self.textbox), fg="Red",
                                bg="Black")
        self.b.pack()

        self.textbox = tkinter.Entry(master=self, font=("Consolas", 15), width=50)
        self.textbox.pack()

        self.text2 = tkinter.Label(master=self,
                                   text="If You Have A Password File Please Enter It !!!!",
                                   font=("Consolas", 15), fg="White", bg="Black")
        self.text2.place(x=240, y=200)

        self.b2 = tkinter.Button(master=self, text="Browse", font=("Consolas", 15),
                                 command=lambda: self.ask_file_and_show_file_directory(textbox=self.textbox2),
                                 fg="Red",
                                 bg="Black")
        self.b2.place(x=400, y=300)

        self.textbox2 = tkinter.Entry(master=self, font=("Consolas", 15), width=50)
        self.textbox2.place(x=210, y=260)

        self.text3 = tkinter.Label(master=self,
                                   text="And Now Let's Go Cracking !!!!\nFor Crack Your File Press This Button.",
                                   font=("Consolas", 15), fg="White", bg="Black")
        self.text3.place(x=240, y=400)

        self.b3 = tkinter.Button(master=self, text="Crack", width=8, font=("Consolas", 15),
                                 command=self.crack,
                                 fg="Red",
                                 bg="Black")
        self.b3.place(x=400, y=500)

    def crack(self):
        global start_again
        messagebox.showinfo("Cracking Status", "Cracking is Started !!!!!")

        if start_again:
            start_again = False

            startagain = True

            def print_banner():
                if startagain:
                    banner = r'''

            ██████╗ ██╗   ██╗    ██████╗ ██████╗ ███████╗     ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
            ██╔══██╗╚██╗ ██╔╝    ██╔══██╗██╔══██╗██╔════╝    ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
            ██████╔╝ ╚████╔╝     ██████╔╝██║  ██║█████╗      ██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
            ██╔═══╝   ╚██╔╝      ██╔═══╝ ██║  ██║██╔══╝      ██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
            ██║        ██║       ██║     ██████╔╝██║         ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
            ╚═╝        ╚═╝       ╚═╝     ╚═════╝ ╚═╝          ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                v2.0

                            Auther : Bardia Ghassemi

                    '''

                    print(Fore.CYAN, banner, Fore.RESET, sep='')

            def Faild():
                print(Fore.RED, f'\b[-] {passtry} Password Tesded, Password Not Found.\n', Fore.RESET)
                sys.exit()

            def main(PDF_File, Password_File):
                global startagain, passtry, passwordlist

                while True:
                    if not Password_File:
                        passwordliste = False
                    else:
                        passwordliste = True

                    if PDF_File[-4:] != '.pdf':
                        startagain = False
                        messagebox.showerror("Error", "This File isn't A PDF File")
                        sys.exit()

                    try:
                        open(PDF_File)
                    except FileNotFoundError:
                        startagain = False
                        messagebox.showerror("Error", "PDF File Not Found")
                        sys.exit()

                    if passwordliste:
                        try:
                            passwordlist = open(Password_File)
                        except FileNotFoundError:
                            startagain = False
                            messagebox.showerror("Error", "Password File Not Found")
                            sys.exit()

                    def check_pass_need():
                        try:
                            pikepdf.open(PDF_File)
                            messagebox.showerror("Error", "The PDF File Has No Password.")
                            sys.exit()
                        except pikepdf._core.PasswordError:
                            pass

                    check_pass_need()

                    def remove_password(password):
                        reader = PdfReader(PDF_File)
                        reader.decrypt(password)

                        writer = PdfWriter()
                        writer.append_pages_from_reader(reader)
                        writer.encrypt("")

                        with open(PDF_File, "wb") as out_file:
                            writer.write(out_file)

                        messagebox.showinfo("Success", "The Password Of PDF File REMOVED Successfully.")

                    passtry = 0

                    if passwordliste:
                        print(Fore.YELLOW, '\b[!] Testing Your Password List.\n', Fore.RESET)
                        for password in passwordlist:
                            password = password.strip("\n")
                            if password == '' or password == '\n' or password == None:
                                continue
                            try:
                                pikepdf.open(PDF_File, password=password)
                                messagebox.showinfo("Success: Find Password",
                                                    f"{passtry} Password is Tested.\nPDF File Password : {password}")
                                ASK = messagebox.askyesno("Remove Password", "Do you want to Remove Password?")
                                if ASK is True:
                                    remove_password(password)
                                sys.exit()
                            except pikepdf._core.PasswordError:
                                passtry += 1
                                print(Fore.RED, f"\b[*] {passtry:,} Password Tesded.", Fore.RESET, end=' \r', sep='')

                        print(Fore.RED, '\b[-] Your PassList Faild.', Fore.RESET)

                    for number_of_passlist in range(1, 17):
                        number_of_passlist = str(number_of_passlist)
                        print(Fore.YELLOW, f'\b\n[!] Testing PassList{number_of_passlist}.', Fore.RESET)

                        passlistall = open(f'core/DefaultPassList/passlist{number_of_passlist}.txt')

                        for password in passlistall:
                            password = password.strip("\n")
                            try:
                                pikepdf.open(PDF_File, password=password)
                                messagebox.showinfo("Success: Find Password",
                                                    f"{passtry} Password is Tested.\nPDF File Password : {password}")
                                ASK = messagebox.askyesno("Remove Password", "Do you want to Remove Password?")
                                if ASK is True:
                                    remove_password(password)
                                sys.exit()
                            except pikepdf._core.PasswordError:
                                passtry += 1
                                print(Fore.RED, f"\b[*] {passtry:,} Password Tesded.", Fore.RESET, end='\r', sep='')

                        print(Fore.RED, f'\b\n[-] The Default PassList{number_of_passlist} Faild.', Fore.RESET)

                    Faild()

            try:
                print_banner()

                main(self.textbox.get(), self.textbox2.get())
            except KeyboardInterrupt:
                messagebox.showwarning("Exit", "You Exiting From Tool Bye !!!")
                sys.exit()

        else:
            messagebox.showinfo("Do Not Click", "Please Do Not Click Again This Option is Set !!!")

        messagebox.showinfo("Cracking Status", "Cracking is Finished !!!!!")

    def ask_file_and_show_file_directory(self, textbox):
        global file_directory

        try:
            if textbox == self.textbox:
                file_directory = askopenfile(title="PDF File For Crack",
                                             filetypes=(("PDF File", "*.pdf"),)).name.strip()
            elif textbox == self.textbox2:
                file_directory = askopenfile(title="Password File For Crack",
                                             filetypes=(("Text File", "*.txt"),)).name.strip()
        except AttributeError:
            file_directory = None

        if file_directory is not None:
            textbox.delete(0, tkinter.END)
            textbox.insert(tkinter.END, file_directory)
        else:
            messagebox.showerror("Error", "Please Select a File !!!!")


if __name__ == "__main__":
    P = Program()
    P.mainloop()
