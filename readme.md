# Jotform prefiller

Thi simple  script allows for the prefilling of a Jotform form based on pre-existing data.
The use case is the following: each year we want to renew the subscription to an association and want to save people time when renewing.
So, when we send the email to ask them to renew, there is a link to the prefilled form.

## Usage

Use a data set in a CSV file. The data set should live in the same folder as your script.
Fill the relative information in the configuration (`data_map` and `form_url`) before running the script.
Start the script with `python jotform_prefiller.py`.

Pay attention to the `main_email_field` field. It's the key that will be used to build the output CSV.


## Configuration


Copy and rename the file `settings_sample.json` to `settings.json`.

### Files
Enter the name of the input file and output file. You can place them in subfolder, but be sure to have the path relative to the script. Example:

```
# In the same folder as the script
"data_set_file": "users_data.csv",
"output_file": "email_link.csv"

# OR
# In subfolder "2016"
"data_set_file": "2016/users_data.csv",
"output_file": "2016/email_link.csv"
```

### Data Mapping
Edit the file settings.json to match the fields you have in your form with the CSV file in input.

We are working with Python, so the first field has a `0` index (and not `1`)

### Phone numbers
Jotform doesn't save phone numbers (but integers). So if your country has phone numbers prefixed with `0` (as in France, a typical phone number here looks like: `06 XX XX XX XX`), the value is wrong.

The script will add a `0` prefix to the all elements listed in `phone_numbers` field.


### Minification (Optional)

Create an API key in [Google Developer console](https://console.developers.google.com/apis/credentials) for Goo.gl url shortener. Open `settings.json` and update the field `google_shortener_api_key` with the corresponding value.


