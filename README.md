# Midjourney API Image Generator

## 项目概述

`Midjourney Image Generator` 是一个自动化工具，旨在通过与 Midjourney API 交互生成图像。该工具支持批量处理图像生成任务，下载生成的图像，并将图像切割成多个部分。此项目展示了如何使用 Python 编写一个多线程程序来高效地处理多个图像生成任务。

## 功能

- **提交任务**: 将图像生成任务提交给 Midjourney API。
- **查询任务状态**: 定期查询任务的状态，直到任务完成。
- **下载并切割图像**: 下载生成的图像，并将其切割成 4 个独立的部分。
- **批量处理**: 从 CSV 文件中读取多个提示词，并使用多线程同时处理这些任务。

## 使用说明

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

