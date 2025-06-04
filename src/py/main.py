import uuid
import datetime
import psycopg2

from Objects.Organization import Organization
from Objects.Category import Category
from Objects.ODMS_User import ODMSUser
from Objects.Dataset import Dataset
from Objects.Tag import Tag
from Objects.DataResource import DataResource
from Objects.AccessLog import AccessLog
from Objects.DatasetTag import DatasetTag

from DBF.dbfOrganization import dbf_Organization
from DBF.dbfCategory import dbf_Category
from DBF.dbf_ODMS_User import dbf_ODMSUser
from DBF.dbfDataset import dbf_Dataset
from DBF.dbfTag import dbf_Tag
from DBF.dbfDataResource import dbf_DataResource
from DBF.dbfAccessLog import dbf_AccessLog
from DBF.dbfDatasetTag import dbf_DatasetTag


def main():
    connection = psycopg2.connect(
        dbname="odms_db",
        user="postgres",
        password="postgres",
        host="localhost",
        port=5432
    )

    organization_dao = dbf_Organization(connection)
    category_dao = dbf_Category(connection)
    user_dao = dbf_ODMSUser(connection)
    dataset_dao = dbf_Dataset(connection)
    tag_dao = dbf_Tag(connection)
    resource_dao = dbf_DataResource(connection)
    log_dao = dbf_AccessLog(connection)
    dataset_tag_dao = dbf_DatasetTag(connection)

    organization = Organization(
        id=uuid.uuid4(),
        name="Geo Analytics Lab",
        description="Research lab focused on geospatial data analysis.",
        contact_email="info@geoanalytics.org",
        website="https://geoanalytics.org"
    )
    organization_dao.insert(organization)
    print("Inserted Organization:", organization)

    category = Category(
        id=uuid.uuid4(),
        name="Environment"
    )
    category_dao.insert(category)
    print("Inserted Category:", category)

    user = ODMSUser(
        id=uuid.uuid4(),
        username="alicegreen",
        email="alice.green@geoanalytics.org",
        role="Administrator"
    )
    user_dao.insert(user)
    print("Inserted User:", user)

    dataset = Dataset(
        id=uuid.uuid4(),
        title="Air Quality Measurements",
        description="Hourly air pollution data collected from urban stations.",
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now(),
        format="JSON",
        license="MIT",
        status="Draft",
        organization_id=organization.id,
        category_id=category.id,
        user_id=user.id
    )
    dataset_dao.insert(dataset)
    print("Inserted Dataset:", dataset)

    tag = Tag(
        id=uuid.uuid4(),
        name="AirPollution"
    )
    tag_dao.insert(tag)
    print("Inserted Tag:", tag)

    resource = DataResource(
        id=uuid.uuid4(),
        file_name="air_quality_2024.json",
        file_type="application/json",
        size=5120,
        url="https://geoanalytics.org/data/air_quality_2024.json",
        uploaded_at=datetime.datetime.now(),
        dataset_id=dataset.id
    )
    resource_dao.insert(resource)
    print("Inserted DataResource:", resource)

    access_log = AccessLog(
        id=uuid.uuid4(),
        accessed_at=datetime.datetime.now(),
        user_id=user.id,
        dataset_id=dataset.id
    )
    log_dao.insert(access_log)
    print("Inserted AccessLog:", access_log)

    dataset_tag = DatasetTag(
        dataset_id=dataset.id,
        tag_id=tag.id
    )
    dataset_tag_dao.insert(dataset_tag)
    print("Inserted DatasetTag:", dataset_tag)

    print("\n--- Querying inserted data ---")
    print("Find Organization by ID:", organization_dao.find_by_id(organization.id))
    print("Find Category by ID:", category_dao.find_by_id(category.id))
    print("Find User by ID:", user_dao.find_by_id(user.id))
    print("Find Dataset by ID:", dataset_dao.find_by_id(dataset.id))
    print("Find Tag by ID:", tag_dao.find_by_id(tag.id))
    print("Find DataResource by ID:", resource_dao.find_by_id(resource.id))
    print("Find AccessLog by ID:", log_dao.find_by_id(access_log.id))
    print("Find DatasetTags by Dataset ID:", dataset_tag_dao.find_by_dataset(dataset.id))

    connection.close()


if __name__ == "__main__":
    main()
