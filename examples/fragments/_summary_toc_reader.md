## 一页摘要

这份讲义回答一个具体问题：如果 overdamped Langevin dynamics 的噪声不是标量 Brownian noise，而是

$$
dX_t=b(X_t)\,dt+A\,dB_t,
$$

其中 $`A`$ 是非退化但可能非对称的矩阵，那么它的平衡态是什么？它如何收敛到平衡态？

第一条结论非常重要：在 Itô、常系数噪声情形，$`A`$ 的非对称性本身不是动力学不变性的来源。生成元只看

$$
\Sigma=A A^\top,
$$

也就是噪声协方差。若要让 $`\pi(dx)=Z^{-1}e^{-V(x)}dx`$ 成为不变分布，漂移必须和 $`\Sigma`$ 匹配。对于本讲义的 convention

$$
dX_t=b(X_t)\,dt+A\,dB_t,
$$

reversible Gibbs drift 是

$$
b_{\mathrm{rev}}(x)=-\frac12 \Sigma \nabla V(x).
$$

更一般地，所有保持同一个 Gibbs 平衡态的常扩散系数 drift 可写成

$$
b(x)=-\frac12\Sigma\nabla V(x)+\gamma(x),\qquad \nabla\cdot(\gamma e^{-V})=0.
$$

其中 $`\gamma`$ 是相对于 $`\pi`$ 的 divergence-free current，它破坏 detailed balance，但不破坏 invariant measure。

这份讲义现在有两条主线。第 1-12 节处理“非对称噪声矩阵 $`A`$”这个容易误读的问题：常系数 $`A dB_t`$ 只通过 $`AA^\top`$ 影响 generator。第 13-24 节处理更核心的不可逆 Langevin：

$$
dX_t=-C\nabla V(X_t)\,dt+\sqrt{2D}\,dB_t,
$$

其中 $`C`$ 不一定对称。若目标仍是 $`e^{-V}`$，常矩阵的结构性条件是

$$
C=D+J,
\qquad D=D^\top\succeq0,
\qquad J=-J^\top.
$$

也就是说，对称部分 $`D`$ 负责 diffusion/dissipation，反对称部分 $`J`$ 负责 stationary rotation current。收敛则分三层：reversible 或对称耗散部分由 Poincare/log-Sobolev/convexity 控制；非可逆 current 可通过 hypocoercivity、谱比较或 Poisson 方程带来加速；若 drift 与 Gibbs 不匹配，则平衡态一般只能通过 stationary Fokker-Planck 或 Lyapunov 方程求出。

## 目录

<table_of_contents color="gray"/>

## 读者画像与预备知识

默认读者是 目标读者。需要熟悉多元微积分、线性代数、Itô diffusion 的 generator、Fokker-Planck 方程、Poincare/log-Sobolev 不等式的基本形式。第一遍不需要完整 Dirichlet form 理论，但需要接受“generator 的 adjoint 决定 density 演化”这个标准事实。

可跳过内容：如果只想纠正“非对称噪声矩阵是否导致不可逆”这个误解，读第 1 到第 5 节；如果关心一般 drift 的存在唯一性与收敛，读第 6 节；如果关心抽象 divergence-free drift 的不可逆加速，读第 7 节；如果想检查线性矩阵条件，读第 8 节；如果真正关心 $`-C\nabla V`$ 且 $`C`$ 不对称的不可逆 Langevin，直接读第 13 到第 20 节，再用第 22 节练习检查理解。
