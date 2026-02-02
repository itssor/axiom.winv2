# Changelog

## [1.5.0]

- Config: save/load round-trips everything (Color3, Enum serialization; keybind conflict check on load; empty config dropdown handled).
- Config: keybind conflict warnings when setting keybinds and after loading a config.
- Config: AxiomResetSection now uses deepClone so nested sections (Aimbot, Visuals, etc.) reset correctly.
- Skeleton ESP: full right leg (14 segments); R6 fallback; optional smoothing.
- ESP: configurable outline for all ESP types (2D box, 3D box, skeleton, tracer, head dot); tracer and head dot use outline layer + gradient color.
- Gradients: UseGradient + GradientColor for 2D/3D box, skeleton, tracer, head dot, text, chams, center dot, offscreen arrow; UI toggles and color pickers in Outline & Smooth.
- Crosshair: Axiom.win crosshair (dot/line/cross, length, thickness, dot mode, spin, gradient, outline); dot style has outline circle; axiom.win text below (color + gradient).
- Customizability: FOV fill/color, outline options, more sliders and toggles across Aimbot, Visuals, Misc.
- Maintenance: single loader URL constant in core.lua; version bump; R6 skeleton; skeleton smoothing option.
- Bug fixes: config dropdown when no configs; AxiomResetSection deep clone; validateConfig revives Color3/Enum from JSON; 3D box outline visibility when Outline off.

## [1.4.0]

- Private revision baseline (aimbot, visuals, movement, MM2, configs, watermark, Cascade UI).
