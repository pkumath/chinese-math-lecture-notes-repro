## 七、analytic core：resolvent convergence 如何恢复 semigroup convergence

上一节已经证明了 Markov 应用中最需要手算的部分。本节证明定理 A 的困难方向：为什么

$$
R_\lambda^{(n)}f\to R_\lambda f
$$

能推出

$$
P_t^{(n)}f\to P_tf
$$

在 $`t\in[0,T]`$ 上一致。证明的工具是 Yosida approximation。它把无界 generator $`L`$ 换成有界算子

$$
B_m=m^2R_m-mI=mLR_m,
$$

再用 $`e^{tB_m}`$ 逼近 $`P_t`$。

### 引理：Hille--Yosida / Trotter--Kato resolvent inversion

设 $`P_t^{(n)}`$ 和 $`P_t`$ 是 Banach space $`X`$ 上的 contraction $`C_0`$ semigroups，generators 为 $`L_n`$ 和 $`L`$。若对所有 $`\lambda>0`$ 与 $`f\in X`$，

$$
R_\lambda^{(n)}f\to R_\lambda f,
$$

则对所有 $`T<\infty`$ 与 $`f\in X`$，

$$
\sup_{0\le t\le T}\|P_t^{(n)}f-P_tf\|\to0.
$$

### 证明路线

证明分四步：

1. resolvent convergence 给出 bounded Yosida generators $`B_{n,m}=m^2R_m^{(n)}-mI`$ 的 strong convergence；
2. $`e^{tB_{n,m}}`$ 对 fixed $`m`$ 收敛到 $`e^{tB_m}`$；
3. $`e^{tB_m}`$ 用一个 Gamma/Poisson 时间平均逼近 $`P_t`$，且对 domain vectors 有显式误差；
4. 先在 $`\mathcal D(L)`$ 上证明 semigroup convergence，再用 density 和 contraction 延拓到全部 $`X`$。

### 第一步：Yosida generators 的 strong convergence

固定 $`m>0`$。定义

$$
B_{n,m}=m^2R_m^{(n)}-mI,
\qquad
B_m=m^2R_m-mI.
$$

由 resolvent convergence，

$$
B_{n,m}x\to B_mx
$$

for every $`x\in X`$。同时由 resolvent contraction bound，

$$
\|B_{n,m}\|
\le m^2\|R_m^{(n)}\|+m
\le 2m,
\qquad
\|B_m\|\le2m.
$$

因此 $`B_{n,m}`$ 是一列 uniformly bounded operators，并且 strong converge to $`B_m`$。

### 第二步：bounded exponentials 的 convergence

固定 $`m`$ 和 $`T`$。我们证明

$$
\sup_{0\le t\le T}\|e^{tB_{n,m}}x-e^{tB_m}x\|\to0
$$

for every $`x\in X`$。因为 $`B_{n,m}`$ 和 $`B_m`$ 都是 bounded operators，Duhamel formula 给

$$
 e^{tB_{n,m}}x-e^{tB_m}x
=\int_0^t e^{(t-s)B_{n,m}}(B_{n,m}-B_m)e^{sB_m}x\,ds.
$$

Yosida exponential 还是 contraction。原因是

$$
e^{tB_{n,m}}
=e^{-mt}\sum_{k=0}^\infty \frac{(mt)^k}{k!}(mR_m^{(n)})^k,
$$

而 $`\|mR_m^{(n)}\|\le1`$，所以 $`\|e^{tB_{n,m}}\|\le1`$。同理 $`\|e^{tB_m}\|\le1`$。

集合

$$
K_T=\{e^{sB_m}x:0\le s\le T\}
$$

是 compact 的，因为 $`s\mapsto e^{sB_m}x`$ 连续且 $`[0,T]`$ compact。Strong convergence $`B_{n,m}y\to B_my`$ 加上 uniform boundedness $`\sup_n\|B_{n,m}-B_m\|\le4m`$，在 compact set $`K_T`$ 上升级为 uniform convergence：

