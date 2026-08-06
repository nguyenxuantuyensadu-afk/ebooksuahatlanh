const fs = require('fs');

let content = fs.readFileSync('src/data.ts', 'utf8');

let menuBlock = content.substring(content.indexOf('id: "menu"') - 12, content.indexOf('id: "equipment"') - 12);
let equipmentBlock = content.substring(content.indexOf('id: "equipment"') - 12, content.indexOf('id: "costing"') - 12);

console.log("menuBlock length", menuBlock.length);
console.log("equipmentBlock length", equipmentBlock.length);
console.log("Content includes menu+equipment:", content.includes(menuBlock + equipmentBlock));

