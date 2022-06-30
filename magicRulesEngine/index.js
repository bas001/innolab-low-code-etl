const fs = require('fs');

tableName= 's_client'

parameter=['sex', 'day', 'month', 'ages']

const obj = JSON.parse('{"name":"John", "age":30, "city":"New York"}');



fs.readFile('.json', (err, data) => {
    if (err) throw err;
    let student = JSON.parse(data);
    console.log(student);
});

console.log('This is after the read call');


