import psutil as pt

class CpuBar:

    def __init__(self):
        self.cpu_count = pt.cpu_count(logical=False)  #cpu_count - количество ядер
        self.cpu_count_logical = pt.cpu_count()      # Количество потоков

    def cpu_percent_return(self):
        return pt.cpu_percent(percpu=True)   #для каждого ядра

    def cpu_one_return(self):
        return pt.cpu_percent()

    def ram_usage(self):
        return pt.virtual_memory()


       
