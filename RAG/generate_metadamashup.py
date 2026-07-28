#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

def infer_category(title: str, path: str, tags: list[str]) -> str:
    title_lower = title.lower()
    path_lower = path.lower()
    tags_lower = [t.lower() for t in tags]

    if "expense" in title_lower or "expense" in path_lower or "expenses" in tags_lower:
        return "Expenses"
    if "withdrawal" in title_lower or "withdrawal" in path_lower or "withdrawals" in tags_lower:
        if "atm" in title_lower or "atm" in tags_lower:
            return "ATM Cash Withdrawals"
        if "branch" in title_lower or "branch" in tags_lower:
            return "Branch Cash Withdrawals"
        return "Cash Withdrawals"
    if "deposit" in title_lower or "deposit" in path_lower or "deposits" in tags_lower:
        if "atm" in title_lower or "atm" in tags_lower:
            if "cash" in title_lower or "cash" in tags_lower:
                return "ATM Cash Deposits"
            return "ATM Check Deposits"
        if "branch" in title_lower or "branch" in tags_lower:
            return "Branch Cash Deposits"
        if "check" in title_lower or "check" in tags_lower:
            return "Check Deposits"
        return "Deposits"
    if "query" in title_lower or "query" in path_lower:
        return "User Query"
    return tags[0] if tags else "General"


def build_mashup(swagger_file: Path, output_file: Path) -> int:
    swagger = json.loads(swagger_file.read_text())
    paths = swagger.get("paths", {})
    records = []

    api_counter = 1
    for path, methods in paths.items():
        for method_details in methods.values():
            summary = method_details.get("summary", "").strip()
            description = method_details.get("description", "").strip() or summary
            tags = method_details.get("tags", [])
            category = infer_category(summary, path, tags)

            records.append(
                {
                    "api_id": f"api_{api_counter:03d}",
                    "title": summary,
                    "description": description,
                    "category": category,
                    "tags": tags,
                }
            )
            api_counter += 1

    output_file.write_text(json.dumps(records, indent=2) + "\n")
    return len(records)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a metadata mashup from Swagger API definitions.")
    parser.add_argument(
        "--swagger",
        default="SwaggerAPIs.json",
        help="Path to the Swagger/OpenAPI JSON file.",
    )
    parser.add_argument(
        "--output",
        default="metadamashup.json",
        help="Path to write the generated metadata mashup JSON file.",
    )

    args = parser.parse_args()
    swagger_path = Path(args.swagger)
    output_path = Path(args.output)

    if not swagger_path.exists():
        raise SystemExit(f"Swagger file not found: {swagger_path}")

    count = build_mashup(swagger_path, output_path)
    print(f"Generated {count} metadata records in {output_path}")


if __name__ == "__main__":
    main()
