# Mapping of full concatenated English UI strings (exactly as they appear in code)
# to Simplified Chinese. Consumed by apply_translations.py.
TRANSLATIONS = {
    # ---- SohMenuDevTools.cpp ----
    'Enables Debug Mode, allowing you to select maps with L + R + Z, noclip with L + D-pad Right, and open the debug menu with L on the pause screen.':
        '启用调试模式，允许你用 L + R + Z 选择地图，用 L + 方向键右键穿墙，并在暂停界面用 L 打开调试菜单。',
    'Enables Skulltula Debug, when moving the cursor in the menu above various map icons (boss key, compass, map screen locations, etc.) will set the GS bits in that area.\nUSE WITH CAUTION AS IT DOES NOT UPDATE THE GS COUNT!':
        '启用黄金骷髅调试：在菜单中将光标移到各种地图图标（头目钥匙、罗盘、地图屏幕位置等）上方时，会设置该区域的黄金骷髅位。\n注意：它不会更新黄金骷髅计数，请谨慎使用！',
    'This allows you to advance through the game one frame at a time on command. To advance a frame, hold Z and tap R on the second controller. Holding Z and R will advance a frame every half second. You can also use the buttons below.':
        '允许你按需逐帧推进游戏。要推进一帧，在第二手柄上按住 Z 并轻点 R。按住 Z 和 R 会每半秒推进一帧。你也可以使用下方的按钮。',

    # ---- SohMenuEnhancements.cpp ----
    "Pierre appears when an Ocarina is pulled out. Requires learning the Scarecrow's Song first.\nWithout the randomizer option \"Skip Scarecrow's Song\" enabled for a seed, this still requires you to teach the scarecrow the song as both ages before summoning.":
        '拔出陶笛时皮埃尔会出现。需要先学会斯卡洛的歌。\n若随机化种子未启用“跳过斯卡洛之歌”选项，仍需要你在两个年龄段都把歌教给斯卡洛才能召唤。',
    'Stops the game from freezing the player when picking up Gold Skulltula Tokens. Does not apply in randomizer savefiles.':
        '防止拾取黄金骷髅代币时游戏冻结玩家。不适用于随机化存档。',
    'Disables the fixed camera in maps that use 2D pre-rendered backgrounds. Enable this when using a mod that implements 3D backdrops for these areas.\nRequires Scene Change to alter.':
        '在使用 2D 预渲染背景的地图中禁用固定相机。使用为这些区域实现 3D 背景的模组时启用。\n需要切换场景才能生效。',
    'Scales all of the Adult Equipment, as well as moving some a bit, to fit on Child Link better. May not work properly with some mods.':
        '缩放所有成人装备，并略微移动部分装备，使其更贴合儿童林克。某些模组下可能工作不正常。',
    'The Kokiri are mystical beings that fade into view when approached. Enabling this will remove their draw distance.':
        '科克里是神秘生物，靠近时才会显现。启用此项将移除它们的显示距离限制。',
    'Exclude Actors that are useful for Glitches from the extended culling ranges. Some actors may still draw in the extended ranges, but will not "update" so that certain glitches that leverage the original culling requirements will still work.\n\nThe following actors are excluded:\n - White Clothed Gerudos\n - King Zora\n - Gossip Stones\n - Boulders\n - Blue Warps\n - Darunia\n - Gold Skulltulas':
        '将有助于故障的演员排除在扩展剔除范围之外。部分演员仍可能在扩展范围内绘制，但不会“更新”，从而让某些依赖原始剔除要求的故障仍然可用。\n\n排除的演员如下：\n - 白衣盖鲁多\n - 佐拉之王\n -  gossip 石\n - 巨石\n - 蓝色传送点\n - 达鲁尼亚\n - 黄金骷髅',
    'Equip items and equipment on the D-pad. If used with "D-pad on Pause Screen", you must hold C-Up to equip instead of navigate.':
        '在十字键上装备物品与装备。若与“暂停界面十字键”配合使用，必须按住 C-Up 来装备而非导航。',
    "Allows unequipping items from C-Buttons/D-pad by hovering over an equipped item and pressing the button it's equipped to.":
        '允许将光标悬停在已装备物品上，并按下其装备到的按钮，从而卸下 C 按钮/十字键上的物品。',
    'Allows Strength to be toggled on and off by pressing A on the Strength Upgrade in the Equipment Subscreen of the Pause Menu. This allows performing some glitches that require the player to not have Strength.':
        '允许在暂停菜单装备子界面中，对力量升级按 A 来开关力量。这允许执行某些要求玩家没有力量的故障。',
    'Stops masks from automatically unequipping on certain situations:\n- When entering a new scene\n- When not in any C-Button or the D-pad\n- When saving and quitting\n- When dying\n- When traveling through time (if "Masks Equippable as Adult" is activated)':
        '阻止面具在特定情况下自动卸下：\n- 进入新场景时\n- 不在任何 C 按钮或十字键上时\n- 保存并退出时\n- 死亡时\n- 穿越时间时（若启用“成人可装备面具”）',
    'After completing the mask trading sub-quest, press A and any direction on the mask slot to change masks.':
        '完成面具交易支线任务后，在面具槽按 A 加任意方向即可切换面具。',
    'Allows you to control a Bombchu after dropping it.\nControl Stick: Steer\nB: Detonate\nA: Quit Control':
        '允许你在丢出炸弹鼠后控制它。\n控制摇杆：转向\nB：引爆\nA：退出控制',
    'Make Deku Nuts explode Bombs, similar to how they interact with Bombchus. This does not affect Bomb Flowers.':
        '让德库坚果引爆炸弹，类似于它们与炸弹鼠的互动方式。不影响炸弹花。',
    "Explosions are now a static size, like in Majora's Mask and OoT3D. Makes Bombchu hovering much easier.":
        '爆炸现在为固定大小，如同《姆吉拉的面具》和 OoT3D 中一样。使炸弹鼠悬停更容易。',
    'Bombchus do not sell out when bought, and a 10 pack of Bombchus costs 99 rupees instead of 100.':
        '炸弹鼠购买后不会售罄，且 10 个装炸弹鼠售价 99 卢比而非 100。',
    "Allow the Bow and Magic Arrows to be equipped at the same time on different slots. NOTE: This will disable the behavior of the 'Equip Dupe' glitch.":
        '允许弓与魔法箭同时装备在不同槽位。注意：这将禁用“装备复制”故障的行为。',
    "Allows Child Link to use a Bow with Arrows.\nAllows Adult Link to use a Slingshot with Seeds.\n\nRequires glitches or the 'Timeless Equipment' cheat to equip.":
        '允许儿童林克使用弓与箭。\n允许成人林克使用弹弓与种子。\n\n需要故障或“ timeless 装备”作弊来装备。',
    'Aiming with a Bow or Slingshot will display a reticle as with the Hookshot when the projectile is ready to fire.':
        '用弓或弹弓瞄准时，在投射物准备发射时会显示准星，如同钩绳一样。',
    'Allows cycling between different arrow types (Normal, Fire, Ice, Light) while aiming the bow. Press the R button to cycle to the next available arrow type. Only works when aiming and only cycles to arrow types you own with sufficient magic.':
        '允许在瞄准弓时在不同类型的箭（普通、火、冰、光）之间循环。按 R 键循环到下一个可用箭型。仅在瞄准时有效，且只循环到你拥有足够魔法的箭型。',
    "Instantly return the Boomerang to Link by pressing its item button while it's in the air.":
        '在回旋镖飞行中按下其物品按钮，可立即将其收回林克手中。',
    'Helps FW persist between ages, gives Child and Adult separate FW points, and can be used in more places.':
        '帮助 FW（Farore 的风）在年龄间持续存在，为儿童与成人分别提供 FW 点，并可在更多地方使用。',
    "Fixes kokiri animation state to match their text state when getting Zelda's Letter before Kokiri Emerald.":
        '修复在获得科克里翡翠之前取得塞尔达的信时，科克里动画状态与其文本状态不匹配的问题。',
    'Fixes the two raised floor switches, the one in Forest Temple Basement and the one at the top of Fire Temple. This will lower them, making activating them easier.':
        '修复森林神殿地下与火之神殿顶部的两个凸起地板开关。这将降低它们，使激活更容易。',
    "Fixes one Zora's dialogue giving a hint about bringing Ruto's Letter to King Zora to properly occur before moving King Zora rather than after.":
        '修复某佐拉对话中关于将露托的信带给佐拉之王的提示，使其正确地发生在移动佐拉之王之前而非之后。',
    'Causes respawning enemies, like Stalchildren, to appear on land near bodies of water. Fixes an incorrect calculation that acted like water underneath ground was above it.':
        '使复活的敌人（如斯塔童）出现在水体附近的陆地上。修复了将地下水体误判为在其上方的不正确计算。',
    'Forces Goron City doors open if you somehow complete Fire Temple without talking to Goron Link  and receiving the Goron Tunic.':
        '若你以某种方式在未与哥隆林克对话并获得哥隆外衣的情况下完成了火之神殿，则强制打开哥隆城大门。',
    "Prevents the Forest Stage Deku Nut upgrade from becoming unobtainable after receiving the Poacher's Saw.":
        '防止森林舞台德库坚果升级在获得偷猎者锯后出现无法获得的情况。',
    'Fixes camera slightly drifting to the left when standing still due to a math error. May impact certain glitches.':
        '修复因数学错误导致静止站立时相机轻微向左漂移的问题。可能影响某些故障。',
    'Fixes camera getting stuck on collision when standing still. Also fixes slight shift back in camera when Link stops moving. May impact certain glitches.':
        '修复静止站立时相机卡在碰撞上的问题。同时修复林克停止移动时相机轻微回移的问题。可能影响某些故障。',
    'Fixes camera swing rate when the player falls off a ledge and the camera swings around. May impact certain glitches.':
        '修复玩家从边缘掉落且相机绕转时的相机摆动速率问题。可能影响某些故障。',
    'Removes the Dungeon Entrance icon on the top-left corner of the screen when no dungeon is present on the current map.':
        '当当前地图没有地牢时，移除屏幕左上角的地牢入口图标。',
    'Re-Enables the two-handed idle animation, a seemingly finished animation that was disabled on accident in the original game.':
        '重新启用双手待机动画——一个在原版游戏中被意外禁用的、看似已完成的动画。',
    "Prevent the Gerudo Warrior's clothes changing color when changing Link's tunic or using bombs in front of her.":
        '防止在更换林克外衣或在其面前使用炸弹时，盖鲁多战士的衣物变色。',
    'Adds 5 higher pitches for the Silver Rupee Jingle for the rooms with more than 5 Silver Rupees. Only relevant for playthroughs involving Master Quest Dungeons.':
        '为含超过 5 枚银卢比的房间，银卢比铃声增加 5 个更高音。仅与涉及大师任务地牢的游玩相关。',
    'Restore a bug from NTSC 1.0 that allows putting away an item without an animation and performing Putaway Ocarina Items.':
        '还原 NTSC 1.0 中的一个漏洞，允许无动画地收起物品并执行收起陶笛物品。',
    'Restores a bug from NTSC 1.0/1.1 that allows you to obtain the eyeball frog from King Zora instead of the Zora Tunic by Holding Shield.':
        '还原 NTSC 1.0/1.1 中的一个漏洞，允许你通过按住盾牌从佐拉之王处获得眼球蛙而非佐拉外衣。',
    'Restores the wider range of certain shutter doors from NTSC 1.0.\nNotably affects Jabu-Jabu and boss doors.':
        '还原 NTSC 1.0 中某些卷帘门的更宽范围。\n显著影响 Jabu-Jabu 与头目门。',
    'When you lose 4 quarters of a heart you will permanently lose that Heart Container.\n\nDisabling this after the fact will restore your Heart Containers.':
        '当你失去 4 分之 1 颗心时，将永久失去该红心容器。\n\n事后禁用此项将恢复你的红心容器。',
    'Disables Heart Drops, but not Heart Placements, like from a Deku Scrub running off.\nThis simulates Hero Mode from other games in the series.':
        '禁用红心掉落，但不禁用心形放置，例如德库树精逃跑时。\n这模拟了本系列其他游戏中的英雄模式。',
    "Always win the Heart Piece/Purple Rupee on the first dig in Dampe's Grave Digging game. In a Randomizer file, this defaults to on if this enhancement has never been changed.":
        '在达姆佩挖坟游戏中，首次挖掘必定获得红心碎片/紫色卢比。在随机化文件中，若从未更改此增强，则默认开启。',
    'Every fish in the Fishing Pond will always be a Hyrule Loach.\n\nNOTE: This requires reloading the area.':
        '钓鱼池中的每条鱼都将是海拉尔泥鳅。\n\n注意：这需要重新加载区域。',
    'Allows Link to bounce off walls when linear velocity is high enough, this is relevant when frequently being knocked back by traps, CC, or in Anchor.':
        '当线速度足够高时，允许林克从墙壁弹开，这在频繁被陷阱、CC 或 Anchor 击退时相关。',
    'Enables Ivan the Fairy upon the next map change. Player 2 can control Ivan and press the C-Buttons to use items and mess with Player 1!':
        '在下一次地图切换时启用精灵 Ivan。玩家 2 可控制 Ivan 并按下 C 按钮使用物品、干扰玩家 1！',
    'Changes Heart Piece and Heart Container functionality.\n\n - Each Heart Container or full Heart Piece reduces Link\'s Hearts by 1.\n - Can be enabled retroactively after a File has already started.':
        '改变红心碎片与红心容器的功能。\n\n - 每个红心容器或完整红心碎片使林克的心减少 1。\n - 可在文件已开始后进行追溯启用。',
    'Allows any item to be equipped, regardless of age.\nAlso allows child to use adult strength upgrades.':
        '允许装备任何物品，不受年龄限制。\n也允许儿童使用成人力量升级。',
    'Keese and Guay no longer target you and simply ignore you as if you were wearing the Skull Mask.':
        '凯斯与瓜伊不再以你为目标，而是像你戴着骷髅面具一样直接忽略你。',
    'Passive Infinite Sword Glitch\nIt makes your sword\'s swing effect and hitbox stay active indefinitely.':
        '被动无限剑故障\n它使你的剑的挥动效果与碰撞箱无限期保持激活。',

    # ---- SohMenuNetwork.cpp ----
    'Sail is a networking protocol designed to facilitate remote control of the Ship of Harkinian client. It is intended to be utilized alongside a Sail server, for which we provide a few straightforward implementations on our GitHub. The current implementations available allow integration with Twitch chat and SAMMI Bot, feel free to contribute your own!\n\nClick this button to copy the link to the Sail Github page to your clipboard.':
        'Sail 是一种网络协议，旨在便于远程控制 Ship of Harkinian 客户端。它 intended 与 Sail 服务器配合使用，我们在 GitHub 上提供了一些简单实现。当前可用的实现允许与 Twitch 聊天和 SAMMI Bot 集成，欢迎贡献你自己的实现！\n\n点击此按钮将 Sail GitHub 页面链接复制到剪贴板。',
    'Crowd Control is a platform that allows viewers to interact with a streamer\'s game in real time.\n\nPlease head over to www.crowdcontrol.live for more information!':
        'Crowd Control 是一个允许观众实时与主播游戏互动的平台。\n\n请前往 www.crowdcontrol.live 了解更多信息！',
    'Enemies spawned by CrowdControl won\'t be considered for "clear enemy rooms", so they don\'t need to be killed to complete these rooms.':
        '由 CrowdControl 生成的敌人不计入“清空敌人房间”，因此无需击杀它们即可完成这些房间。',

    # ---- SohMenuRandomizer.cpp ----
    'Play unique fanfares when obtaining quest items (medallions/stones/songs). Note that these fanfares can be longer than usual.':
        '获得任务物品（勋章/石头/歌曲）时播放独特的号角声。注意这些号角声可能比平常更长。',
    'Displays a "Mystery Item" model in place of any freestanding/GS/shop items that were shuffled, and replaces item names for them and scrubs and merchants, regardless of hint settings, so you never know what you\'re getting.':
        '为任何被洗牌的静止/黄金骷髅/商店物品显示“神秘物品”模型，并替换它们以及灌木与商人的物品名称，无论提示设置如何，因此你永远不知道会得到什么。',
    "When shuffling boss souls, they'll appear as a simpler model instead of showing the boss' models.This might make boss souls more distinguishable from a distance, and can help with performance.":
        '随机化头目灵魂时，它们会显示为更简单的模型，而非显示头目模型。这可能使头目灵魂在远处更易区分，并有助于性能。',

    # ---- SohMenuWindWakerStyle.cpp ----
    'Draws a debug ray from each actor for every candidate light (coloured by the light, longer when stronger), a cyan range ring around each point light, and a bold magenta needle down the chosen key light, so you can see which light is winning and where the key points.':
        '为每个候选光源从每个演员绘制一条调试射线（按光源着色，越强越长），为每个点光源绘制青色范围环，并为所选关键光源绘制粗洋红色指针，以便你查看哪个光源获胜以及关键点指向何处。',
    'Renders every cel-shaded object as flat white on the lit side and flat black in shadow (the texture is discarded), so it is obvious which draws are being relit — handy for confirming whether large surfaces like water or lava are getting relit.':
        '将每个卡通着色物体在受光面渲染为纯白、在阴影中为纯黑（丢弃纹理），从而清楚地看出哪些绘制正在被重新光照——便于确认水或熔岩等大型表面是否正在被重新光照。',
    'Overlays a translucent faceted shell of each light\'s icosphere — the volume used for its cast pool — tinted by the light, so you can see where the pools are, their size, and their spin. (The renderer has no line primitive, so this is a shell rather than a true wireframe.)':
        '为每个光源的二十面体覆盖一层半透明多面外壳——即其投射池所用的体积——按光源着色，以便你查看池的位置、大小与旋转。（渲染器没有线图元，因此这是外壳而非真正的线框。）',
    'Draws the actual 3D shadow volume translucently so you can see its shape: black top/bottom caps, blue side walls. The ground inside this volume is what gets shadowed.':
        '半透明地绘制实际 3D 阴影体积，以便你查看其形状：黑色顶/底盖、蓝色侧壁。此体积内的地面即为被阴影遮挡的部分。',
}
