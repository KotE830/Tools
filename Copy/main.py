import openpyxl

from modules import macro

pos_start = macro.get_mouse_position()
pos_end = macro.get_mouse_position()
pos_move = macro.get_mouse_position()

wb = openpyxl.Workbook()
sheet = wb.active

for i in range(3):
  macro.drag(pos_start, pos_end)
  texts = macro.copy()

  words = []
  for text in texts.split():
    if "N" in text:
      sheet.title = text
    elif text.isdigit():
      macro.paste_in_excel(sheet, words)
      words = []
    else:
      if "[" in text:
        words.append(text[1:-1])
      elif text[-1] != ")" and ")" in text:
        words.append(text.replace(")", ") "))
      elif "│" not in text:
        words.append(text.replace(".", ","))

  macro.click(pos_move)

wb.save(macro.config.filename)