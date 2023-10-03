# 导入 sys 模块以接收命令行参数
import sys
from scheduler.deployment_create import create_deployment

# 输出帮助信息
def print_help():
    print("command list:")
    print("register submit a job to the system")
    print("create deployment")
    print("... help info")


# 定义一个函数，根据用户输入的命令执行相应操作
def process_command(command):
    if command == "hello":
        print("Hello, World!")
    elif command == "create deployment":
        create_deployment()
    elif command == "bye":
        print("Goodbye, World!")
    elif command == "help":
        print_help()
    else:
        print("Unknown command. Try 'help'.")

def main():
    # 程序的主要逻辑代码
    while True:
        user_input = input("$ ")    
        process_command(user_input)

if __name__ == "__main__":
    main()  # 调用主函数
