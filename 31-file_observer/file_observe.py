from pathlib import Path
import time
# 事件处理器
from watchdog.events import PatternMatchingEventHandler
# 导观察者
from watchdog.observers import Observer


# 重命名
txtpath = Path("test.txt")
txtpath.rename(txtpath.parent.joinpath("2.txt"))


# 监控文件变化
def on_created(event):
    print(f"创建了 {event.src_path}")


def on_deleted(event):
    print(f"删除了 {event.src_path}")


def on_modified(event):
    print(f"修改了 {event.src_path}")


def on_moved(event):
    print(f"文件从 {event.src_path}")


# 要处理的文件的匹配规则 *代表所有文件
pattern = "*"
# 不需要处理文件的匹配规则
ignore_patterns = ""
# 是否只监听常规文件 不包含文件夹 False表示文件夹也要监听
ignore_directories = False
# 设置为True 表示区分路径大小写
case_sensitive = True
# 创建事件处理器
event_handler = PatternMatchingEventHandler(
    pattern,
    ignore_patterns,
    ignore_directories,
    case_sensitive
)
# 绑定对应的方法
event_handler.on_created = on_created
event_handler.on_deleted = on_deleted
event_handler.on_modified = on_modified
event_handler.on_moved = on_moved

# 要监听的路径
path = "test"
# 是否要监听当前目录的子目录文件发生的变化 True表示子目录的变化也监听
recursive = True
# 创建观察者
observer = Observer()
# event_handler 事件处理器
observer.schedule(event_handler, path, recursive=recursive)
# 启动事件处理器
observer.start()

try:
    while True:
        time.sleep(1)
# 按 ctrl + c 组合键退出程序
except KeyboardInterrupt:
    # 停止观察者
    observer.stop()
    observer.join()
