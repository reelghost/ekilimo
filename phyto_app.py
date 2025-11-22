import cloudscraper


# apply_url = "https://ekilimo.kilimo.go.tz/gateway/ikmis-license-permit-billing-service/api/v1/application"
apply_url = "https://ekilimo.kilimo.go.tz/gateway/ikmis-license-permit-billing-service/api/v1/atmis-application"

get_applicants_url = "https://ekilimo.kilimo.go.tz/gateway/ikmis-license-permit-billing-service/api/v1/tmx/get-applicants"
payl = {"pageNo":0,"pageSize":10,"applicantUuid":"519fd962-8467-4584-ac9f-807f465a6880","search":""}
payload = {
    "institutionId":23,
    "applicationTypeUuid":"e01af0b1-5270-42d2-9842-9ab9cc1ab3ac",
    "status":"SUBMITTED",
    "cropUuid":"ba44dbda-6618-48c0-b950-c89689119abc",
    "productUuid":"18e2d8b7-4cdb-4d83-941c-bc2099b471e8",
    "quantity":2759,
    "uomUuid":"9b6fbe86-df95-43db-ab1f-626b0320e5d1",
    "invoiceAmount":0,
    "previousExpiryDate":"",
    "listOfGrades":[{"grade":"","quantity":"","uomUuid":"","fobPrice":"","currency":""}],
    "seasonStartDate":"",
    "exitStationUuid":"082a40bf-cf1c-4ead-aa70-abc6ccd18305",
    "inspectionElements":[{"785ac04d-7c49-486d-a5e9-b60f28bfbdbb":"luke hussein"},{"434a89f4-084e-4c0e-969d-52e944a2ef86":"nyatika ytandei"},{"cdb0ec83-dd62-40cf-8d1e-63bea7ecdf74":"Port of Entry"},{"0816afbf-9120-46ec-9c5d-fe0f8a84839c":"2025-11-17"},{"02a23cb5-155f-4f12-9bcc-36b619ca2f89":"Holili Border Post"},{"50be713a-f56f-4c5b-aee8-0a3f78b23789":"holili"},{"4d003961-74ba-4569-8960-d4e24d6deb75":"10"},{"0501b23d-ab73-40cd-b233-bcc21f397802":"Bags "},{"085ba8bd-3cd5-4945-9246-f2fc656fe2df":""},{"83e4b02b-38f8-4cba-ab05-9497829d59e9":"Road transport "},{"3220cca6-e604-4f5c-8dc1-aff92e3366c6":"holili"},{"faea000c-05cb-48be-9b7c-f6ee371e2c03":"For non-commercial consignment"},{"747235b7-25b5-4e23-8c2a-cc35301d7df6":"Tanzania"},{"0701bd75-8f91-4192-8dd2-f80e3cab005d":"Kenya"}],
    "scientificName":"Nicotiana tabacum",
    "institutionName":"Institution",
    "visibleToApplicant":True,
    "applicantUuid":"519fd962-8467-4584-ac9f-807f465a6880"
}
headers = {
    "Authorization": "Bearer CCNp2ym24Rkmb7zzKqKPJmsI0BcYBa6ZkJI7OzZotNVVBJT2cQ2xJmcVLi3TKmw1BNhZVIRqCpHEG6n9qcWtbPjQhblFjVdwwpb9olUhMHhfWJou1rDTLHGqdmPnWQHN",
    "Content-Type": "application/json",
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "x-request-source": "web"
}


scraper = cloudscraper.create_scraper()
# resp = scraper.post(apply_url, json=payload, headers=headers)
resp = scraper.post(apply_url, json=payload, headers=headers)
print(resp.text)