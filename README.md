# Numbers API

This is a public API developed for the HNG12 Stage 1 Backend task. It takes a number as input and returns interesting mathematical properties about it, along with a fun fact.

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/Ayobamidele/numbers_api.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the API locally

```bash
uvicorn main:app --reload
```

or

```bash
fastapi dev
```

### API Documentation

## Endpoint

**GET** `/api/classify-number`

### Query Parameters

- `number` (required): The number to classify.

### Example Request

```bash
GET http://127.0.0.1:8000/api/classify-number?number=371
```

### Response

```json
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### Error Response (400 Bad Request)

If a non-integer value is passed in the number parameter:

```json
{
  "number": "alphabet",
  "error": true
}
```

## Example Usage

Here’s an example of how to use the API:

![Numbers API](/assets/image.png)

This image shows how the API returns the expected JSON response when you make a `GET` request.
