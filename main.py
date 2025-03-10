import shutil
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import os
import uuid
import json
import torch

from tqdm import tqdm
from fastapi.routing import APIRouter

import logging

from untils.logger import setup_logger

logger = setup_logger(log_dir="my_project_logs", log_level=logging.INFO,log_to_console=True)

# 初始化主应用
app = FastAPI()

# >>>>>>>>>>>>>>>> 初始化路由<<<<<<<<<<<<<<< # Optional
your_router = APIRouter(prefix="/node1")
# >>>>>>>>>>>>>>>>>>*****<<<<<<<<<<<<<<<<<<< #


@your_router.post("/predict_node/")
async def predict_node(file: UploadFile = File(...)):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    try:
        # 保存上传的视频
        video_id = str(uuid.uuid4())
        video_path = f"tempDir/{video_id}.mp4"
        os.makedirs(os.path.dirname(video_path), exist_ok=True)
        with open(video_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # 进行推理
        results = inferVedio(para1, para2, ...)  # 替换为实际参数

        # 成功响应
        return {
            "status": "success",
            "results": results
        }
        
    except Exception as e:
        logger.error(f"处理视频时发生错误: {str(e)}", exc_info=True)
        # 错误响应
        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "detail": str(e)
            }
        )

# >>>>>>>>>>>>>>>> 路由挂载到主应用<<<<<<<<<<<<<<< # Optional
app.include_router(your_router)


# 启动服务
if __name__ == "__main__":
    import uvicorn  # type: ignore
    uvicorn.run(app, host="0.0.0.0", port=...)
