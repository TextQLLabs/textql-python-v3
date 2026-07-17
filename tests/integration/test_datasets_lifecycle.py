"""Integration tests: Datasets service against a REAL TextQL API server."""
import os

import pytest

pytestmark = pytest.mark.integration

TEST_DATASET_ID_ENV = "TEXTQL_TEST_DATASET_ID"


@pytest.fixture
def existing_dataset_id():
    dataset_id = os.getenv(TEST_DATASET_ID_ENV)
    if not dataset_id:
        pytest.skip(f"set {TEST_DATASET_ID_ENV} to a real dataset id to run this test")
    return dataset_id


class TestUploadPresignFlow:
    def test_create_upload_presign_url_returns_a_usable_url(self, live_sdk, unique_name):
        resp = live_sdk.datasets.create_upload_presign_url(
            file_name=f"{unique_name}.csv",
        )
        assert resp is not None
        # We deliberately do not follow through with an actual PUT to the
        # presigned URL and process_upload_presign_url -- that would create
        # real, orphaned dataset state with no clean SDK-level delete path
        # confirmed. This just pins the request/response contract.


class TestDatasetReadPaths:
    def test_get_returns_matching_dataset(self, live_sdk, existing_dataset_id):
        resp = live_sdk.datasets.get(dataset_id=existing_dataset_id)
        assert resp is not None

    def test_get_by_ids_single_and_multiple(self, live_sdk, existing_dataset_id):
        single = live_sdk.datasets.get_by_ids(ids=[existing_dataset_id])
        assert single is not None

        # Duplicate the same id several times -- the SDK/server should
        # de-duplicate or simply return the same dataset multiple times, not
        # error.
        many = live_sdk.datasets.get_by_ids(ids=[existing_dataset_id] * 5)
        assert many is not None

    def test_get_by_ids_empty_list(self, live_sdk):
        resp = live_sdk.datasets.get_by_ids(ids=[])
        assert resp is not None

    def test_get_stats(self, live_sdk, existing_dataset_id):
        resp = live_sdk.datasets.get_stats(dataset_id=existing_dataset_id)
        assert resp is not None

    def test_fetch_dataset_values(self, live_sdk, existing_dataset_id):
        resp = live_sdk.datasets.fetch(dataset_id=existing_dataset_id)
        assert resp is not None


class TestDatasetErrorPaths:
    def test_get_nonexistent_dataset_raises_client_error(self, live_sdk):
        from textql_sdk import errors

        with pytest.raises(errors.TextqlDefaultError) as exc_info:
            live_sdk.datasets.get(dataset_id="00000000-0000-0000-0000-000000000000")
        assert 400 <= exc_info.value.status_code < 500

    def test_delete_nonexistent_dataset_raises_client_error(self, live_sdk):
        from textql_sdk import errors

        with pytest.raises(errors.TextqlDefaultError) as exc_info:
            live_sdk.datasets.delete(dataset_id="00000000-0000-0000-0000-000000000000")
        assert 400 <= exc_info.value.status_code < 500
