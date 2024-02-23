
# Correct import statement
# from httpClient.http_client import FindJobClient

import sys
sys.path.extend([r"..\\http_client"])
import os
import random
from functional import seq
import pytest
from http_client.http_client import FindJobClient, Company
from http_client.models import JobDto, WorkerDto

@pytest.mark.job
@pytest.mark.get
def test_get_jobs_api():

    client = FindJobClient()
    response = client.get_jobs()
    assert response.status_code == 200
    assert type(response.response) is list

@pytest.mark.worker
@pytest.mark.get
def test_get_workers_api():

    client = FindJobClient()
    response = client.get_workers()
    assert response.status_code == 200
    assert type(response.response) is list

@pytest.mark.company
@pytest.mark.get
def test_get_companies_api():

    client = FindJobClient()
    response = client.get_companies()
    assert response.status_code == 200
    assert type(response.response) is list

@pytest.mark.company
@pytest.mark.create
def test_create_company_api():
    
    # Craete
    client = FindJobClient()
    companies_count = len(client.get_companies().response)
    fake_company = Company.create_fake_company()

    # Act
    response = client.post_compnay(fake_company)
    
    # Assert
    assert response.status_code ==  200, f"Wrong status code: {response.status_code}, shuld be 200"
    assert response.response, f"No response"
    assert len(client.get_companies().response) - companies_count == 1, "List of companies is not incrised by one"

@pytest.mark.job
@pytest.mark.create
def test_create_job_api():

    # Craete
    client = FindJobClient()
    try:
        res = client.get_companies().response
        random_company = random.choice(res)
    except Exception as e:
        raise Exception(f"Could not choose a random company beacuse there is no company: {e.args[0]}") 
    jobs_count = len(random_company["jobs"])
    fake_job = JobDto.create_fake_job(Company.create_form_json(random_company))

    # Act
    response = client.post_job(fake_job)
    assert response.status_code ==  200, f"Wrong status code: {response.status_code}, shuld be 200"
    assert response.response, f"No response"
    assert len(seq(client.get_companies().response).find(lambda c : c["id"] == random_company["id"])["jobs"]) - 1 == jobs_count

@pytest.mark.worker
@pytest.mark.create
def test_create_worker_api():

    # Craete
    client = FindJobClient()
    try:
        res = client.get_companies().response
        random_company = random.choice(res)
    except Exception as e:
        raise Exception(f"Could not choose a random company beacuse there is no company: {e.args[0]}") 
    worker_count = len(random_company["workers"])
    fake_worker = WorkerDto.create_fake_worker(Company.create_form_json(random_company))

    # Act
    response = client.post_worker(fake_worker)
    assert response.status_code ==  200, f"Wrong status code: {response.status_code}, shuld be 200"
    assert response.response, f"No response"
    assert len(seq(client.get_companies().response).find(lambda c : c["id"] == random_company["id"])["workers"]) - 1 == worker_count

@pytest.mark.company
@pytest.mark.update
def test_update_company_api():

    # Create
    client = FindJobClient()
    random_company = random.choice(client.get_companies().response)
    company = Company.create_form_json(random_company)
    company.change_random_property()

    # Act
    response = client.update_company(company)
    updated_compnay = seq(client.get_companies().response).find(lambda c : c["id"] == company.id)

     # Assert
    assert response.status_code ==  204, f"Wrong status code: {response.status_code}, shuld be 204"
    assert response.response, f"No response"
    assert random_company != updated_compnay, f"Company is not updated: {updated_compnay}, before: {random_company}"

@pytest.mark.worker
@pytest.mark.update
def test_update_worker_api():

    # Create
    client = FindJobClient()
    random_worker = random.choice(client.get_workers().response)
    worker = WorkerDto.create_form_json(random_worker)


    # worker.change_random_property()-------------------------------------------------------treba dodat

    worker.firstName = f"Update->{worker.firstName}"

    # Act
    response = client.update_worker(worker)
    updated_worker = seq(client.get_workers().response).find(lambda c : c["id"] == worker.id)

     # Assert
    assert response.status_code ==  204, f"Wrong status code: {response.status_code}, shuld be 204"
    assert response.response, f"No response"
    assert random_worker != updated_worker, f"Worker is not updated: {updated_worker}, before: {random_worker}"

@pytest.mark.job
@pytest.mark.update
def test_update_job_api():

    # Create
    client = FindJobClient()
    random_job = random.choice(client.get_jobs().response)
    job = JobDto.create_form_json(random_job)

    # job.change_random_property()-------------------------------------------------------treba dodat

    job.experience = job.experience + 1

    # Act
    response = client.update_job(job)
    updated_job= seq(client.get_companies().response).find(lambda c : c["id"] == job.id)

     # Assert
    assert response.status_code ==  204, f"Wrong status code: {response.status_code}, shuld be 204"
    assert response.response, f"No response"
    assert random_job != updated_job, f"Job is not updated: {updated_job}, before: {random_job}"

@pytest.mark.company
@pytest.mark.delete
def test_delete_company_api():

    #  Create
    client = FindJobClient()
    random_company = random.choice(client.get_companies().response)

    #  Act
    response = client.delete_company(random_company["id"])

    # Assert
    assert response.status_code ==  204, f"Wrong status code: {response.status_code}, shuld be 204"
    assert response.response, f"No response"
    company_found = seq(client.get_companies().response).find(lambda x: x["id"] == random_company["id"])
    assert company_found == None, "Company is still in the list of companies"

@pytest.mark.worker
@pytest.mark.delete
def test_delete_worker_api():

    #  Create
    client = FindJobClient()
    random_worker = random.choice(client.get_workers().response)

    #  Act
    response = client.delete_worker(random_worker["id"])

    # Assert
    assert response.status_code ==  204, f"Wrong status code: {response.status_code}, shuld be 204"
    assert response.response, f"No response"
    company_found = seq(client.get_workers().response).find(lambda x: x["id"] == random_worker["id"])
    assert company_found == None, "Worker is still in the list of companies"

@pytest.mark.job
@pytest.mark.delete
def test_delete_job_api():

    #  Create
    client = FindJobClient()
    random_job= random.choice(client.get_jobs().response)

    #  Act
    response = client.delete_job(random_job["id"])

    # Assert
    assert response.status_code ==  204, f"Wrong status code: {response.status_code}, shuld be 204"
    assert response.response, f"No response"
    company_found = seq(client.get_jobs().response).find(lambda x: x["id"] == random_job["id"])
    assert company_found == None, "Job is still in the list of companies"


@pytest.mark.no_db
def test_simple():
    a = 5
    b = 6
    assert a <  b, "Test failed"


if __name__ == '__main__':
    pytest.main(["-v", "-s", "-m no_db", os.path.abspath(__file__)])

