const express = require('express');
const mysql = require('mysql');

const app = express();

const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'root',
});

app.get('/', (req, res) => {
    // get '/' root route
    connection.connect((err) => {
        if (err) {
            console.log(JSON.stringify(err, null, 4));
            return res.status(500).json({
                message: 'invalid database connection.',
            });
        }
        console.log('Connection is OK.');
        const query = "SELECT * from testDatabase.Subjects";
        connection.query(query, (queryErr, results, fields) => {
            console.log('Connection is OK.');
            if (queryErr) {
                console.log(JSON.stringify(queryErr, null, 4));
                return res.status(500).json({
                    message: 'invalid database query.',
                });
            }
            console.log('Query is ok.');
            let data = [];
            for (row in results) {
                const item = results[row];
                data = [
                    ...data,
                    { id: item.id, text: item.text, }
                ];
            }
            return res.json({
                data: data,
            });
        });
    });
});

app.listen(3333);