$$
\sup_{y\in K_T}\|(B_{n,m}-B_m)y\|\to0.
$$

于是

$$
\begin{aligned}
\sup_{0\le t\le T}\|e^{tB_{n,m}}x-e^{tB_m}x\|
&\le \int_0^T\sup_{y\in K_T}\|(B_{n,m}-B_m)y\|\,ds\\
&=T\sup_{y\in K_T}\|(B_{n,m}-B_m)y\|\to0.
\end{aligned}
$$

这证明了 fixed $`m`$ 的 bounded exponential convergence。

### 第三步：Yosida approximation 的概率表示和误差估计

现在证明 $`e^{tB_m}`$ 逼近 $`P_t`$。先对任意 contraction semigroup $`Q_t`$ 说明通用估计。令 generator 为 $`A`$，resolvent 为 $`S_m`$，Yosida generator 为

$$
C_m=m^2S_m-mI.
$$

由 resolvent 的 Laplace 表示，

$$
mS_mx=\int_0^\infty me^{-ms}Q_sx\,ds.
$$

若 $`E_1,E_2,\ldots`$ 是 rate $`m`$ 的 exponential random variables，则

$$
(mS_m)^kx=\mathbb E[Q_{E_1+\cdots+E_k}x].
$$

这是由 iterated integral 和 semigroup property $`Q_{s_1}\cdots Q_{s_k}=Q_{s_1+\cdots+s_k}`$ 得到的。又因为

$$
e^{tC_m}=e^{-mt}\sum_{k=0}^\infty\frac{(mt)^k}{k!}(mS_m)^k,
$$

若 $`N`$ 服从 Poisson distribution with mean $`mt`$，并令

$$
S_{m,t}=E_1+\cdots+E_N
$$

其中 $`N=0`$ 时 $`S_{m,t}=0`$，则

$$
e^{tC_m}x=\mathbb E[Q_{S_{m,t}}x].
$$

这个随机时间的均值和方差为

$$
\mathbb E S_{m,t}=t,
\qquad
\operatorname{Var}(S_{m,t})=\frac{2t}{m}.
$$

若 $`x\in\mathcal D(A)`$，则对任意 $`s,t\ge0`$，variation formula 给

$$
Q_sx-Q_tx=\int_t^s Q_rAx\,dr
$$

其中若 $`s<t`$，积分按负方向理解。因此

$$
\|Q_sx-Q_tx\|\le |s-t|\|Ax\|.
$$

于是对 $`0\le t\le T`$，

$$
\begin{aligned}
\|e^{tC_m}x-Q_tx\|
&\le \mathbb E\|Q_{S_{m,t}}x-Q_tx\|\\
&\le \mathbb E|S_{m,t}-t|\,\|Ax\|\\
&\le \sqrt{\operatorname{Var}(S_{m,t})}\,\|Ax\|\\
&\le \sqrt{\frac{2T}{m}}\|Ax\|.
\end{aligned}
$$

因此

$$
\sup_{0\le t\le T}\|e^{tC_m}x-Q_tx\|
\le
\sqrt{\frac{2T}{m}}\|Ax\|.
$$

这个 estimate 很重要：它不依赖 semigroup 的其他细节，只依赖 contraction 和 $`\|Ax\|`$。

### 第四步：在 domain 上证明 convergence

先取 $`x\in\mathcal D(L)`$。由 resolvent convergence，固定一个 $`\alpha>0`$，定义

$$
x_n=R_\alpha^{(n)}(\alpha-L)x.
$$

则

$$
x_n\to R_\alpha(\alpha-L)x=x.
$$

并且 $`x_n\in\mathcal D(L_n)`$，且

$$
L_nx_n=\alpha x_n-(\alpha-L)x\to Lx.
$$

于是 $`\sup_n\|L_nx_n\|<\infty`$ for all sufficiently large $`n`$。

对 $`0\le t\le T`$，写三角分解：

