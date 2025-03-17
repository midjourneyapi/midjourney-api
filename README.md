# MidJourney API 图像生成演示

这个项目是一个简单的 MidJourney API 图像生成演示程序，通过 aiyiapi 平台聚合全球 AI API，实现一个代码轻松接入 MidJourney 服务的功能。MidJourney 是一个强大的 AI 图像生成服务，能够根据文本提示词生成高质量图像。本项目支持多线程处理提示词、图像下载与切割，并完全兼容 MidJourney 的接口规范。

## 功能特点

- 通过文本提示词生成 AI 图像
- 支持从 CSV 文件批量读取提示词
- 多线程处理，提高任务提交和图像生成效率
- 自动下载生成的图像并切割为 4 张独立子图
- 详细的调试信息输出，便于跟踪任务状态
- 通过 aiyiapi 平台统一调用，稳定且高效

## 使用方法

1. 克隆此仓库到本地
2. 安装所需依赖：`pip install requests pillow`
3. 在脚本中填入您的 aiyiapi 平台 API 密钥（替换 `headers` 中的 `Authorization` 值）
4. 准备一个 `prompts.csv` 文件，包含 `prompt` 列（示例格式见下文）

### 安装依赖

在开始使用之前，你需要安装项目的依赖库。请确保你已经安装了 Python 环境，并运行以下命令来安装所需的库：

```
 bash
pip install requests pillo
```

## 配置 API 密钥
在 midjourney.py 文件中，你需要设置 API 密钥以便进行身份验证。找到以下部分，并将 YOUR_API_KEY_HERE 替换为你的实际 API 密钥
``` ·headers = {
    'Authorization': 'Bearer YOUR_API_KEY_HERE',
    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
    'Content-Type': 'application/json'
}
```
确保你的 API 密钥具有相应的权限来访问 Midjourney API。

## 准备 CSV 文件
创建一个名为 prompts.csv 的文件，文件中应包含一列 prompt，其中每行是一个图像生成的提示词。例如：
```
prompt
"A beautiful sunset over the mountains"
"A futuristic city skyline"
"A serene lake surrounded by forests"
```

## 运行脚本
确保 prompts.csv 文件与 midjourney.py 脚本在同一目录下。运行以下命令来启动脚本：
```
python midjourney.py
```
脚本将会读取 CSV 文件中的提示词，提交生成图像的任务，并处理图像。


## 代码结构
### midjourney.py: 主脚本文件，包含所有功能实现。
### submit_task(prompt): 提交图像生成任务。
### fetch_task_status(task_id): 查询任务状态。
### save_and_split_image(image_url, base_filename): 下载图像并切割为 4 张部分。
### process_prompt(prompt): 处理单个提示词的任务提交和状态查询。
### process_prompts(csv_file): 从 CSV 文件中处理每个提示词。
开发和贡献
如果你有任何建议或想要为项目做出贡献，欢迎提交问题或发起拉取请求。请遵循以下步骤：

## Fork 本仓库。
创建一个新的分支 (git checkout -b feature-branch)。
提交你的更改 (git commit -am 'Add new feature')。
推送到远程分支 (git push origin feature-branch)。
创建一个新的 Pull Request。
许可证
此项目采用 MIT 许可证，更多细节请参见 LICENSE 文件。

## 联系方式
如果你有任何问题或需要进一步的帮助，可以通过以下方式联系我：

电子邮件: xiaofanqiesic@gmail.com

