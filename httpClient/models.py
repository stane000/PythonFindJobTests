

from dataclasses import dataclass
from enum import Enum
import random   
from faker import Faker
from typing import Dict, List, Optional


class Position(Enum):
    SoftwareEngineer = 0,
    SoftwareTestEngineer = 1,
    FrontEndDeveloper = 2,
    BackEndDeveloper = 3,
    FullStackDeveloper = 4,

    JuniorSoftwareEngineer = 5,
    JuniorSoftwareTestEngineer  = 6,
    JuniorFrontEndDeveloper = 7, 
    JuniorBackEndDeveloper = 8, 
    JuniorFullStackDeveloper = 9,

    SeniorSoftwareEngineer = 10,
    SeniorSoftwareTestEngineer = 11,
    SeniorFrontEndDeveloper = 12,
    SeniorBackEndDeveloper = 13,
    SeniorFullStackDeveloper = 14,

    ProjectManager = 15

class Collage(Enum):
    TVZ = 0,
    FER = 1,
    PMF = 2,
    ALGEBRA = 3,
    FESB = 4

@dataclass
class Company:

    id: int
    name: str
    avgSalary: int
    workers: List
    hiring: bool
    jobs: []

    @classmethod
    def create(cls, name, avgSalary, workers, hiring, jobs):   
        return cls(0, name, avgSalary, workers, hiring, jobs) 
    
    @classmethod
    def create_form_json(cls, company: Dict):
        return cls(company["id"], company["name"], company["avgSalary"], company["workers"], company["hiring"], company["jobs"])
    
    @staticmethod
    def create_fake_company():
        fake = Faker()
        # Generate a fake Company instance
        return Company.create(
                name=fake.company(),
                avgSalary=fake.random_int(min=0, max=1000),
                workers=[],
                hiring=fake.boolean(),
                jobs=[]
            )
    
    def change_random_property(self):
   
        # Select a random property name, no Id included
        random_property_name = random.choice(["name", "avgSalary", "hiring"])

        # Assuming property is an integer, you can change it to a new random value
        if random_property_name == "hiring":
            setattr(self, random_property_name, not getattr(self, random_property_name))
        elif random_property_name == "avgSalary":
            setattr(self, random_property_name, random.randint(1, 1000))  # Change to a random integer value
        elif random_property_name == "name":
            setattr(self, random_property_name, Faker().text(max_nb_chars=100))  # Change to a string value for non-integer properties
    
        self.workers = None
        self.jobs = None
        print(f"Changed {random_property_name} to: {getattr(self, random_property_name)}")

@dataclass
class Job:
    
    id: int
    company: Company
    position: Position
    experience: int
    collage: Collage

    @classmethod
    def create(cls, company, position, experience, collage):   
        return cls(0, company, position, experience, collage) 

    @classmethod
    def create_fake_job(cls, company: Company):  
        fake = Faker()
        # Generate a fake Job instance
        return cls(
                id=0,
                company=company,
                position= random.choice(list(Position)),
                experience=fake.random_int(min=0, max=35),
                collage= random.choice(list(Position)
            ))
    
@dataclass
class Worker:

    id: int
    firstName: str
    lastName: str
    age: int
    college: str
    position: str
    experience: int
    lookingForJob: bool	
    companyName: str

    @classmethod
    def create(cls, firstName: str, lastName: str, age: int, college: str, position: str, 
               experience: int, lookingForJob: bool, companyName: str):
        return cls(0, firstName, lastName, age, college, position, 
                   experience, lookingForJob, companyName)  
    
    @classmethod
    def create_fake_worker(cls, company: Company):  
        fake = Faker()
        # Generate a fake Job instance
        return cls(
                id=0,
                firstName=fake.first_name(),
                lastName=fake.last_name(),
                age=fake.random_int(min=0, max=65),
                college= random.choice(list(Collage)).name,
                position= random.choice(list(Position)).name,
                experience=fake.random_int(min=0, max=35),
                lookingForJob=fake.boolean(), 
                companyName=company.name
            )
    