$$
\begin{aligned}
\|P_t^{(n)}x-P_tx\|
&\le \|P_t^{(n)}(x-x_n)\|\\
&\quad +\|P_t^{(n)}x_n-e^{tB_{n,m}}x_n\|\\
&\quad +\|e^{tB_{n,m}}x_n-e^{tB_m}x\|\\
&\quad +\|e^{tB_m}x-P_tx\|.
\end{aligned}
$$

第一项由 contraction 控制为 $`\|x-x_n\|`$。第二项对 semigroup $`P_t^{(n)}`$ 使用第三步的 estimate，得到

$$
\sup_{0\le t\le T}\|P_t^{(n)}x_n-e^{tB_{n,m}}x_n\|
\le
\sqrt{\frac{2T}{m}}\|L_nx_n\|.
$$

第四项对极限 semigroup 使用同一 estimate：

$$
\sup_{0\le t\le T}\|e^{tB_m}x-P_tx\|
\le
\sqrt{\frac{2T}{m}}\|Lx\|.
$$

第三项在 fixed $`m`$ 下由第二步得到

$$
\sup_{0\le t\le T}\|e^{tB_{n,m}}x_n-e^{tB_m}x\|\to0,
$$

因为 $`x_n\to x`$ 且 $`e^{tB_{n,m}}`$ 是 contractions。

现在给出 $`\varepsilon`$ argument。先选 $`m`$ 大，使

$$
\sqrt{\frac{2T}{m}}\left(\sup_{n\ge N_0}\|L_nx_n\|+\|Lx\|\right)<\frac\varepsilon3.
$$

再在这个 fixed $`m`$ 下取 $`n`$ 大，使 $`\|x-x_n\|<\varepsilon/3`$ 且 bounded exponential 中间项小于 $`\varepsilon/3`$。于是

$$
\sup_{0\le t\le T}\|P_t^{(n)}x-P_tx\|<\varepsilon.
$$

这证明了 convergence for all $`x\in\mathcal D(L)`$。

### 第五步：由 domain density 延拓到全部空间

Generator of a $`C_0`$ semigroup has dense domain，所以 $`\mathcal D(L)`$ dense in $`X`$。给定 $`f\in X`$ 和 $`\varepsilon>0`$，取 $`x\in\mathcal D(L)`$ 使

$$
\|f-x\|<\varepsilon.
$$

由 contraction，

$$
\begin{aligned}
\sup_{0\le t\le T}\|P_t^{(n)}f-P_tf\|
&\le \sup_t\|P_t^{(n)}(f-x)\|+\sup_t\|P_t^{(n)}x-P_tx\|+\sup_t\|P_t(x-f)\|\\
&\le 2\varepsilon+\sup_t\|P_t^{(n)}x-P_tx\|.
\end{aligned}
$$

对这个 $`x`$，上一段已经证明中间项趋于 $`0`$。先取 $`n`$ 大，再让 $`\varepsilon`$ 小，就得到

$$
\sup_{0\le t\le T}\|P_t^{(n)}f-P_tf\|\to0.
$$

引理证明完成。

### 为什么这个引理不是普通 Laplace transform 唯一性

单纯知道一列 bounded functions 的 Laplace transforms 收敛，不一定给出 uniform-in-time convergence。这里能推出结论，依赖的是额外 semigroup structure：

- $`P_{t+s}=P_tP_s`$ 给时间方向的刚性；
- contraction bound 给 Yosida approximation 的统一误差；
- strong continuity 让 generator domain dense；
- resolvent identity 保证不同 $`\lambda`$ 的 Laplace 信息来自同一个 generator。

这也是为什么 Trotter--Kato theorem 是 semigroup theorem，而不是普通 Laplace transform theorem。

**本节带走什么。**

- Resolvent-to-semigroup 可以用 Yosida approximation 证明，不只是抽象引用。
- 关键 estimate 是 $`\sup_{t\le T}\|e^{tC_m}x-Q_tx\|\le\sqrt{2T/m}\|Ax\|`$。
- Graph approximation 先给 domain vectors 上的 convergence，再由 contraction 和 density 延拓到全部测试函数。
