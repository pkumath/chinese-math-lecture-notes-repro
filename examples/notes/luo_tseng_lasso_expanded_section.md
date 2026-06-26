## Luo--Tseng 路线：把 LASSO 的算法收敛证明拆开
前面 LASSO rate 证明回答的是统计问题：经验 minimizer $`\widehat\beta`$ 离真参数 $`\beta^\star`$ 多近。本节回答另一个问题：给定同一个经验目标，proximal gradient 产生的算法点 $`\beta^k`$ 离经验解集 $`\widehat\Theta`$ 多近。

固定样本和设计矩阵，写
$$
F(\beta)=f(\beta)+g(\beta),
\qquad
f(\beta)=\frac{1}{2n}\|X\beta-y\|_2^2,
\qquad
g(\beta)=\lambda\|\beta\|_1.
$$
令
$$
A=\frac{1}{n}X^\top X,
\qquad
b=\frac{1}{n}X^\top y,
\qquad
\nabla f(\beta)=A\beta-b.
$$
LASSO 的 proximal-gradient map 是
$$
T_\eta(\beta)
=
\operatorname{prox}_{\eta\lambda\|\cdot\|_1}\{\beta-\eta(A\beta-b)\}
=S_{\eta\lambda}\{\beta-\eta(A\beta-b)\},
$$
其中 $`S_\tau`$ 是 coordinate-wise soft-thresholding：
$$
S_\tau(u)_j=
\begin{cases}
 u_j-\tau, & u_j>\tau,\\
 0, & |u_j|\le \tau,\\
 u_j+\tau, & u_j<-\tau.
\end{cases}
$$
定义 step 和 residual：
$$
d_\eta(\beta)=T_\eta(\beta)-\beta,
\qquad
r_\eta(\beta)=\frac{\beta-T_\eta(\beta)}{\eta}=-\frac{d_\eta(\beta)}{\eta}.
$$
Luo--Tseng proof 的中心不是 cone condition，而是下面这条链：
$$
\text{soft-threshold residual small}
\Longrightarrow
\text{distance to KKT solution set small}
\Longrightarrow
\text{cost-to-go controlled by step size}
\Longrightarrow
\text{linear convergence}.
$$

### 第零步：soft-threshold fixed point 就是 LASSO KKT
经验解集记作
$$
\widehat\Theta=\arg\min_\beta F(\beta).
$$
LASSO 的 KKT 条件是
$$
0\in A\beta-b+\lambda\partial\|\beta\|_1.
$$
逐坐标写就是
$$
\begin{cases}
(A\beta-b)_j+\lambda=0, & \beta_j>0,\\
(A\beta-b)_j-\lambda=0, & \beta_j<0,\\
|(A\beta-b)_j|\le \lambda, & \beta_j=0.
\end{cases}
$$
现在证明 $`\beta=T_\eta(\beta)`$ 等价于 KKT。设
$$
u=\beta-\eta(A\beta-b).
$$
若 $`\beta=T_\eta(\beta)`$，逐坐标看：

- 若 $`\beta_j>0`$，soft-thresholding 必须处在正分支，所以 $`\beta_j=\nu_j-\eta\lambda`$。代入 $`\nu_j=\beta_j-\eta(A\beta-b)_j`$，得 $`(A\beta-b)_j+\lambda=0`$。
- 若 $`\beta_j<0`$，soft-thresholding 必须处在负分支，所以 $`\beta_j=\nu_j+\eta\lambda`$，得 $`(A\beta-b)_j-\lambda=0`$。
- 若 $`\beta_j=0`$，soft-thresholding 处在中间分支，所以 $`|\nu_j|\le\eta\lambda`$，即 $`|(A\beta-b)_j|\le\lambda`$。

反过来，如果 KKT 成立，三种坐标情况代回 soft-thresholding 公式，会得到 $`T_\eta(\beta)_j=\beta_j`$。因此
$$
\operatorname{Fix}(T_\eta)=\widehat\Theta.
$$
这一步很重要：proximal residual 不是任意 stopping criterion，它的零点正好是 LASSO 解集。

**本小节带走什么。**

- LASSO 的 non-smooth KKT 可以完全由 soft-thresholding 三分支表示。
- $`r_\eta(\beta)=0`$ 等价于 $`\beta`$ 是经验 LASSO minimizer。
- Luo--Tseng error bound 要做的事，是把 “$`r_\eta`$ 很小”升级成“离 $`\widehat\Theta`$ 很近”。

