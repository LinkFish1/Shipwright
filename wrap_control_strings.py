import io, sys, traceback

try:

    files = [
    r"e:\Shipwright-wind-waker-style-cel-shading\soh\soh\Enhancements\controls\SohInputEditorWindow.cpp",
    r"e:\Shipwright-wind-waker-style-cel-shading\soh\soh\Enhancements\controls\InputViewer.cpp",
]

# (old_substring, new_substring) -- exact static UI strings only.
repls = [
    # CollapsingHeader labels (both flagged and unflagged forms share the prefix)
    ('ImGui::CollapsingHeader("Buttons"',
     'ImGui::CollapsingHeader(StringHelper::Translate("Buttons").c_str()'),
    ('ImGui::CollapsingHeader("Analog Stick"',
     'ImGui::CollapsingHeader(StringHelper::Translate("Analog Stick").c_str()'),
    ('ImGui::CollapsingHeader("Rumble")',
     'ImGui::CollapsingHeader(StringHelper::Translate("Rumble").c_str()'),
    ('ImGui::CollapsingHeader("Gyro")',
     'ImGui::CollapsingHeader(StringHelper::Translate("Gyro").c_str()'),
    ('ImGui::CollapsingHeader("LEDs")',
     'ImGui::CollapsingHeader(StringHelper::Translate("LEDs").c_str()'),
    ('ImGui::CollapsingHeader("Additional (\\"Right\\") Stick")',
     'ImGui::CollapsingHeader(StringHelper::Translate("Additional (\\"Right\\") Stick").c_str()'),

    # TreeNode "Analog Stick Options##%d"
    ('StringHelper::Sprintf("Analog Stick Options##%d", id)',
     'StringHelper::Sprintf((StringHelper::Translate("Analog Stick Options") + "##%d").c_str(), id)'),

    # ImGui::Text(...) static labels
    ('ImGui::Text("Sensitivity:");',
     'ImGui::Text(StringHelper::Translate("Sensitivity:").c_str());'),
    ('ImGui::Text("Deadzone:");',
     'ImGui::Text(StringHelper::Translate("Deadzone:").c_str());'),
    ('ImGui::Text("Notch Snap Angle:");',
     'ImGui::Text(StringHelper::Translate("Notch Snap Angle:").c_str());'),
    ('ImGui::Text("Small Motor Intensity:");',
     'ImGui::Text(StringHelper::Translate("Small Motor Intensity:").c_str());'),
    ('ImGui::Text("Large Motor Intensity:");',
     'ImGui::Text(StringHelper::Translate("Large Motor Intensity:").c_str());'),
    ('ImGui::Text("LED Color:");',
     'ImGui::Text(StringHelper::Translate("LED Color:").c_str());'),
    ('ImGui::Text("Custom Color");',
     'ImGui::Text(StringHelper::Translate("Custom Color").c_str());'),
    ('ImGui::Text("Press any button\\nor move any axis\\nto add rumble device");',
     'ImGui::Text(StringHelper::Translate("Press any button\\nor move any axis\\nto add rumble device").c_str());'),
    ('ImGui::Text("Press any button\\nor move any axis\\nto add LED device");',
     'ImGui::Text(StringHelper::Translate("Press any button\\nor move any axis\\nto add LED device").c_str());'),
    ('ImGui::Text("Press any button\\nor move any axis\\nto add gyro device");',
     'ImGui::Text(StringHelper::Translate("Press any button\\nor move any axis\\nto add gyro device").c_str());'),

    # BulletText static labels
    ('ImGui::BulletText("Add LED device");',
     'ImGui::BulletText(StringHelper::Translate("Add LED device").c_str());'),
    ('ImGui::BulletText("Add gyro device");',
     'ImGui::BulletText(StringHelper::Translate("Add gyro device").c_str());'),
    ('ImGui::BulletText("Add rumble device");',
     'ImGui::BulletText(StringHelper::Translate("Add rumble device").c_str());'),

    # Button static label
    ('ImGui::Button("Recalibrate")',
     'ImGui::Button(StringHelper::Translate("Recalibrate").c_str())'),
]

for f in files:
    with io.open(f, 'r', encoding='utf-8') as fh:
        src = fh.read()
    total = 0
    for old, new in repls:
        cnt = src.count(old)
        if cnt:
            src = src.replace(old, new)
            total += cnt
    with io.open(f, 'w', encoding='utf-8') as fh:
        fh.write(src)
    print(f"{f.split('\\')[-1]}: {total} replacements")
