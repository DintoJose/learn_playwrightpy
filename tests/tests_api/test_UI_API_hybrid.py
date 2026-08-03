import allure
from playwright.sync_api import expect, Page, APIRequestContext



def test_hybrid_create_and_verify_account(page: Page, api_request_context: APIRequestContext):
    # Step 1 — Create account via API
    with allure.step("Create account via API"):
        response = api_request_context.post(
            "/api/createAccount",
            form={
                "name": "Test User1221",
                "email": "hybridtest@email.com",
                "password": "test1234",
                "title": "Mr",
                "birth_date": "01",
                "birth_month": "01",
                "birth_year": "1990",
                "firstname": "Test",
                "lastname": "User",
                "company": "Test Co",
                "address1": "123 Test St",
                "address2": "add2",
                "country": "India",
                "zipcode": "560001",
                "state": "Karnataka",
                "city": "Bangalore",
                "mobile_number": "9999999999"
            }
        )
        assert response.ok
        assert response.json()["responseCode"] == 201
        assert response.json()["message"] == "User created!"

    # Step 2 — Verify account exists via API through POST and GET requests
    with allure.step("Verify account exists via API"):
        verify = api_request_context.post(
            "/api/verifyLogin",
            form={"email": "hybridtest@email.com", "password": "test1234"}
        )
        assert verify.json()["responseCode"] == 200
        assert verify.json()["message"] == "User exists!"

    with allure.step("Get user details via API"):
        get_user = api_request_context.get(
            "/api/getUserDetailByEmail",
            params={"email": "hybridtest@email.com"}
        )
        assert get_user.json()["responseCode"] == 200
        assert get_user.json()["user"]["name"] == "Test User1221"

    # Step 3 — Login through UI using the API-created account and do UI actions as the API-created user
    with allure.step("Login through UI using the API-created account"):
        page.goto("https://automationexercise.com/login")
        page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").fill("hybridtest@email.com")
        page.get_by_role("textbox", name="Password").fill("test1234")
        page.get_by_role("button", name="Login").click()
        expect(page.get_by_text("Logged in as Test User1221")).to_be_visible()

        page.get_by_role("link", name="Products").click()
        expect(page).to_have_title("Automation Exercise - All Products")

    # Step 4 — Cleanup: delete account via API after test
    with allure.step("Cleanup: delete account via API after test"):
        delete = api_request_context.delete(
            "/api/deleteAccount",
            form={"email": "hybridtest@email.com", "password": "test1234"}
        )
        assert delete.json()["responseCode"] == 200
        assert delete.json()["message"] == "Account deleted!"

    # Step 5 — Check if login possible through UI after account deletion
    with allure.step("Check if login possible through UI after account deletion"):
        page.goto("https://automationexercise.com/login")
        page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").fill("hybridtest@email.com")
        page.get_by_role("textbox", name="Password").fill("test1234")
        page.get_by_role("button", name="Login").click()
        expect(page.get_by_text("Your email or password is")).to_be_visible()