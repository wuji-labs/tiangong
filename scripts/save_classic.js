// 在Node.js中保存抓取的文本
const fs = require('fs');
const dir = 'D:\\Projects\\tiangong\\reference\\classics';
if (!fs.existsSync(dir)) fs.mkdirSync(dir, {recursive: true});

// Save function
function save(name, content) {
  fs.writeFileSync(`${dir}/${name}.txt`, content, 'utf8');
  console.log(`Saved ${name}: ${content.length} chars`);
}

module.exports = { save };
