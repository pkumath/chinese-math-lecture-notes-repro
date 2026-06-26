### 17.5 Harris / Lyapunov 条件：非凸和非紧空间的实用收敛

前面 Poincare 和 log-Sobolev 的优点是证明短、rate 清楚；缺点是它们把难点转移到“证明目标分布满足函数不等式”。在非凸、多井、非紧空间或 heavy-tail 情形，研究里更常用的兜底路线是 Harris theorem。它回答的问题不是“Dirichlet form 有没有 spectral gap”，而是：过程会不会反复回到一个局部可混合区域，并且从无穷远回来的时间有没有指数尾。

**先把三个对象说清楚。**

| 名称 | 数学形式 | 直觉 |
|---|---|---|
| Lyapunov function | $`W:E\to[1,\infty)`$ | 测量“离无穷远有多远”的函数 |
| drift condition | $`\mathcal LW\le -aW+b\mathbf 1_K`$ | 在 compact set $`K`$ 外，过程平均往回走 |
| small set / minorization | $`P_T(x,\cdot)\ge \varepsilon\nu(\cdot)`$ for $`x\in K`$ | 只要进入 $`K`$，不同初值有统一概率被“刷新”到同一分布 |

这里 $`P_T`$ 是时间 $`T`$ 的 Markov kernel。连续时间扩散用 Harris theorem 时，通常先固定一个 $`T>0`$，对 skeleton chain $`X_0,X_T,X_{2T},\ldots`$ 应用离散时间 Harris theorem，再把结论扩展回所有 $`t\ge0`$。

**定理 4，Harris theorem 的一个够用版本。** 设 $`P`$ 是 Polish space $`E`$ 上的 Markov kernel。假设存在 $`W\ge1`$、$`0<\lambda<1`$、$`B<\infty`$，使得

$$
PW(x)\le \lambda W(x)+B.
$$

再假设某个 sublevel set

$$
C_R=\{x:W(x)\le R\}
$$

是 small set，即存在概率测度 $`\nu`$ 和 $`\varepsilon>0`$，使得

$$
P(x,A)\ge \varepsilon \nu(A),
\qquad x\in C_R,
$$

对所有 measurable set $`A`$ 成立。若 $`R`$ 取得足够大，则 $`P`$ 至多有一个 invariant probability measure $`\pi`$，且若 invariant measure 存在，则存在常数 $`M<\infty`$ 和 $`0<r<1`$，使得

$$
\lVert P^n(x,\cdot)-\pi\rVert_W
\le M W(x) r^n.
$$

这里 weighted total variation norm 定义为

$$
\lVert \mu\rVert_W
=\sup_{|f|\le W}\left|\int f\,d\mu\right|.
$$

对连续时间 semigroup $`P_t`$，若 generator 满足

$$
\mathcal LW\le -aW+b
$$

且某个 $`P_T`$ 的 sublevel set small，则由 Dynkin 公式得到

$$
P_TW(x)\le e^{-aT}W(x)+\frac{b}{a}(1-e^{-aT}),
$$

于是上面的离散时间定理给

$$
\lVert P_t(x,\cdot)-\pi\rVert_W
\le C W(x)e^{-\kappa t}.
$$

**证明脊柱。** Harris theorem 的完整证明通常用 Nummelin splitting 或 Hairer-Mattingly 的 weighted norm argument。讲义里需要记住四步。

1. Lyapunov drift 给回归：$`PW\le \lambda W+B`$ 意味着 $`W`$ 很大时下一步的平均 $`W`$ 会缩小，所以过程不会长期留在无穷远。
2. 选 $`R`$ 足够大，使 $`C_R`$ 成为“再生区域”：每次进入 $`C_R`$，minorization 给出至少 $`\varepsilon`$ 的概率从同一个 $`\nu`$ 重新开始。
3. 两个从不同初值出发的过程，只要都回到 $`C_R`$，就有正概率在下一步耦合；Lyapunov drift 控制等待回归的尾部。
4. 回归的指数尾加上局部统一耦合概率，推出全局指数收敛。权重 $`W(x)`$ 只是在记录：从很远的初值出发，前面需要更久才能回到可混合区域。

所以 Harris 不是一句“有 Lyapunov 就收敛”。它必须同时有：远处回拉、局部混合、不可爆炸、以及 invariant measure 的存在或 tightness。

**怎么用于不可逆矩阵 Langevin。** 考虑

$$
dX_t=-(D+J)\nabla V(X_t)dt+\sqrt{2D}\,dB_t,
\qquad D\succ0,
\qquad J=-J^\top.
$$

假设 $`V\in C^2`$、$`\nabla V`$ 局部 Lipschitz、$`V(x)\to\infty`$，并且已经由第 15 节知道

$$
\pi(dx)=Z^{-1}e^{-V(x)}dx
$$

