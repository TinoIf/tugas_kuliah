class ManagePerintah:
    def __init__(self):
        self.history = []
        self.stack_redo = []

    def eksekusi(self, perintah):
        perintah.eksekusi()
        self.history.append(perintah)
        self.stack_redo.clear()

    def kembalikan(self):
        if self.history:
            history_perintah = self.history.pop()
            history_perintah.kembalikan()
            self.stack_redo.append(history_perintah)

    def redo(self):
        if self.stack_redo:
            histori_perintah = self.stack_redo.pop()
            histori_perintah.eksekusi()
            self.history.append(histori_perintah)

