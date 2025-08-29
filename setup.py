from setuptools import setup

setup(
    name="trillion-vllm-plugin",
    version="0.1",
    packages=["src"],
    entry_points={
        "vllm.general_plugins": [
            "register_trillion_model = src:register"
        ]
    }
)