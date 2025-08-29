from vllm import ModelRegistry

from .model import TrillionForCausalLM


def register():
    ModelRegistry.register_model("TrillionForCausalLM", TrillionForCausalLM)
