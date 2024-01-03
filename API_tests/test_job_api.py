


# Correct import statement
# from httpClient.http_client import FindJobClient

import os
import random
from functional import seq
import pytest
from httpClient.http_client import FindJobClient, Company, Job, Worker


def test_get_jobs_api():

    client = FindJobClient()
    response = client.get_jobs()
    assert response.status_code == 200
    assert type(response.response) is list

def test_get_workers_api():

    client = FindJobClient()
    response = client.get_workers()
    assert response.status_code == 200
    assert type(response.response) is list

def test_get_companies_api():

    client = FindJobClient()
    response = client.get_companies()
    assert response.status_code == 200
    assert type(response.response) is list

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


def test_create_job():

    # Craete
    client = FindJobClient()
    random_company = random.choice(seq(client.get_companies().response).filter(lambda x: x["jobs"]).to_list())
    jobs_count = len(random_company["jobs"])
    fake_job = Job.create_fake_job(Company.create_form_json(random_company))

    # Act
    response = client.post_job(fake_job)
    
    # Assert
    assert response.status_code ==  200, f"Wrong status code: {response.status_code}, shuld be 200"
    assert response.response, f"No response"
    assert len(seq(client.get_companies().response).find(lambda c : c["id"] == random_company["id"])) - 1 == jobs_count





if __name__ == '__main__':
    pytest.main(["-v", "-s", os.path.abspath(__file__)])
    # test_create_company_api()
    # test_delete_company_api()

