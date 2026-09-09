# 戴南.cn 产业信息门户

中国不锈钢名镇（江苏兴化戴南）产业信息单页门户，纯静态、零依赖，托管于 GitHub Pages。

- 仓库：https://github.com/mfujun2025/dainan
- 自定义域名：戴南.cn（国际编码 `xn--6krt95a.cn`）
- 仓库需包含：`index.html`（站点）、`CNAME`（域名绑定）

## 部署三步

### 第 1 步：推送到 GitHub（已完成方式记录）

```bash
cd dainan-site
git remote add origin https://github.com/mfujun2025/dainan.git
git push -u origin main
```

### 第 2 步：开启 GitHub Pages 并绑定域名

1. 仓库 → Settings → Pages（左侧栏）
2. Source 选 **Deploy from a branch**，Branch 选 **main / root** → Save
3. 稍等 1-2 分钟，出现 `https://mfujun2025.github.io/dainan/` 即部署成功
4. 同页 Custom domain 填 **`xn--6krt95a.cn`** → Save（仓库里的 CNAME 文件内容须一致）
5. 证书签发成功后勾选 **Enforce HTTPS**

### 第 3 步：设置 DNS（域名注册商控制台）

| 记录类型 | 主机记录 | 记录值 |
|---|---|---|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | `mfujun2025.github.io` |

说明：
- 部分注册商控制台里域名会显示为 `xn--6krt95a.cn`，与 `戴南.cn` 是同一个域名，属正常现象。
- DNS 生效需要几分钟到几小时。
- 解析到 GitHub Pages（境外）无需 ICP 备案即可访问；今后若迁移国内云并要求备案，另议。

## 验证

浏览器直接输入 `戴南.cn`（或 `xn--6krt95a.cn`），能看到站点即成功。
