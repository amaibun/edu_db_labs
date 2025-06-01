import uuid
import datetime
import psycopg2

from model.organization import Organization
from model.category import Category
from model.odms_user import ODMSUser
from model.dataset import Dataset
from model.tag import Tag
from model.data_resource import DataResource
from model.access_log import AccessLog
from model.dataset_tag import DatasetTag

from dao.organization_dao import OrganizationDAO
from dao.category_dao import CategoryDAO
from dao.odms_user_dao import ODMSUserDAO
from dao.dataset_dao import DatasetDAO
from dao.tag_dao import TagDAO
from dao.data_resource_dao import DataResourceDAO
from dao.access_log_dao import AccessLogDAO
from dao.dataset_tag_dao import DatasetTagDAO

def main():
    conn = psycopg2.connect(
        dbname="odms_db",
        user="postgres",
        password="postgres",
        host="localhost",
        port=5432
    )

    org_dao = OrganizationDAO(conn)
    cat_dao = CategoryDAO(conn)
    user_dao = ODMSUserDAO(conn)
    dataset_dao = DatasetDAO(conn)
    tag_dao = TagDAO(conn)
    data_res_dao = DataResourceDAO(conn)
    access_log_dao = AccessLogDAO(conn)
    dataset_tag_dao = DatasetTagDAO(conn)

    org = Organization(
        id=uuid.uuid4(),
        name="Open Data Org",
        description="Organization that provides open data.",
        contact_email="contact@opendata.org",
        website="https://opendata.org"
    )
    org_dao.insert(org)
    print("Inserted Organization:", org)

    cat = Category(
        id=uuid.uuid4(),
        name="Transport"
    )
    cat_dao.insert(cat)
    print("Inserted Category:", cat)

    user = ODMSUser(
        id=uuid.uuid4(),
        username="johndoe",
        email="john.doe@example.com",
        role="Publisher"
    )
    user_dao.insert(user)
    print("Inserted User:", user)

    dataset = Dataset(
        id=uuid.uuid4(),
        title="City Transport Routes",
        description="Dataset containing routes for city buses.",
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now(),
        format="CSV",
        license="CC-BY",
        status="Published",
        organization_id=org.id,
        category_id=cat.id,
        user_id=user.id
    )
    dataset_dao.insert(dataset)
    print("Inserted Dataset:", dataset)

    tag = Tag(
        id=uuid.uuid4(),
        name="Bus"
    )
    tag_dao.insert(tag)
    print("Inserted Tag:", tag)

    data_res = DataResource(
        id=uuid.uuid4(),
        file_name="routes.csv",
        file_type="text/csv",
        size=2048,
        url="https://opendata.org/datasets/routes.csv",
        uploaded_at=datetime.datetime.now(),
        dataset_id=dataset.id
    )
    data_res_dao.insert(data_res)
    print("Inserted DataResource:", data_res)

    access_log = AccessLog(
        id=uuid.uuid4(),
        accessed_at=datetime.datetime.now(),
        user_id=user.id,
        dataset_id=dataset.id
    )
    access_log_dao.insert(access_log)
    print("Inserted AccessLog:", access_log)

    dataset_tag = DatasetTag(
        dataset_id=dataset.id,
        tag_id=tag.id
    )
    dataset_tag_dao.insert(dataset_tag)
    print("Inserted DatasetTag:", dataset_tag)

    print("\n--- Querying inserted data ---")

    print("Find Organization by ID:", org_dao.find_by_id(org.id))
    print("Find Category by ID:", cat_dao.find_by_id(cat.id))
    print("Find User by ID:", user_dao.find_by_id(user.id))
    print("Find Dataset by ID:", dataset_dao.find_by_id(dataset.id))
    print("Find Tag by ID:", tag_dao.find_by_id(tag.id))
    print("Find DataResource by ID:", data_res_dao.find_by_id(data_res.id))
    print("Find AccessLog by ID:", access_log_dao.find_by_id(access_log.id))
    print("Find DatasetTags by Dataset ID:", dataset_tag_dao.find_by_dataset(dataset.id))

    conn.close()

if __name__ == "__main__":
    main()