### 定理：LASSO 的 Luo--Tseng error bound
取 $`0<\eta<1/L`$，其中 $`L=\|A\|_{\operatorname{op}}`$ 是 $`\nabla f`$ 的 Lipschitz 常数。固定初始点 $`\beta^0`$，考虑 level set
$$
\mathcal L_0=\{\beta:F(\beta)\le F(\beta^0)\}.
$$
因为 $`\lambda>0`$，$`F`$ coercive，所以 $`\mathcal L_0`$ 是 compact。则存在一个依赖于 $`X,y,\lambda,\eta,\beta^0`$ 的常数 $`C_{\rm EB}`$，使得对所有 $`\beta\in\mathcal L_0`$，
$$
\operatorname{dist}(\beta,\widehat\Theta)
\le
C_{\rm EB}\|r_\eta(\beta)\|_2
=
\frac{C_{\rm EB}}{\eta}\|\beta-T_\eta(\beta)\|_2.
$$
这就是 LASSO 版本的 Luo--Tseng error bound：step length 或 proximal residual 控制到解集的距离。

### 证明第一步：把 soft-thresholding 分成有限多个 polyhedral 区域
对每个坐标，soft-thresholding 有三种分支。令
$$
u(\beta)=\beta-\eta(A\beta-b).
$$
给定一个三分支模式 $`\sigma\in\{+,0,-\}^p`$，定义区域
$$
P_\sigma=\{\beta:
\nu_j(\beta)\ge \eta\lambda\ \text{if }\sigma_j=+,
\ -\eta\lambda\le \nu_j(\beta)\le\eta\lambda\ \text{if }\sigma_j=0,
\ \nu_j(\beta)\le -\eta\lambda\ \text{if }\sigma_j=-
\}.
$$
每个 $`P_\sigma`$ 都由线性不等式定义，所以是 polyhedron。这样的区域只有 $`3^p`$ 个。虽然数量很大，但证明只需要“有限多个”。

在固定区域 $`P_\sigma`$ 内，$`T_\eta`$ 是 affine map，残差 $`r_\eta`$ 也是 affine map。逐坐标地说：
$$
r_\eta(\beta)_j=
\begin{cases}
(A\beta-b)_j+\lambda, & \sigma_j=+,\\
\beta_j/\eta, & \sigma_j=0,\\
(A\beta-b)_j-\lambda, & \sigma_j=-.
\end{cases}
$$
这个公式值得停一下看。正分支和负分支测的是 KKT stationarity violation；中间分支测的是坐标本身离零有多远。也就是说 residual 同时看 stationarity 和 active-set consistency。

### 证明第二步：在一个非空 fixed-face 上用 Hoffman bound
先调用一个标准引理。

**Hoffman bound。** 若一个 polyhedral set
$$
Q=\{x:Bx\le c,\ Dx=e\}
$$
非空，则存在常数 $`H_Q<\infty`$，使得所有 $`x`$ 都满足
$$
\operatorname{dist}(x,Q)
\le
H_Q\left(\|(Bx-c)_+\|_2+\|Dx-e\|_2\right).
$$
这个引理的作用是：对线性等式和线性不等式系统，只要 violations 小，到可行集的距离就小。

现在固定一个模式 $`\sigma`$。令
$$
Q_\sigma=\{\beta\in P_\sigma:r_\eta(\beta)=0\}.
$$
由于 $`P_\sigma`$ 是 polyhedron，且 $`r_\eta`$ 在 $`P_\sigma`$ 上是 affine，$`Q_\sigma`$ 也是 polyhedron。若 $`Q_\sigma`$ 非空，则对任意 $`\beta\in P_\sigma`$，区域不等式已经满足，唯一剩下的 violation 是 $`r_\eta(\beta)`$。Hoffman bound 给
$$
\operatorname{dist}(\beta,Q_\sigma)
\le H_\sigma\|r_\eta(\beta)\|_2.
$$
又因为 $`r_\eta=0`$ 等价于 KKT，所以
$$
Q_\sigma\subseteq \widehat\Theta.
$$
因此
$$
\operatorname{dist}(\beta,\widehat\Theta)
\le
\operatorname{dist}(\beta,Q_\sigma)
\le
H_\sigma\|r_\eta(\beta)\|_2.
$$
这就是 error bound 在一个 active face 上的证明。