是不变分布。为了用 Harris theorem，我们还需要验证两个东西。

**第一步，构造 Lyapunov function。** 最自然的选择不是 $`|x|^2`$，而是

$$
W(x)=e^{\eta V(x)},
\qquad 0<\eta<1.
$$

原因是对 $`W=\phi(V)`$，反对称 drift 在 $`\mathcal LW`$ 中自动消失。直接计算：

$$
\nabla W=\eta W\nabla V,
\qquad
\nabla^2W=\eta W\nabla^2V+
\eta^2W\nabla V\nabla V^\top.
$$

生成元

$$
\mathcal L f=-(D+J)\nabla V\cdot\nabla f+D:\nabla^2f
$$

作用到 $`W`$ 上，得到

$$
\mathcal LW
=\eta W\left[D:\nabla^2V-(1-\eta)\nabla V^\top D\nabla V\right].
$$

这里没有 $`J`$，因为

$$
(J\nabla V)\cdot\nabla V=0.
$$

因此如果存在 $`c>0`$ 和 compact set $`K`$，使得在 $`K^c`$ 上

$$
(1-\eta)\nabla V^\top D\nabla V-D:\nabla^2V\ge c,
$$

那么

$$
\mathcal LW\le -\eta c W+b\mathbf 1_K
$$

对某个 $`b<\infty`$ 成立。这就是 Harris 所需的 Lyapunov drift。这个条件的含义很直观：远处梯度回拉 $`\nabla V^\top D\nabla V`$ 必须压过 Hessian correction $`D:\nabla^2V`$。

**第二步，验证 small set。** 因为 $`D\succ0`$，扩散是 uniformly elliptic。若系数光滑且过程非爆炸，则 $`P_T(x,dy)`$ 有正的、连续的 transition density。于是对任意 compact set $`K`$，可以找到 $`\varepsilon>0`$ 和一个局部概率测度 $`\nu`$，使得

$$
P_T(x,\cdot)\ge \varepsilon\nu(\cdot),
\qquad x\in K.
$$

这就是 minorization。技术上可由 Aronson 型 heat-kernel lower bound、support theorem，或扩散的强 Feller + irreducibility 推出。若 $`D`$ 只是半正定，这一步不再自动成立；通常需要 Hörmander bracket condition 或控制可达性假设。

**结论。** 在上述 Lyapunov 条件、uniform ellipticity、小集条件和非爆炸条件下，Harris theorem 给出唯一遍历并且

$$
\lVert P_t(x,\cdot)-\pi\rVert_W
\le C W(x)e^{-\kappa t}.
$$

这是一种 weighted total variation 收敛。它和 Poincare 的 $`L^2(\pi)`$ 收敛、LSI 的 entropy 收敛不是同一个 norm；它更适合从点初值 $`X_0=x`$ 出发、非紧状态空间上的全局遍历性证明。

**Subgeometric 版本。** 如果远处回拉较弱，只能证明

$$
\mathcal LW\le -\phi(W)+b\mathbf 1_K,
$$

其中 $`\phi`$ 是递增但次线性的函数，例如 $`\phi(u)=cu^\alpha`$、$`0<\alpha<1`$，则通常得到 subgeometric convergence，而不是指数收敛。Douc-Fort-Guillin 的框架就是把这种 drift inequality 转换成显式 subgeometric rate。

**这节最容易错的地方。**

| 错误说法 | 为什么错 | 正确说法 |
|---|---|---|
| “有 Lyapunov function 就 Harris 收敛” | 少了 small set / minorization | Lyapunov 控制远处回归，minorization 控制局部混合 |
| “uniform elliptic 就够了” | 只给局部混合，不保证从无穷远回来 | 还需要 Lyapunov drift 或 tightness |
| “不可逆项 $`J`$ 会破坏 Lyapunov drift” | 对 $`W=\phi(V)`$，$`J\nabla V\cdot\nabla V=0`$ | $`J`$ 通常不改变这种能量型回拉验证 |
| “Harris rate 就是 spectral gap” | norm 不同，常数也不同 | Harris 给 weighted total variation，Poincare 给 $`L^2(\pi)`$ |

**Reference 定位。** Harris theorem 的现代清晰证明可看 Hairer-Mattingly；general state space Markov chain 的系统理论见 Meyn-Tweedie；SDE 中用 Lyapunov + minorization 证明几何遍历性的典型入口是 Mattingly-Stuart-Higham；subgeometric drift 条件见 Douc-Fort-Guillin。

**本节带走什么。** Harris/Lyapunov 是“远处回拉 + 局部混合 = 全局遍历”的工具。对不可逆 Langevin，选 $`W=e^{\eta V}`$ 时 skew drift 不进入 Lyapunov 计算；真正要检查的是对称耗散 $`D`$ 是否足够 confining，以及扩散是否能在 compact set 上产生 minorization。
