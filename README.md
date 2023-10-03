a job scheduling system based on k8s implementes by python


##### 参考项目结构
my_project/
│
├── README.md                # 项目文档，包含项目介绍、安装和使用说明等
├── requirements.txt         # 项目依赖的 Python 包列表
│
├── config/                  # 配置文件目录
│   ├── yaml                 # k8s yaml 配置 
│   └── ...
│
├── data/                    # 数据文件目录
│   ├── data.csv             # 项目所需的数据文件
│   └── ...
│
├── src/                     # 项目源代码目录
│   ├── __init__.py
│   ├── main.py              # 主应用程序入口
│   ├── module1.py           # 自定义模块1
│   ├── module2.py           # 自定义模块2
│   └── ...
│
├── tests/                   # 单元测试目录
│   ├── test_module1.py      # 对模块1的单元测试
│   ├── test_module2.py      # 对模块2的单元测试
│   └── ...
│
├── static/                  # 静态文件目录（如 CSS、JavaScript、图像等）
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/               # 模板文件目录（如 HTML 模板文件）
│   ├── index.html
│   ├── ...
│
├── logs/                    # 日志文件目录
│   ├── error.log            # 错误日志
│   ├── access.log           # 访问日志
│   └── ...
│
├── venv/                    # 虚拟环境目录（可选）
│
└── .gitignore               # Git 忽略文件配置
