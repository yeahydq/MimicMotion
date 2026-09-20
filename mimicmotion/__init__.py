"""MimicMotion package compatibility checks."""

try:
    import transformers
except ImportError as exc:
    raise ImportError(
        "MimicMotion requires transformers>=4.42.3. "
        "Upgrade the ComfyUI environment before loading this node."
    ) from exc

# Recent PEFT releases import HybridCache during diffusers' lazy imports.
# Fail early with an actionable message instead of exposing the nested import
# error from diffusers.loaders.peft.
if not hasattr(transformers, "HybridCache"):
    raise ImportError(
        "MimicMotion requires transformers>=4.42.3 because the installed "
        "PEFT package imports HybridCache. Upgrade transformers in the same "
        "Python environment used by ComfyUI."
    )
