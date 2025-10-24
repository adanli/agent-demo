from fastmcp import FastMCP

mcp_server = FastMCP()


def greet(name: str) -> str:
    """
    生成个性化问候
    :param name: 要问候的人的姓名
    :return: 问候语字符串
    """
    return f"你好, {name}!很高兴认识你"


if __name__ == '__main__':
    mcp_server.run(
        transport='http',
        host='localhost',
        port=8080
    )
