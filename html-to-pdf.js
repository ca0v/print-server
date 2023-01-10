import puppeteer from "puppeteer";
const URL = process.argv[2] || "https://ca0v.us/resume.cv.html";

(async () => {
  const browser = await puppeteer.launch({
    headless: true,
    executablePath: "/opt/homebrew/bin/chromium",
  });
  const page = await browser.newPage();

  console.log("goto", URL);
  await page.goto(URL);

  // print the page to PDF
  await page.pdf({
    path: "page.pdf",
    printBackground: false,
  });

  // Print all the files.

  await browser.close();
})();
