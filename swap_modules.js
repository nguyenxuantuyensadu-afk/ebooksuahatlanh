const fs = require('fs');

let content = fs.readFileSync('src/data.ts', 'utf8');

const menuStart = content.indexOf('{', content.indexOf('id: "menu"')) - 50; // find the block start
const equipmentStart = content.indexOf('{', content.indexOf('id: "equipment"')) - 50;

console.log("Found menu:", content.indexOf('id: "menu"'));
console.log("Found equipment:", content.indexOf('id: "equipment"'));

// Let's just parse it manually or use a simpler regex.
// Actually, it's a TS file exporting an object. We can just use string replacements.
let menuBlock = content.substring(content.indexOf('id: "menu"') - 12, content.indexOf('id: "equipment"') - 12);
let equipmentBlock = content.substring(content.indexOf('id: "equipment"') - 12, content.indexOf('id: "costing"') - 12);

// modify titles
menuBlock = menuBlock.replace('"2. Thiết kế Menu Tối Ưu"', '"3. Thiết kế Menu Tối Ưu"');
equipmentBlock = equipmentBlock.replace('"3. Danh sách Dụng cụ Setup"', '"2. Danh sách Dụng cụ Setup"');

content = content.replace(menuBlock + equipmentBlock, equipmentBlock + menuBlock);

fs.writeFileSync('src/data.ts', content);
console.log("Done");
