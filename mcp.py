# demo.py
from fastmcp import FastMCP, Tool
from datetime import datetime

app = FastMCP(title="Time Tool Service", version="1.0.0")

@app.tool(name="get_current_time", description="获取当前的日期和时间")
def get_current_time() -> str:
    """返回当前时间的字符串表示"""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"当前时间是：{now}"

@app.tool(name="add_numbers", description="将两个数字相加")
def add_numbers(a: float, b: float) -> float:
    """返回 a + b 的结果"""
    return a + b

if __name__ == "__main__":
    # 启动 MCP 服务，默认监听 8000 端口
    app.run(host="0.0.0.0", port=8000)
