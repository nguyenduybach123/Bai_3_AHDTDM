from ._anvil_designer import Form1Template
from anvil import *
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def drop_down_sort_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  def drop_down_sort_show(self, **event_args):
    sorting_algorithms = ['Insertion Sort', 'Selection Sort', 'Bubble Sort', 'Merge Sort']
    self.drop_down_sort.items = sorting_algorithms
    pass

  def button_sort_click(self, **event_args):
    if(self.text_box_input_sort.text == ""):
      alert("Yêu cầu nhập giá trị đầu vào")
      return
    step = []
    lstNumber = anvil.server.call('convertStringToArr',self.text_box_input_sort.text)
    selectSort = self.drop_down_sort.selected_value
    if(selectSort == 'Insertion Sort'):
      lstNumber, step = anvil.server.call('insertionSort',lstNumber)
    elif(selectSort == 'Selection Sort'):
      lstNumber, step = anvil.server.call('selectionSort',lstNumber, len(lstNumber))
    elif(selectSort == 'Bubble Sort'):
      lstNumber, step = anvil.server.call('bubbleSort',lstNumber)
    else:
      lstNumber = anvil.server.call('mergeSortResult',lstNumber)
    a_string = ','.join(map(str, lstNumber))
    self.label_result.text = "Kết quả : " + a_string
    self.label_step.text = step
    pass
