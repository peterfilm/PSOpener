def disable_item(combo_box, item_name):
    index = combo_box.findText(item_name)
    combo_box.model().item(index).setEnabled(False)
