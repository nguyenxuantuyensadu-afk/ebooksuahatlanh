const fs = require('fs');

let content = fs.readFileSync('src/data.ts', 'utf8');

let menuBlockOrig = content.substring(content.indexOf('id: "menu"') - 12, content.indexOf('id: "equipment"') - 12);
let equipmentBlockOrig = content.substring(content.indexOf('id: "equipment"') - 12, content.indexOf('id: "costing"') - 12);

let menuBlockNew = menuBlockOrig.replace('"2. Thiết kế Menu Tối Ưu"', '"3. Thiết kế Menu Tối Ưu"');
let equipmentBlockNew = equipmentBlockOrig.replace('"3. Danh sách Dụng cụ Setup"', '"2. Danh sách Dụng cụ Setup"');

content = content.replace(menuBlockOrig + equipmentBlockOrig, equipmentBlockNew + menuBlockNew);

fs.writeFileSync('src/data.ts', content);
console.log("Done");
