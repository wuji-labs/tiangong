/**
 * 抓取维基文库古籍原文
 * 在浏览器console中运行
 */

// 获取纯正文（去除注释）
function getMainText() {
  const content = document.querySelector('.mw-parser-output');
  if (!content) return '';
  
  // 克隆节点避免影响原页面
  const clone = content.cloneNode(true);
  
  // 移除注释部分（small标签通常是注释）
  clone.querySelectorAll('small, .reference, .reflist, .mw-editsection').forEach(e => e.remove());
  
  return clone.innerText;
}
