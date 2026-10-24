"""Shared model catalog for CLI selections and validation."""

from __future__ import annotations

from typing import Dict, List, Tuple

ModelOption = Tuple[str, str]
ProviderModeOptions = Dict[str, Dict[str, List[ModelOption]]]


MODEL_OPTIONS: ProviderModeOptions = {
    "openai": {
        "quick": [
            ("GPT-6 Luna - Most efficient for high-volume tasks", "gpt-6-luna"),
            ("GPT-6 Sol - Strong reasoning and agentic workflows", "gpt-6-sol"),
            ("GPT-5.6 Luna - Efficient previous-generation model", "gpt-5.6-luna"),
        ],
        "deep": [
            ("GPT-6 Astra - Most capable for complex reasoning and coding", "gpt-6-astra"),
            ("GPT-6 Sol - Strong reasoning and agentic workflows", "gpt-6-sol"),
            ("GPT-5.6 Sol - Previous-generation flagship", "gpt-5.6-sol"),
            ("Custom model ID", "custom"),
        ],
    },

    "anthropic": {
        "quick": [
            ("Claude Sonnet 5 - Fast and capable for agents and coding", "claude-sonnet-5"),
            ("Claude Haiku 4.5 - Fastest, cost-efficient", "claude-haiku-4-5"),
        ],
        "deep": [
            ("Claude Opus 5.5 - Latest flagship for complex agentic work", "claude-opus-5-5"),
            ("Claude Fable 5.1 - Long-running agents and complex workflows", "claude-fable-5-1"),
            ("Claude Sonnet 5 - Strong speed/intelligence balance", "claude-sonnet-5"),
            ("Custom model ID", "custom"),
        ],
    },

    "google": {
        "quick": [
            ("Gemini 3.8 Flash - Latest stable fast model", "gemini-3.8-flash"),
            ("Gemini 3.5 Flash-Lite - Cost-efficient high-volume", "gemini-3.5-flash-lite"),
            ("Gemini 3.7 Flash - Previous-generation stable Flash", "gemini-3.7-flash"),
        ],
        "deep": [
            ("Gemini 3.1 Pro - Advanced reasoning and complex workflows", "gemini-3.1-pro-preview"),
            ("Gemini 3.8 Flash - Latest stable general model", "gemini-3.8-flash"),
            ("Gemini 2.5 Pro - Legacy stable Pro model", "gemini-2.5-pro"),
            ("Custom model ID", "custom"),
        ],
    },

    "xai": {
        "quick": [
            ("Grok 4.7 - Latest flagship, configurable reasoning", "grok-4.7"),
            ("Grok 4.6 - Fast frontier model", "grok-4.6"),
            ("Grok 4.5 - Agentic coding and knowledge work", "grok-4.5"),
        ],
        "deep": [
            ("Grok 4.20 - Deep reasoning model", "grok-4.20"),
            ("Grok 4.7 - Latest flagship reasoning model", "grok-4.7"),
            ("Grok 4.5 - Strong agentic coding and reasoning", "grok-4.5"),
            ("Custom model ID", "custom"),
        ],
    },

    "deepseek": {
        "quick": [
            ("DeepSeek V4.1 Flash - Latest fast model", "deepseek-flash"),
            ("DeepSeek V4 Flash - Legacy alias", "deepseek-v4-flash"),
            ("Custom model ID", "custom"),
        ],
        "deep": [
            ("DeepSeek V4 Pro - Latest flagship reasoning model", "deepseek-v4-pro"),
            ("DeepSeek V4.1 Flash - Latest fast reasoning model", "deepseek-flash"),
            ("Custom model ID", "custom"),
        ],
    },

    "qwen": {
        "quick": [
            ("Qwen 3.8 Flash - Latest fast model", "qwen3.8-flash"),
            ("Qwen 3.7 Flash - Fast previous-generation model", "qwen3.7-flash"),
            ("Qwen Plus - Stable general-purpose model", "qwen-plus"),
            ("Custom model ID", "custom"),
        ],
        "deep": [
            ("Qwen 3.8 Max - Latest flagship reasoning model", "qwen3.8-max"),
            ("Qwen 3.7 Plus - Strong reasoning and agent workflows", "qwen3.7-plus"),
            ("Qwen 3.7 Max - Previous-generation flagship", "qwen3.7-max"),
            ("Custom model ID", "custom"),
        ],
    },

    "glm": {
        "quick": [
            ("GLM-5.3-Flash - Latest fast multimodal Agent model", "glm-5.3-flash"),
            ("GLM-5.3 - Latest flagship model", "glm-5.3"),
            ("GLM-5.2 - Previous-generation flagship", "glm-5.2"),
            ("Custom model ID", "custom"),
        ],
        "deep": [
            ("GLM-5.3 - Latest flagship reasoning model", "glm-5.3"),
            ("GLM-5.2 - Strong previous-generation model", "glm-5.2"),
            ("GLM-5.1 - Previous-generation model", "glm-5.1"),
            ("Custom model ID", "custom"),
        ],
    },

    "minimax": {
        "quick": [
            ("MiniMax-M3 - Latest multimodal Agent model", "MiniMax-M3"),
            ("MiniMax-M2.7-highspeed - Fast M2.7 model", "MiniMax-M2.7-highspeed"),
            ("MiniMax-M2.7 - Previous flagship", "MiniMax-M2.7"),
            ("Custom model ID", "custom"),
        ],
        "deep": [
            ("MiniMax-M3 - Latest flagship reasoning model", "MiniMax-M3"),
            ("MiniMax-M2.7 - Strong reasoning model", "MiniMax-M2.7"),
            ("MiniMax-M2.7-highspeed - Faster alternative", "MiniMax-M2.7-highspeed"),
            ("Custom model ID", "custom"),
        ],
    },

    # Ollama models depend on what you have pulled locally.
    # Keep these as common examples; users can add their own model IDs.
    "ollama": {
        "quick": [
            ("Qwen3 - Local model", "qwen3:latest"),
            ("GPT-OSS - Local model", "gpt-oss:latest"),
            ("GLM-4.7-Flash - Local model", "glm-4.7-flash:latest"),
            ("Custom local model", "custom"),
        ],
        "deep": [
            ("GLM-4.7-Flash - Local model", "glm-4.7-flash:latest"),
            ("GPT-OSS - Local model", "gpt-oss:latest"),
            ("Qwen3 - Local model", "qwen3:latest"),
            ("Custom local model", "custom"),
        ],
    },
}

def get_model_options(provider: str, mode: str) -> List[ModelOption]:
    """Return shared model options for a provider and selection mode."""
    return MODEL_OPTIONS[provider.lower()][mode]


def get_known_models() -> Dict[str, List[str]]:
    """Build known model names from the shared CLI catalog."""
    return {
        provider: sorted(
            {
                value
                for options in mode_options.values()
                for _, value in options
            }
        )
        for provider, mode_options in MODEL_OPTIONS.items()
    }
