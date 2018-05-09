from tkinter import *
from huffman import HuffmanCoding
import sys

class Application:
    def __init__(self, master=None):
        self.font = ("Calibri", "20")
        self.firstContainer = Frame(master)
        self.firstContainer["pady"] = 10
        self.firstContainer.pack()

        self.secondContainer = Frame(master)
        self.secondContainer["padx"] = 20
        self.secondContainer.pack()

        self.thirdContainer = Frame(master)
        self.thirdContainer["padx"] = 10
        self.thirdContainer["pady"] = 10
        self.thirdContainer.pack()

        self.fourthContainer = Frame(master)
        self.fourthContainer["pady"] = 10
        self.fourthContainer.pack()

        self.title = Label(self.firstContainer, text="Huffman Compress")
        self.title["font"] = ("Arial", "20", "bold")
        self.title.pack()

        self.nameLbl = Label(self.secondContainer,text="Name", font=self.font)
        self.nameLbl.pack(side=LEFT)

        self.name = Entry(self.secondContainer)
        self.name["width"] = 30
        self.name["font"] = self.font
        self.name.bind("<Button-1>", self.changeTextInitial)
        self.name.pack(side=LEFT)

        self.compress = Button(self.thirdContainer)
        self.compress["text"] = "Compress"
        self.compress["font"] = ("Calibri", "16")
        self.compress["width"] = 20
        self.compress["command"] = self.compressFunc
        self.compress.pack()

        self.decompress = Button(self.fourthContainer)
        self.decompress["text"] = "Decompress"
        self.decompress["font"] = ("Calibri", "16")
        self.decompress["width"] = 20
        self.decompress["command"] = self.decompressFunc
        self.decompress.pack()

        self.message = Label(self.fourthContainer, text="", font=self.font)
        self.message.pack()

    def changeTextCompress(self, event):
        if self.title["text"] == "Huffman Compress":
            self.title["text"] = "O arquivo foi comprimido!"
        else:
            self.title["text"] = "Huffman Compress"

    def changeTextDecompress(self, event):
        if self.title["text"] == "Huffman Compress":
            self.title["text"] = "O arquivo foi descomprimido!"
        else:
            self.title["text"] = "Huffman Compress"

    def changeTextInitial(self, event):
        self.title["text"] = "Huffman Compress"

    #Método de compressão
    def compressFunc(self):
        path = self.name.get()
        h = HuffmanCoding(path)
        output_path = h.compress()
        print("Compressed file path: " + output_path)

    #Método de descompressão
    def decompressFunc(self):
        path = self.name.get()
        decom_path = h.decompress(output_path)
        print("Decompressed file path: " + decom_path)

root = Tk()
root.title('Magic Compress')
Application(root)
root.mainloop()
