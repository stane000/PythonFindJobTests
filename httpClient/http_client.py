

from dataclasses import dataclass, asdict
from typing import List, Dict

from requests import Session

# from .models import Company, Job, Worker
from httpClient.models import Company, Job, Worker, Position

@dataclass
class ResponseList:

    response: List[Dict]
    status_code: int
    
    @classmethod
    def return_respone(cls, response):
        if response.status_code == 200:
            return  cls(response.json(), response.status_code)
        else: 
            return cls([], response.status_code)
        
@dataclass
class ResponseBool:

    response: bool
    status_code: int


class FindJobClient:

    def __init__(self) -> None:
        self.local_jost = "https://localhost:7021"
        self.session = Session()

    def get_companies(self) -> ResponseList:
        response = self.session.get(f'{self.local_jost}/api/Company', verify=False)
        return ResponseList.return_respone(response)
    
    def get_workers(self) -> ResponseList:
        response = self.session.get(f'{self.local_jost}/api/Worker', verify=False)
        return ResponseList.return_respone(response)
    
    def get_jobs(self) -> ResponseList:
        response = self.session.get(f'{self.local_jost}/api/Job', verify=False)
        return ResponseList.return_respone(response)
    
    def post_compnay(self, compnay: Company):
        response = self.session.post(f'{self.local_jost}/api/Company', json=asdict(compnay), 
                                     headers={'accept': '*/*', 'Content-Type': 'application/json'}, verify=False)
        return ResponseBool(response.ok, response.status_code )

    def post_job(self, job: Job):
        response = self.session.post(f'{self.local_jost}/api/Job', json=asdict(job), 
                                     headers={'accept': '*/*', 'Content-Type': 'application/json'}, verify=False)
        return ResponseBool(response.ok, response.status_code )   
    
    def post_worker(self, worker: Worker):
        response = self.session.post(f'{self.local_jost}/api/Worker', json=asdict(worker), 
                                     headers={'accept': '*/*', 'Content-Type': 'application/json'}, verify=False)
        return ResponseBool(response.ok, response.status_code )   
    
    def update_company(self, company: Company):
        response = self.session.put(f'{self.local_jost}/api/Company/{company.id}', json=asdict(company), 
                                     headers={'accept': '*/*', 'Content-Type': 'application/json'}, verify=False)
        return ResponseBool(response.ok, response.status_code )
    
    def update_worker(self, worker: Worker):
        response = self.session.put(f'{self.local_jost}/api/Worker/{worker.id}', json=asdict(worker), 
                                     headers={'accept': '*/*', 'Content-Type': 'application/json'}, verify=False)
        return ResponseBool(response.ok, response.status_code )
    
    def update_job(self, job: Job):
        response = self.session.put(f'{self.local_jost}/api/Job/{job.id}', json=asdict(job), 
                                     headers={'accept': '*/*', 'Content-Type': 'application/json'}, verify=False)
        return ResponseBool(response.ok, response.status_code )
    
    def delete_company(self, company_id):
        response = self.session.delete(f'{self.local_jost}/api/Company/{company_id}', 
                                     headers={'accept': '*/*', 'Content-Type': 'application/json'}, verify=False)
        return ResponseBool(response.ok, response.status_code )
    
    def delete_worker(self, company_id):
        response = self.session.delete(f'{self.local_jost}/api/Worker/{company_id}', 
                                        headers={'accept': '*/*', 'Content-Type': 'application/json'}, verify=False)
        return ResponseBool(response.ok, response.status_code )
    
    def delete_job(self, company_id):
        response = self.session.delete(f'{self.local_jost}/api/Job/{company_id}', 
                                        headers={'accept': '*/*', 'Content-Type': 'application/json'}, verify=False)
        return ResponseBool(response.ok, response.status_code )

    
    # def get_company_by_id(self, company_id):
    #     response = self.session.put(f'{self.local_jost}/api/Company/{company.id}', json=asdict(company), 
    #                                  headers={'accept': '*/*', 'Content-Type': 'application/json'}, verify=False)
    #     return ResponseBool(response.ok, response.status_code )
    
    # def post_worker(self, worker: Worker):
    #     response = self.session.post(f'{self.local_jost}/api/Worker', json=asdict(worker), 
    #                                  headers={'accept': '*/*', 'Content-Type': 'application/json'}, verify=False)
    #     return ResponseBool(response.ok, response.status_code )
    
        
if __name__ == "__main__":

    client = FindJobClient()
    companies = companies = client.get_companies()
    a  = 5
    c = Company(**companies.response[0])
    # company = client.post_compnay(Company.create("Rimac3", 5000, [], False, []))
    # a = 5
    # job = Job(companies, Position.BackEndDeveloper, 3, Collage.ALGEBRA)
    worker = Worker.create(firstName="Hrvoje", lastName="Nezic", age=60, college="FER", position=f"{Position.BackEndDeveloper.name}", experience=30,
                            lookingForJob=False, companyName=c.name)
    a = client.post_worker(worker)
    b = 3
    # v = client.post_job(job)