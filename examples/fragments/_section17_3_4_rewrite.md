### 17.3 谱加速：Hwang-Hwang-Ma-Sheu 型结论

先定义这里说的“谱加速”是什么。设 $`\mathcal L`$ 在 $`L^2_0(\pi)=\{f:\pi f=0\}`$ 上生成 semigroup。若 spectrum 离 $`0`$ 有 gap，可以定义 convergence exponent

$$
\lambda(\mathcal L)
=-\sup\{\operatorname{Re}z:z\in\sigma(\mathcal L|_{L^2_0(\pi)})\}.
$$

越大的 $`\lambda(\mathcal L)`$ 代表 asymptotic spectral decay 越快。注意它不同于前面的能量证明 rate：能量证明给的是一定成立的 semigroup norm 上界；谱指数描述的是长时间最慢模态。

Hwang-Hwang-Ma-Sheu 的典型设定是

$$
dX_t=(-\nabla U(X_t)+C(X_t))dt+\sqrt2dW_t,
\qquad \nabla\cdot(Ce^{-U})=0.
$$

令

$$
\mathcal L_C=\mathcal L_0+C\cdot\nabla,
\qquad
\mathcal L_0=\Delta-\nabla U\cdot\nabla.
$$

由于 $`\nabla\cdot(Ce^{-U})=0`$，$`C\cdot\nabla`$ 在 $`L^2(\pi)`$ 中是反对称项。Hwang-Hwang-Ma-Sheu 证明，在合适的 compact-resolvent / discrete-spectrum / regularity 条件下，加入这样的 divergence-free drift 不会降低 convergence exponent，并且在慢特征空间被非可逆 transport 有效耦合时可以严格提升指数。

**一个本讲义够用的谱比较 lemma。** 令

$$
\mathcal L=\mathcal S+\mathcal A,
$$

其中 $`\mathcal S`$ 自伴、非正，$`\mathcal A`$ 反自伴。假设 $`\mathcal S`$ 在平均为零函数上有 spectral gap $`\lambda_0>0`$，即

$$
\langle f,\mathcal Sf\rangle_\pi
\le -\lambda_0\lVert f\rVert_{L^2(\pi)}^2,
\qquad \pi f=0.
$$

若 $`u`$ 是 $`\mathcal L`$ 的平均为零 eigenfunction，$`\mathcal Lu=zu`$，则

$$
\operatorname{Re}z\le -\lambda_0.
$$

**证明。** 对 eigenvalue equation 取内积：

$$
z\lVert u\rVert^2=\langle u,\mathcal Su\rangle+\langle u,\mathcal Au\rangle.
$$

第二项纯虚，因为 $`\mathcal A^*=-\mathcal A`$。所以

$$
\operatorname{Re}z\lVert u\rVert^2
=\langle u,\mathcal Su\rangle
\le -\lambda_0\lVert u\rVert^2.
$$

证毕。

这个 lemma 只说明“不会比 reversible 的 gap 更差”。真正的严格加速来自更细的结构：旧的慢 eigenfunction 若被 $`\mathcal A`$ 搬到其他方向，就不能继续作为慢模态存在。直观上，$`\mathcal A`$ 不耗散能量，但它把概率质量沿等高线搬运，让 $`\mathcal S`$ 更快看见原来难耗散的方向。

**在常矩阵模型中的翻译。** 对

$$
dX_t=-(D+J)\nabla V(X_t)dt+\sqrt{2D}dB_t,
$$

有

$$
\mathcal S f=-D\nabla V\cdot\nabla f+D:\nabla^2f,
\qquad
\mathcal A f=-J\nabla V\cdot\nabla f.
$$

如果 $`D`$ 对应的 reversible dynamics 已有 $`L^2(\pi)`$ gap，那么 $`J`$ 至少不破坏这个保底谱位置；是否严格加速，要看 $`-J\nabla V\cdot\nabla`$ 是否真正耦合了慢 eigenspace。Gaussian case 中这个问题可完全化成矩阵 $`(D+J)H`$ 的谱和 semigroup norm，见第 18 节。