### 证明第三步：处理没有 fixed point 的区域
如果某个 $`Q_\sigma`$ 是空的，不能直接用上一段。可是这种区域在 compact level set 上也不会坏。

考虑 $`\mathcal L_0\cap P_\sigma`$。这是 compact set。若 $`Q_\sigma=\varnothing`$，则在这个 compact set 上不可能有 $`r_\eta(\beta)=0`$，否则就得到一个 fixed point。于是连续函数 $`\|r_\eta(\beta)\|_2`$ 有正下界：
$$
\delta_\sigma
=
\min_{\beta\in\mathcal L_0\cap P_\sigma}\|r_\eta(\beta)\|_2
>0.
$$
另一方面，$`\mathcal L_0`$ compact，所以到解集的距离有有限上界
$$
D_0=\sup_{\beta\in\mathcal L_0}\operatorname{dist}(\beta,\widehat\Theta)<\infty.
$$
因此对 $`\beta\in\mathcal L_0\cap P_\sigma`$，
$$
\operatorname{dist}(\beta,\widehat\Theta)
\le D_0
\le \frac{D_0}{\delta_\sigma}\|r_\eta(\beta)\|_2.
$$
所以空 fixed-face 也有 error bound，只是常数来自 compactness，而不是 Hoffman。

### 证明第四步：有限覆盖取最大常数
一共有有限多个 $`P_\sigma`$。对有 fixed point 的区域取 Hoffman 常数 $`H_\sigma`$；对没有 fixed point 的区域取 $`D_0/\delta_\sigma`$。令 $`C_{\rm EB}`$ 是这些常数的最大值，就得到对整个 level set 的统一 bound：
$$
\operatorname{dist}(\beta,\widehat\Theta)
\le C_{\rm EB}\|r_\eta(\beta)\|_2.
$$
证明完成。

**这段证明为什么是 Luo--Tseng 味道？** 因为它没有要求 $`A=X^\top X/n`$ 在全空间正定。高维时 $`p>n`$，$`A`$ 必然 rank deficient，全空间 strong convexity 不可能。证明依靠的是两件事：soft-threshold map 的 polyhedral 分支结构，以及 residual 到 fixed point set 的 Hoffman 型距离估计。这正是 Luo--Tseng error-bound route 的精神。

**本小节带走什么。**

- LASSO 的 proximal residual 在每个 threshold pattern 上是 affine。
- $`\ell_1`$ 的 polyhedral geometry 让 Hoffman bound 可用。
- error bound 是 residual-to-solution-distance，不是 statistical parameter rate。

### 从 error bound 到 proximal-gradient linear convergence
现在把 error bound 接到算法收敛。令
$$
\beta^+=T_\eta(\beta),
\qquad
d=\beta^+-\beta.
$$
proximal step 的定义等价于
$$
\beta^+
=
\arg\min_z\left\{
\langle \nabla f(\beta),z-\beta\rangle+rac{1}{2\eta}\|z-\beta\|_2^2+g(z)
\right\}.
$$
把 $`z=\beta`$ 作为竞争者，得到
$$
\langle \nabla f(\beta),d\rangle+rac{1}{2\eta}\|d\|_2^2+g(\beta^+)
\le g(\beta).
$$
即
$$
\langle \nabla f(\beta),d\rangle+g(\beta^+)-g(\beta)
\le
-\frac{1}{2\eta}\|d\|_2^2.
$$
由 $`L`$-smoothness，
$$
f(\beta^+)
\le
f(\beta)+\langle \nabla f(\beta),d\rangle+rac{L}{2}\|d\|_2^2.
$$
两式相加：
$$
F(\beta^+)
\le
F(\beta)-\left(\frac{1}{2\eta}-\frac{L}{2}\right)\|d\|_2^2.
$$
记
$$
c_{\rm dec}=\frac{1}{2\eta}-\frac{L}{2}>0.
$$
于是
$$
F(\beta)-F(\beta^+)
\ge c_{\rm dec}\|d\|_2^2.
$$
这就是 sufficient decrease。

