<script>	
	import { onMount } from 'svelte';
	import Applicants from './Components/Applicants.svelte';
	let adminhide = false;
	let edithide  = false
	let createhide  = false
	let candihide = false

  let editDisabled = false;
  let candisabled = false;
  let applyCheck = false
  let applicationCheck = false

  let disabled = true;
  let recdisabled = false;
  
  let listJobs = false;
  let addJobs = false;
  let item="data"
  let recruiter = "recruiter@screel.in"
  let candidate = "candidate@screel.in"
  let user = '';
  let tempId = ''
  let job={
		job_id:"",
		job_name:"",
		description:"",
		role : '',
		experience : '',
		qualification: '',
		job_location : '',
		salary: ''
        }   
	let promise = Promise.resolve([]);
	let promises = Promise.resolve([]);
	
	//Load Jobs
	async function fetchJobs() {
		const response = await self.fetch(`http://127.0.0.1:8000/jobs?skip=0&limit=100`);

		if (response.ok) {
  		return response.json();
		} else {
			console.log("Failed")
			throw new Error(users);
		}
	}
	onMount(async () => {
		promise = fetchJobs();
		promises = getApplications();
	});

	//Load Job Applications
	async function getApplications(){
		const response = await self.fetch(`http://127.0.0.1:8000/jobs/applications?skip=0&limit=100`);

		if (response.ok) {
  		return response.json();
		} else {
			console.log("Failed")
			throw new Error(users);
		}
	}

	//To Display List of Apllications
	function showApplications(){
		if(applicationCheck){
			applicationCheck = false
		}else{
			resetData()
			listJobs = false
			addJobs = false
			applicationCheck = true
		promises = getApplications();
		}
	}

	//To Create new Job
	async function doPost () {
		
		if (confirm('Are  you sure to Create this '+ job.job_name +' Job?')) {		

		
		console.log(JSON.stringify(job))
		const res = await fetch(`http://127.0.0.1:8000/jobs`, {
			method: 'POST',
			headers: {
				'accept': 'application/json',
    			'Content-Type': 'application/json'
			  },
			body: JSON.stringify(job)
		})
		
		if (res.ok) {
			
            alert("Job Created Successfully!!")
			resetData()
			console.log(res)
  		return res.json();
		} else {
			console.log("Failed")
			throw new Error(users);
		}
	}
	}

	//To Display  Job Application UI
	function applyJob(tempJob){
		if(applyCheck){
			applyCheck = false
		}else{
			job = tempJob
			listJobs = false
			addJobs = false
			applicationCheck= false
			applyCheck = true
		}

	}

	//To Delete Job
	async function deleteJob(job){
		if (confirm('Are  you sure to Delete '+ job.job_name +' Job?')) {
			const res = await fetch(`http://127.0.0.1:8000/jobs?sl_id=${job.id}`, {
			method: 'DELETE',
			headers: {
				'accept': 'application/json',
			  }
		})
		
		if (res.ok) {
            alert("Job Deleted Successfully!!")
			promise = fetchJobs();
			console.log(res)
  		return res.json();
		} else {
			console.log("Failed")
		}
		}
		
}

//To load edit job UI
	function editJob(tempJob){
		job = tempJob
		editDisabled = true
		tempId = tempJob.id
		listJobs = false
			applicationCheck= false
			addJobs=true
			edithide = true
			disabled = false
			createhide = false
	}

	// To Load list of jobs in UI
  function handleClick() {
	if(listJobs){
		listJobs = false
		}else{
			if (user.includes(recruiter)) {
				candihide = true
				adminhide = false
				recdisabled = true
				candisabled = false
				promise = fetchJobs();	
			listJobs = true
			applicationCheck = false
			addJobs=false
			applyCheck = false
			} else if(user.includes(candidate)){
				adminhide = true
				candihide = false
				promise = fetchJobs();	
				recdisabled = false
				candisabled = true
			listJobs = true
			addJobs=false
			applicationCheck = false
			applicationCheck= false
			applyCheck = false
			}else{

				listJobs = false
			}
		}
	}

	// To Reset Data
	function resetData(){
		job={
		job_id:"",
		job_name:"",
		description:"",
		role : '',
		experience : '',
		qualification: '',
		job_location : '',
		salary: ''
        }  
	}

	// To Create Job
	function createJob(){
		if(addJobs){
			addJobs = false
		}else{
			editDisabled = false
			listJobs = false
			applicationCheck= false
			addJobs = true
			edithide = false
			createhide = true
		}
		
	}

	// To Update job
	async function updateJob(){
		if (confirm('Are  you sure to Update this '+ job.job_name +' Job?')) {		
		let editjobs={
			experience : job.experience,
			qualification: job.qualification,
			job_location : job.job_location,
			salary: job.salary
		}
		console.log(JSON.stringify(job))
		const res = await fetch(`http://127.0.0.1:8000/jobs?sl_id=${tempId}`, {
			method: 'PUT',
			headers: {
				'accept': 'application/json',
    			'Content-Type': 'application/json'
			  },
			body: JSON.stringify(editjobs)
		})
		
		if (res.ok) {
            alert("Job Updated Successfully!!")
			resetData()
			console.log(res)
  		return res.json();
		} else {
			console.log("Failed")
			throw new Error(users);
		}
	}
	}
	
</script>

