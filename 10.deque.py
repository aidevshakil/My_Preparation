from collections import deque


class Browser:
    def __init__(self):
        self.history = deque()  # present stack
        self.forward_stack = deque()  # Forward stack

    def visit(self, url):
        self.history.append(url)
        self.forward_stack.clear()  # Clear forward stack on new visit
        print(f"visited → {url}")

    def back(self):
        if len(self.history) <= 1:
            print("Cannot go back further")
            return
        current = self.history.pop()
        self.forward_stack.append(current)
        print(f"Back → {self.history[-1]}")

    def forward(self):
        if not self.forward_stack:
            print("Cannot go forward")
            return
        next_page = self.forward_stack.pop()
        self.history.append(next_page)
        print(f"Forward → {next_page}")

    def current(self):
        return self.history[-1] if self.history else "No page available"


# ─────── Using it ───────
browser = Browser()

browser.visit("google.com")
browser.visit("youtube.com")
browser.visit("facebook.com")
browser.visit("github.com")

print("i am now →", browser.current())  # github.com

browser.back()  # facebook.com
browser.back()  # youtube.com
browser.forward()  # github.com
browser.back()  # youtube.com

print("final page →", browser.current())