
# 比特币：一个点对点的电子现金系统

Satoshi Nakamoto

satoshin@gmx.com

https://bitcoin.org

**Abstract.**

**摘要：**

A purely peer-to-peer version of electronic cash would allow online
payments to be sent directly from one party to another without going through a
financial institution.

一个完全的点对点的现金版本，可以让在线支付从一方直接发送给另外一方，而不通过金融机构。

Digital signatures provide part of the solution, but the main
benefits are lost if a trusted third party is still required to prevent double-spending.

数字签名提供了部分解决方案，但是如果仍然需要一个第三方去防止双花，主要的优点仍然缺失。

We propose a solution to the double-spending problem using a peer-to-peer network.

我们提出一个用点对点的网络解决双花问题的方案。

The network timestamps transactions by hashing them into an ongoing chain of
hash-based proof-of-work, forming a record that cannot be changed without redoing
the proof-of-work. 

网络通过将交易哈希进基于哈希的工作量证明的持续增长的链上，给交易打上时间戳，形成一个不重做工作证明就不能修改的记录。

The longest chain not only serves as proof of the sequence of
events witnessed, but proof that it came from the largest pool of CPU power. 

最长的链不仅可以作为事件见证序列证明，也是它来自CPU算力最大池的证明。

As long as a majority of CPU power is controlled by nodes that are not cooperating to attack the network, they'll generate the longest chain and outpace attackers.

只要大部分CPU算力不是由链和攻击网络的节点控制，它们将会生成最长链，并超过攻击者的速度。

The network itself requires minimal structure. 

网络本身需要最极简的架构。

Messages are broadcast on a best effort basis, and nodes can leave and rejoin the network at will, accepting the longest proof-of-work chain as proof of what happened while they were gone.

消息将被尽力广播，节点可以随时离开和重新加入网络，接受最长的工作量证明链作为它们离开时，发生事件的证明。

## 1.Introduction

## 1.介绍

Commerce on the Internet has come to rely almost exclusively on financial institutions serving as
trusted third parties to process electronic payments. 

互联网上的贸易几乎是完全依赖金融机构作为可信赖的第三方去处理电子支付。

While the system works well enough for most transactions, it still suffers from the inherent weaknesses of the trust based model.

这个系统对大部分交易都运行的足够好，但是仍然要忍受它固有的基于信任的模型的缺点。

Completely non-reversible transactions are not really possible, since financial institutions cannot
avoid mediating disputes. 

完全不可撤销的交易真的不可能，因为金融机构不能避免仲裁纠纷。

The cost of mediation increases transaction costs, limiting the minimum practical transaction size and cutting off the possibility for small casual transactions, and there is a broader cost in the loss of ability to make non-reversible payments for nonreversible services. 

仲裁成本增加了交易成本，限制了最小实际交易额，切断了小额临时交易的可能性，失去做不可撤销支付的能力使得对对非可撤销服务需要更大的成本。

With the possibility of reversal, the need for trust spreads.

由于有撤销的可能性，对信任的需求更广泛。

Merchants must be wary of their customers, hassling them for more information than they would otherwise need.

商人必须提防他们的客户，麻烦它们要比他们原本需要的更多的信息。

A certain percentage of fraud is accepted as unavoidable.

一定比例的欺诈被认为是不可避免的。

These costs and payment uncertainties can be avoided in person by using physical currency, but no mechanism exists to make payments over a communications channel without a trusted party

这些成本和支付的不确定性可以通过当面使用实物货币而避免，但是不存在通过不需要可信任的第三方的通信通道去支付的机制。

What is needed is an electronic payment system based on cryptographic proof instead of trust,
allowing any two willing parties to transact directly with each other without the need for a trusted third party. 

所需要的是基于加密证明而不是信任的电子支付系统，允许两个意愿双方不需要一个可信任第三方而相互直接交易。

Transactions that are computationally impractical to reverse would protect sellers from fraud, and routine escrow mechanisms could easily be implemented to protect buyers.

在计算上不能撤销的交易将保护卖方不被欺骗，常规的暂由第三方保管的机制很容易被实现去保护买方。

