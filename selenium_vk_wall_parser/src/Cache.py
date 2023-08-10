import multiprocessing
import threading

class Cache:

    def __init__(self, cache_file):
        self.cache_file = cache_file
        self.lock = multiprocessing.Lock()

    def save(self, data_to_save):
        thread = threading.Thread(target=self.writeToFile, args=[data_to_save])
        thread.start()
        thread.join()

    def writeToFile(self, text):
        with self.lock:
            file = open(self.cache_file, 'a', encoding="cp1251")
            file.write(text + '\n')