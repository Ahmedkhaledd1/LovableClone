from pydantic import BaseModel,Field

class File(BaseModel):
    name: str = Field(..., description="The patjh of the file to be created or modified")
    purpose: str = Field(..., description="The purpose of the file")


class Plan(BaseModel):
    name: str = Field(..., description="Name of the project")
    description: str = Field(..., description="Description of the project")
    techstack: str = Field(..., description="Technology stack to be used")
    features: list[str] = Field(..., description="List of features to be implemented")
    files: list[File] = Field(..., description="List of files to be created")
