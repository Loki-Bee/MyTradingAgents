from dotenv import load_dotenv

from tradingagents.graph.trading_graph import TradingAgentsGraph
load_dotenv()
# ── MiniMax 示例（推荐）─────────────────────────────
# config = {
#     "llm_provider": "glm",
#     "deep_think_llm": "MiniMax-M2.7",
#     "quick_think_llm": "MiniMax-M2.7-highspeed",
#     "output_language": "Chinese",
# }
# ── DeepSeek 示例 ───────────────────────────────────
# config = {
#     "llm_provider": "deepseek",
#     "deep_think_llm": "deepseek-v4-pro",
#     "quick_think_llm": "deepseek-flash",
#     "output_language": "Chinese",
#     "llm_timeout": 300,           # ← 新增：超时从 150 秒放宽到 300 秒
#     "checkpoint_enabled": True,   # ← 新增：开断点续跑，崩了可从断点恢复
# }

# ── Anthropic + Kimi 示例 ───────────────────────────
# config = {
#     "llm_provider": "anthropic",
#     "deep_think_llm": "claude-sonnet-4-6",
#     "quick_think_llm": "claude-sonnet-4-6",
#     "backend_url": "https://api.kimi.com/coding/",
#     "output_language": "Chinese",
# }


config = {
    "llm_provider": "glm",
    "deep_think_llm": "glm-5.3",
    "quick_think_llm": "glm-5.3-flash",
    "output_language": "Chinese",
    "llm_timeout": 300,           # ← 新增：超时从 150 秒放宽到 300 秒
    "checkpoint_enabled": True,   # ← 新增：开断点续跑，崩了可从断点恢复
}


ta = TradingAgentsGraph(config=config)
final_state, decision = ta.propagate("600872", "2026-10-23")
print(decision)