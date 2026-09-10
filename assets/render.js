const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
    const browser = await puppeteer.launch({ headless: true });
    const page = await browser.newPage();
    
    // Set viewport to 1200x1200 with device scale factor 2 for retina
    await page.setViewport({ 
        width: 1200, 
        height: 1200, 
        deviceScaleFactor: 2 
    });
    
    // Load the HTML file
    const htmlPath = path.join(__dirname, 'post.html');
    await page.goto(`file://${htmlPath}`, { waitUntil: 'networkidle0' });
    
    // Wait for fonts to load
    await page.evaluateHandle('document.fonts.ready');
    await new Promise(r => setTimeout(r, 1000));
    
    // Take screenshot
    await page.screenshot({ 
        path: path.join(__dirname, 'post.png'),
        type: 'png',
        fullPage: false
    });
    
    await browser.close();
    console.log('Image rendered successfully: post.png');
})();
