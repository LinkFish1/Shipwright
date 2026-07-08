#pragma once

#include <string>

namespace SohGui {

// Registers the Simplified-Chinese UI translator with libultraship's StringHelper.
// Call once during menu initialization. The translator reads the
// "gSohGui.Menu.InterfaceLanguage" cvar ("English" / "简体中文") on every call,
// so switching the language in the settings menu takes effect immediately.
void RegisterLocalization();

} // namespace SohGui
