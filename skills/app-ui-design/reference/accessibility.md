# Mobile Accessibility Guidelines

WCAG 2.2 AA compliance checklist for mobile app design.

## POUR Principles

### Perceivable
Content must be presentable in ways users can perceive.

### Operable
Interface must be operable by all users.

### Understandable
Information and UI must be understandable.

### Robust
Content must work with assistive technologies.

---

## Visual Accessibility

### Color Contrast

| Element | Minimum Ratio | Tool |
|---------|---------------|------|
| Normal text (<18pt) | 4.5:1 | WebAIM Contrast Checker |
| Large text (≥18pt or 14pt bold) | 3:1 | Stark (Figma plugin) |
| UI components | 3:1 | Color Oracle |
| Focus indicators | 3:1 | - |

```markdown
## Contrast Examples

Good ✓
├── Black (#000000) on White (#FFFFFF) = 21:1
├── Dark Gray (#333333) on White (#FFFFFF) = 12.6:1
└── Blue (#0066CC) on White (#FFFFFF) = 5.3:1

Bad ✗
├── Light Gray (#999999) on White (#FFFFFF) = 2.8:1
├── Yellow (#FFFF00) on White (#FFFFFF) = 1.07:1
└── Green (#00FF00) on White (#FFFFFF) = 1.37:1
```

### Color Independence

Never use color as the only means of conveying information.

```markdown
❌ Bad:
"Fields marked in red are required"
(Users with colorblindness can't identify)

✅ Good:
"Required fields are marked with *"
+ Red color for additional emphasis
+ Error icon next to invalid fields
```

### Text Sizing

| Platform | Minimum | Recommended | Support |
|----------|---------|-------------|---------|
| iOS | 11pt | 17pt body | Dynamic Type |
| Android | 12sp | 16sp body | Font Scaling |

```markdown
## Font Scaling Support

Must support:
├── 100% (default)
├── 150% (medium scaling)
├── 200% (large scaling)
└── 250%+ (extra large, if possible)

All content must remain readable and usable at 200% scaling.
```

### Focus Indicators

```markdown
Requirements:
- Visible focus ring on all interactive elements
- Minimum 2px width
- 3:1 contrast against adjacent colors
- Consistent across app

Example CSS-like styling:
focus: {
  outline: 2px solid #0066CC
  outlineOffset: 2px
}
```

---

## Motor Accessibility

### Touch Targets

| Platform | Minimum Size | Recommended |
|----------|--------------|-------------|
| iOS | 44×44pt | 48×48pt |
| Android | 48×48dp | 48×48dp |
| Web (mobile) | 44×44px | 48×48px |

```markdown
## Target Spacing

Minimum gap between targets: 8px
Recommended gap: 12-16px

┌────────────────────────────────────────┐
│                                        │
│  ┌─────────┐   8px+   ┌─────────┐     │
│  │  44pt   │   gap    │  44pt   │     │
│  │ Button  │ ←─────→ │ Button  │     │
│  └─────────┘          └─────────┘     │
│                                        │
└────────────────────────────────────────┘
```

### Gesture Alternatives (WCAG 2.2)

```markdown
For every gesture-based action, provide an alternative:

Gesture → Alternative
─────────────────────────────────────────
Swipe to delete → Tap to reveal delete button
Pinch to zoom → Zoom +/- buttons
Drag to reorder → Tap to move up/down
Long press → Tap for options button
Two-finger scroll → Single finger scroll
Drawing gesture → Button to perform action
```

### Timing

```markdown
Requirements:
- No time limits on actions (or extendable)
- Auto-advancing content can be paused
- Session timeouts warn user with extension option

❌ Bad: Form submits automatically after 30 seconds
✅ Good: User controls when to submit
```

---

## Cognitive Accessibility

### Clear Labels

```markdown
Every form input needs:
1. Visible label (not placeholder only)
2. Associated label (for screen readers)
3. Clear instructions if needed
4. Error messages that explain the fix

❌ Bad:
┌─────────────────────────┐
│ Email                   │  ← Placeholder disappears
└─────────────────────────┘

✅ Good:
Email *
┌─────────────────────────┐
│ example@email.com       │  ← Placeholder as hint
└─────────────────────────┘
Enter your work email address
```

### Error Messages

```markdown
Error messages must:
1. Identify the field with error
2. Explain what went wrong
3. Suggest how to fix it

❌ Bad: "Invalid input"
✅ Good: "Email address must include @"

❌ Bad: "Error"
✅ Good: "Password must be at least 8 characters"
```

### Consistent Navigation

```markdown
Navigation must be:
- Consistent across all screens
- Predictable in behavior
- Clear in current location

┌──────────────────────────────────┐
│  ← Back     Profile    ⚙️       │  Consistent header
├──────────────────────────────────┤
│                                  │
│         Page Content             │
│                                  │
├──────────────────────────────────┤
│  🏠    🔍    ➕    👤           │  Consistent footer
│        Active indicator          │
└──────────────────────────────────┘
```

---

## Screen Reader Support

### Required Labels

