# 项目长期记忆 (Shipwright wind-waker cel-shading 中文本地化)

## UIWidgets 翻译机制（重要）
- `soh/soh/SohGui/UIWidgets.cpp` 中 `Tooltip(const char*)` 在显示时调用 `WrappedText(text)`，而 `WrappedText` 内部已执行 `StringHelper::Translate(text)` 查表翻译。
- 结论：**所有 tooltip 文本在渲染时已被自动翻译** → 给 tooltip 字符串包 `StringHelper::Translate(...)` 是**冗余的**，且可能因 MSVC 对含 `\n`/`\"`/`(` 字符串字面量的解析怪病引发 C2143。
- 相反：**label（控件标签）经 `ImGui::Text(label)` 直接渲染，无自动翻译**，所以 label 的 `StringHelper::Translate(...).c_str()` 包裹是**必要的**，不可移除。
- 中文化准则：仅包裹未被自动翻译的 label；tooltip 保持英文原串（作为翻译表 key），由 WrappedText 自动翻译。

## MSVC 构建排查经验
- 本项目用 `run_build.ps1` 构建：`cmake --build build/x64 --config Release --target soh > build_log10.txt 2>&1`，日志末尾追加 `BUILD_RC_<exitcode>`。成功为 `BUILD_RC_0`。
- C2143 “缺少’)’(在’;’的前面)” 常表现为**级联误报**：真正根因往往是前面某处 `CVarCheckbox(` / `Options(` / `CVarCombobox(` 调用**少了一个闭合 `)`**（应为 `));` 而非 `);`）。
- 对照同级能编译的调用（如 `...c_str()));`）即可定位缺失的右括号。
- 用户约定：仅当明确说“编译”时才执行构建；指出未翻译文本时只改翻译表/包裹代码，不自动编译。
