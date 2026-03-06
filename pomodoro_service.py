from models import WorkTimer, BreakTimer

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, task):
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index]['priority'] > self.heap[parent]['priority']:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def extract_max(self):
        if not self.heap:
            return None
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        max_item = self.heap.pop()
        self._heapify_down(0)
        return max_item

    def _heapify_down(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < len(self.heap) and self.heap[left]['priority'] > self.heap[largest]['priority']:
            largest = left
        if right < len(self.heap) and self.heap[right]['priority'] > self.heap[largest]['priority']:
            largest = right
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

class PomodoroService:
    def __init__(self):
        self.tasks = []
        self.heap = MaxHeap()

    def add_task(self, name, priority):
        task = {"name": name, "priority": priority}
        self.tasks.append(task)
        self.heap.insert(task)
        print(f"✅ 已新增任務：{name} (優先度 {priority})")

    def show_priority_tasks(self):
        if not self.tasks:
            print("目前沒有任務")
            return
        print("\n=== 任務優先排行 (Heap Sort，由高到低) ===")
        temp_heap = MaxHeap()
        for task in self.tasks:
            temp_heap.insert(task)
        rank = 1
        while temp_heap.heap:
            task = temp_heap.extract_max()
            print(f"{rank}. {task['name']} (優先度 {task['priority']})")
            rank += 1

    def start_pomodoro_cycle(self):
        if not self.tasks:
            print("請先新增至少一個任務！")
            return
        print("開始標準番茄鐘循環（4 工作 + 長休息）")
        for cycle in range(1, 5):
            print(f"\n第 {cycle} 輪")
            WorkTimer(25).start()
            if cycle < 4:
                BreakTimer(5).start()
            else:
                BreakTimer(15).start()
        print("\n🎉 今日番茄鐘完成！好好休息～")