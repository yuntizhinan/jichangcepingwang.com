import os

base_dir = r"C:\Users\PC\.gemini\antigravity-ide\scratch\airport-review-blog"

articles = {
    "tutorial-clash-verge.html": {
        "title": "Clash Verge Rev 零基础配置教程 (Windows / macOS 全指南)",
        "tag": "Clash",
        "desc": "Clash Verge Rev 是 2026 年最强 Clash 替代客户端，基于 Tauri 架构，内存占用极低且支持 Clash Meta 内核。本文详细讲解下载、安装、订阅导入、TUN 模式及高级规则配置。",
        "content_sections": """
        <h2>一、Clash Verge Rev 核心优势与版本选型</h2>
        <p>随着原 Clash Premium / Clash for Windows 停止维护，<strong>Clash Verge Rev</strong> 凭借其基于 Rust + Tauri 的高效轻量设计，已正式成为 2026 年全平台科学上网的首选客户端。它不仅完美集成了 Clash.Meta (Mihomo) 开源内核，更提供了极佳的中文图形界面与智能化分流策略管理。</p>
        <ul>
            <li><strong>内存占用极低：</strong> 基于 Tauri 开发，后台驻留仅占约 30MB-50MB 内存，远低于 Electron 框架。</li>
            <li><strong>完整支持 Mihomo 内核：</strong> 原生支持 Hysteria2、TUIC v5、VLESS-Reality 等现代加密传输协议。</li>
            <li><strong>TUN 虚拟网卡模式：</strong> 支持全局接管桌面所有软件网络流量，对 UWP 应用、游戏及终端命令行极其友好。</li>
        </ul>

        <h2>二、软件下载与安装步骤</h2>
        <p>请认准官方 GitHub 开源仓库进行下载，切勿下载来源不明的第三方编译修改版：</p>
        <ul>
            <li><strong>GitHub 官方发布页：</strong> <a href="https://github.com/clash-verge-rev/clash-verge-rev/releases" target="_blank" rel="noopener">clash-verge-rev/releases (官方直达)</a></li>
            <li><strong>Windows 用户：</strong> 建议下载 <code>Clash.Verge_x64-setup.exe</code> 安装包。</li>
            <li><strong>macOS 用户：</strong> Intel 芯片选择 <code>x64.dmg</code>，Apple Silicon (M1/M2/M3) 芯片选择 <code>aarch64.dmg</code>。</li>
        </ul>

        <h2>三、订阅链接导入与节点选择</h2>
        <ol>
            <li>打开 Clash Verge Rev，在左侧导航栏点击 <strong>“订阅 (Profiles)”</strong>。</li>
            <li>在顶部输入框中粘贴您在机场后台复制的 <strong>Clash 订阅链接 (URL)</strong>，点击右侧 <strong>“导入 (Import)”</strong>。</li>
            <li>导入成功后，鼠标左键点击切换选中刚下载的配置文件。</li>
            <li>进入 <strong>“代理 (Proxies)”</strong> 页面，选择 <strong>“规则 (Rule)”</strong> 模式，并选择延迟最低的专线节点（如香港 IEPL 或日本 IPLC）。</li>
            <li>在左侧点击 <strong>“设置 (Settings)”</strong>，勾选 <strong>“系统代理 (System Proxy)”</strong> 即可畅享高速网络。</li>
        </ol>

        <h2>四、TUN 虚拟网卡模式与高级功能开启</h2>
        <p>部分应用程序（如 Spotify 客户端、Git 终端、独立游戏）可能不会遵循系统代理设置。此时开启 TUN 模式可全面接管电脑全局流量：</p>
        <ol>
            <li>在 Clash Verge Rev 界面左侧进入 <strong>“设置 (Settings)”</strong>。</li>
            <li>找到 <strong>“TUN 模式 (TUN Mode)”</strong> 开关并开启。首次开启 Windows 会弹出管理员权限提示，选择“允许”。</li>
            <li>在 TUN 模式下，系统会自动安装虚拟网卡，实现全自动游戏加速与终端全流量代理。</li>
        </ol>

        <h2>❓ Clash Verge Rev 用户常见问题 FAQ (8条)</h2>
        <div class="faq-list">
            <div class="faq-item"><div class="faq-question">Q1: 为什么导入订阅时提示 Network Error 或下载失败？</div><div class="faq-answer">答：通常是因为机场订阅域名受公网干扰。解决办法：1. 在订阅链接后追加临时代理，或先通过手机热点导入；2. 检查订阅链接 URL 是否完整粘贴。</div></div>
            <div class="faq-item"><div class="faq-question">Q2: 开启系统代理后网页依然打不开怎么处理？</div><div class="faq-answer">答：请先检查“代理”页面是否选择了具体的可用节点；若节点连通性正常，请检查系统时间是否与北京时间完全一致（时区偏差会导致 TLS 握手失败）。</div></div>
            <div class="faq-item"><div class="faq-question">Q3: TUN 模式和系统代理模式有什么区别？应该选哪个？</div><div class="faq-answer">答：系统代理仅作用于遵循系统 HTTP 代理的浏览器与常规软件；TUN 模式通过虚拟网卡接管电脑所有流量（包括游戏、命令行、UWP）。日常浏览网页开启系统代理即可，玩游戏或用命令行推荐开启 TUN 模式。</div>
            <div class="faq-item"><div class="faq-question">Q4: 如何设置开机自启与静默启动？</div><div class="faq-answer">答：在软件“设置”页面中，同时开启“开机自启动 (Auto Launch)”与“最小化到系统托盘 (Silent Start)”即可。</div></div>
            <div class="faq-item"><div class="faq-question">Q5: 为什么节点延迟显示为 Timeout（超时）？</div><div class="faq-answer">答：可能由于机场节点正在维护，或您的套餐流量已耗尽。请前往机场后台确认订阅状态，并在软件中右键点击订阅执行“更新 (Update)”。</div></div>
            <div class="faq-item"><div class="faq-question">Q6: Clash Verge Rev 如何切换内核 (Mihomo / Premium)？</div><div class="faq-answer">答：软件默认内置最新的 Mihomo (Clash.Meta) 内核，支持全部现代协议。可在“设置”->“Clash 内核”中随时一键切换或更新内核版本。</div></div>
            <div class="faq-item"><div class="faq-question">Q7: 开启 Clash 后微信或国内软件变慢或加载失败怎么办？</div><div class="faq-answer">答：请确保运行模式设置为“Rule (规则分流)”而非“Global (全局代理)”，规则模式会自动将国内流量直连，不消耗机场流量且保障速度。</div></div>
            <div class="faq-item"><div class="faq-question">Q8: 软件更新提示失败或报错怎么解决？</div><div class="faq-answer">答：建议直接前往官方 GitHub 仓库下载新的 `.exe` 或 `.dmg` 覆盖安装，配置与订阅数据会自动保留。</div></div>
        </div>
        """
    },
    "tutorial-shadowrocket.html": {
        "title": "Shadowrocket (小火箭) 零基础上手与配置教程 (iOS 苹果全指南)",
        "tag": "iOS",
        "desc": "Shadowrocket（俗称小火箭）是 iOS 平台上口碑极佳的代理工具。本文讲解如何获取美区 Apple ID、安装小火箭、节点导入、规则分流及场景自动化设置。",
        "content_sections": """
        <h2>一、Shadowrocket 软件简介与下载方式</h2>
        <p><strong>Shadowrocket（小火箭）</strong> 是苹果 iOS / iPadOS 系统上功能最强劲、操作最简单的高性能代理软件。由于中国大陆 App Store 无法搜索下载，用户需要通过外区（如美区、港区）Apple ID 登入 App Store 购买下载（售价 $2.99）。</p>

        <h2>二、如何获取与登录外区 Apple ID 下载小火箭</h2>
        <ol>
            <li><strong>注意安全：</strong> 严禁在 iPhone 设备的 <code>设置 -> iCloud</code> 中登录他人共享账号！仅在 <code>App Store</code> 中切换账号。</li>
            <li>打开 iPhone 的 <strong>App Store</strong>，点击右上角个人头像。</li>
            <li>滑动到最底部点击 <strong>“退出登录 (Sign Out)”</strong>。</li>
            <li>输入您自建的外区（美区）Apple ID 账号与密码登录。</li>
            <li>登录成功后，在 App Store 搜索 <code>Shadowrocket</code> 并下载安装。安装完成后退出外区账号，切回您的个人 App Store 账号。</li>
        </ol>

        <h2>三、节点订阅导入与节点切换</h2>
        <ol>
            <li>打开 Shadowrocket，点击右上角 <strong>“+”</strong> 号。</li>
            <li>在 <strong>“类型 (Type)”</strong> 中选择 <strong>“Subscribe (订阅)”</strong>。</li>
            <li>在 <strong>“URL”</strong> 输入框中粘贴在机场后台复制的小火箭订阅链接，在“备注”中填写机场名称，点击右上方“保存”。</li>
            <li>小火箭会自动从服务器下载节点列表。在首页列表中，点击选中一个低延迟的 IEPL 专线节点。</li>
            <li>将顶部的 <strong>“未连接”</strong> 开关开启，首次开启会弹出系统提示“添加 VPN 配置”，输入 iPhone 解锁密码授权即可。</li>
        </ol>

        <h2>四、路由全局与规则模式设置</h2>
        <p>小火箭默认推荐开启 <strong>“配置 (Config)”</strong> 模式（即智能分流）：</p>
        <ul>
            <li><strong>配置 (Config) 模式：</strong> 国内网站与 APP 直接连接，海外受限网站走加速节点，省电且不影响微信使用。</li>
            <li><strong>代理 (Proxy) 模式：</strong> 强制全局所有流量经过节点代理。</li>
            <li><strong>直连 (Direct) 模式：</strong> 不经过任何节点，全局直连。</li>
        </ul>

        <h2>❓ Shadowrocket 用户常见问题 FAQ (8条)</h2>
        <div class="faq-list">
            <div class="faq-item"><div class="faq-question">Q1: App Store 搜出来的“小火箭”图标不对是假软件吗？</div><div class="faq-answer">答：请认准软件名称 `Shadowrocket`，图标为正方形阴影小火箭图标，开发者为 `Lining Guo`。市面上有很多山寨仿冒版，切勿下载。</div></div>
            <div class="faq-item"><div class="faq-question">Q2: 为什么开启小火箭后提示“无法添加 VPN 配置”？</div><div class="faq-answer">答：请检查 iPhone 的 `设置 -> 通用 -> VPN 与设备管理`，删掉残留的其他 VPN 描述文件，重启手机后再试。</div></div>
            <div class="faq-item"><div class="faq-question">Q3: 共享 Apple ID 提示账号锁定或需要双重验证怎么办？</div><div class="faq-answer">答：共享账号容易被多人使用锁定，强烈建议参考网上教程使用个人邮箱花费 5 分钟注册一个专属的美区 Apple ID。</div></div>
            <div class="faq-item"><div class="faq-question">Q4: 为什么小火箭连接后可以上网，但延迟测速全显示 Ping 失败？</div><div class="faq-answer">答：请在小火箭 `设置 -> 测试分组` 中将测试网址更改为 `https://www.google.com/generate_204` 或 `Cloudflare`。</div></div>
            <div class="faq-item"><div class="faq-question">Q5: 如何设置定时自动刷新订阅节点？</div><div class="faq-answer">答：进入小火箭 `设置 -> 订阅`，开启 `打开时更新` 和 `自动更新`，确保每次打开小火箭都能同步最新节点。</div></div>
            <div class="faq-item"><div class="faq-question">Q6: 小火箭支持 TikTok 刷视频和 ChatGPT 吗？</div><div class="faq-answer">答：完美支持。小火箭配合带有原生 IP 的专线节点，可无缝畅刷海外版 TikTok 并稳定对话 ChatGPT。</div></div>
            <div class="faq-item"><div class="faq-question">Q7: 开启小火箭后连接 Wi-Fi 正常，切换到 4G/5G 手机网络就断网？</div><div class="faq-answer">答：请在 iPhone `设置 -> 蜂窝网络` 中找到小火箭，确保已勾选 `无线局域网与蜂窝数据` 权限。</div></div>
            <div class="faq-item"><div class="faq-question">Q8: 小火箭节点可以共享给同一 Wi-Fi 下的 iPad 或电脑使用吗？</div><div class="faq-answer">答：可以。在小火箭 `设置 -> 代理 -> 允许代理` 开启代理共享，其他设备设置代理 HTTP 主机 IP 与端口即可。</div></div>
        </div>
        """
    },
    "tutorial-v2rayn.html": {
        "title": "v2rayN Windows 客户端深度配置指南",
        "tag": "v2rayN",
        "desc": "v2rayN 是 Windows 平台上最成熟经典的开源代理客户端。本文提供 v2rayN 7.x 最新版下载、Core 内核更新、订阅导入与系统代理设置全教程。",
        "content_sections": """
        <h2>一、v2rayN 软件概述与版本下载</h2>
        <p><strong>v2rayN</strong> 是 Windows 系统上使用最广泛的开源代理图形客户端，原生支持 Xray-core、sing-box 等多种前沿内核。界面简洁、功能强大，适合注重稳定性与极客自定义的用户。</p>
        <ul>
            <li><strong>官方 GitHub 下载：</strong> <a href="https://github.com/2dust/v2rayN/releases" target="_blank" rel="noopener">2dust/v2rayN (官方 Release)</a></li>
            <li><strong>推荐版本：</strong> 建议下载包含内核的 <code>v2rayN-With-Core.zip</code>（无需额外配置内核）。</li>
        </ul>

        <h2>二、软件解压与运行说明</h2>
        <ol>
            <li>下载压缩包后，将其解压到一个<strong>非中文路径</strong>的文件夹中（例如 <code>D:\\Software\\v2rayN\\</code>）。</li>
            <li>右键点击 <code>v2rayN.exe</code>，选择“以管理员身份运行”。</li>
            <li>如果系统提示需要安装 <code>.NET Desktop Runtime 8.0</code>，请点击提示链接前往微软官网安装依赖运行库。</li>
        </ol>

        <h2>三、机场订阅导入与节点测试</h2>
        <ol>
            <li>在 v2rayN 主界面顶部菜单栏中，点击 <strong>“订阅分组” -> “订阅分组设置”</strong>。</li>
            <li>在弹出的窗口中点击 <strong>“添加”</strong>，在“备注”中输入机场名称，在“地址 (url)”中粘贴机场订阅链接，点击“保存”。</li>
            <li>回到主界面，点击顶部菜单 <strong>“订阅分组” -> “更新订阅 (不通过代理)”</strong>。</li>
            <li>节点加载完成后，按键盘 <code>Ctrl + A</code> 全选节点，按 <code>Ctrl + O</code> 批量测试节点真连接延迟 (Ping)。</li>
            <li>选中延迟较低的专线节点，按 Enter 键设为活动节点。</li>
        </ol>

        <h2>四、系统代理与路由规则开启</h2>
        <p>在 v2rayN 主界面底部底部状态栏中：</p>
        <ul>
            <li><strong>自动配置系统代理：</strong> 将状态切换为“自动配置系统代理”（图标变红），此时电脑浏览器即可科学上网。</li>
            <li><strong>路由规则：</strong> 推荐选择 <code>绕过大陆 (bypass mainland)</code>，实现国内流量直连、国外流量加速。</li>
        </ul>

        <h2>❓ v2rayN 用户常见问题 FAQ (8条)</h2>
        <div class="faq-list">
            <div class="faq-item"><div class="faq-question">Q1: 双击 v2rayN.exe 无反应或直接报错崩塌怎么办？</div><div class="faq-answer">答：请检查是否缺失微软 .NET Framework 4.8 或 .NET 8.0 Desktop Runtime。下载并安装最新微软依赖库即可解决。</div></div>
            <div class="faq-item"><div class="faq-question">Q2: 为什么更新订阅时提示“基础连接已经关闭”？</div><div class="faq-answer">答：尝试在“订阅分组设置”中将该订阅的“通过代理更新”勾选打开，或切换为手机热点后再尝试更新。</div></div>
            <div class="faq-item"><div class="faq-question">Q3: v2rayN 的“真连接延迟”与“Tcping”有什么区别？</div><div class="faq-answer">答：Tcping 仅测试本地到节点的网络连通性；真连接延迟会真正发送数据到 Google 并返回时间，数据更加真实。</div></div>
            <div class="faq-item"><div class="faq-question">Q4: 如何更新最新的 Xray-core / sing-box 内核？</div><div class="faq-answer">答：在 v2rayN 顶部菜单点击 `检查更新 -> 更新 Core`，勾选对应内核点击更新即可自动替换升级。</div></div>
            <div class="faq-item"><div class="faq-question">Q5: 开启系统代理后，Edge/Chrome 浏览器依然无法访问海外网站？</div><div class="faq-answer">答：请检查浏览器是否安装了冲突的 SwitchyOmega 插件。若有，请在插件中选择“使用系统代理”。</div></div>
            <div class="faq-item"><div class="faq-question">Q6: v2rayN 开启自动配置系统代理后，关闭软件会导致电脑彻底断网吗？</div><div class="faq-answer">答：非正常退出可能导致系统代理未自动清除。请重新打开 v2rayN，将底部系统代理改为“清除系统代理”后正常退出即可。</div></div>
            <div class="faq-item"><div class="faq-question">Q7: v2rayN 支持 Hysteria2 和 TUIC 协议吗？</div><div class="faq-answer">答：支持。只要将内核更新到最新的 Xray-core 或 sing-box 内核，导入对应协议订阅即可正常连接。</div></div>
            <div class="faq-item"><div class="faq-question">Q8: 如何开启 v2rayN 的 TUN 模式接管游戏流量？</div><div class="faq-answer">答：在软件主界面底部找到 `TUN 模式` 开关，将其勾选开启（需要管理员权限），即可全局接管桌面游戏流量。</div></div>
        </div>
        """
    },
    "tutorial-android.html": {
        "title": "安卓手机客户端选型指南与配置教程 (Clash Meta / v2rayNG)",
        "tag": "Android",
        "desc": "深入对比 Android 平台两大主流科学上网工具 Clash Meta for Android 与 v2rayNG。提供 APK 官方下载、分流设置与电池优化避坑指南。",
        "content_sections": """
        <h2>一、安卓客户端两大主流选型对比</h2>
        <p>在 Android（安卓）系统上，由于开放性极佳，用户无需外区账号即可免费安装强大的科学上网工具。目前最受推崇的客户端主要为以下两款：</p>
        <ul>
            <li><strong>Clash Meta for Android (CMFA)：</strong> 界面美观、分流规则极其强大，支持分应用代理，适合追求智能分流与极致体验的用户。</li>
            <li><strong>v2rayNG：</strong> 经典稳定、极简轻量，对低配置手机极为友好，适合零基础小白用户。</li>
        </ul>

        <h2>二、Clash Meta for Android 安装与配置步骤</h2>
        <ol>
            <li><strong>下载 APK：</strong> 前往开源仓库下载安装包（选择 <code>cmfa-*-universal-release.apk</code>）。</li>
            <li>打开应用，点击 <strong>“配置 (Profiles)” -> “新配置 (New Profile)” -> “URL”</strong>。</li>
            <li>名称填写机场名，URL 粘贴机场 Clash 订阅链接，自动更新间隔设置为 <code>1440</code> 分钟（24小时），点击右上角保存。</li>
            <li>回到配置列表，选中刚导入的配置文件。</li>
            <li>回到首页，点击右下角的 <strong>“已停止 (Stopped)”</strong> 按钮开启代理。在弹出的系统 VPN 权限申请中点击“允许”。</li>
            <li>在“代理 (Proxies)”页面中选择合适的 IEPL 专线节点。</li>
        </ol>

        <h2>三、防止后台被安卓系统杀进程 (电池优化设置)</h2>
        <p>国产生态手机（小米 HyperOS、华为鸿蒙、OPPO ColorOS、vivo OriginOS）通常具有严格的后台保活清理机制。为防止科学上网中断，请务必完成以下设置：</p>
        <ol>
            <li>在手机“设置” -> “应用管理”中找到 Clash 或 v2rayNG。</li>
            <li>进入“电池”或“后台管理”，将省电策略修改为 <strong>“无限制 (允许后台高耗电)”</strong>。</li>
            <li>在多任务后台卡片中，将客户端应用卡片下拉 <strong>“加锁 (Lock)”</strong>，防止一键清理。</li>
        </ol>

        <h2>❓ 安卓客户端用户常见问题 FAQ (8条)</h2>
        <div class="faq-list">
            <div class="faq-item"><div class="faq-question">Q1: 安卓安装 APK 时提示“高危应用”或“禁止安装”怎么处理？</div><div class="faq-answer">答：这是国产手机安全管家的误报。请在安装界面关闭“联网安全扫描”或断开 Wi-Fi 允许安装即可。</div></div>
            <div class="faq-item"><div class="faq-question">Q2: 如何设置部分国内 APP（如微信/淘宝）不走代理？</div><div class="faq-answer">答：在 Clash Meta 中进入 `设置 -> 应用分流`，开启分流开关，并勾选微信、支付宝等应用设置为“直连”即可。</div></div>
            <div class="faq-item"><div class="faq-question">Q3: 为什么连接代理后手机热点共享给电脑，电脑无法上网？</div><div class="faq-answer">答：安卓默认热点不经过代理。请在 Clash Meta `设置 -> 网络` 中开启 `允许局域网连接` 及 `热点共享代理` 开关。</div></div>
            <div class="faq-item"><div class="faq-question">Q4: Clash Meta 和 v2rayNG 哪个更省电？</div><div class="faq-answer">答：v2rayNG 代码极其轻量，后台耗电略低于 Clash。但只要正确配置分流，两者的日常耗电差异并不明显。</div></div>
            <div class="faq-item"><div class="faq-question">Q5: 为什么锁屏一段时间后代理会自动断开连不上网？</div><div class="faq-answer">答：说明客户端后台被手机系统休眠清理了。请按照本文第三节完成电池优化无限制与后台锁定设置。</div></div>
            <div class="faq-item"><div class="faq-question">Q6: 安卓手机可以使用小火箭 (Shadowrocket) 吗？</div><div class="faq-answer">答：不能。Shadowrocket 是 iOS 苹果系统独占软件。安卓平台请认准 Clash Meta for Android 或 v2rayNG。</div></div>
            <div class="faq-item"><div class="faq-question">Q7: 为什么更新订阅提示 DNS 解析失败？</div><div class="faq-answer">答：请在应用设置中将自定义 DNS 修改为 `223.5.5.5` (阿里 DNS) 或 `119.29.29.29` (腾讯 DNS) 重新尝试。</div></div>
            <div class="faq-item"><div class="faq-question">Q8: 安卓端如何测试节点的真实延迟？</div><div class="faq-answer">答：在 Clash 的 Proxies 代理页面右上角点击“闪电图标”或“双箭号”，即可批量对全节点发起真实 HTTP 延迟测试。</div></div>
        </div>
        """
    },
    "tutorial-mac.html": {
        "title": "Mac 苹果电脑科学上网配置全指南 (Clash Verge / Sing-Box)",
        "tag": "Mac",
        "desc": "专为 macOS 苹果电脑用户打造的代理配置教程。讲解 Apple Silicon 芯片适配、Clash Verge Rev Mac 版配置、增强模式及权限设置。",
        "content_sections": """
        <h2>一、Mac 苹果电脑代理客户端选型</h2>
        <p>macOS 系统拥有优雅的图形界面与强劲的 M 系列芯片效能。在 macOS 平台，我们强烈推荐以下两款客户端：</p>
        <ul>
            <li><strong>Clash Verge Rev (Mac 版)：</strong> 完美原生支持 M1/M2/M3/M4 芯片，内存占用极低，界面美观。</li>
            <li><strong>Sing-Box GUI for macOS：</strong> 现代通用内核客户端，支持全协议架构。</li>
        </ul>

        <h2>二、macOS 安装包选择与“已损坏无法打开”解决办法</h2>
        <ol>
            <li><strong>芯片识别：</strong> 点击 Mac 屏幕左上角苹果 Logo  -> “关于本机”。若显示 Apple M1/M2/M3，请下载 <code>aarch64.dmg</code>；若显示 Intel 处理器，下载 <code>x64.dmg</code>。</li>
            <li>双击 <code>.dmg</code> 镜像包，将应用程序图标拖入 <code>Applications (应用程序)</code> 文件夹中。</li>
            <li><strong>Gatekeeper 提示解决：</strong> 首次打开若提示“应用已损坏，无法打开”或来自未身份验证开发者，请打开 Mac 的 <code>终端 (Terminal)</code>，执行以下命令并输入 Mac 解锁密码：<br>
            <code>sudo xattr -rd com.apple.quarantine /Applications/Clash\\ Verge.app</code></li>
        </ol>

        <h2>三、订阅导入与系统代理设置</h2>
        <ol>
            <li>打开 Clash Verge Rev，进入 <strong>“Profiles (订阅)”</strong> 页面。</li>
            <li>粘贴机场 Clash 订阅链接，点击 <strong>“Import”</strong> 导入。</li>
            <li>在 <strong>“Settings (设置)”</strong> 中开启 <strong>“System Proxy (系统代理)”</strong>。</li>
            <li>在 Mac 屏幕右上角菜单栏找到小图标，可随时快捷切换代理节点或模式。</li>
        </ol>

        <h2>四、开启 TUN 虚拟网卡 (解决 Terminal 终端与软件不走代理)</h2>
        <p>Mac 上的终端命令行 (Brew, Git, npm) 及部分桌面软件默认不遵循系统代理：</p>
        <ol>
            <li>在 Clash Verge 软件设置中开启 <strong>“TUN Mode (TUN 模式)”</strong>。</li>
            <li>系统会弹出 Mac 管理员密码授权窗口，输入解锁密码允许安装 Helper 辅助程序。</li>
            <li>开启 TUN 模式后，终端 `git clone` 及 `npm install` 即可自动享受飞速下载。</li>
        </ol>

        <h2>❓ Mac 用户常见问题 FAQ (8条)</h2>
        <div class="faq-list">
            <div class="faq-item"><div class="faq-question">Q1: 为什么 Mac 提示“无法打开，因为无法确认开发者”？</div><div class="faq-answer">答：请进入 Mac `系统设置 -> 隐私与安全性`，向下滚动找到该软件，点击“仍要打开”即可授权运行。</div></div>
            <div class="faq-item"><div class="faq-question">Q2: Mac 睡眠唤醒后网络出现断连如何解决？</div><div class="faq-answer">答：可在 Clash Verge 设置中关闭“睡眠时保持连接”，或唤醒后右键菜单栏图标点击“Reload Helper”。</div></div>
            <div class="faq-item"><div class="faq-question">Q3: 为什么在 Mac 终端中运行 git clone 依然提示 Connection Refused？</div><div class="faq-answer">答：建议开启 TUN 模式；或在终端中手动执行：`export https_proxy=http://127.0.0.1:7897` 临时指定终端代理。</div></div>
            <div class="faq-item"><div class="faq-question">Q4: Apple Silicon (M1/M2/M3) 误装了 Intel 版本会有什么影响？</div><div class="faq-answer">答：Intel 版本会在 Rosetta 2 转译下运行，增加额外的 CPU 和内存消耗。建议卸载并重装 ARM64 架构版本。</div></div>
            <div class="faq-item"><div class="faq-question">Q5: macOS 上 ClashX 和 Clash Verge Rev 选哪个更好？</div><div class="faq-answer">答：ClashX 已经停止更新维护；Clash Verge Rev 保持活跃更新，且原生集成 Mihomo 内核，体验全面领先。</div></div>
            <div class="faq-item"><div class="faq-question">Q6: 如何设置软件随 Mac 自动开机启动？</div><div class="faq-answer">答：在软件设置中开启“Auto Launch”；或在 Mac `系统设置 -> 通用 -> 登录项` 中添加该应用。</div></div>
            <div class="faq-item"><div class="faq-question">Q7: 为什么开启代理后 Safari 可以上网，但 Chrome 提示无网络连接？</div><div class="faq-answer">答：请检查 Chrome 浏览器是否安装了第三方代理扩展插件，将其设置为“使用系统代理”模式。</div></div>
            <div class="faq-item"><div class="faq-question">Q8: 如何彻底干净卸载 Mac 上的代理客户端？</div><div class="faq-answer">答：退出软件后，在应用程序中将其移入废纸篓，并删除 `~/.config/clash` 或 `~/Library/Application Support/clash-verge` 缓存文件夹。</div></div>
        </div>
        """
    },
    "tutorial-sing-box.html": {
        "title": "Sing-Box 极速上手与配置全指南 (全平台跨时代客户端)",
        "tag": "Sing-Box",
        "desc": "Sing-Box 是新一代通用网络代理架构，支持全协议出入站。本文讲解 Sing-Box 核心特性、GUI 客户端选型、订阅转换与一键配置操作。",
        "content_sections": """
        <h2>一、Sing-Box 跨时代通用架构简介</h2>
        <p><strong>Sing-Box</strong> 被誉为下一代通用代理内核（Universal Proxy Platform），由 SFA 团队打造。它具备极高的代码质量与极强的协议兼容性，原生支持 Shadowsocks、VLESS、Trojan、Hysteria2、TUIC v5、WireGuard 等几乎所有主流加密协议。</p>

        <h2>二、全平台 Sing-Box 客户端推荐与下载</h2>
        <ul>
            <li><strong>Windows / macOS / Linux：</strong> 推荐使用 <code>sing-box GUI</code> 或 <code>GUI.for.Sing-Box</code> 客户端。</li>
            <li><strong>iOS (iPhone/iPad)：</strong> 在 App Store 下载官方客户端 <code>sing-box</code>（免费软件）。</li>
            <li><strong>Android (安卓)：</strong> 前往开源 GitHub 下载 <code>SFA-sing-box-android.apk</code>。</li>
        </ul>

        <h2>三、Sing-Box 订阅导入与配置使用</h2>
        <ol>
            <li>打开 Sing-Box 客户端，进入 <strong>“Profiles / 订阅”</strong> 管理页面。</li>
            <li>点击 <strong>“Add Profile / 添加订阅”</strong>，输入机场提供的 Sing-Box 专属订阅 URL。</li>
            <li>若机场仅提供通用 Clash 订阅，可选择 <strong>“Auto Convert (自动转换格式)”</strong> 功能，客户端会自动将其编译为 Sing-Box 兼容 JSON 配置文件。</li>
            <li>保存并选择该配置，开启代理开关即可享受极致低延迟连接。</li>
        </ol>

        <h2>四、Hysteria2 与 TUIC 协议在 Sing-Box 中的极致压榨</h2>
        <p>Sing-Box 对基于 UDP 的现代 QUIC 协议（Hysteria2 / TUIC）提供了全网最优质的吞吐量优化。在弱网或恶劣公网环境下，Sing-Box 能够自动实施拥塞控制，实现秒开 4K/8K 视频体验。</p>

        <h2>❓ Sing-Box 用户常见问题 FAQ (8条)</h2>
        <div class="faq-list">
            <div class="faq-item"><div class="faq-question">Q1: Sing-Box 和 Clash 相比有什么优势？</div><div class="faq-answer">答：Sing-Box 原生支持 Hysteria2、TUIC 等协议，内存占用更小，分流性能更高，且 iOS 官方版完全免费。</div></div>
            <div class="faq-item"><div class="faq-question">Q2: 为什么导入 Clash 订阅链接提示 JSON 语法错误？</div><div class="faq-answer">答：Clash 采用 YAML 语法，Sing-Box 采用 JSON 语法。请使用支持订阅转换的 Sing-Box GUI 客户端，或在机场后台获取 Sing-Box 专用订阅。</div></div>
            <div class="faq-item"><div class="faq-question">Q3: iOS 版 Sing-Box 需要外区 Apple ID 才能下载吗？</div><div class="faq-answer">答：Sing-Box 在大部分区域 App Store（包括港区、美区等）均可免费下载，无需付费。</div></div>
            <div class="faq-item"><div class="faq-question">Q4: Sing-Box 的 TUN 模式如何开启？</div><div class="faq-answer">答：在客户端配置面板中找到 `Inbound (入站设置)`，将模式切换为 `TUN` 并给予管理员/VPN 权限即可。</div></div>
            <div class="faq-item"><div class="faq-question">Q5: 开启 Sing-Box 后本地局域网设备无法访问怎么解决？</div><div class="faq-answer">答：请在规则配置文件中确保包含 `geoip:private` 直连规则，即可放行本地打印机及 NAS 设备。</div></div>
            <div class="faq-item"><div class="faq-question">Q6: 为什么使用 Hysteria2 节点时提示 UDP 被运营商 QOS 封锁？</div><div class="faq-answer">答：部分地区移动或电信宽带会对 UDP 流量限速。可在节点设置中降低 `up_mbps / down_mbps` 突发上限，或切换至 TCP 类的 IEPL 专线节点。</div></div>
            <div class="faq-item"><div class="faq-question">Q7: Sing-Box 如何查看详细的错误日志排查故障？</div><div class="faq-answer">答：在客户端界面切换至 `Log (日志)` 页面，把日志级别设置为 `Debug` 或 `Info`，即可实时查看 TLS 握手与连接报错。</div></div>
            <div class="faq-item"><div class="faq-question">Q8: Sing-Box 配置文件支持热加载无需重启软件吗？</div><div class="faq-answer">答：支持。只要在 GUI 客户端中修改或重新勾选 Profile，Sing-Box 即可完成无缝热重载，不会影响已有长连接。</div></div>
        </div>
        """
    }
}