```markdown
## iOS (VoiceOver)

Every interactive element needs:
├── accessibilityLabel → What it is
├── accessibilityHint → What happens when activated
├── accessibilityTraits → Type (button, link, etc.)
└── accessibilityValue → Current value (if applicable)

SwiftUI Example:
Button("Add to cart") { }
  .accessibilityLabel("Add to cart")
  .accessibilityHint("Adds this item to your shopping cart")

## Android (TalkBack)

contentDescription → What it is
stateDescription → Current state
roleDescription → Type override
accessibilityLiveRegion → For dynamic content

Compose Example:
Button(
  onClick = { },
  modifier = Modifier.semantics {
    contentDescription = "Add to cart"
  }
) { Text("Add") }
```

### Heading Structure

```markdown
Use proper heading hierarchy for navigation:

Screen Title (Heading 1)
├── Section A (Heading 2)
│   ├── Subsection A.1 (Heading 3)
│   └── Subsection A.2 (Heading 3)
└── Section B (Heading 2)
    └── Content

iOS: accessibilityTraits = .header
Android: heading = true
```

### Reading Order

```markdown
Ensure logical reading order matches visual order:

1. Top to bottom
2. Left to right (or right to left for RTL)
3. Group related elements

Test by:
- Using screen reader
- Checking tab order
- Verifying announcements make sense
```

### Dynamic Content

```markdown
Announce changes to screen:

iOS:
UIAccessibility.post(notification: .announcement, argument: "Item added")

Android:
View.announceForAccessibility("Item added")

Use for:
├── Loading states
├── Error messages
├── Success confirmations
├── Content updates
└── Navigation changes
```

---

## Platform Features

### iOS Accessibility Features

```markdown
Support these system features:
├── Dynamic Type → Scalable text
├── Bold Text → Heavier font weights
├── Increase Contrast → Higher contrast UI
├── Reduce Motion → Minimize animations
├── Reduce Transparency → Solid backgrounds
├── VoiceOver → Screen reader
├── Switch Control → Physical switch navigation
├── Voice Control → Voice commands
└── AssistiveTouch → Custom gestures
```

### Android Accessibility Features

```markdown
Support these system features:
├── Font size → Text scaling
├── Display size → UI scaling
├── High contrast text → Enhanced contrast
├── Color correction → Colorblind modes
├── Color inversion → Dark mode alternative
├── TalkBack → Screen reader
├── Switch Access → Physical switch navigation
├── Voice Access → Voice commands
└── BrailleBack → Braille display support
```

---

## Testing Checklist

### Automated Testing

```markdown
□ Run accessibility scanner
  - iOS: Accessibility Inspector
  - Android: Accessibility Scanner app

□ Check contrast ratios
  - WebAIM Contrast Checker
  - Stark plugin

□ Validate focus order
  - Use keyboard navigation
  - Check logical sequence
```

### Manual Testing

```markdown
## Screen Reader Testing

□ VoiceOver (iOS)
  - Enable: Settings > Accessibility > VoiceOver
  - Navigate entire app
  - Verify all elements announced
  - Check announcement clarity

□ TalkBack (Android)
  - Enable: Settings > Accessibility > TalkBack
  - Navigate entire app
  - Verify all elements announced
  - Check announcement clarity

## Motor Testing

□ Keyboard navigation (external keyboard)
  - Tab through all elements
  - Activate with Enter/Space
  - Use arrow keys where appropriate

□ Switch Control
  - Navigate and activate all features
  - No time-dependent actions
```

### User Testing

```markdown
Include users with disabilities:
├── Vision impairments
├── Motor impairments
├── Cognitive differences
├── Hearing impairments (for audio content)
└── Temporary impairments (arm in cast, etc.)
```

---

## Common Mistakes

```markdown
❌ Placeholder-only labels
   Fix: Add visible label above input

❌ Color-only indicators
   Fix: Add icons, text, or patterns

❌ Small touch targets
   Fix: Minimum 44pt/48dp size

❌ Missing alt text
   Fix: Add descriptive labels to all images

❌ Auto-playing media
   Fix: Require user action to play

❌ Motion without control
   Fix: Respect "Reduce Motion" setting

❌ Time limits
   Fix: Allow extension or removal

❌ Keyboard traps
   Fix: Allow tab navigation in and out

❌ Unclear focus
   Fix: Visible focus indicator on all elements

❌ Non-semantic structure
   Fix: Use proper headings and landmarks
```

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────┐
│              ACCESSIBILITY QUICK REFERENCE               │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  CONTRAST                                                │
│  • Text: 4.5:1 (normal), 3:1 (large)                    │
│  • UI components: 3:1                                    │
│                                                          │
│  TOUCH TARGETS                                           │
│  • iOS: 44×44pt minimum                                  │
│  • Android: 48×48dp minimum                              │
│  • Spacing: 8px minimum gap                              │
│                                                          │
│  TEXT                                                    │
│  • Support Dynamic Type / Font Scaling                   │
│  • Must work at 200% zoom                                │
│  • Visible labels, not placeholder-only                  │
│                                                          │
│  SCREEN READERS                                          │
│  • Label all interactive elements                        │
│  • Announce dynamic changes                              │
│  • Logical reading order                                 │
│                                                          │
│  MOTION                                                  │
│  • Respect Reduce Motion setting                         │
│  • Provide alternatives to gestures                      │
│  • No auto-playing content                               │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

---

## Resources

- [WCAG 2.2 Guidelines](https://www.w3.org/TR/WCAG22/)
- [Apple Accessibility](https://developer.apple.com/accessibility/)
- [Android Accessibility](https://developer.android.com/guide/topics/ui/accessibility)
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [A11y Project Checklist](https://www.a11yproject.com/checklist/)
