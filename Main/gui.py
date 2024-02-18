from tkinter import Tk, Label, Text, Scrollbar
from PIL import Image, ImageTk, ImageDraw, ImageFont  # Import ImageFont from PIL package

class MusicDisplayGUI:
    def __init__(self, notes, lyrics):
        self.notes = notes
        self.lyrics = lyrics

        # Initialize Tkinter window
        self.root = Tk()
        self.root.title("Music Display")

        # Initialize GUI components
        self.notes_label = Label(self.root)
        self.lyrics_text = Text(self.root, wrap="word")
        self.scrollbar = Scrollbar(self.root, command=self.lyrics_text.yview)

        # Display notes and lyrics
        self.display_notes()
        self.display_lyrics()

        # Pack GUI components
        self.notes_label.pack()
        self.lyrics_text.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Run the Tkinter main loop
        self.root.mainloop()

    def display_notes(self):
        # Specify the absolute path to the font file
        font_path = "Lassus-7BRA.ttf"  # Modify this path accordingly
        font_size = 50

        # Load the musical note font
        note_font = ImageFont.truetype(font_path, font_size)

        # Create a blank image for displaying notes with more space
        image_width = 800  # Increased width
        image_height = 400  # Increased height
        notes_image = Image.new("RGB", (image_width, image_height), color="white")
        notes_draw = ImageDraw.Draw(notes_image)

        # Draw notes on the image
        note_x = 10
        note_y = 10
        max_width = image_width  # Maximum width of the image
        spacing = 40     # Spacing between notes
        for note in self.notes:
            # Draw the note on the image using the musical note font
            notes_draw.text((note_x, note_y), note, fill="black", font=note_font)

            # Update the position for the next note
            note_x += spacing
            if note_x >= max_width:
                note_x = 10
                note_y += 40  # Move to the next line

        # Convert the image to a Tkinter-compatible format
        notes_photo = ImageTk.PhotoImage(notes_image)

        # Display the image on the label
        self.notes_label.configure(image=notes_photo)
        self.notes_label.image = notes_photo  # Keep a reference to prevent garbage collection

    def display_lyrics(self):
        # Display lyrics in the Text widget
        self.lyrics_text.insert("1.0", self.lyrics)

# Example usage:
if __name__ == "__main__":
    # Assume 'notes' and 'lyrics' are provided
    notes = ["C", "D", "E", "F", "G"]
    lyrics = "This is the lyrics"

    # Create the GUI instance
    gui = MusicDisplayGUI(notes, lyrics)