**需要注意的技术条件。** 谱比较不是只靠形式计算。通常需要：

| 条件 | 为什么需要 |
|---|---|
| $`e^{-U}`$ 可积且过程 non-explosive | semigroup 和 invariant measure 真实存在 |
| $`C`$ smooth 且 $`\nabla\cdot(Ce^{-U})=0`$ | 保持 invariant measure 且给反自伴性 |
| reversible generator 有 spectral gap 或 compact resolvent | convergence exponent 可被谱描述 |
| domain 对 $`C\cdot\nabla`$ 稳定 | 防止反对称 perturbation 只是形式上的 |

### 17.4 Poisson 方程与 asymptotic variance

谱 gap 讨论的是分布收敛；采样里更常见的问题是时间平均的方差。令 $`f`$ 是平均为零 observable，考虑

$$
\frac1T\int_0^T f(X_t)dt.
$$

若 Poisson equation

$$
-\mathcal L\phi=f
$$

有足够好的解，则中心极限定理中的 asymptotic variance 通常写成

$$
\sigma^2_{\mathcal L}(f)
=2\langle \phi,f\rangle_\pi
=2\langle (-\mathcal L)^{-1}f,f\rangle_\pi.
$$

这给出不可逆加速的另一个精确含义：即使 $`L^2`$ 能量 rate 看不出变快，Poisson resolvent 也可能变小，从而长期平均方差降低。

**定理 5，反对称 perturbation 降低 asymptotic variance 的 Hilbert-space 模板。** 设

$$
\mathcal L=\mathcal S+\mathcal A,
$$

其中 $`\mathcal S`$ 自伴负定，$`\mathcal A`$ 反自伴。为了避免 domain 技术，先在有限维或 bounded perturbation 情形下理解。对平均为零的 $`f`$，若 resolvent 都存在，则

$$
\sigma^2_{\mathcal S+\mathcal A}(f)
\le \sigma^2_{\mathcal S}(f).
$$

**证明。** 令 $`G=(-\mathcal S)^{1/2}`$，并写

$$
B=G^{-1}\mathcal A G^{-1}.
$$

因为 $`\mathcal A`$ 反自伴，$`B`$ 也是反自伴。令 $`g=G^{-1}f`$。则

$$
-(\mathcal S+
\mathcal A)=G(I-B)G,
$$

所以

$$
\frac12\sigma^2_{\mathcal S+\mathcal A}(f)
=\langle (I-B)^{-1}g,g\rangle.
$$

取实部，并用 $`B^*=-B`$：

$$
\operatorname{Re}(I-B)^{-1}
=\frac12\left[(I-B)^{-1}+(I+B)^{-1}\right]
=(I-B^2)^{-1}.
$$

由于 $`-B^2\succeq0`$，有

$$
0\preceq (I-B^2)^{-1}\preceq I.
$$

因此

$$
\frac12\sigma^2_{\mathcal S+\mathcal A}(f)
\le \lVert g\rVert^2
=\frac12\sigma^2_{\mathcal S}(f).
$$

证毕。

**强不可逆极限。** 若考虑

$$
\mathcal L_\alpha=\mathcal S+\alpha\mathcal A,
$$

上面的证明把关键对象变成 $`(I-\alpha B)^{-1}`$。当 $`\alpha\to\infty`$ 时，实部只保留 $`\ker B`$ 上的投影。因此强不可逆扰动的极限方差由 $`\mathcal A`$ 的守恒方向控制：若 $`f`$ 的相关分量落在 $`\ker\mathcal A`$，再大的不可逆强度也不能消除那部分方差。

**本节带走什么。** Poisson 方程把“加速”变成 resolvent 变小的问题。反对称项通常降低 asymptotic variance，但降低多少取决于 observable 是否被不可逆 transport 真正混合；强扰动极限由 $`\ker\mathcal A`$ 决定。
