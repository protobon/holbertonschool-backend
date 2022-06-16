const kue = require('kue');

const jobs = [
    {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    },
    {
      phoneNumber: '4153518781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153518743',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153538781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153118782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4159518782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4158718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153818782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4154318781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4151218782',
      message: 'This is the code 4321 to verify your account'
    }
  ];

const queue = kue.createQueue();

function jobProgress(job, complete=0, total=jobs.length) {
    console.log(`Notification job ${job.id} ${complete/total}% complete`);
}

for (const job_data of jobs) {
    const job = queue.create('push_notification_code_2', job_data)
    .save( function(err){
       err ? console.log(`Notification job ${job.id} failed: ${job.error}`) :
       console.log(`Notification job created: ${job.id}`);
    });

    job.on('complete', function(result) {
        console.log(`Notification job ${job.id} completed`);
    });

    job.progress(jobs, jobs.length);
}