<h2>Welcome to Job Tracker</h2>

<label class="input-label" for="user">
	User : 
	<input
	class="wide"
	id="user"
	name="user"
	bind:value={user}
	type=text
	data-multistep-error-message="name couldn't be empty"
	placeholder="User" 
   />
   
</label>

{#if candidate.includes(user.toString())}
<button id="showBtn" name="showBtn" on:click={ handleClick } >
	Show Jobs
</button>
	 {:else  if  recruiter.includes(user.toString())}
	 
	<button id="showBtn" name="showBtn" on:click={ handleClick } >
		Show Jobs
	</button>
	<button id="createBtn" name="createBtn" on:click={ createJob }  >
		Create Jobs
	</button>
	<button id="applicantBtn" name="applicantBtn" on:click={ showApplications }  >
		Applications
	</button>
	{:else }
	<div></div>
	 {/if}
	{#if applyCheck}
		 <Applicants job = {job} user = {user}/>
	{:else}
		 <div></div>
	{/if}
	 {#if addJobs}
		 <div>
			<label class="input-label" for="jobId">
				Job Id : 
				<input
				class="wide"
				id="jobId"
				name="jobId"
				bind:value={job.job_id}
				type=text
				disabled={editDisabled}
				data-multistep-error-message="name couldn't be empty"
				placeholder="Enter job's Name" 
			   />
			   
			</label>
			<label class="input-label" for="JobName">
				Job Name : 
				<input
				class="wide"
				id="JobName"
				name="JobName"
				bind:value={job.job_name}
				type=text
				disabled={editDisabled}
				data-multistep-error-message="name couldn't be empty"
				placeholder="Enter job's Name" 
			   />
			   
			</label>
			<label class="input-label" for="description">
				Job Description : 
				<input
				class="wide"
				id="description"
				name="description"
				bind:value={job.description}
				type=text
				disabled={editDisabled}
				data-multistep-error-message="name couldn't be empty"
				placeholder="Enter job's Description" 
			   />
			   
			</label>
			<label class="input-label" for="role">
				Job Role : 
				<input
				class="wide"
				id="role"
				name="role"
				bind:value={job.role}
				type=text
				disabled={editDisabled}
				data-multistep-error-message="name couldn't be empty"
				placeholder="Enter Job's Role" 
			   />
			   
			</label>
			<label class="input-label" for="experience">
				Job Experience : 
				<input
				class="wide"
				id="experience"
				name="experience"
				bind:value={job.experience}
				type=text
				data-multistep-error-message="name couldn't be empty"
				placeholder="Enter job's Experience" 
			   />
			   
			</label>
			<label class="input-label" for="qualification">
				Job Qualification : 
				<input
				class="wide"
				id="qualification"
				name="qualification"
				bind:value={job.qualification}
				type=text
				data-multistep-error-message="name couldn't be empty"
				placeholder="Enter job's Qualification" 
			   />
			   
			</label>
			<label class="input-label" for="location">
				Job Location : 
				<input
				class="wide"
				id="location"
				name="location"
				bind:value={job.job_location}
				type=text
				data-multistep-error-message="name couldn't be empty"
				placeholder="Enter job's Location" 
			   />
			   
			</label>
			<label class="input-label" for="salary">
				Salary : 
				<input
				class="wide"
				id="salary"
				name="salary"
				bind:value={job.salary}
				type=text
				data-multistep-error-message="name couldn't be empty"
				placeholder="Enter job's Salary" 
			   />
			   
			</label>
			<button id="showBtn" name="showBtn" on:click={ doPost } hidden = {edithide} >
				post Job
			</button>
			<button id="editBtn" name="editBtn" {disabled}  on:click={ updateJob  } hidden = {createhide}   >
				Update Job
			</button>
		 </div>
	 {:else}
		  <div></div>
	 {/if}

	 {#if applicationCheck}
		  {#await promises}
		  <p>...waiting</p>
		  {:then value}
		  {#each value as application (application.id) }
		    <h3>Applicant Name : {application.applicant_name}</h3>
			<h3>Applicant Phone : {application.applicant_phone}</h3>
			<h3>Applicant Email : {application.applicant_email}</h3>
			<h3>Job Id : {application.job_id}</h3>
			<h3>Job Name : {application.job_name}</h3>
			
	<hr>
		  {/each}
		  {:catch error}
			  <p style="color: red">{error.message}</p>
		  {/await}
	 {:else}
		  <div></div>
	 {/if}

{#if listJobs}
{#await promise}
	<p>...waiting</p>
{:then users}
  {#each users as job (job.id) }
    <h3>Job Name : {job.job_name}</h3>
	<h3>Job Description : {job.description}</h3>
	<h3>Job Qualification : {job.qualification}</h3>
	<h3>Job Location : {job.job_location}</h3>
	<h3>Salary : {job.salary}</h3>
	<button on:click={ editJob(job) } hidden = {adminhide} disabled= {candisabled}  >
		Edit Job
	</button>
	<button on:click={ applyJob(job) }   hidden = {candihide}>
		Apply Job
	</button>
	<button on:click={ deleteJob(job) } hidden = {adminhide} disabled= {candisabled} >
		Delete Job
	</button>
	<hr>
  {/each}
{:catch error}
	<p style="color: red">{error.message}</p>
{/await}
{:else}
<div></div>
{/if}