html_template = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | 闪电机场评测</title>
    <meta name="description" content="{desc}">
    <link rel="stylesheet" href="css/style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        .tutorial-article {{
            background: #ffffff;
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 32px;
            box-shadow: var(--shadow-sm);
            margin-bottom: 30px;
        }}
        .tutorial-article h1 {{
            font-size: 1.8rem;
            line-height: 1.35;
            margin-bottom: 16px;
            color: var(--text-primary);
        }}
        .article-meta-bar {{
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
            align-items: center;
            font-size: 0.85rem;
            color: var(--text-muted);
            padding-bottom: 20px;
            border-bottom: 1px solid var(--border);
            margin-bottom: 24px;
        }}
        .tag-badge {{
            padding: 3px 10px;
            border-radius: 4px;
            font-weight: 600;
            font-size: 0.775rem;
        }}
        .tag-badge.blue {{ background: #eff6ff; color: var(--primary); border: 1px solid #bfdbfe; }}
        .tag-badge.green {{ background: #ecfdf5; color: var(--accent-green-dark); border: 1px solid #a7f3d0; }}

        .callout-box {{
            background: #f8fafc;
            border-left: 4px solid var(--primary);
            border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
            padding: 18px 20px;
            margin: 24px 0;
            font-size: 0.925rem;
            color: var(--text-secondary);
        }}

        .article-body h2 {{
            font-size: 1.35rem;
            margin: 32px 0 16px;
            color: var(--text-primary);
            padding-bottom: 8px;
            border-bottom: 1px solid var(--border);
        }}
        .article-body h3 {{
            font-size: 1.1rem;
            margin: 20px 0 12px;
            color: var(--text-primary);
        }}
        .article-body p {{
            font-size: 0.95rem;
            color: var(--text-secondary);
            line-height: 1.75;
            margin-bottom: 16px;
        }}
        .article-body ul, .article-body ol {{
            margin: 0 0 20px 20px;
            color: var(--text-secondary);
            font-size: 0.95rem;
            line-height: 1.8;
        }}
        .article-body li {{ margin-bottom: 8px; }}

        .faq-item {{
            background: var(--bg-secondary);
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
            padding: 16px 20px;
            margin-bottom: 12px;
        }}
        .faq-question {{
            font-weight: 700;
            font-size: 0.975rem;
            color: var(--text-primary);
            margin-bottom: 8px;
        }}
        .faq-answer {{
            font-size: 0.9rem;
            color: var(--text-secondary);
            line-height: 1.6;
        }}
    </style>
</head>
<body>
    <header class="navbar">
        <div class="container navbar-container">
            <a href="index.html" class="logo">
                <span class="logo-icon">⚡</span>
                <span class="logo-text">闪电机场评测</span>
            </a>
            <nav class="nav-links">
                <a href="index.html" class="nav-item">首页</a>
                <a href="rankings.html" class="nav-item">机场排行榜</a>
                <a href="reviews.html" class="nav-item">深度测评</a>
                <a href="tutorials.html" class="nav-item active">新手教程</a>
                <a href="speedtest.html" class="nav-item">实时测速</a>
                <a href="coupons.html" class="nav-item">优惠福利</a>
                <a href="about.html" class="nav-item">关于我们</a>
            </nav>
            <div class="nav-actions">
                <a href="rankings.html" class="btn btn-primary">Top 10 推荐</a>
            </div>
        </div>
    </header>

    <main class="container section">
        <article class="tutorial-article">
            <h1>{title}</h1>
            
            <div class="article-meta-bar">
                <span class="tag-badge blue">{tag}</span>
                <span class="tag-badge green">2026年最新配置</span>
                <span>更新于 2026-10-04</span>
                <span>阅读时间：约 10 分钟</span>
            </div>

            <div class="callout-box">
                <strong>💡 教程摘要与学习指南：</strong><br>
                {desc} 建议配合稳定高速的专线机场节点使用，以获得最佳网络体验。
            </div>

            <div class="article-body">
                {content_sections}

                <div style="margin-top: 40px; text-align: center; border-top: 1px solid var(--border); padding-top: 24px;">
                    <a href="rankings.html" class="btn btn-lg btn-primary">搭配优质专线机场使用 &rarr;</a>
                    <a href="tutorials.html" class="btn btn-lg btn-outline" style="margin-left: 12px;">返回教程总览</a>
                </div>
            </div>
        </article>
    </main>

    <footer class="footer">
        <div class="container footer-container">
            <div class="footer-col brand-col">
                <a href="index.html" class="logo"><span class="logo-icon">⚡</span><span class="logo-text">闪电机场评测</span></a>
                <p>客观、独立、深度的网络加速与机场服务测评平台。</p>
                <p class="copyright">© 2026 闪电机场评测. All rights reserved.</p>
            </div>
            <div class="footer-col">
                <h4>导航快捷链接</h4>
                <ul>
                    <li><a href="index.html">网站首页</a></li>
                    <li><a href="rankings.html">机场排行榜</a></li>
                    <li><a href="tutorials.html">客户端教程指南</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>特色专题</h4>
                <ul>
                    <li><a href="reviews.html">深度测评报告</a></li>
                    <li><a href="speedtest.html">实时专线测速</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>关于我们</h4>
                <ul>
                    <li><a href="about.html">测评标准与声明</a></li>
                </ul>
            </div>
        </div>
    </footer>
</body>
</html>
"""

for fname, data in articles.items():
    file_path = os.path.join(base_dir, fname)
    html_content = html_template.format(
        title=data["title"],
        tag=data["tag"],
        desc=data["desc"],
        content_sections=data["content_sections"]
    )
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Generated {fname} successfully.")