接着证明 cost-to-go。取 $`\beta^\star_\eta`$ 为 $`\beta`$ 到 $`\widehat\Theta`$ 的一个最近点。proximal optimality 给存在 $`s^+\in\partial g(\beta^+)`$，使得
$$
s^+=-\nabla f(\beta)-\frac{1}{\eta}d.
$$
由 convexity，
$$
g(\beta^+)-g(\beta^\star_\eta)
\le
\langle s^+,\beta^+-\beta^\star_\eta\rangle,
$$
并且
$$
f(\beta^+)-f(\beta^\star_\eta)
\le
\langle \nabla f(\beta^+),\beta^+-\beta^\star_\eta\rangle.
$$
相加得
$$
F(\beta^+)-F^\star
\le
\left\langle
\nabla f(\beta^+)-\nabla f(\beta)-\frac{1}{\eta}d,
\beta^+-\beta^\star_\eta
\right\rangle.
$$
用 Cauchy--Schwarz 和 Lipschitz gradient，
$$
F(\beta^+)-F^\star
\le
\left(L+\frac{1}{\eta}\right)\|d\|_2\,\|\beta^+-\beta^\star_\eta\|_2.
$$
而
$$
\|\beta^+-\beta^\star_\eta\|_2
\le
\|\beta-\beta^\star_\eta\|_2+\|d\|_2
=
\operatorname{dist}(\beta,\widehat\Theta)+\|d\|_2.
$$
由 error bound 和 $`\|r_\eta(\beta)\|_2=\|d\|_2/\eta`$，
$$
\operatorname{dist}(\beta,\widehat\Theta)
\le
\frac{C_{\rm EB}}{\eta}\|d\|_2.
$$
于是
$$
F(\beta^+)-F^\star
\le
\left(L+\frac{1}{\eta}\right)
\left(1+\frac{C_{\rm EB}}{\eta}\right)
\|d\|_2^2.
$$
记右侧常数为 $`C_{\rm cg}\|d\|_2^2`$，即
$$
F(\beta^+)-F^\star
\le C_{\rm cg}\|d\|_2^2.
$$
把 sufficient decrease 代入，
$$
F(\beta^+)-F^\star
\le
\frac{C_{\rm cg}}{c_{\rm dec}}
\{F(\beta)-F(\beta^+)\}.
$$
令
$$
a=F(\beta)-F^\star,
\qquad
a^+=F(\beta^+)-F^\star,
\qquad
\gamma=\frac{C_{\rm cg}}{c_{\rm dec}}.
$$
上式是
$$
a^+\le \gamma(a-a^+).
$$
移项得到
$$
(1+\gamma)a^+\le \gamma a,
$$
所以
$$
a^+\le q a,
\qquad
q=\frac{\gamma}{1+\gamma}<1.
$$
这就证明了 objective gap 的 Q-linear convergence：
$$
F(\beta^{k})-F^\star
\le
q^k\{F(\beta^0)-F^\star\}.
$$
再由 error bound 和 sufficient decrease，
$$
\operatorname{dist}(\beta^k,\widehat\Theta)
\le
\frac{C_{\rm EB}}{\eta}\|\beta^{k+1}-\beta^k\|_2
\le
\frac{C_{\rm EB}}{\eta\sqrt{c_{\rm dec}}}
\sqrt{F(\beta^k)-F(\beta^{k+1})},
$$
因此 distance to solution set 也以几何速度下降，通常写成 R-linear distance convergence。

### 一个二维例子：为什么 residual 比 objective gap 更像“到解集的距离”
取
$$
F(\beta_1,\beta_2)=\frac{1}{2}(\beta_1-c)^2+\lambda(|\beta_1|+|\beta_2|),
\qquad c>\lambda>0.
$$
这里 $`X`$ 只看第一坐标，第二坐标完全不进入 loss。解是
$$
\widehat\beta_1=c-\\lambda,
\qquad
\widehat\beta_2=0.
$$
虽然 smooth loss 对 $`\beta_2`$ 没有任何曲率，但 L1 的 soft-thresholding 中间分支直接给
$$
r_\eta(\beta)_2=\beta_2/\eta
\quad\text{when }|\beta_2|\le\eta\lambda.
$$
也就是说，靠近零 active face 时，residual 直接测量第二坐标离 active face $`\beta_2=0`$ 多远。这就是 L1 polyhedral geometry 补上 rank deficiency 的最小模型。它不是 strong convexity；它是 kink 加上 Hoffman error bound。

