# FastAPI Model 🎭🚀 - 扩展版

# Hey there! 👋  

## 🎉 这个模板能帮你快速搭建基于深度学习的视频检测服务，无需复杂配置，AI能力即刻上线！

---
# 目录结构
```bash
my_project/
├── app.py                # FastAPI 主程序
├── untils/
│   └── logger.py         # 日志工具
├── tempDir/              # 用于存储临时上传文件的目录
└── my_project_logs/      # 日志文件存储路径

```
## 闪电启动 ⚡

### 安装依赖
```bash
pip install fastapi uvicorn tqdm python-multipart
```
**torch默认正常安装**

# 推理部分更新 🔍
## 推理的部分，你可以根据实际需求进行修改：
```bash
results = inferVedio(para1, para2, ....)
```

# 使用指南
## 启动服务器
**启动 FastAPI 服务器**：
```bash
python main.py
```
### 服务将在 http://0.0.0.0:10086 燃情启动！🔥

# 接口使用指南 📮

## API 端点

### POST /node1/predict_node/
**描述：上传视频文件进行推理**

### 请求体：
**file: 一个视频文件，支持 mp4 格式**

### 响应：
**成功时：返回推理结果（具体内容取决于 inferVedio() 方法的实现）**
**失败时：返回 500 错误，错误信息会被记录到日志中**

## 请求示例
```bash
curl -X 'POST' \
  'http://127.0.0.1:10086/node1/predict_node/' \
  -F 'file=@/path/to/your/video.mp4'
```
## 处理逻辑✨
### 文件上传：用户通过 API 上传一个视频文件，FastAPI 将文件保存到 tempDir 目录，文件名使用一个唯一的 UUID 标识。
### 推理处理：上传的视频文件通过 inferVedio() 函数进行推理。该函数可以根据需求修改，具体推理逻辑需要根据模型来实现。
### 日志记录：服务器运行日志会保存到 my_project_logs 目录中，方便调试和监控。

## 错误处理🧪
### 如果在上传或推理过程中发生错误，API 会返回一个 HTTP 500 错误，并且错误信息会被记录到日志文件中。

## 开发与扩展💡
### 添加更多推理节点
**您可以通过 FastAPI 的 APIRouter 来扩展更多推理节点。例如，您可以添加其他 /node2/predict_node/ 这样的路由来实现不同模型的推理任务**
```bash
your_router_2 = APIRouter(prefix="/node2")

@your_router_2.post("/predict_node/")
async def predict_node_2(file: UploadFile = File(...)):
    # 执行其他推理逻辑
    return {"message": "New inference result"}
    
app.include_router(your_router_2)
```
# 日志📊
## 日志将记录每次请求的详细信息，包括上传文件、推理过程中的错误或成功信息。
## 可以根据需要调整日志级别，当前设置为 INFO，可以通过修改 logger 配置来调整。
# Happy Codeing! 😎👨💻
# 用AI守护世界和平！🛡️🔍
