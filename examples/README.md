# Examples

`examples/notes/mup_tensor_programs_lecture7.md` 是当前 validator 的完整通过样例。

其他文件保留为历史样例、Notion 显示变体、局部重写片段或旧标准下的讲义输出。它们对复现写作演化有用，但不代表当前发布门槛。

运行当前通过样例：

```bash
python3 scripts/audit_examples.py --current-only
```

查看所有历史样例在当前规则下的状态：

```bash
python3 scripts/audit_examples.py --all
```

全量审计失败不一定表示仓库损坏；多数失败来自标准后续升级，例如后来新增的 `术语约定`、早期 `贯穿例子` 和 `复现测试` 硬门槛。
