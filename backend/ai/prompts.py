from typing import Optional


def build_prompt(code: str, filename: Optional[str] = None) -> str:
    header = f"File: {filename}\n\n" if filename else ""
    return (
        header
        + "Analyze the following C function and return a JSON object ONLY (no additional text) with the following keys:\n"
        + '  - "title": short title for the function\n'
        + '  - "summary": one-paragraph summary\n'
        + '  - "details": longer explanation of what it does\n'
        + '  - "rationale": why it may be implemented this way\n'
        + '  - "performance": performance considerations\n'
        + '  - "hidden_insights": list of non-obvious observations\n'
        + '  - "where_used": list of likely call-sites or modules\n'
        + '  - "tags": list of short tags\n'
        + '  - "markdown": a ready-to-save Obsidian note body (string)\n\n'
        + "Ensure the JSON is well-formed. Do not include code fences in the markdown field.\n\n"
        + "Code:\n\n"
        + code
    )
