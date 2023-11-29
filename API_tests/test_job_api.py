


# Correct import statement
# from httpClient.http_client import FindJobClient
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
    fake_job = Job.create_fake_job(fake_company)
    fake_worker = Worker.create_fake_worker(fake_company)
    fake_company.workers = [fake_worker]
    #fake_company.jobs = [fake_job]    
    # Act
    response = client.post_compnay(fake_company)
    
    # Assert
    assert response.status_code ==  200
    assert response.response
    assert len(client.get_companies().response) - companies_count == 1, "List of companies is not incrised by one"

if __name__ == '__main__':
    test_create_company_api()

