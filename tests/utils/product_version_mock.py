from res.database import db

MOCK_PRODUCT_TITLE_1 = 'titulo1'
MOCK_PRODUCT_TITLE_2 = 'titulo2'
MOCK_PRODUCT_ID_1 = 1
MOCK_PRODUCT_ID_2 = 2
MOCK_VERSION_CODE_1 = "90.90.90"
MOCK_VERSION_CODE_2 = "70.70.70"
MOCK_RELEASE_NOTE_1 = "esto es una release note 1"
MOCK_RELEASE_NOTE_2 = "esto es una release note 2"

def create_version_and_product_1():

    product_id = db.create_product(MOCK_PRODUCT_TITLE_1)
    db.create_version(
        product_id,
        MOCK_VERSION_CODE_1,
        MOCK_RELEASE_NOTE_1
    )
    return product_id, MOCK_VERSION_CODE_1