### 和统计 RSC 证明如何合并
若你真正关心算法输出 $`\beta^k`$ 到真参数 $`\beta^\star`$ 的距离，应当分两项：
$$
\|\beta^k-\beta^\star\|_2
\le
\operatorname{dist}(\beta^k,\widehat\Theta)
+
\sup_{\widehat\beta\in\widehat\Theta}\|\widehat\beta-\beta^\star\|_2.
$$
第一项由本节 Luo--Tseng EB + PGM convergence 控制；第二项由前面的 basic inequality + cone + RE/RSC 控制。因此算法误差和统计误差的组合形式是
$$
\|\beta^k-\beta^\star\|_2
\lesssim
\rho^k\operatorname{dist}(\beta^0,\widehat\Theta)
+
\frac{\lambda\sqrt{s}}{\kappa}.
$$
更精确地说，第一项的指数率常数来自 optimization geometry 和 step size；第二项的统计率来自 score event 和 restricted curvature。两者不是同一个 theorem，但可以叠加成算法输出的总误差。

### 假设在哪里用，弱化会坏在哪里
<table header-row="true">
<tr><td>假设/工具</td><td>用在哪里</td><td>弱化后的风险</td></tr>
<tr><td>$`\lambda>0`$ 与 level set compact</td><td>空 fixed-face 的 residual 正下界、统一常数</td><td>常数可能不能在整条迭代路径上统一</td></tr>
<tr><td>$`\ell_1`$ polyhedral</td><td>soft-threshold 分成有限个 affine 区域</td><td>非 polyhedral penalty 不能直接套 Hoffman 分区证明</td></tr>
<tr><td>Hoffman bound</td><td>把 affine KKT violation 转成到 fixed-face 的距离</td><td>只有 residual 小，但没有距离估计</td></tr>
<tr><td>$`0<\eta<1/L`$</td><td>sufficient decrease</td><td>step 太大时 objective 不一定下降，线性收敛拼不起来</td></tr>
<tr><td>convexity 与 $`L`$-smoothness</td><td>cost-to-go proof</td><td>非凸时需要 stationarity/KL/subregularity 等额外条件</td></tr>
</table>

### 局部 active-set 直觉，但不要把它当成完整证明
很多 LASSO 算法看起来像“先识别 support，再在线性子空间上线性收敛”。这是一种有用直觉：一旦 threshold pattern 稳定，$`T_\eta`$ 就是一个 affine map，active coordinates 上的行为由 restricted Hessian 控制，inactive coordinates 由 soft-thresholding 压回零。

但 Luo--Tseng proof 更强一点：它不要求你先证明 support 已经正确识别，也不要求解唯一。它直接在所有可能的 threshold faces 上用有限分区和 error bound 统一控制到解集的距离。active-set identification 是这个几何的后续现象，不是 error bound 本身的前提。

**本节带走什么。**

- Luo--Tseng 线证明的是 $`\operatorname{dist}(\beta^k,\widehat\Theta)`$，不是 $`\|\widehat\beta-\beta^\star\|_2`$。
- 对 LASSO，关键是 soft-threshold map 是 piecewise affine，fixed point set 等于 KKT solution set。
- Hoffman bound 把每个 active face 上的 KKT violation 转成距离；有限 face 和 compact level set 给统一常数。
- PGM linear convergence 由三块拼出：sufficient decrease、error bound、cost-to-go。

### 本节练习
Level 0：逐坐标验证 $`\beta=T_\eta(\beta)`$ 与 LASSO KKT 三种情况等价。

Level 1：在一个固定 threshold pattern $`\sigma`$ 上，手算 $`r_\eta(\beta)_j`$ 的三分支 affine 公式。

Level 2：把 $`p=2`$ 且 $`A=\operatorname{diag}(1,0)`$ 的例子完整分区，画出 $`\beta_2`$ 如何被 soft-threshold residual 控制。

Level 3：用本节 cost-to-go 推导检查常数：证明 $`a^+\le\gamma(a-a^+)`$ 确实推出 $`a^+\le\gamma(1+\gamma)^{-1}a`$。

Level 4：比较本节的 error bound 和前一节统计 RE：找一个 $`X`$，使 $`A`$ 不全空间正定，但 LASSO PGM 仍可有 Luo--Tseng EB；再解释为什么这不自动给 support recovery。
