<script>
    export let job;
    export let user;
    let application = {
        application_id : uniqueID(),
        job_id : job.job_id,
        job_name :job.job_name,
        applicant_id :  user,
        applicant_name : "",
        applicant_phone : "",
        applicant_email : "",
        applied_time : Date.now()
    }
    function uniqueID() {
return Math.floor(Math.random() * Date.now())
}

async function submitApllication(){
console.log(application)
console.log(JSON.stringify(application))
if (confirm('Are you sure to Apply for '+ job.job_name +' Job?')) {
    const res = await fetch(`http://127.0.0.1:8000/jobs/apply`, {
			method: 'POST',
			headers: {
				'accept': 'application/json',
    			'Content-Type': 'application/json'
			  },
			body: JSON.stringify(application)
		})
		
		if (res.ok) {
            alert("Job Applied Successfully!!")
			resetData()
			console.log(res)
  		return res.json();
		} else {
			console.log("Failed")
			throw new Error(users);
		}
}
		
}
function resetData(){
    application = {
        application_id : "",
        job_id : "",
        job_name :"",
        applicant_id :  "",
        applicant_name : "",
        applicant_phone : "",
        applicant_email : "",
        applied_time : ""
    }
}
</script>

<style>
   
</style>

<h5>You are applying for</h5>
<h4>Job Name : {job.job_name}</h4>
<h4>Job Description : {job.description}</h4>
<h4>Job Location : {job.job_location}</h4>
<!-- <label class="input-label" for="applicationId">
	Application Id : 
	<input
	class="wide"
	id="applicationId"
	name="applicationId"
	bind:value={application.applicant_id}
	type=text
	data-multistep-error-message="name couldn't be empty"
	placeholder="User" 
   />
</label> -->
<label class="input-label" for="applicantName">
	Applicant Name : 
	<input
	class="wide"
	id="applicantName"
	name="applicantName"
	bind:value={application.applicant_name}
	type=text
	data-multistep-error-message="name couldn't be empty"
	placeholder="Enter Applicant Name" 
   />
</label>
<label class="input-label" for="applicantPhone">
	Applicant Phone : 
	<input
	class="wide"
	id="applicantPhone"
	name="applicantPhone"
	bind:value={application.applicant_phone}
	type=text
	data-multistep-error-message="name couldn't be empty"
	placeholder="Enter Applicant Phone Number" 
   />
</label>
<label class="input-label" for="applicantEmail">
	Applicant Email : 
	<input
	class="wide"
	id="applicantEmail"
	name="applicantEmail"
	bind:value={application.applicant_email}
	type=text
	data-multistep-error-message="name couldn't be empty"
	placeholder="Enter Applicant Email" 
   />
</label>
<button id="applyBtn" name="applyBtn" on:click={ submitApllication } >
	Apply
</button>
