# 🚀 Deployment Guide

Quick guide to get your Gesture Meme Tracker live on the internet!

## ⚡ Option 1: Vercel (Recommended - Easiest)

### Steps:

1. **Make sure your code is on GitHub:**
   ```bash
   git add .
   git commit -m "Add web version"
   git push origin main
   ```

2. **Go to Vercel:**
   - Visit [vercel.com](https://vercel.com)
   - Click "Sign Up" (if new) or "Login"
   - Choose "Continue with GitHub"

3. **Import Your Project:**
   - Click "Add New..." → "Project"
   - Find your `gesture-meme-tracker-1` repository
   - Click "Import"

4. **Deploy:**
   - Leave all settings as default
   - Click "Deploy"
   - Wait ~30 seconds ⏳

5. **Done! 🎉**
   - Your site is live at `https://your-project-name.vercel.app`
   - Share this link with anyone!

### Automatic Updates:
- Every time you push to GitHub, Vercel automatically redeploys
- No need to manually redeploy!

---

## 🌐 Option 2: GitHub Pages (Free)

### Steps:

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Add web version"
   git push origin main
   ```

2. **Enable GitHub Pages:**
   - Go to your repository on GitHub.com
   - Click "Settings" (top right)
   - Scroll down to "Pages" (left sidebar)
   - Under "Source", select:
     - Branch: `main`
     - Folder: `/ (root)`
   - Click "Save"

3. **Wait a few minutes** (2-5 min for first deploy)

4. **Access your site:**
   - URL will be: `https://yourusername.github.io/gesture-meme-tracker-1`
   - GitHub will show the URL in the Pages settings

### Updates:
- Push to `main` branch to update
- Takes 2-5 minutes to reflect changes

---

## 💻 Test Locally First

Before deploying, test locally:

```bash
# Start a local server
python -m http.server 8000
```

Then open: `http://localhost:8000`

**Important:** Local testing won't have HTTPS, so camera might not work. That's normal! It will work once deployed.

---

## 🔍 Troubleshooting

### Vercel Issues

**"Build Failed":**
- Check that all files are committed: `git status`
- Ensure `index.html`, `style.css`, `script.js` exist
- Check Vercel build logs for specific errors

**Site loads but no videos:**
- Ensure `images/` folder is committed to Git
- Check file names match in `script.js` (case-sensitive!)
- Videos must be `.mp4` or `.webm` format

### GitHub Pages Issues

**404 Error:**
- Wait 5-10 minutes after enabling Pages
- Check that Pages is enabled in Settings
- Verify repository is public (or you have GitHub Pro for private)

**Camera not working:**
- GitHub Pages uses HTTPS automatically ✅
- Allow camera permissions in browser
- Try different browser (Chrome recommended)

---

## ✅ Deployment Checklist

Before deploying, verify:

- [ ] All meme videos/images are in `images/` folder
- [ ] `images/` folder is committed to Git (`git add images/`)
- [ ] All code files committed: `index.html`, `style.css`, `script.js`
- [ ] Tested locally (optional, but recommended)
- [ ] Git repository pushed to GitHub
- [ ] Ready to deploy! 🚀

---

## 🌟 After Deployment

Once live, share your link:
- `https://your-project.vercel.app` (Vercel)
- `https://yourusername.github.io/gesture-meme-tracker-1` (GitHub Pages)

### Test on Multiple Devices:
- ✅ Desktop/Laptop
- ✅ Mobile phone
- ✅ Tablet
- ✅ Different browsers (Chrome, Firefox, Safari)

---

## 🎨 Custom Domain (Optional)

### For Vercel:
1. Go to your project on Vercel
2. Settings → Domains
3. Add your custom domain
4. Follow DNS instructions

### For GitHub Pages:
1. Settings → Pages
2. Add custom domain
3. Update DNS records with your domain provider

---

## 📊 Analytics (Optional)

Want to see how many people use your app?

### Add Google Analytics:
1. Get tracking ID from analytics.google.com
2. Add to `index.html` before `</head>`:
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=YOUR-ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'YOUR-ID');
</script>
```

---

## Need Help?

- **Vercel Docs:** [vercel.com/docs](https://vercel.com/docs)
- **GitHub Pages Docs:** [docs.github.com/pages](https://docs.github.com/en/pages)
- **MediaPipe Issues:** Check browser console (F12)

Happy deploying! 🚀

