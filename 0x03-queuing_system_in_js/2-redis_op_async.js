import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient({
    url: 'redis://127.0.0.1:6379'
    });

const getAsync = promisify(client.get).bind(client);

client.on('connect', () => {
    console.log('Redis client connected to the server');
});
client.on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err.message}`);
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
};

async function displaySchoolValue(schoolName) {
    console.log(await getAsync(schoolName));
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