In this paper, we propose a solution to the double-spending problem using a peer-to-peer distributed timestamp server to generate computational proof of the chronological order of transactions.

在这篇论文里，我们提出一个用点对点的分布式时间戳服务器去生成交易的先后顺序的计算证明的方式作为双花问题的解决方案。

The system is secure as long as honest nodes collectively control more CPU power than any
cooperating group of attacker nodes.

只要诚实的节点共同控制的CPU算力多于合作的攻击者节点群，系统就是安全的。

## 2. Transactions

## 2.交易

We define an electronic coin as a chain of digital signatures. 

我们定义一个电子货币作为数字签名的链。

Each owner transfers the coin to the next by digitally signing a hash of the previous transaction and the public key of the next owner and adding these to the end of the coin. 

每个所有者，通过数码上签署上一笔交易和下一个所有者的公钥的哈希值的签名，并把数字签名添加到货币的末尾，把货币转给下一个所有者。

A payee can verify the signatures to verify the chain of ownership.

收款人可以通过验证这个签名去验证这个链的所有者。

![](https://raw.githubusercontent.com/gdkr100/Writing_Public/master/pictures/bitcoin_white_paper/1_transaction.jpg)

![](https://raw.githubusercontent.com/gdkr100/Writing_Public/master/pictures/bitcoin_white_paper/1_transaction_cn.png)

----------------------------------------------------------------

这个问题当然是收款人不能验证所有者有没有双花代币。通常的解决方案是引入一个可信任的中心化的机构，或者造币厂，来检查每笔交易有没有双花。每笔交易后，代币必须返还给造币厂去发行一个新的。代币直接从可以被信任的不会被双花的造币厂发行。这个解决方案的问题是，整个金钱系统的命运取决于运行造币厂的公司，每笔交易都要通过它们，像一个银行。

我们需要有一个方法让收款人知道之前的所有者没有签署任何更早的交易。为了我们的目的，最早的交易是已经被计数的，所以我们不在乎后面双花的尝试。唯一确认交易缺席的方法是知道所有交易。在基于造币厂的模型，造币厂知道所有的交易，并决定哪个先到。要在没有第三方的情况下完成它，交易必须被公开宣布，我们需要一个系统让参与者同意一个它们所收到的顺序的历史。收款人需要每笔交易的时间和节点大多数同意的是首先收到的证明。

## 3.时间戳服务器

我们提议的解决方案以时间戳服务器开始。时间戳服务器是把项目区块的哈希值盖上时间戳，并广泛的发布这个哈希，比如在报纸上或新闻组帖子上。时间戳证明数据在这个时候存在，显然，未了进这个哈希。每个时间戳在它的哈希里包含之前的时间戳，形成一个新链，每个额外的时间戳，增加之前的那个。

![](https://raw.githubusercontent.com/gdkr100/Writing_Public/master/pictures/bitcoin_white_paper/2_timestamp.jpg)

## 4.工作证明

在一个点对点的基础上去实施一个分布式的时间戳服务器，我们将用一个类似于Adam Back的哈希现金的工作证明，而不是报纸或 Usene帖子。工作证明涉及扫描被哈希的值，例如用SHA-256，哈希以0字节的数字开头。所需要的平均工作是指数的，在需要的零字节的数字上，可以通过执行一条哈希验证。

对于我们的时间戳网络，我们通过在区块中增加一个随机数，直到一个给定所需零字节区块哈希的值被找到的方式实施。一旦CPU努力被扩展到可以满足工作证明，不重做这个工作，区块不能被改变。因为后面的区块会链到后面，改变区块的工作包括重做后面的所有区块。

![](https://raw.githubusercontent.com/gdkr100/Writing_Public/master/pictures/bitcoin_white_paper/3_proof_of_work.jpg)

工作证明也解决了决定大多数决策制定表达的问题。如果大多数基于1个IP地址1票，它就会被任何分配许多IP的人破会。工作证明本质上是一个CPU一票，大部分人的决定由最长链代表，拥有最多的工作证明努力投入到里面。如果大部分算力由诚实节点控制，诚实的链会增长最快，并超过其它竞争链。修改一个过去的链，攻击者需要重做这个区块的工作证明，和所有它后的的区块的工作证明，然后赶上并超过诚实节点的工作。随后，我们会展示一个较慢的攻击者以指数方式赶上缩减当随后区块被增加。

为了补偿增加的硬件速度和在运行网络中的不同利益随着时间，工作证明难度是由一个变化的平均值决定，这个平均值致力于每小时的区块数。如果增长过快，难度会增加。

## 5.网络

运行网络的步骤如下：

1）新交易会广播给所有节点
2）每个节点加新交易增加进区块
3）每个节点为这个区块寻找一个有难度的工作证明
4）当一个区块找到工作证明，会把这个区块广播给所有节点
5）只有当区块中的交易都是有效的，并没有被花掉，节点们才会接受这个区块
6）节点通过开始在链上建立下个区块，把接受的区块的哈希作为之前的哈希的方式来表达对这个区块的接受

节点总是认为最长的链是正确的那个，并继续工作去扩展它。如果两个节点同时广播下个节点的不同版本，一些节点首先会收到一个或另外一个。在那种情况下，它们处理它们收到的第一个，保存另外一个分支万一它变得更长。联系会被打破，当下个工作证明被找到，一个分支变的更长。处理另外一个分支的节点会切换到这个更长的上面。

新的交易广播不必要到达所有节点。只要它们到达许多节点，它们不久以后就会进入一个区块。区块广播也容忍丢失的消息。当一个节点收不到一个区块，当它们收到下个区块，并意识到丢了一个，会请求它。

## 6.动机

按照惯例，区块中的第一个交易时一个特殊的交易，开始一个由区块建立者拥有的新代币。这增加了节点支持这个网络的动机，提供一个最初分发代币进行流通的方法，因为没有中心化的机构发行它们。稳定增加的新币的恒定数量和花费资源去增加黄金到流通里的的黄金矿工类似。在我们这里，花费的时CPU时间和电力。

激励也由交易费提供资金。如果一个交易的输出值少于它的输入值，这个差值就是交易费，加到区块包含交易的激励值。当预先决定的代币数量完全进入流通，激励会完全过渡到交易费，而不会通胀。

动机会有助于让矿工保持诚实。当贪婪的攻击者能够比诚实的节点聚集更多的算力，它们会在用它偷回它的支付去欺诈别人或用它生成新币。它应该会发现按照规则来做会获利更多，相比破坏这个系统和它自己财富的有效性，规则会让得到比它们人加起来更多的币对他更有利。

## 7.回收再利用磁盘空间

一旦一个代币里的最近的交易埋藏在足够的区块下面，它之前的消费交易可以被丢弃去节省空空间。在不打破区块哈希值的情况下实施它，交易在默克尔树下哈希化，在区块哈希中仅仅保留根。旧区块会被压缩，通过拔除树枝。内部的哈希不需要被存储。

![](https://raw.githubusercontent.com/gdkr100/Writing_Public/master/pictures/bitcoin_white_paper/4_reclaim_disk_space.jpg)

不包含交易的区块头大概80字节。如果我们假设每10分钟生成一个区块，每年80 bytes * 6 * 24 * 365 = 4.2MB。2008年计算机系统典型配置是 2GBRAM。摩尔定律预测现在的增长是1.2GB每年，即使区块头必须存储在内存中，存储也不是问题。

## 8.简易支付验证

在不运行全节点的情况下可以进行支付验证。用户仅需要保存一份最长工作证明链的区块头，可以通过查询网络节点得到知道它确信它拥有的是最长链。得到把交易链接到它时间戳所在区块的的默克尔分支。它不能为自己检查交易，但是可以把它链接到链上的一个地方，它可以看到网络节点接受它，加在它后面的区块进一步确认网络已接受它。

![](https://raw.githubusercontent.com/gdkr100/Writing_Public/master/pictures/bitcoin_white_paper/5_SPV.jpg)

同样地，只要诚实的节点控制这个网络，验证就是可信的，但是如果网络被攻击者控制，它会更脆弱。当网络节点可以为他们自己验证交易，只要攻击者继续控制网络，简单的方式就会被攻击者编造的交易欺骗。一个保护它的策略是接受网络节点的警告，当检测到一个无效交易，提示用户的节点下载全区块，并警告交易确认不一致。频繁交易的商家可能像运行他们自己的节点，以获得独立的安全和更快的确认。

## 9.结合和拆分价值

虽然能单独的处理代币，为交易中的每一分钱做一个交易是不灵便的。为了让价值可以被拆分和组合，交易包含多重输入和输出。正常会有来自更大的之前的交易的输入或结合小额的多重输入，至多两个输出：一个用于支付，另外一个找零，如果有，返回给发送者。

![](https://raw.githubusercontent.com/gdkr100/Writing_Public/master/pictures/bitcoin_white_paper/6_combine_split_value.jpg)

应该注意扇出，一笔交易依赖若干交易，这些交易依赖更多的交易，在这里不是问题，从不需要提取一份独立运行的交易历史。

## 10.隐私

传统银行模型通过对涉及的相关方和可信赖第三方提供限制的准入来达到一定程度的隐私。有必要声明所有交易公开的排除了这个方式。但通过打断其它地方的信息流，隐私任然可以保持：通过保持公钥匿名。公众可以看到某人给其它人发送一定的金额，但没有信息把这笔交易链接到任何人。这和股票加偶一所释放的一定程度的信息相似，个人交易的时间和尺寸，“胶带”，是公开的，但没有告诉这一方是谁。

![](https://raw.githubusercontent.com/gdkr100/Writing_Public/master/pictures/bitcoin_white_paper/7_privacy.jpg)

作为一个额外的防火墙，每笔交易要用一个新的密钥对，去保持不被链接到一个普通的用户。多重输入的交易中，一些链接是不可避免的，必须显示输入由相同的所有者拥有。风险是一个密钥的所有者被显示，链接可以显示属于相同所有者的其它交易。

## 11.计算

我们考虑一个试图生成一个比诚实链快的替代链的方案。即使完成这个，也不会让系统可以被任意修改,比如无中生有地的创造价值或拿走从不属于攻击者的财产。节点不会接受一笔无效的交易作为支付，诚实节点从来不会接受包含他们的区块。一个攻击者只能改变一个它自己的交易，拿回最近它花出去的钱。

诚实的链和攻击者的链的竞赛可被称为二项随机过程。成功的事件是诚实链扩展你一个区块，领导位置加1。失败的事件是攻击者的链扩展一个区块，差距缩小1 。

一个攻击者赶上一个给定赤字的可能性类似于赌徒输光问题。假设一个从赤字开始的拥有无限额度的赌徒，可能尝试无限次数达到一个不赔不赚。我们计算它曾经到达不亏不赚的可能性或一个攻击者赶上诚实链，如下：

p = 一个诚实节点找到下个区块的可能性

q = 一个攻击者找到下个区块的可能性

qz = 一个攻击者赶上从z区块后面的可能性

![](https://raw.githubusercontent.com/gdkr100/Writing_Public/master/pictures/bitcoin_white_paper/8_calculation_1.jpg)

假设p>q,可能性呈指数级下降，当攻击者需要赶上的区块数增加。他们的机会渺茫，如果他们没有在早期由一个幸运的猛冲，它的机会趋于零地当进一步落后。

我们现在考虑一笔新交易的接收者需要等多久才能充分确定发送者不能改变这笔交易。我们假设发送者是一个想暂时让接收者相信它已经支付的攻击者，然后过段时间再付回给自己。当这个发生，接收者回被提醒。发送者希望这会太迟了。

接受者生成一个新密钥对，在签名之前立刻把公钥给发送者。这阻止了发送者提前准备一个区块链，通过持续的工作，直到它足够幸运领先足够多，然后在那时执行交易。一旦交易被发送，不诚实的发送者秘密地在一个包含它交易的替代版本的平行链上工作。

接受者会等到直到交易被加入一个区块，z区块链接在它后面。它不直到攻击者进程的具体数量，但是假设诚实节点每个区块花费平均的期望时间，攻击者的进程会是一个带由期望值的泊松分布：

![](https://raw.githubusercontent.com/gdkr100/Writing_Public/master/pictures/bitcoin_white_paper/9_calculation_2.jpg)

得到攻击者仍然能赶上的可能性，我们为每个进程数量增加泊松密度，它能达到的它可以跟上那个点的可能性：

![](https://raw.githubusercontent.com/gdkr100/Writing_Public/master/pictures/bitcoin_white_paper/10_calculation_3.jpg)

重排去避免对分布的无限尾巴求和。

![](https://raw.githubusercontent.com/gdkr100/Writing_Public/master/pictures/bitcoin_white_paper/11_calculation_4.jpg)

转换称C语言：

```
#include <math.h>
double AttackerSuccessProbability(double q, int z)
{
 double p = 1.0 - q;
 double lambda = z * (q / p);
 double sum = 1.0;
 int i, k;
 for (k = 0; k <= z; k++)
 {
 double poisson = exp(-lambda);
 for (i = 1; i <= k; i++)
 poisson *= lambda / i;
 sum -= poisson * (1 - pow(q / p, z - k));
 }
 ret
```

运行一些结果，我们看到可能性随着z指数级下降：

```
q=0.1
z=0 P=1.0000000
z=1 P=0.2045873
z=2 P=0.0509779
z=3 P=0.0131722
z=4 P=0.0034552
z=5 P=0.0009137
z=6 P=0.0002428
z=7 P=0.0000647
z=8 P=0.0000173
z=9 P=0.0000046
z=10 P=0.0000012
q=0.3
z=0 P=1.0000000
z=5 P=0.1773523
z=10 P=0.0416605
z=15 P=0.0101008
z=20 P=0.0024804
z=25 P=0.0006132
z=30 P=0.0001522
z=35 P=0.0000379
z=40 P=0.0000095
z=45 P=0.0000024
z=50 P=0.0000006
```

解决P小于 0.1%...

```
P < 0.001
q=0.10 z=5
q=0.15 z=8
q=0.20 z=11
q=0.25 z=15
q=0.30 z=24
q=0.35 z=41
q=0.40 z=89
q=0.45 z=340
```

# 12.结论

我们提议了一个不依赖信任的电子交易系统。我们从来自数字签名的代币的通常网络开始，提供很强的所有权控制，但是不完整因为没有阻止双花的方法。为了解决这个，我们提议的了一个点对点的网络，使用工作证明去记录公共的交易历史，如果诚实节点控制大部分算力，一个攻击者在计算上改变它不切实际。这个网络是健壮的，在他们的没有正式组织的简洁。节点立刻工作，只要很少的协作。他们不需要被识别，因为信息不经过特定的地方，只要基于最佳努力基础传递。节点可以任意离开或重新加入网络，接受工作证明链，作为他们离开时所发生事情的证明。他们用算力投票，表达他们接受有效区块，通过扩展他们和拒绝无效区块，通过拒绝在上面工作。任何需要的规则和动机由这个共识机制实施。

**引用**

[1] W. Dai, "b-money," http://www.weidai.com/bmoney.txt, 1998.

[2] H. Massias, X.S. Avila, and J.-J. Quisquater, "Design of a secure timestamping service with minimal
trust requirements," In 20th Symposium on Information Theory in the Benelux, May 1999.

[3] S. Haber, W.S. Stornetta, "How to time-stamp a digital document," In Journal of Cryptology, vol 3, no
2, pages 99-111, 1991.

[4] D. Bayer, S. Haber, W.S. Stornetta, "Improving the efficiency and reliability of digital time-stamping,"
In Sequences II: Methods in Communication, Security and Computer Science, pages 329-334, 1993.

[5] S. Haber, W.S. Stornetta, "Secure names for bit-strings," In Proceedings of the 4th ACM Conference
on Computer and Communications Security, pages 28-35, April 1997.

[6] A. Back, "Hashcash - a denial of service counter-measure,"
http://www.hashcash.org/papers/hashcash.pdf, 2002.

[7] R.C. Merkle, "Protocols for public key cryptosystems," In Proc. 1980 Symposium on Security and
Privacy, IEEE Computer Society, pages 122-133, April 1980.

[8] W. Feller, "An introduction to probability theory and its applications," 1957.

