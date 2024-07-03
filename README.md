1. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

2. Configure the API keys in the `.env` file:
    ```
    openai_api_key=your_openai_api_key
    firecrawl_api_key=your_firecrawl_api_key
    ```

3. Configure the Graph API in `jobPostingAgent/tools/PostJobDescriptionsOnFacebook.py`:
    ```python
    # page_access_token: str = Field(
    default="EAAOeanJcLZAQBO3Qmcb9lEuMhqQX236ClEXv9Hfc71aziFgrLRD57U3OoPLJ0keRaUYbDI27dBQB69KPLWpFa1e3TPAq2A9EPjm1mzoZBysxEA01bGQNOk8v4ir6r1txfQPGyCzoGLUHwlrVZBZCFEKWIiB1qlzSfCYwZBgAfxatdZCjNQ5ngJHNS2TEz0LGtcW9ZB7nE5WHmtmQZCMcusURcqWZAKNl3BGBD",
    description="The Facebook Page Access Token used to authenticate the API requests."
    )

    page_id: str = Field(
    default="371375712720815",
    description="The ID of the Facebook page where the job descriptions will be posted."
    )
    ```

4. Run the main script:
    ```bash
    python main.py
    ```

5. Open your browser and go to `localhost` to see the Gradio interface. You can enter a prompt like "I wanna hire a senior Python developer," and it will automatically post the job description on Facebook.
