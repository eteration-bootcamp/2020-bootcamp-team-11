package com.kuraykanli.jobsapi.model;
import java.time.LocalDateTime;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;


@Entity
@Table(name = "jobs")	
public class Job {
	
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private long id;
	
	@Column(name = "name")
	private String jobName;
	
	@Column(name = "company")
	private String jobCompany;
	
	@Column(name = "description")
	private String jobDescription;
	
	@Column(name = "location")
	private String jobLocation;
	
	@Column(name = "contract")
	private String jobContract;
	
	@Column(name = "tags")
	private String jobTags;
	
	@Column(name = "new")
	private Boolean jobNew;
	
	@Column(name = "featured")
	private Boolean jobFeatured;
	
	@Column(name = "time")
	private LocalDateTime jobDate = LocalDateTime.now().withNano(0);
	
	
	public Job() {
		super();
	}

	public Job(String jobName, String jobCompany, String jobDescription, String jobLocation, String jobContract,
			String jobTags, Boolean jobNew, Boolean jobFeatured) {
		super();
		this.jobName = jobName;
		this.jobCompany = jobCompany;
		this.jobDescription = jobDescription;
		this.jobLocation = jobLocation;
		this.jobContract = jobContract;
		this.jobTags = jobTags;
		this.jobNew = jobNew;
		this.jobFeatured = jobFeatured;
	}

	public long getId() {
		return id;
	}

	public void setId(long id) {
		this.id = id;
	}

	public String getJobName() {
		return jobName;
	}

	public void setJobName(String jobName) {
		this.jobName = jobName;
	}

	public String getJobCompany() {
		return jobCompany;
	}

	public void setJobCompany(String jobCompany) {
		this.jobCompany = jobCompany;
	}

	public String getJobDescription() {
		return jobDescription;
	}

	public void setJobDescription(String jobDescription) {
		this.jobDescription = jobDescription;
	}

	public String getJobLocation() {
		return jobLocation;
	}

	public void setJobLocation(String jobLocation) {
		this.jobLocation = jobLocation;
	}

	public String getJobContract() {
		return jobContract;
	}

	public void setJobContract(String jobContract) {
		this.jobContract = jobContract;
	}

	public String getJobTags() {
		return jobTags;
	}

	public void setJobTags(String jobTags) {
		this.jobTags = jobTags;
	}

	public Boolean getJobNew() {
		return jobNew;
	}

	public void setJobNew(Boolean jobNew) {
		this.jobNew = jobNew;
	}

	public Boolean getJobFeatured() {
		return jobFeatured;
	}

	public void setJobFeatured(Boolean jobFeatured) {
		this.jobFeatured = jobFeatured;
	}

	public String getJobDate() {
		return jobDate.toString().replace("T", " ");
	}

	public void setJobDate(LocalDateTime jobDate) {
		this.jobDate = jobDate;
	}
}
