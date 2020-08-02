package com.kuraykanli.jobsapi.exception;


public class ErrorDetails {
	private Integer status = 404;

	public ErrorDetails(Integer status) {
		super();
		this.status = status;
	}

	public Integer getStatus() {
		return status;
	}

}