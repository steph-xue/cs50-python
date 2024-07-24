# The "shirtificate" program allows the user to input their name
# It produces a pdf file with an image of their name on a CS50 tshirt showing their certificate of completion of the CS50 course


from fpdf import FPDF


class PDF(FPDF):
    # Adds the CS50 Shirtificate header to each page of the pdf file
    def header(self):
        self.set_font("helvetica", "", 50)
        self.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")


    # Adds the name logo to the CS50 tshirt on the pdf file
    def print_logo(self, name):
        self.set_x(10)
        self.set_y(135)
        self.set_font("helvetica", "", 25)
        self.set_text_color(255, 255, 255)
        self.cell(0, 30, f"{name} took CS50", new_x="LMARGIN", new_y="NEXT", align="C")


def main():
    # Gets user to input their name
    name = input("Name: ").strip().title()

    # Creates an object from the PDF class with default parameters for page size (portrait, A4)
    pdf = PDF()

    # Adds a new page to the pdf file
    pdf.add_page()

    # Adds the CS50 tshirt image fo the pdf file
    pdf.image("shirtificate.png", w=pdf.epw)

    # Adds the name logo to the CS50 tshirt on the pdf file
    pdf.print_logo(name)

    # Saves the pdf file
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
