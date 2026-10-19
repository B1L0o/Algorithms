# GPT helped me making the animations way faster and smoother by skipping frames

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import random
import heapq

def selection_sort(arr,record_frame, frame_interval=50, stop_flag=None):
    n=len(arr)
    steps=0

    for i in range(n-1):
        if stop_flag and stop_flag[0]:  
            return
        
        min_val=arr[i]
        pos=i
        for j in range(i+1,n):
            if stop_flag and stop_flag[0]: 
                return
            
            if arr[j] < min_val:
                min_val=arr[j]
                pos=j

        arr[i],arr[pos] = arr[pos],arr[i]
        if steps % frame_interval == 0:
                record_frame(arr)

    record_frame(arr)

def insertion_sort(arr,record_frame, frame_interval=50, stop_flag=None):
    n=len(arr)
    steps=0

    for i in range(1,n):
        if stop_flag and stop_flag[0]:  
            return
        
        j = i-1
        while j >= 0 and arr[j] > arr[j+1]:
            if stop_flag and stop_flag[0]: 
                return
            
            arr[j],arr[j+1] = arr[j+1],arr[j]
            j-=1
            if steps % frame_interval == 0:
                record_frame(arr)

    record_frame(arr)

def heapsort(arr, record_frame, frame_interval=50, stop_flag=None):
    n = len(arr)
    pq = []
    steps = 0

    for element in arr:
        heapq.heappush(pq, element)

    for i in range(n):
        if stop_flag and stop_flag[0]: 
            return
        arr[i] = heapq.heappop(pq)
        steps += 1
        if steps % frame_interval == 0:
            record_frame(arr)
    record_frame(arr)

def bubble_sort(arr, record_frame, frame_interval=50, stop_flag=None):
    n = len(arr)
    steps = 0

    for i in range(n - 1):
        if stop_flag and stop_flag[0]:  
            return
        
        for j in range(n - i - 1):
            if stop_flag and stop_flag[0]: 
                return
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            steps += 1

            if steps % frame_interval == 0:
                record_frame(arr)
    record_frame(arr)

def helper(arr, left, mid, right, record_frame, frame_interval=50, stop_flag=None):
    if stop_flag and stop_flag[0]:  
        return
        
    steps = 0
    l_half = mid - left + 1
    r_half = right - mid

    L = [0] * l_half
    R = [0] * r_half

    for i in range(l_half):
        L[i] = arr[left + i]
    for i in range(r_half):
        R[i] = arr[mid + 1 + i]

    i, j, k = 0, 0, left

    while i < l_half and j < r_half:
        if stop_flag and stop_flag[0]:  
            return
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        steps += 1
        if steps % frame_interval == 0:
            record_frame(arr)
        k += 1

    while i < l_half:
        if stop_flag and stop_flag[0]:  
            return
        arr[k] = L[i]
        i += 1
        k += 1
        steps += 1
        if steps % frame_interval == 0:
            record_frame(arr)

    while j < r_half:
        if stop_flag and stop_flag[0]: 
            return
        arr[k] = R[j]
        j += 1
        k += 1
        steps += 1
        if steps % frame_interval == 0:
            record_frame(arr)

def mergesort(arr, left, right, record_frame, frame_interval=50, stop_flag=None):
    if stop_flag and stop_flag[0]: 
        return

    if left < right:
        mid = (left + right) // 2
        mergesort(arr, left, mid, record_frame, frame_interval, stop_flag)
        mergesort(arr, mid + 1, right, record_frame, frame_interval, stop_flag)
        helper(arr, left, mid, right, record_frame, frame_interval, stop_flag)

class SortVisualizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Visualizer")
        self.array_size = tk.IntVar(value=100)
        self.is_running = False
        self.stop_flag = [False]  
        self.current_after_id = None  
        
        self.control_frame = ttk.Frame(root, padding=10)
        self.control_frame.pack(fill=tk.X)

        ttk.Label(self.control_frame, text="Array size:").pack(side=tk.LEFT)
        ttk.Combobox(self.control_frame, textvariable=self.array_size, 
                    values=[10,25,50, 100, 200,250, 500], state="readonly").pack(side=tk.LEFT, padx=(5,15))

        self.algo = tk.StringVar(value="Bubble Sort")
        ttk.Label(self.control_frame, text="Algorithm:").pack(side=tk.LEFT)
        ttk.Combobox(self.control_frame, textvariable=self.algo, 
                    values=["Bubble Sort","Insertion Sort","Selection Sort","Heap Sort", "Merge Sort"], state="readonly").pack(side=tk.LEFT, padx=(5,15))

        self.animation_speed = tk.IntVar(value=2)
        ttk.Label(self.control_frame, text="Speed:").pack(side=tk.LEFT)
        ttk.Scale(self.control_frame, from_=1, to=100, orient=tk.HORIZONTAL, 
                 variable=self.animation_speed, length=100).pack(side=tk.LEFT, padx=(5,15))

        self.start_button = ttk.Button(self.control_frame, text="Start", command=self.run_sort)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = ttk.Button(self.control_frame, text="Stop", command=self.stop_sort, state="disabled")
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.canvas_frame = ttk.Frame(root)
        self.canvas_frame.pack(fill=tk.BOTH, expand=True)

    def get_dynamic_frame_interval(self):
        size = self.array_size.get()
        return max(10, size // 20)

    def get_playback_delay(self):
        base_delay = 101 - self.animation_speed.get()
        return base_delay

    def run_sort(self):
        if self.is_running:
            return
            
        self.is_running = True
        self.stop_flag[0] = False
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        
        array = [random.randint(10, 500) for _ in range(self.array_size.get())]
        self.frames = []
        frame_interval = self.get_dynamic_frame_interval()

        def record_frame(snapshot):
            if not self.stop_flag[0]: 
                self.frames.append(snapshot[:])

        for w in self.canvas_frame.winfo_children():
            w.destroy()

        fig, ax = plt.subplots(figsize=(12, 6))
        
        bars = ax.bar(range(len(array)), array, color='mediumseagreen', width=0.8)
        
        ax.set_xlim(-1, len(array))
        ax.set_ylim(0, max(array) * 1.1)
        ax.axis('off')
        
        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        if self.algo.get() == "Bubble Sort":
            bubble_sort(array, record_frame, frame_interval, self.stop_flag)
        if self.algo.get() == "Insertion Sort":
            insertion_sort(array, record_frame, frame_interval, self.stop_flag)
        elif self.algo.get() == "Selection Sort":
            selection_sort(array, record_frame, frame_interval, self.stop_flag)
        elif self.algo.get() == "Heap Sort":
            heapsort(array, record_frame, frame_interval, self.stop_flag)
        elif self.algo.get() == "Merge Sort":
            mergesort(array, 0, len(array) - 1, record_frame, frame_interval, self.stop_flag)


        if not self.stop_flag[0]:
            self.playback_frames(bars, canvas)
        else:
            self.reset_buttons()

    def playback_frames(self, bars, canvas):
        playback_delay = self.get_playback_delay()
        
        def update(i):
            if self.stop_flag[0] or i >= len(self.frames):
                self.reset_buttons()
                return
                
            frame = self.frames[i]
            
            for rect, height in zip(bars, frame):
                rect.set_height(height)
            
            canvas.draw_idle()  
            
            if i + 1 < len(self.frames) and not self.stop_flag[0]:
                self.current_after_id = self.root.after(playback_delay, lambda: update(i + 1))
            else:
                self.reset_buttons()

        if self.frames:
            update(0)

    def stop_sort(self):
        self.stop_flag[0] = True
        if self.current_after_id:
            self.root.after_cancel(self.current_after_id)
            self.current_after_id = None
        self.reset_buttons()

    def reset_buttons(self):
        self.is_running = False
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = SortVisualizerApp(root)

    def on_closing():
        if app.current_after_id:
            root.after_cancel(app.current_after_id)
        root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()