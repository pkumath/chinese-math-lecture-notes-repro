# Reproduce Checklist

下面是一条从空白主题到可发布中文数学讲义的复现路径。

## 1. 选择主题和源材料

写作前先固定三件事：

- 主题问题：这份讲义到底要让读者会判断、会计算或会证明什么。
- 源材料：论文、教材章节、讲义或用户给出的草稿。
- 主题主干：不能缺席的定义、定理、参数化、证明工具、例子或算法。

把主题主干写进草稿；如果某个主干对象不覆盖，必须在一页摘要里明确说出范围边界。

## 2. 起草结构

复制模板：

```bash
cp templates/lecture-note-template.md my_note.md
```

正式讲义至少要有：

- `## 一页摘要`
- `## 目录` 后紧跟 `<table_of_contents color="gray"/>`
- `## 前置路线图`
- `## 术语约定` 或 `## 符号与术语`
- 早期命名的 `贯穿例子` / `核心例子`
- 核心定义、正例、非例子、定理、证明
- 分层练习
- `## 复现测试`

## 3. 运行结构验证

```bash
python3 scripts/validate_lecture_note.py --note my_note.md --mode full
```

如果主题主干里有必须出现的词，用 repeated `--required-term`：

```bash
python3 scripts/validate_lecture_note.py \
  --note my_note.md \
  --mode full \
  --required-term "abc 参数化" \
  --required-term "高斯条件化" \
  --required-term "多步递推"
```

## 4. 做证明颗粒度审计

validator 通过后，逐节回答 `skill/references/proof-granularity-audit.md` 里的问题。重点检查：

- 每节到底证明或推导了什么。
- 哪些假设被使用，弱化后哪里会坏。
- 贯穿例子是否真的贯穿定义、证明和边界。
- 读者能不能完成同型计算或证明。

## 5. Notion 发布复现

见 `notion/README.md`。公开仓库不包含任何私有 Notion 页面 ID、token 或浏览器会话脚本。
