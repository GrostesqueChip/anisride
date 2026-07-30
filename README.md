# Ani's Ride 🚌

A modern, soft-minimalist Progressive Web App (PWA) built specifically for Anika's daily BMTC bus commute between **Vinyaas Virtue** (Bahubali Nagar) and **MS Ramaiah Institute of Technology** (Mathikere).

---

## 🌟 Features

- **Real BMTC Bus Routes (Google Maps Verified)**:
  - **Direct (`273-B` / `276`)**: Boards at **HMT Hospital Stop** (~5 min walk) → **MS Ramaiah College Stop** (Gate 11, ~25 min direct ride).
  - **Gate 11 Shortcut**: Drops at **MS Ramaiah College Stop** with a quick ~2 min walk (150m) straight into Gate 11.
  - **2-Bus Transfers via BEL Circle**: Boards feeder **`502-C`**, **`501-NH`**, or **`502-E`** at **Jalahalli Village Stop** (~3 min walk) → Transfers at **BEL Circle** to **`273`**, **`276`**, or **`401-K`** → **MS Ramaiah College Stop (Gate 11)** (~28–30 min total).
- **Tabbed View**: Auto-switches between **To MSRIT** (morning) and **To Home** (afternoon).
- **Time Calculations**: Shows live countdown, exact departure, walk-adjusted **"Leave by"** time, and transit-adjusted **"Reach by"** time.
- **Google Maps Walking Directions**: Quick-action links directly to walking routes for both bus stops and Gate 11.
- **WhatsApp Safe Arrival**: One-tap button (`I reached loveyyy 🤍`) sends a message to Sharvesh (`+91 9448176034`).
- **iOS & Android PWA Support**: Can be added to the iPhone home screen with a native app icon and full-screen experience.

---

## 📁 File Structure

```
Anu/
├── index.html        # Main app (HTML + CSS + JS)
├── manifest.json     # PWA Web App Manifest
├── sw.js             # Service Worker (offline cache)
├── icons/            # App icons (192x192 & 512x512)
└── README.md         # Documentation
```

---

## 🚀 How to Deploy / Share

1. **Option A (Netlify — Easiest & Free)**:
   - Go to [Netlify Drop](https://app.netlify.com/drop).
   - Drag & drop the entire `Anu` folder.
   - You will instantly get a live shareable link (e.g., `https://anis-ride.netlify.app`).

2. **Option B (GitHub Pages)**:
   - Push this repo to GitHub.
   - Go to Repository Settings → Pages → Select `main` branch → Save.

---

## 📱 How to Install on Anika's iPhone

1. Open the deployed website link in **Safari**.
2. Tap the **Share** button (bottom bar).
3. Scroll down and tap **"Add to Home Screen"**.
4. Tap **Add**. The app will appear on her home screen like a native app!

---

## ⚙️ Customization Guide

- **Update WhatsApp Number**: Edit line in `index.html`:
  `const WA_PHONE = "XXXXX";`
- **Update WhatsApp Message**: Edit line in `index.html`:
  `const WA_MSG = "I reached loveyyy";`
- **Update Bus Timings**: Modify `SCHEDULE_TO_COLLEGE` and `SCHEDULE_TO_HOME` arrays at the top of the `<script>` tag in `index.html`.

