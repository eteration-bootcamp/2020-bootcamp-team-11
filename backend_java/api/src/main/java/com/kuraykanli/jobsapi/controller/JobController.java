package com.kuraykanli.jobsapi.controller;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import com.kuraykanli.jobsapi.model.Job;
import com.kuraykanli.jobsapi.repo.JobRepo;
import com.kuraykanli.jobsapi.exception.ResourceNotFoundException;

@RestController
@RequestMapping("/api")
public class JobController {

	@Autowired
	private JobRepo jobRepo;
	
	@PostMapping("/job")
	public Job createJob(@RequestBody Job job) {
		return jobRepo.save(job);
	}
	
	@GetMapping("/jobs")
	public List<Job> getAllJobs() {
		return this.jobRepo.findAll();
		
	}
		
	@GetMapping("/job/{id}")
	public ResponseEntity<Job> getJobById(@PathVariable(value = "id") Long jobId) throws ResourceNotFoundException {
		Job job = jobRepo.findById(jobId).orElseThrow(() -> new ResourceNotFoundException("NOOOOF :: " + jobId));
		return ResponseEntity.ok().body(job);
	}
		
	@PutMapping("/job/{id}")
	public ResponseEntity<Job> updateJob(@PathVariable(value = "id") Long jobId, @RequestBody Job jobDetails) throws ResourceNotFoundException {
		Job job= jobRepo.findById(jobId).orElseThrow(() -> new ResourceNotFoundException("NF :: " + jobId));
		
		if (jobDetails.getJobName() != null) {job.setJobName(jobDetails.getJobName());}
		if (jobDetails.getJobCompany() != null) {job.setJobCompany(jobDetails.getJobCompany());}
		if (jobDetails.getJobDescription() != null) {job.setJobDescription(jobDetails.getJobDescription());}
		if (jobDetails.getJobLocation() != null) {job.setJobLocation(jobDetails.getJobLocation());}
		if (jobDetails.getJobContract() != null) {job.setJobContract(jobDetails.getJobContract());}
		if (jobDetails.getJobTags() != null) {job.setJobTags(jobDetails.getJobTags());}
		if (jobDetails.getJobFeatured() != null) {job.setJobFeatured(jobDetails.getJobFeatured());}
		
		final Job updatedEmployee = jobRepo.save(job);
		return ResponseEntity.ok(updatedEmployee);
	}
	
	@DeleteMapping("/job/{id}")
	public Map<String, Integer> deleteJob(@PathVariable(value = "id") Long jobId) throws ResourceNotFoundException {
		Job job = jobRepo.findById(jobId).orElseThrow(() -> new ResourceNotFoundException("NF :: " + jobId));

		jobRepo.delete(job);
		Map<String, Integer> response = new HashMap<>();
		response.put("status", 200);
		return response;
	}
	
}
