const kue = require('kue'),
queue = kue.createQueue();


const job = queue.create('push_notification_code', {
    "phoneNumber": "099999991",
    "message": "Full perspective",
  }).save( function(err){
   err ? console.log("Notification job failed") :
   console.log(`Notification job created: ${job.id}`);
});


job.on('complete', function(result) {
    console.log("Notification job completed");
});
