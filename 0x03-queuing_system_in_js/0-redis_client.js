import { createClient } from 'redis';

const client = createClient({
    url: 'redis://127.0.0.1:6379'
    })

client.on('connect', () => {
    console.log('Redis client connected to the server');
});
client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

(async () => {
    // Connect to redis server
    await client.connect();
})();
