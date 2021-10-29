class DeckException(Exception):
  def __init__(self, text):
    self.Text = text

  def GetText(self):
    return self.Text
