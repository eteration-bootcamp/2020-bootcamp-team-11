import React, {useState, useEffect} from 'react';
import data from './assets/data.json';
import JobBoardComponent from './components/JobBoardComponent';


function App() {
  const [jobs, setJobs] =  useState([]);
  const [filters, setFilters] = useState([]);

  useEffect(() =>  setJobs(data),[]);

  const filterFunc = ({jobName,jobTags}
    ) => {
    if(filters.length === 0){
      return true;
    }

    const tags = [jobName,jobTags];

    if(jobTags){
      tags.push(...jobTags);
    }

  

    return filters.every(filter => tags.includes(filter));
  }

  const handleTagClick = (tag) => {
    if(filters.includes(tag)) return; 
    setFilters([...filters, tag]);
  }

  const handleFilterClick = (passedFilter) =>{
    setFilters(filters.filter(
      f=> f !== passedFilter
      ));
  }

  const clearFilters = () => {
    setFilters([]);
  }

  const filteredJobs = jobs.filter(filterFunc);


  


  return (
    <>
  
      <div className='container m-auto'>  
          {filters.length > 0 && (
            <div className={`flex 
                            bg-white 
                            shadow-md -my-16
                            mb-16 mx-10 p-6 
                            rounded z-10 
                            relative`}>
            {(filters.map((filter) => 
                <span className='mr-4 mb-4 p-2 
                                rounded font-bold  
                                lg:mb-0'>
                  <span className='text-teal-500 
                                  bg-teal-100 p-2'>
                    {filter}
                  </span>
                  <span onClick={() => handleFilterClick(filter)} className='cursos-pointer 
                                                                  bg-teal-500 text-teal-100 p-2'>❌</span>
                </span>))} 
                <button onClick={clearFilters} className='font-bold 
                                                          text-gray-700
                                                           ml-auto'>Clear</button>
            </div>
          )}  
        {jobs.length === 0 ? (
            <p>Jobs are fetching...</p>
          ): (
            filteredJobs.map((job)=>(
              <JobBoardComponent 
                job={job} 
                key={job.id} 
                handleTagClick={handleTagClick}
              />
            ))
          )}
      </div>
    </>  
  );
}

export default App;