const kue = require('kue'),
queue = kue.createQueue();

const sendNotification = (phoneNumber, message) => {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code', (job, done) => {
    done();
    sendNotification(job.data.phoneNumber, job.data.message);
});
