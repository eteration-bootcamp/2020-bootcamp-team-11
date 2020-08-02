package com.kuraykanli.jobsapi.repo;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.kuraykanli.jobsapi.model.Job;

@Repository
public interface JobRepo extends JpaRepository<Job, Long> {

}
