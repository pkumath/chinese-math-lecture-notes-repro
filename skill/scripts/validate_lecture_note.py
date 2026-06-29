#!/usr/bin/env python3
"""Validate math lecture-note skill files and draft notes.

This is a structural and Notion-math hygiene gate. It does not certify
mathematical correctness.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_SKILL_FILES = [
    "SKILL.md",
    "references/quality-rubric.md",
    "references/proof-granularity-audit.md",
    "scripts/validate_lecture_note.py",
]

REQUIRED_NOTE_PATTERNS_ZH = [
    r"预备知识",
    r"学习目标|目标",
    r"目录",
    r"路线图|Roadmap",
    r"核心定义|定义",
    r"贯穿例子|核心例子|主例子",
    r"例子",
    r"非例子|反例",
    r"定理",
    r"证明",
    r"练习",
    r"复现测试|读者复现",
    r"常见误解|误区",
    r"总结|带走",
]

REQUIRED_NOTE_PATTERNS_EN = [
    r"Prerequisites",
    r"Learning Goals|Learning Objectives|Goals",
    r"Table of Contents|Contents",
    r"Roadmap|Learning Path|Dependency Map",
    r"Core Definition|Definition",
    r"Running Example|Core Example|Guiding Example",
    r"Example",
    r"Non-example|Counterexample",
    r"Theorem|Proposition|Lemma",
    r"Proof",
    r"Exercises",
    r"Reproduction Test|Reader Reproduction",
    r"Common Pitfalls|Pitfalls|Misconceptions",
    r"Summary|Takeaways",
]

VISUAL_PATTERNS = [
    r"```mermaid",
    r"<table\b",
    r"\|[^\n]+\|[^\n]*\n\|[-:| ]+\|",
    r"ASCII",
    r"!\[[^\]]*\]\(",
    r"流程图|关系图|依赖图|路线图|相图|示意图",
    r"flowchart|dependency graph|phase map|commutative diagram|schematic",
]

SUMMARY_HEADING_PATTERN_ZH = re.compile(r"^##\s*一页摘要\s*$", re.M)
SUMMARY_HEADING_PATTERN_EN = re.compile(r"^##\s*One-Page Summary\s*$", re.M | re.I)

FRONT_ROADMAP_HEADING_PATTERN_ZH = re.compile(
    r"^##+\s*(?:前置路线图|路线图|学习路径图|依赖图|路线图与关系图)\b",
    re.M,
)
FRONT_ROADMAP_HEADING_PATTERN_EN = re.compile(
    r"^##+\s*(?:Front Roadmap|Roadmap|Learning Path|Dependency Map|Roadmap and Dependencies)\b",
    re.M | re.I,
)

CORE_EXAMPLE_HEADING_PATTERN_ZH = re.compile(
    r"^##+\s*(?:\d+[.、]\s*)?(?:贯穿例子|核心例子|主例子|从一个模型开始)\b",
    re.M,
)
CORE_EXAMPLE_HEADING_PATTERN_EN = re.compile(
    r"^##+\s*(?:\d+[.]\s*)?(?:Running Example|Core Example|Guiding Example|Start from an Example)\b",
    re.M | re.I,
)
REPRODUCTION_HEADING_PATTERN_ZH = re.compile(
    r"^##+\s*(?:\d+[.、]\s*)?(?:复现测试|读者复现|学习复现测试)\b",
    re.M,
)
REPRODUCTION_HEADING_PATTERN_EN = re.compile(
    r"^##+\s*(?:\d+[.]\s*)?(?:Reproduction Test|Reader Reproduction|Learning Reproduction Test)\b",
    re.M | re.I,
)
THEOREM_HEADING_PATTERN_ZH = re.compile(
    r"^##+\s*(?:\d+[.、]\s*)?(?:定理|命题|引理)\b",
    re.M,
)
THEOREM_HEADING_PATTERN_EN = re.compile(
    r"^##+\s*(?:\d+[.]\s*)?(?:Theorem|Proposition|Lemma)\b",
    re.M | re.I,
)

BROKEN_LATEX_PATTERNS = [
    r"pimathbb",
    r"A\^top",
    r"topsucceq",
    r"(?<!\\)mathbb\s*[A-Za-z]",
    r"(?<!\\)nabla\s+[A-Za-z]",
]

HANDWAVE_PATTERNS = [
    r"证明略",
    r"略证",
    r"不再证明",
    r"显然",
    r"容易看出",
    r"it is easy to see",
    r"omitted",
]

TERMINOLOGY_HEADING_PATTERN_ZH = re.compile(
    r"^##+\s*(?:\d+[.、]\s*)?(?:术语约定|符号与术语|术语表|记号与术语)\b",
    re.M,
)
TERMINOLOGY_HEADING_PATTERN_EN = re.compile(
    r"^##+\s*(?:\d+[.]\s*)?(?:Terminology|Notation and Terminology|Notation|Terms and Notation)\b",
    re.M | re.I,
)
ENGLISH_WORD_PATTERN = re.compile(r"\b[A-Za-z][A-Za-z-]{2,}\b")
ALLOWED_ENGLISH_WORDS = {
    "adam",
    "adamw",
    "api",
    "appendix",
    "arxiv",
    "clt",
    "dom",
    "garrett",
    "github",
    "html",
    "json",
    "katex",
    "latex",
    "mlp",
    "mup",
    "netsor",
    "notion",
    "ntk",
    "pdf",
    "programs",
    "pytorch",
    "section",
    "sgd",
    "sp",
    "tensor",
}
TRANSLATABLE_ENGLISH_TERMS = {
    "base": "基准",
    "check": "检查",
    "coord": "坐标",
    "coordinate": "坐标",
    "coordinates": "坐标",
    "copy": "复制",
    "desiderata": "判据",
    "diagnostic": "诊断",
    "interface": "接口",
    "learning": "学习",
    "loss": "损失",
    "master": "主坐标/主超参数",
    "model": "模型",
    "models": "模型",
    "optimizer": "优化器",
    "proxy": "代理模型/调参模型",
    "rate": "率",
    "raw": "原始数值",
    "readout": "读出层",
    "schedule": "调度",
    "shape": "形状",
    "shapes": "形状",
    "surface": "曲面/景观",
    "target": "目标模型",
    "transfer": "迁移",
    "tuning": "调参",
    "validation": "验证",
    "width": "宽度",
    "zero-shot": "零样本/零调参",
}

CLICKABLE_TOC_PATTERN = re.compile(r"<table_of_contents\b[^>]*/>", re.I)
TOC_HEADING_PATTERN_ZH = re.compile(r"^##\s*目录\s*$", re.M)
TOC_HEADING_PATTERN_EN = re.compile(r"^##\s*(?:Table of Contents|Contents)\s*$", re.M | re.I)


LANGUAGE_BUNDLES = {
    "zh": {
        "required_note_patterns": REQUIRED_NOTE_PATTERNS_ZH,
        "summary_heading": SUMMARY_HEADING_PATTERN_ZH,
        "front_roadmap_heading": FRONT_ROADMAP_HEADING_PATTERN_ZH,
        "core_example_heading": CORE_EXAMPLE_HEADING_PATTERN_ZH,
        "reproduction_heading": REPRODUCTION_HEADING_PATTERN_ZH,
        "theorem_heading": THEOREM_HEADING_PATTERN_ZH,
        "terminology_heading": TERMINOLOGY_HEADING_PATTERN_ZH,
        "toc_heading": TOC_HEADING_PATTERN_ZH,
        "first_substantive": r"^##\s+(?:预备知识|读者画像|\d+\.|一、)",
        "core_terms": r"贯穿例子|核心例子|主例子",
        "repro_labels": [
            ("input", r"输入|给定|题目"),
            ("expected output", r"输出|产出|得到|写出"),
            ("pass criteria", r"通过标准|合格|检查"),
        ],
        "summary_required_groups": [
            ("central problem", r"问题|缺口|回答"),
            ("main answer", r"答案|核心|结论|主线"),
            ("reading path", r"读|路线|流程|步骤"),
            ("boundary", r"边界|不能|不自动|额外|不是"),
        ],
        "summary_max_chars": 1100,
        "summary_para_max_chars": 260,
    },
    "en": {
        "required_note_patterns": REQUIRED_NOTE_PATTERNS_EN,
        "summary_heading": SUMMARY_HEADING_PATTERN_EN,
        "front_roadmap_heading": FRONT_ROADMAP_HEADING_PATTERN_EN,
        "core_example_heading": CORE_EXAMPLE_HEADING_PATTERN_EN,
        "reproduction_heading": REPRODUCTION_HEADING_PATTERN_EN,
        "theorem_heading": THEOREM_HEADING_PATTERN_EN,
        "terminology_heading": TERMINOLOGY_HEADING_PATTERN_EN,
        "toc_heading": TOC_HEADING_PATTERN_EN,
        "first_substantive": r"^##\s+(?:Prerequisites|Reader Profile|\d+\.)",
        "core_terms": r"Running Example|Core Example|Guiding Example",
        "repro_labels": [
            ("input", r"Input|Given|Task"),
            ("expected output", r"Expected Output|Output|Derive|Prove|Produce"),
            ("pass criteria", r"Pass Criteria|Criteria|Check|Passes"),
        ],
        "summary_required_groups": [
            ("central problem", r"problem|question|gap|answer"),
            ("main answer", r"answer|main|core|claim|conclusion"),
            ("reading path", r"read|path|route|section|sequence"),
            ("boundary", r"boundary|scope|does not|not prove|outside"),
        ],
        "summary_max_chars": 1600,
        "summary_para_max_chars": 450,
    },
}


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def bundle(language: str) -> dict[str, object]:
    try:
        return LANGUAGE_BUNDLES[language]
    except KeyError:
        fail(f"unsupported language: {language}")


def check_skill(skill_dir: Path, language: str) -> None:
    missing = [rel for rel in REQUIRED_SKILL_FILES if not (skill_dir / rel).exists()]
    if missing:
        fail("missing required skill files: " + ", ".join(missing))
    text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    if language == "zh":
        if "name: chinese-math-lecture-notes" not in text:
            fail("SKILL.md frontmatter name is missing or wrong")
        if "Chinese-first terminology" not in text:
            fail("SKILL.md must require Chinese-first terminology discipline")
    else:
        if "name: english-math-lecture-notes" not in text:
            fail("SKILL.md frontmatter name is missing or wrong for English skill")
        if "English mathematical prose" not in text:
            fail("SKILL.md must require polished English mathematical prose")
        if "terminology discipline" not in text:
            fail("SKILL.md must require terminology discipline")
    if "Lecture Notes" not in text or "Notion" not in text:
        fail("SKILL.md must mention the Lecture Notes Notion destination")
    if "dollar-backtick" not in text:
        fail("SKILL.md must state Notion inline math format")
    for gate in [
        "Proof-Granularity Gate",
        "Standard Sync Gate",
        "One-Page Summary Gate",
        "Front Roadmap Gate",
        "Learning-Load and Reproduction Gate",
        "Source-Spine Coverage Gate",
    ]:
        if gate not in text:
            fail(f"SKILL.md must include the {gate}")
    if "<table_of_contents" not in text:
        fail("SKILL.md must require a clickable Notion table of contents")
    rubric = (skill_dir / "references/quality-rubric.md").read_text(encoding="utf-8")
    if language == "zh":
        required_rubric_terms = [
            ("section-by-section proof granularity", "逐节证明颗粒度"),
            ("one-page summary gate", "一页摘要门槛"),
            ("Chinese-first terminology gate", "中文优先术语门槛"),
            ("front-roadmap gate", "前置路线图"),
            ("learning-load/reproduction gate", "复现测试"),
            ("source/request spine coverage gate", "主题主干"),
            ("clickable Notion table of contents rule", "<table_of_contents"),
        ]
    else:
        required_rubric_terms = [
            ("section-by-section proof granularity", "section-by-section proof granularity"),
            ("one-page summary gate", "One-Page Summary Gate"),
            ("terminology gate", "terminology discipline"),
            ("front-roadmap gate", "Front Roadmap"),
            ("learning-load/reproduction gate", "Reproduction Test"),
            ("source/request spine coverage gate", "source/request spine"),
            ("clickable Notion table of contents rule", "<table_of_contents"),
        ]
    rubric_scan = rubric if language == "zh" else rubric.lower()
    for label, needle in required_rubric_terms:
        expected = needle if language == "zh" else needle.lower()
        if expected not in rubric_scan:
            fail(f"quality rubric must include the {label}")
    print(f"OK: skill structure ({language})")


def strip_display_math(text: str) -> str:
    return re.sub(r"\$\$.*?\$\$", "", text, flags=re.S)


def strip_code(text: str) -> str:
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    return re.sub(r"`[^`]*`", "", text)


def strip_html_tags(text: str) -> str:
    return re.sub(r"<[^>]+>", " ", text)


def check_terminology(text: str, mode: str, language: str) -> None:
    if mode != "full":
        return
    b = bundle(language)
    terminology_heading = b["terminology_heading"]
    assert isinstance(terminology_heading, re.Pattern)
    if not terminology_heading.search(text):
        if language == "zh":
            fail("missing `术语约定` / `符号与术语` section for Chinese-first terminology")
        fail("missing `Terminology` / `Notation and Terminology` section")
    if language == "en":
        scan_text = strip_html_tags(strip_code(strip_display_math(text)))
        cjk_chars = len(re.findall(r"[\u4e00-\u9fff]", scan_text))
        if cjk_chars > 80:
            fail("too much unresolved non-English text for an English lecture note")
        ai_like_patterns = [
            r"\bAI assistant\b",
            r"\bagent audit\b",
            r"\bworkflow log\b",
            r"\bdashboard\b",
        ]
        for pattern in ai_like_patterns:
            if re.search(pattern, scan_text, flags=re.I):
                fail(f"agent-facing prose found in English lecture note: {pattern}")
        return
    scan_text = strip_html_tags(strip_code(strip_display_math(text)))
    words = []
    for match in ENGLISH_WORD_PATTERN.finditer(scan_text):
        word = match.group(0)
        lower = word.lower()
        if lower in ALLOWED_ENGLISH_WORDS:
            continue
        if word.isupper() and 3 <= len(word) <= 8:
            continue
        words.append(lower)
    counts: dict[str, int] = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    repeated = {
        word: count
        for word, count in counts.items()
        if word in TRANSLATABLE_ENGLISH_TERMS and count > 2
    }
    if repeated:
        details = ", ".join(
            f"{word}({count}, use {TRANSLATABLE_ENGLISH_TERMS[word]})"
            for word, count in sorted(repeated.items(), key=lambda item: (-item[1], item[0]))[:8]
        )
        fail("repeated untranslated English lecture terms: " + details)
    cjk_chars = len(re.findall(r"[\u4e00-\u9fff]", scan_text))
    if cjk_chars and len(words) > 80 and len(words) / cjk_chars > 0.015:
        fail(f"too many unresolved English terms for a Chinese lecture note: {len(words)} terms")


def find_bad_inline_math(text: str) -> list[str]:
    body = strip_display_math(text)
    bad = []
    i = 0
    while i < len(body):
        if body[i] != "$":
            i += 1
            continue
        if body.startswith("$`", i):
            end = body.find("`$", i + 2)
            if end == -1:
                bad.append(body[i:i + 80])
                break
            i = end + 2
            continue
        if body.startswith("$$", i):
            i += 2
            continue
        j = body.find("$", i + 1)
        if j == -1:
            bad.append(body[i:i + 80])
            break
        snippet = body[i:j + 1]
        if "\n" not in snippet:
            bad.append(snippet[:80])
        i = j + 1
    return bad


def check_learning_load_and_reproduction(text: str, language: str) -> None:
    b = bundle(language)
    core_heading = b["core_example_heading"]
    theorem_heading = b["theorem_heading"]
    reproduction_heading = b["reproduction_heading"]
    assert isinstance(core_heading, re.Pattern)
    assert isinstance(theorem_heading, re.Pattern)
    assert isinstance(reproduction_heading, re.Pattern)
    core_match = core_heading.search(text)
    if not core_match:
        if language == "zh":
            fail("missing early named `贯穿例子` / `核心例子` section")
        fail("missing early named `Running Example` / `Core Example` section")
    if core_match.start() > 6500:
        fail("core example appears too late; reduce front matter and enter the mathematical point earlier")
    theorem_match = theorem_heading.search(text)
    if theorem_match and theorem_match.start() < core_match.start():
        fail("theorem-heavy section appears before the named core example")
    repro_match = reproduction_heading.search(text)
    if not repro_match:
        if language == "zh":
            fail("missing `复现测试` section")
        fail("missing `Reproduction Test` section")
    repro_block = text[repro_match.start():]
    next_heading = re.search(r"^##\s+", repro_block[1:], flags=re.M)
    if next_heading:
        repro_block = repro_block[: next_heading.start() + 1]
    repro_labels = b["repro_labels"]
    assert isinstance(repro_labels, list)
    for label, pattern in repro_labels:
        if not re.search(pattern, repro_block, flags=re.I):
            fail(f"reproduction test is missing {label} criteria")
    core_terms = b["core_terms"]
    assert isinstance(core_terms, str)
    core_phrase_count = len(re.findall(core_terms, text, flags=re.I))
    if core_phrase_count < 3:
        fail("core example is not reused enough across the lecture")


def check_source_spine_terms(text: str, required_terms: list[str]) -> None:
    for term in required_terms:
        if not re.search(term, text, flags=re.I):
            fail(f"missing required source/request spine term: {term}")


def check_one_page_summary(text: str, language: str) -> re.Match[str]:
    b = bundle(language)
    summary_heading = b["summary_heading"]
    assert isinstance(summary_heading, re.Pattern)
    summary_match = summary_heading.search(text)
    if not summary_match:
        if language == "zh":
            fail("missing `## 一页摘要` section")
        fail("missing `## One-Page Summary` section")
    next_heading = re.search(r"^##\s+", text[summary_match.end():], flags=re.M)
    if not next_heading:
        fail("one-page summary must be followed by another section heading")
    summary_end = summary_match.end() + next_heading.start()
    summary_block = text[summary_match.end():summary_end].strip()
    if "$$" in summary_block:
        fail("one-page summary must not contain display math or derivations")
    plain_summary = strip_html_tags(strip_code(strip_display_math(summary_block)))
    compact_len = len(re.sub(r"\s+", "", plain_summary))
    summary_max_chars = b["summary_max_chars"]
    assert isinstance(summary_max_chars, int)
    if compact_len > summary_max_chars:
        fail(f"one-page summary is too long ({compact_len} non-space chars); compress the orientation")
    prose_blocks = [p.strip() for p in re.split(r"\n\s*\n", summary_block) if p.strip()]
    prose_paragraphs = [p for p in prose_blocks if "<table" not in p and "</table" not in p]
    if len(prose_paragraphs) > 4:
        fail("one-page summary has too many prose paragraphs; keep at most four")
    summary_para_max_chars = b["summary_para_max_chars"]
    assert isinstance(summary_para_max_chars, int)
    for para in prose_paragraphs:
        para_plain = strip_html_tags(strip_code(para))
        para_len = len(re.sub(r"\s+", "", para_plain))
        if para_len > summary_para_max_chars:
            fail(f"one-page summary paragraph is too long ({para_len} non-space chars)")
    required_groups = b["summary_required_groups"]
    assert isinstance(required_groups, list)
    missing = [name for name, pattern in required_groups if not re.search(pattern, plain_summary, flags=re.I)]
    if missing:
        fail("one-page summary misses orientation signals: " + ", ".join(missing))
    return summary_match


def check_note(note: Path, mode: str, required_terms: list[str] | None = None, language: str = "zh") -> None:
    text = note.read_text(encoding="utf-8")
    required_terms = required_terms or []
    b = bundle(language)
    check_source_spine_terms(text, required_terms)
    if len(text.strip()) < 2500 and mode == "full":
        fail("full lecture note is too short")
    if text.lstrip().startswith("# "):
        fail("body starts with an H1; Notion title should live in page properties")
    bad_inline = find_bad_inline_math(text)
    if bad_inline:
        fail("ordinary inline math found; use dollar-backtick math: " + "; ".join(bad_inline[:5]))
    if text.count("$$") % 2:
        fail("unbalanced display math delimiters")
    check_terminology(text, mode, language)
    if mode == "full":
        summary_match = check_one_page_summary(text, language)
        toc_heading = b["toc_heading"]
        assert isinstance(toc_heading, re.Pattern)
        if not toc_heading.search(text):
            if language == "zh":
                fail("missing `## 目录` heading for clickable table of contents")
            fail("missing `## Table of Contents` heading for clickable table of contents")
        toc_match = CLICKABLE_TOC_PATTERN.search(text)
        if not toc_match:
            fail('missing clickable Notion table of contents block: <table_of_contents color="gray"/>')
        if toc_match.start() < summary_match.end():
            fail("clickable table of contents must appear after the one-page summary")
        first_substantive_pattern = b["first_substantive"]
        assert isinstance(first_substantive_pattern, str)
        first_substantive = re.search(first_substantive_pattern, text, flags=re.M | re.I)
        if first_substantive and toc_match.start() > first_substantive.start():
            fail("clickable table of contents must appear before the first substantive section")
        roadmap_heading = b["front_roadmap_heading"]
        assert isinstance(roadmap_heading, re.Pattern)
        roadmap_match = roadmap_heading.search(text)
        if not roadmap_match:
            fail("missing front roadmap heading after the clickable table of contents")
        if roadmap_match.start() < toc_match.end():
            fail("front roadmap must appear after the clickable table of contents")
        if first_substantive and roadmap_match.start() > first_substantive.start():
            fail("front roadmap must appear before the first substantive section")
        roadmap_end = first_substantive.start() if first_substantive else min(len(text), roadmap_match.start() + 3000)
        roadmap_block = text[roadmap_match.start():roadmap_end]
        if not any(re.search(p, roadmap_block, flags=re.M | re.I) for p in VISUAL_PATTERNS):
            fail("front roadmap must contain a visual path/dependency block, not only prose")
        check_learning_load_and_reproduction(text, language)
    latex_scan_text = strip_code(text)
    for pattern in BROKEN_LATEX_PATTERNS:
        if re.search(pattern, latex_scan_text):
            fail(f"possible damaged LaTeX command: {pattern}")
    required_patterns = b["required_note_patterns"]
    assert isinstance(required_patterns, list)
    missing = [p for p in required_patterns if not re.search(p, text, flags=re.I)]
    if missing and mode == "full":
        fail("missing required lecture sections/patterns: " + ", ".join(missing))
    if mode == "full" and not any(re.search(p, text, flags=re.M | re.I) for p in VISUAL_PATTERNS):
        fail("missing visual structure block: mermaid/table/image/diagram")
    if mode == "full" and len(re.findall(r"\$`[^`]+`\$", text)) < 8:
        fail("too few Notion inline math expressions")
    if mode == "full" and text.count("$$") < 4:
        fail("too few display equations")
    if mode == "full":
        for pattern in HANDWAVE_PATTERNS:
            if re.search(pattern, text, flags=re.I):
                fail(f"hand-waved proof phrase found: {pattern}")
        theorem_terms = r"定理|命题|引理" if language == "zh" else r"Theorem|Proposition|Lemma"
        theorem_count = len(re.findall(theorem_terms, text, flags=re.I))
        if theorem_count and not re.search(r"证明路线|证明脊柱|proof spine|proof route|proof outline|proof roadmap", text, flags=re.I):
            fail("theorem-like content exists but no proof spine/route is marked")
        if theorem_count and not re.search(r"假设在哪里用|Where the hypotheses are used|Hypothesis use", text, flags=re.I):
            fail("theorem-like content exists but hypotheses-use explanation is missing")
        if language == "zh":
            major_section_pattern = r"^##\s+(?:\d+\.|[一二三四五六七八九十]+|总结|下一步|Reference)"
            takeaways_pattern = r"本(?:节|小节)带走什么"
        else:
            major_section_pattern = r"^##\s+(?:\d+\.|Summary|Next Steps|Reference)"
            takeaways_pattern = r"Takeaway|Takeaways|What to remember"
        major_sections = len(re.findall(major_section_pattern, text, flags=re.M | re.I))
        takeaways = len(re.findall(takeaways_pattern, text, flags=re.I))
        if major_sections >= 4 and takeaways < max(4, major_sections // 2):
            fail(
                "too few section-end memory-compression blocks "
                f"({takeaways} takeaways for {major_sections} major sections)"
            )
    print(f"OK: note {note} ({language})")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--language", choices=["zh", "en"], default="zh")
    parser.add_argument("--skill-dir", type=Path)
    parser.add_argument("--note", type=Path)
    parser.add_argument("--mode", choices=["light", "full"], default="light")
    parser.add_argument(
        "--required-term",
        action="append",
        default=[],
        help="Regex that must appear in the note because it belongs to the source/request spine. Repeat for multiple terms.",
    )
    args = parser.parse_args()

    if not args.skill_dir and not args.note:
        fail("provide --skill-dir and/or --note")
    if args.skill_dir:
        check_skill(args.skill_dir, args.language)
    if args.note:
        check_note(args.note, args.mode, args.required_term, args.language)


if __name__ == "__main__":
    main()
