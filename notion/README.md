# Notion Publishing Notes

The private workspace used a Notion page named `Lecture Notes` as the destination and a Notion page named `中文数学讲义生成标准` as the standards authority.

This public repo intentionally does not include:

- Notion API tokens.
- Private page IDs.
- Browser/CDP scripts bound to a local authenticated profile.
- Readback logs that expose private workspace URLs.

To reproduce publication in your own Notion workspace:

1. Create a parent page named `Lecture Notes`.
2. Create or copy a standards page named `中文数学讲义生成标准`.
3. Draft the note locally in Markdown.
4. Run:

```bash
python3 scripts/validate_lecture_note.py --note path/to/note.md --mode full
```

5. Publish with your own Notion connector or importer.
6. Read the page back and verify:
   - `## 一页摘要`
   - clickable table of contents
   - front roadmap
   - terminology table
   - early core example
   - reproduction test
   - display math and inline math rendering

The readback/render check is part of the workflow. A successful Markdown validation does not prove the Notion page rendered correctly.
