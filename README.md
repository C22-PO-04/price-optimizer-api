# Price Optimizer API 

This API is intended for the purposes of our capstone project at Bangkit Academy 2022 to solve the study case provided by Traveloka Singapore Company

## Table of Contents

* [Setup](#setup)
* [Routes](#routes)
* [API Documentation](#api-documentation)
* [Contributor](#contributor)

## Setup

To run this project, follow these steps:

- run `pip install -r requirements.txt` to install dependencies
- run `cp .env-example .env`
- setup .env to handle connection with database
- run `flask db init`
- run `flask db migrate`
- run `flask db upgrade`
- run `flask run`

## Routes

*Still work on progress*
| HTTP METHOD | POST            | GET       | PUT         | DELETE |
| ----------- | :-------: | :------:  | :------:  | :------: |
| /users       | - | List Users | - | - |
| /products  | Add product | List Products | - | - |
| /products/`<string:id>`  | - | Detail Product | Update Product | Delete Product |
| /products?page=`<string>` | - | Detail Product per Page | - | - |
| /products?category=`<string>` | - | Detail Product per category | - | - |
| /campaigns  | Add Campaign | List Campaigns | - | - |
| /campaigns/`<int:id>`  | - | - | Update Campaign | Delete Campaign |
| /promos  | Add Promo | List Promos | - | - |
| /promos/`<int:id>`  | - | - | Update Promo | Delete Promo |
| /vouchers  | Add Voucher | List Vouchers | - | - |
| /vouchers/`<int:id>`  | - | - | Update Voucher | Delete Voucher |


## API Documentation 
*Still work on progress*
### List of Endpoints
* [User](#user)
    * [Get All Users](#get-all-users)
* [Product](#product)
    * [Get All Products or By Page](#get-all-products-or-by-page)
    * [Get Products By Category](#get-products-by-category)
    * [Get Product By Id](#get-product-by-id)
    * [Add Product](#add-product)
    * [Update Product](#update-product)
    * [Delete Product](#delete-product)
* [Campaign](#campaign)
    * [Get All Campaigns](#get-all-campaigns)
    * [Add Campaign](#add-campaign)
    * [Update Campaign](#update-campaign)
    * [Delete Campaign](#delete-campaign)
* [Promo](#promo)
    * [Get All Promos](#get-all-promos)
    * [Add Promo](#add-promo)
    * [Update Promo](#update-promo)
    * [Delete Promo](#delete-promo)
* [Voucher](#voucher)
    * [Get All Vouchers](#get-all-vouchers)
    * [Add Voucher](#add-voucher)
    * [Update Voucher](#update-voucher)
    * [Delete Voucher](#delete-voucher)

## User

### Get All Users
* Method : GET
* URL : `/users`    
* Response body  :
```json 
{
    "message": "",
    "values": [
        {
            "id": "000161a058600d5901f007fab4c27140",
            "name": "",
            "voucher": []
        },
        {
            "id": "0001fd6190edaaf884bcaf3d49edf079",
            "name": "",
            "voucher": []
        },
        {
            "id": "000379cdec625522490c315e70c7a9fb",
            "name": "",
            "voucher": []
        },
        {
            "id": "0004164d20a9e969af783496f3408652",
            "name": "",
            "voucher": []
        },
        {
            "id": "000419c5494106c306a97b5635748086",
            "name": "",
            "voucher": []
        }
    ]
}
```


## Product

### Get All Products or By Page
* Method : GET
* URL : `/products` or `/products?page=<int>`    
* Response body  :
```json
{
    "message": "",
    "values": [
        {
            "base_price": 310390.0,
            "competitor_price": null,
            "created_at": "Sun, 20 May 2018 18:45:21 GMT",
            "discount": 0.0,
            "final_price": 310390.0,
            "id": "00066f42aeeb9f3007548bb9d3f33c38",
            "name": "",
            "product_category": "perfumery",
            "updated_at": "Sun, 20 May 2018 18:45:21 GMT"
        },
        {
            "base_price": 396652.0,
            "competitor_price": null,
            "created_at": "Tue, 12 Dec 2017 19:20:28 GMT",
            "discount": 0.0,
            "final_price": 396652.0,
            "id": "00088930e925c41fd95ebfe695fd2655",
            "name": "",
            "product_category": "auto",
            "updated_at": "Tue, 12 Dec 2017 19:20:28 GMT"
        },
        {
            "base_price": 699256.0,
            "competitor_price": null,
            "created_at": "Thu, 21 Dec 2017 16:21:47 GMT",
            "discount": 0.0,
            "final_price": 699256.0,
            "id": "0009406fd7479715e4bef61dd91f2462",
            "name": "",
            "product_category": "bed_bath_table",
            "updated_at": "Thu, 21 Dec 2017 16:21:47 GMT"
        },
        {
            "base_price": 179852.0,
            "competitor_price": null,
            "created_at": "Wed, 01 Aug 2018 22:00:33 GMT",
            "discount": 0.0,
            "final_price": 179852.0,
            "id": "000b8f95fcb9e0096488278317764d19",
            "name": "",
            "product_category": "housewares",
            "updated_at": "Fri, 10 Aug 2018 13:24:35 GMT"
        },
        {
            "base_price": 607650.0,
            "competitor_price": null,
            "created_at": "Tue, 03 Apr 2018 09:24:12 GMT",
            "discount": 0.0,
            "final_price": 607650.0,
            "id": "000d9be29b5207b54e86aa1b1ac54872",
            "name": "",
            "product_category": "watches_gifts",
            "updated_at": "Tue, 03 Apr 2018 09:24:12 GMT"
        }
    ]
}
```
### Get Products By Category
* Method : GET
* URL : `/products?category=<string>`    
* Response body  :
```json
{
    "message": "",
    "values": [
        {
            "base_price": 396652.0,
            "competitor_price": null,
            "created_at": "Tue, 12 Dec 2017 19:20:28 GMT",
            "discount": 0.0,
            "final_price": 396652.0,
            "id": "00088930e925c41fd95ebfe695fd2655",
            "name": "",
            "product_category": "auto",
            "updated_at": "Tue, 12 Dec 2017 19:20:28 GMT"
        },
        {
            "base_price": 158783.0,
            "competitor_price": null,
            "created_at": "Thu, 14 Dec 2017 20:30:29 GMT",
            "discount": 0.0,
            "final_price": 158783.0,
            "id": "0011c512eb256aa0dbbb544d8dffcf6e",
            "name": "",
            "product_category": "auto",
            "updated_at": "Thu, 14 Dec 2017 20:30:29 GMT"
        },
        {
            "base_price": 182906.0,
            "competitor_price": null,
            "created_at": "Sat, 19 May 2018 14:46:42 GMT",
            "discount": 0.0,
            "final_price": 182906.0,
            "id": "006c67546bfe73c33b83f6bd1ad58c36",
            "name": "",
            "product_category": "auto",
            "updated_at": "Sat, 19 May 2018 14:46:42 GMT"
        },
        {
            "base_price": 2900540.0,
            "competitor_price": null,
            "created_at": "Mon, 14 May 2018 21:03:30 GMT",
            "discount": 0.0,
            "final_price": 2900540.0,
            "id": "009df2b0bc078648fc4f5898de8cabff",
            "name": "",
            "product_category": "auto",
            "updated_at": "Mon, 14 May 2018 21:03:30 GMT"
        },
        {
            "base_price": 393935.0,
            "competitor_price": null,
            "created_at": "Mon, 30 Jul 2018 18:41:35 GMT",
            "discount": 0.0,
            "final_price": 393935.0,
            "id": "00b264091d1c8df03976c3f3b176b35c",
            "name": "",
            "product_category": "auto",
            "updated_at": "Mon, 30 Jul 2018 18:41:35 GMT"
        }
    ]
}
```

### Get Product By Id
* Method : GET
* URL : `/products/<string:id>`    
* Response body  :
```json
{
    "message": "",
    "values": {
        "base_price": 310390.0,
        "competitor_price": 0,
        "created_at": "Sun, 20 May 2018 18:45:21 GMT",
        "id": "00066f42aeeb9f3007548bb9d3f33c38",
        "name": "",
        "product_category": "perfumery",
        "updated_at": "Sun, 20 May 2018 18:45:21 GMT"
    }
}
```

### Add Product
* Method : POST
* URL : `/products`    
* Request body :
```json
{
    "name" : "jaket erigo",
    "base_price" : 159000,
    "product_category" : "Pakaian"
}
```
* Response body:
```json
{
    "message": "Product added",
    "values": ""
}
``` 

### Update Product
* Method : PUT
* URL : `/products/<string:id>`       
* Request body:
```json
{
    "name" : "baju",
    "base_price" : 140000
}
```
* Response body:
`status code 201`
```json
{
    "message": "successfully updated",
    "values": ""
}
```

### Delete Product
* Method : DELETE
* URL : `/products/<string:id>`    
* Response body :
```json
{
    "message": "product deleted",
    "values": ""
}
```



## Campaign
### Get All Campaigns
* Method : GET
* URL : `/campaigns`    
* Response body :
```json
{
    "message": "",
    "values": [
        {
            "created_at": "Thu, 02 Jun 2022 14:23:12 GMT",
            "end_date": "Tue, 10 May 2022 00:00:00 GMT",
            "every_weekend": false,
            "id": 1,
            "is_active": false,
            "name": "Back to School",
            "periodical": true,
            "promo": [
                {
                    "campaign_id": 1,
                    "category_name": "peralatan alat tulis",
                    "created_at": "Thu, 02 Jun 2022 14:41:33 GMT",
                    "discount": 0.1,
                    "id": 1,
                    "max_discount": 10000.0,
                    "name": "Diskon Alat Tulis",
                    "updated_at": "Thu, 02 Jun 2022 14:41:33 GMT"
                }
            ],
            "start_date": "Sun, 01 May 2022 00:00:00 GMT",
            "updated_at": "Thu, 02 Jun 2022 14:23:12 GMT"
        }
    ]
}
```

### Add Campaign
* Method : POST
* URL : `/campaigns`    
* Request body :
```json
{
    "name" : "Back to School",
    "start_date" : "2022-05-01",
    "end_date" : "2022-05-10",
    "periodical" : true,
    "every_weekend" : false

}
```
* Response body:
```json
{
    "message": "Campaign added",
    "values": ""
}
``` 

### Update Campaign
* Method : PUT
* URL: `/campaigns/<int:id>`
* Request body:
```json
{
    "name" : "Back to School 2022",
    "category_name" : "peralatan alat tulis",
    "start_date" : "2022-05-01",
    "end_date" : "2022-05-10",
    "periodical" : true,
    "every_weekend" : true,
    "is_active" : true

}
```
* Response body :
`status code 201`
```json
{
    "message": "successfully updated",
    "values": ""
}
```
`status code 400`
```json
{
    "message": "campaign not found",
    "values": ""
}
```

### Delete Campaigns
* Method : DELETE
* URL : `/campaigns<int:id>`    
* Response body :
```json
{
    "message": "campaign deleted",
    "values": ""
}
```

### Change Active
* Method : PUT
* URL: `/campaigns/<int:id>/change_active`
* Request body:
```json
{
    "is_active" : true
}
```
* Response body :
`status code 201`
```json
{
    "message": "Campaign Turned ON",
    "values": ""
}
```


## Promo
### Get All Promos
* Method : POST
* URL: `/promos`
* Response body:
```json
{
    "message": "",
    "values": [
        {
            "campaign_id": 1,
            "category_name": "peralatan alat tulis",
            "created_at": "Thu, 02 Jun 2022 14:41:33 GMT",
            "discount": 0.1,
            "id": 1,
            "max_discount": 10000.0,
            "name": "Diskon Alat Tulis",
            "updated_at": "Thu, 02 Jun 2022 14:41:33 GMT"
        }
    ]
}
```

### Add Promo
* Method : POST
* URL: `/promos`
* Request body:
```json
{
    "name": "Diskon Alat Tulis",
    "discount" : 0.1,
    "category_name": "peralatan alat tulis",
    "campaign_id" : 1,
    "max_discount": 10000
}
```
* Response body:
```json
{
    "message": "Promo added",
    "values": ""
}
```

### Update Promo
* Method : PUT
* URL: `/promos/<int:id>`
* Request body:
```json
{
    "name": "Diskon Alat Tulis",
    "category_name" : "Peralatan Alat Tulis",
    "discount" : 0.2,
    "max_discount": 5000
}
```
* Response body:
`if succeed`
```json
{
    "message": "successfully updated",
    "values": ""
}
```
`if total discount reach 100%`
```json
{
    "message": "successfully updated",
    "values": "Discount reach 100%"
}
```
`else`
```json
{
    "message": "Bad request",
    "values": "error"
}
```

### Delete Promo
* Method : DELETE
* URL : `/promos/<int:id>`    
* Response body :
```json
{
    "message": "promo deleted",
    "values": ""
}
```

## Voucher
*Still work on progress*
### Get All Vouchers
* Method : GET
* URL: `/vouchers`
* Response body:
```json
{
    "message": "",
    "values": [
        {
            "budget": 100000,
            "category_name": "perfumery",
            "created_at": "Tue, 07 Jun 2022 17:30:07 GMT",
            "discount_percent": 0.1,
            "experied_date": "Mon, 10 Oct 2022 00:00:00 GMT",
            "id": 1,
            "name": "Voucher parfum",
            "updated_at": "Tue, 07 Jun 2022 17:30:07 GMT"
        }
    ]
}
```
### Add Voucher
* Method : POST
* URL: `/vouchers`
* Request body:
```json
{
    "name": "Voucher parfum",
    "category_name": "perfumery",
    "discount_percent": 0.1,
    "experied_date": "2022-10-10",
    "budget": 100000
}
``` 
* Response body:
```json
{
    "message": "Voucher added",
    "values": ""
}
```

### Update Voucher
* Method : PUT
* URL: `/vouchers/<int:id>`
* Request body:
```json
{
    "name": "Voucher parfum",
    "category_name": "perfumery",
    "discount_percent": 0.2,
    "experied_date": "2022-10-10",
    "budget": 100000
}
```
* Response body:
```json
{
    "message": "Voucher added",
    "values": ""
}
```
`if not found`
```json
{
    "message": "",
    "values": [
        {
            "budget": 100000,
            "category_name": "perfumery",
            "created_at": "Tue, 07 Jun 2022 17:30:07 GMT",
            "discount_percent": 0.1,
            "experied_date": "Mon, 10 Oct 2022 00:00:00 GMT",
            "id": 1,
            "name": "Voucher parfum",
            "updated_at": "Tue, 07 Jun 2022 17:30:07 GMT"
        }
    ]
}
```
### Delete Voucher
* Method : DELETE
* URL: `/vouchers/<int:id>`
* Response body:
```json
{
    "message": "Vocuher deleted",
    "values": ""
}
```


## Status Code
returns the following status codes in its API:

| Status Code | Description |
| :--- | :--- |
| 200 | `OK` |
| 201 | `CREATED` |
| 400 | `BAD REQUEST` |

<br>

## Contributor

1. Diva Ratna Kumala Ardellia (C2006F0502)
2. Sarah Uli Octavia          (C7006F0503)
3. Yulyano Thomas Djaya       (C20090F998)


