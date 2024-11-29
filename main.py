import webview  # Webview library
from kivymd.app import MDApp  # KivyMD app class
from kivy.lang import Builder  # Builder to load the GUI
from kivymd.uix.button import MDRaisedButton  # KivyMD button
from kivymd.uix.screen import MDScreen  # KivyMD screen class

# This is your KivyMD GUI
kv = """
MDScreen:
    MDRaisedButton:
        text: "Open WebView"
        size_hint: None, None
        size: "200dp", "50dp"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        on_release: app.open_webview()
"""

class Kishore(MDApp):

    def build(self):
        # Load the KivyMD GUI from the string defined above
        return Builder.load_string(kv)

    def open_webview(self):
        # HTML content for the WebView
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Hello World</title>
        </head>
        <body>
            <h1>Hello, World! This is a WebView example using pywebview.</h1>
        </body>
        </html>
        """

        # Create a WebView window with the HTML content
        webview.create_window('Hello WebView', html=html_content)

        # Start the WebView event loop (blocks until the window is closed)
        webview.start()

# Run the app
if __name__ == "__main__":
   Kishore().run()
