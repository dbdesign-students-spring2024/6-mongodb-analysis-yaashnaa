# AirBnB MongoDB Analysis

#Data Set Details 

The dataset used for this analysis was taken from the official AirBnb, specifically airbnb listings in Rhode Island, United States. 

[Link to source](https://insideairbnb.com/get-the-data/)

The data was in CSV format. 

## Raw data

| id    | name                                           | host_name | neighbourhood_cleansed | room_type       | price  | minimum_nights | maximum_nights | number_of_reviews | review_scores_rating |
|-------|------------------------------------------------|-----------|------------------------|-----------------|--------|----------------|----------------|-------------------|----------------------|
| 10262 | Home in Glocester · ★5.0 · 1 bedroom · 1 bed... | Paula     | Glocester              | Private room    | $65.00 | 1              | 7              | 37                | 5.0                  |
| 15373 | Home in Narragansett · ★4.83 · 13 bedrooms ·... | Brian     | Narragansett           | Entire home/apt | $475.00| 7              | 256            | 6                 | 4.83                 |
| 50791 | Rental unit in Providence · ★4.88 · 2 bedroo... | Martina   | Providence             | Entire home/apt | $192.00| 2              | 270            | 86                | 4.88                 |
| 50817 | Rental unit in Pawtucket · ★4.72 · 2 bedrooms...| Nancy     | Pawtucket              | Entire home/apt | $93.00 | 3              | 1125           | 162               | 4.72                 |
| 51583 | Rental unit in Providence · ★4.78 · 1 bedroom...| Chip      | Providence             | Private room    | $66.00 | 2              | 365            | 433               | 4.78                 |
| ...   | ...                                            | ...       | ...                    | ...             | ...    | ...            | ...            | ...               | ...                  |

## Problems in the dataset 

- **Textual Data Inconsistency:** Fields like name, description, host_name, and neighborhood_overview had inconsistent capitalizations.
- **Percentage Strings:** The host_response_rate and host_acceptance_rate fields contained percentage values as strings, not suitable for numerical operations.
- **Boolean Values as Strings:** The host_is_superhost field used 't'/'f' strings to represent boolean values.
- **Numeric Field Errors:** Fields intended to be numeric, such as latitude, longitude, and price, contained non-numeric characters or were improperly formatted.
**Date Format Issues:** Date fields like host_since and last_scraped needed to be in a consistent 'YYYY-MM-DD' format for analysis.

## Scrubbing performed

[Scrubbing File](./scrubbing.py)
### Text Normalization
Convert all text fields to lowercase to ensure consistency.

```
def normalize_text(text):
    return text.lower()
```

### Convert Percentages to Decimals

```
def convert_percentage_to_decimal(percentage):
    if percentage.endswith('%'):
        return str(float(percentage.replace('%', '')) / 100)
    return percentage
```
### Convert Strings to Boolean Values

```
def convert_to_boolean(text):
    if text == 't':
        return 'True'
    elif text == 'f':
        return 'False'
    return text

```
### Validate Numeric Fields

```
def validate_numeric(field):
    try:
        return str(float(field))
    except ValueError:
        return ''
```

### Date validation 

```
def format_date(date_string):
    return date_string
```



# Analysis performed 

### 1. Show exactly two documents from the `listings` collection in any order

### Code 
```
db.listing.find().limit(2)
```
### Result

---
```
[
  {
    _id: ObjectId('660c6787b55bac758d387a65'),
    id: 10262,
    listing_url: 'https://www.airbnb.com/rooms/10262',
    scrape_id: Long('20231230181051'),
    last_scraped: '2023-12-30',
    source: 'city scrape',
    name: 'home in glocester · ★5.0 · 1 bedroom · 1 bed · 1 shared bath',
    description: '',
    neighborhood_overview: 'the peace and quiet, nature, ponds, hiking trails, antique shops, proximity to providence.......',
    picture_url: 'https://a0.muscache.com/pictures/42287/55a1cad0_original.jpg',
    host_id: 35244,
    host_url: 'https://www.airbnb.com/users/show/35244',
    host_name: 'paula',
    host_since: '2009-08-31',
    host_location: 'Glocester, RI',
    host_about: 'We enjoy people,conversation, growing and cooking good food, bicycling, kayaking, x-country skiing, dogs and cats. We love the area we live in and are happy to share our favorite spots with visitors. The music scene,good cycling, hiking, ethnic food, art museums and the ocean are what keeps us living here. ',
    host_response_time: 'within an hour',
    host_response_rate: 1,
    host_acceptance_rate: 0,
    host_is_superhost: 'False',
    host_thumbnail_url: 'https://a0.muscache.com/im/users/35244/profile_pic/1387981588/original.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/users/35244/profile_pic/1387981588/original.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: '',
    host_listings_count: 1,
    host_total_listings_count: 1,
    host_verifications: "['email', 'phone']",
    host_has_profile_pic: 't',
    host_identity_verified: 't',
    neighbourhood: 'Glocester, Rhode Island, United States',
    neighbourhood_cleansed: 'Glocester',
    neighbourhood_group_cleansed: 'Providence',
    latitude: 41.86683,
    longitude: -71.72481,
    property_type: 'Private room in home',
    room_type: 'Private room',
    accommodates: 2,
    bathrooms: '',
    bathrooms_text: '1 shared bath',
    bedrooms: '',
    beds: 1,
    amenities: '[]',
    price: '',
    minimum_nights: 1,
    maximum_nights: 7,
    minimum_minimum_nights: 1,
    maximum_minimum_nights: 1,
    minimum_maximum_nights: 7,
    maximum_maximum_nights: 7,
    minimum_nights_avg_ntm: 1,
    maximum_nights_avg_ntm: 7,
    calendar_updated: '',
    has_availability: 't',
    availability_30: 0,
    availability_60: 0,
    availability_90: 28,
    availability_365: 28,
    calendar_last_scraped: '2023-12-30',
    number_of_reviews: 37,
    number_of_reviews_ltm: 0,
    number_of_reviews_l30d: 0,
    first_review: '2014-04-21',
    last_review: '2017-08-31',
    review_scores_rating: 5,
    review_scores_accuracy: 4.97,
    review_scores_cleanliness: 4.92,
    review_scores_checkin: 4.95,
    review_scores_communication: 5,
    review_scores_location: 4.84,
    review_scores_value: 5,
    license: '',
    instant_bookable: 'f',
    calculated_host_listings_count: 1,
    calculated_host_listings_count_entire_homes: 0,
    calculated_host_listings_count_private_rooms: 1,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 0.31
  },
  {
    _id: ObjectId('660c6787b55bac758d387a66'),
    id: 15373,
    listing_url: 'https://www.airbnb.com/rooms/15373',
    scrape_id: Long('20231230181051'),
    last_scraped: '2023-12-31',
    source: 'city scrape',
    name: 'home in narragansett · ★4.83 · 13 bedrooms · 11 beds · 1.5 baths',
    description: '',
    neighborhood_overview: 'very quiet one-way street even though it is very close to the shore.',
    picture_url: 'https://a0.muscache.com/pictures/e1b639c9-0bd9-40d2-af7a-f4ef798bdab2.jpg',
    host_id: 60209,
    host_url: 'https://www.airbnb.com/users/show/60209',
    host_name: 'brian',
    host_since: '2009-12-05',
    host_location: '',
    host_about: '',
    host_response_time: 'within a day',
    host_response_rate: 1,
    host_acceptance_rate: 'N/A',
    host_is_superhost: 'False',
    host_thumbnail_url: 'https://a0.muscache.com/im/pictures/user/43936cff-00f9-40a4-ad38-c4bc58851590.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/pictures/user/43936cff-00f9-40a4-ad38-c4bc58851590.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: '',
    host_listings_count: 1,
    host_total_listings_count: 1,
    host_verifications: "['phone']",
    host_has_profile_pic: 't',
    host_identity_verified: 't',
    neighbourhood: 'Narragansett, Rhode Island, United States',
    neighbourhood_cleansed: 'Narragansett',
    neighbourhood_group_cleansed: 'Washington',
    latitude: 41.3919,
    longitude: -71.47568,
    property_type: 'Entire home',
    room_type: 'Entire home/apt',
    accommodates: 14,
    bathrooms: '',
    bathrooms_text: '1.5 baths',
    bedrooms: '',
    beds: 11,
    amenities: '[]',
    price: '',
    minimum_nights: 7,
    maximum_nights: 256,
    minimum_minimum_nights: 7,
    maximum_minimum_nights: 7,
    minimum_maximum_nights: 1125,
    maximum_maximum_nights: 1125,
    minimum_nights_avg_ntm: 7,
    maximum_nights_avg_ntm: 1125,
    calendar_updated: '',
    has_availability: 't',
    availability_30: 29,
    availability_60: 59,
    availability_90: 89,
    availability_365: 364,
    calendar_last_scraped: '2023-12-31',
    number_of_reviews: 6,
    number_of_reviews_ltm: 0,
    number_of_reviews_l30d: 0,
    first_review: '2020-07-21',
    last_review: '2021-08-05',
    review_scores_rating: 4.83,
    review_scores_accuracy: 4.83,
    review_scores_cleanliness: 5,
    review_scores_checkin: 4.67,
    review_scores_communication: 4.83,
    review_scores_location: 5,
    review_scores_value: 4.67,
    license: 205978,
    instant_bookable: 't',
    calculated_host_listings_count: 1,
    calculated_host_listings_count_entire_homes: 1,
    calculated_host_listings_count_private_rooms: 0,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 0.14
  }
]

```


### 2. show exactly 10 documents in any order, but "prettyprint" in easier to read format, using the `pretty()` function.

### Code

```
db.listing.find().limit(10).pretty()
```
### Result 

```
[
  {
    _id: ObjectId('660c6787b55bac758d387a65'),
    id: 10262,
    listing_url: 'https://www.airbnb.com/rooms/10262',
    scrape_id: Long('20231230181051'),
    last_scraped: '2023-12-30',
    source: 'city scrape',
    name: 'home in glocester · ★5.0 · 1 bedroom · 1 bed · 1 shared bath',
    description: '',
    neighborhood_overview: 'the peace and quiet, nature, ponds, hiking trails, antique shops, proximity to providence.......',
    picture_url: 'https://a0.muscache.com/pictures/42287/55a1cad0_original.jpg',
    host_id: 35244,
    host_url: 'https://www.airbnb.com/users/show/35244',
    host_name: 'paula',
    host_since: '2009-08-31',
    host_location: 'Glocester, RI',
    host_about: 'We enjoy people,conversation, growing and cooking good food, bicycling, kayaking, x-country skiing, dogs and cats. We love the area we live in and are happy to share our favorite spots with visitors. The music scene,good cycling, hiking, ethnic food, art museums and the ocean are what keeps us living here. ',
    host_response_time: 'within an hour',
    host_response_rate: 1,
    host_acceptance_rate: 0,
    host_is_superhost: 'False',
    host_thumbnail_url: 'https://a0.muscache.com/im/users/35244/profile_pic/1387981588/original.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/users/35244/profile_pic/1387981588/original.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: '',
    host_listings_count: 1,
    host_total_listings_count: 1,
    host_verifications: "['email', 'phone']",
    host_has_profile_pic: 't',
    host_identity_verified: 't',
    neighbourhood: 'Glocester, Rhode Island, United States',
    neighbourhood_cleansed: 'Glocester',
    neighbourhood_group_cleansed: 'Providence',
    latitude: 41.86683,
    longitude: -71.72481,
    property_type: 'Private room in home',
    room_type: 'Private room',
    accommodates: 2,
    bathrooms: '',
    bathrooms_text: '1 shared bath',
    bedrooms: '',
    beds: 1,
    amenities: '[]',
    price: '',
    minimum_nights: 1,
    maximum_nights: 7,
    minimum_minimum_nights: 1,
    maximum_minimum_nights: 1,
    minimum_maximum_nights: 7,
    maximum_maximum_nights: 7,
    minimum_nights_avg_ntm: 1,
    maximum_nights_avg_ntm: 7,
    calendar_updated: '',
    has_availability: 't',
    availability_30: 0,
    availability_60: 0,
    availability_90: 28,
    availability_365: 28,
    calendar_last_scraped: '2023-12-30',
    number_of_reviews: 37,
    number_of_reviews_ltm: 0,
    number_of_reviews_l30d: 0,
    first_review: '2014-04-21',
    last_review: '2017-08-31',
    review_scores_rating: 5,
    review_scores_accuracy: 4.97,
    review_scores_cleanliness: 4.92,
    review_scores_checkin: 4.95,
    review_scores_communication: 5,
    review_scores_location: 4.84,
    review_scores_value: 5,
    license: '',
    instant_bookable: 'f',
    calculated_host_listings_count: 1,
    calculated_host_listings_count_entire_homes: 0,
    calculated_host_listings_count_private_rooms: 1,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 0.31
  },
  {
    _id: ObjectId('660c6787b55bac758d387a66'),
    id: 15373,
    listing_url: 'https://www.airbnb.com/rooms/15373',
    scrape_id: Long('20231230181051'),
    last_scraped: '2023-12-31',
    source: 'city scrape',
    name: 'home in narragansett · ★4.83 · 13 bedrooms · 11 beds · 1.5 baths',
    description: '',
    neighborhood_overview: 'very quiet one-way street even though it is very close to the shore.',
    picture_url: 'https://a0.muscache.com/pictures/e1b639c9-0bd9-40d2-af7a-f4ef798bdab2.jpg',
    host_id: 60209,
    host_url: 'https://www.airbnb.com/users/show/60209',
    host_name: 'brian',
    host_since: '2009-12-05',
    host_location: '',
    host_about: '',
    host_response_time: 'within a day',
    host_response_rate: 1,
    host_acceptance_rate: 'N/A',
    host_is_superhost: 'False',
    host_thumbnail_url: 'https://a0.muscache.com/im/pictures/user/43936cff-00f9-40a4-ad38-c4bc58851590.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/pictures/user/43936cff-00f9-40a4-ad38-c4bc58851590.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: '',
    host_listings_count: 1,
    host_total_listings_count: 1,
    host_verifications: "['phone']",
    host_has_profile_pic: 't',
    host_identity_verified: 't',
    neighbourhood: 'Narragansett, Rhode Island, United States',
    neighbourhood_cleansed: 'Narragansett',
    neighbourhood_group_cleansed: 'Washington',
    latitude: 41.3919,
    longitude: -71.47568,
    property_type: 'Entire home',
    room_type: 'Entire home/apt',
    accommodates: 14,
    bathrooms: '',
    bathrooms_text: '1.5 baths',
    bedrooms: '',
    beds: 11,
    amenities: '[]',
    price: '',
    minimum_nights: 7,
    maximum_nights: 256,
    minimum_minimum_nights: 7,
    maximum_minimum_nights: 7,
    minimum_maximum_nights: 1125,
    maximum_maximum_nights: 1125,
    minimum_nights_avg_ntm: 7,
    maximum_nights_avg_ntm: 1125,
    calendar_updated: '',
    has_availability: 't',
    availability_30: 29,
    availability_60: 59,
    availability_90: 89,
    availability_365: 364,
    calendar_last_scraped: '2023-12-31',
    number_of_reviews: 6,
    number_of_reviews_ltm: 0,
    number_of_reviews_l30d: 0,
    first_review: '2020-07-21',
    last_review: '2021-08-05',
    review_scores_rating: 4.83,
    review_scores_accuracy: 4.83,
    review_scores_cleanliness: 5,
    review_scores_checkin: 4.67,
    review_scores_communication: 4.83,
    review_scores_location: 5,
    review_scores_value: 4.67,
    license: 205978,
    instant_bookable: 't',
    calculated_host_listings_count: 1,
    calculated_host_listings_count_entire_homes: 1,
    calculated_host_listings_count_private_rooms: 0,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 0.14
  },
  {
    _id: ObjectId('660c6787b55bac758d387a67'),
    id: 50791,
    listing_url: 'https://www.airbnb.com/rooms/50791',
    scrape_id: Long('20231230181051'),
    last_scraped: '2023-12-31',
    source: 'city scrape',
    name: 'rental unit in providence · ★4.88 · 2 bedrooms · 2 beds · 2 baths',
    description: '',
    neighborhood_overview: '',
    picture_url: 'https://a0.muscache.com/pictures/333382/dcb183fb_original.jpg',
    host_id: 233834,
    host_url: 'https://www.airbnb.com/users/show/233834',
    host_name: 'martina',
    host_since: '2010-09-13',
    host_location: 'Providence, RI',
    host_about: 'Designer, writer and yoga teacher with a passion for art and travel. Currently studying Fashion Design at MassArt in Boston',
    host_response_time: 'within a few hours',
    host_response_rate: 1,
    host_acceptance_rate: 0.62,
    host_is_superhost: 'True',
    host_thumbnail_url: 'https://a0.muscache.com/im/users/233834/profile_pic/1286145973/original.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/users/233834/profile_pic/1286145973/original.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: '',
    host_listings_count: 3,
    host_total_listings_count: 3,
    host_verifications: "['email', 'phone']",
    host_has_profile_pic: 't',
    host_identity_verified: 't',
    neighbourhood: '',
    neighbourhood_cleansed: 'Providence',
    neighbourhood_group_cleansed: 'Providence',
    latitude: 41.81488,
    longitude: -71.43021,
    property_type: 'Entire rental unit',
    room_type: 'Entire home/apt',
    accommodates: 4,
    bathrooms: '',
    bathrooms_text: '2 baths',
    bedrooms: '',
    beds: 2,
    amenities: '[]',
    price: '',
    minimum_nights: 2,
    maximum_nights: 270,
    minimum_minimum_nights: 2,
    maximum_minimum_nights: 2,
    minimum_maximum_nights: 270,
    maximum_maximum_nights: 270,
    minimum_nights_avg_ntm: 2,
    maximum_nights_avg_ntm: 270,
    calendar_updated: '',
    has_availability: 't',
    availability_30: 0,
    availability_60: 0,
    availability_90: 14,
    availability_365: 269,
    calendar_last_scraped: '2023-12-31',
    number_of_reviews: 86,
    number_of_reviews_ltm: 3,
    number_of_reviews_l30d: 0,
    first_review: '2010-10-11',
    last_review: '2023-10-08',
    review_scores_rating: 4.88,
    review_scores_accuracy: 4.83,
    review_scores_cleanliness: 4.95,
    review_scores_checkin: 4.84,
    review_scores_communication: 4.87,
    review_scores_location: 4.63,
    review_scores_value: 4.8,
    license: 'RE.03989-STR',
    instant_bookable: 'f',
    calculated_host_listings_count: 3,
    calculated_host_listings_count_entire_homes: 1,
    calculated_host_listings_count_private_rooms: 2,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 0.53
  }
]
  ```
### 3. Choose two hosts (by reffering to their `host_id` values) who are superhosts (available in the `host_is_superhost` field), and show all of the listings offered by both of the two hosts only show the `name`, `price`, `neighbourhood`, `host_name`, and `host_is_superhost` for each result
  
  ```
db.listing.aggregate([
  {
    $match: {
      host_id: { $in: ["146281658", "3686343"] }, 
      host_is_superhost: "true" 
    }
  },
  {
    $project: {
      _id: 0,
      name: 1,
      price: 1,
      neighbourhood: 1,
      host_name: 1,
      host_is_superhost: 1
    }
  }
]).pretty()
```

### 4. Find all the unique `host_name` values 

### Code

```
db.listing.distinct("host_name")
```
### Result 
```
[
  'abdul',
  'abel',
  'adam',
]
```

### 5. Find all of the places that have more than 2 `beds` in a neighborhood of your choice (referred to as either the `neighborhood` or `neighbourhood_group_cleansed` fields in the data file), ordered by `review_scores_rating` descending

### Code
```
   db.listing.aggregate([
  {
    $match: {
      beds: { $gt: 2 }, // Filter places with more than 2 beds
      neighbourhood_group_cleansed: "Newport", // Filter by specific neighborhood
      review_scores_rating: { $exists: true, $gt: 0 } // Adjusted to check for existence and non-zero
    }
  },
  {
    $project: {
      _id: 0,
      name: 1,
      beds: 1,
      review_scores_rating: 1,
      price: 1,
      neighbourhood_group_cleansed: 1 // Include this field if you want it in the output
    }
  },
  {
    $sort: { review_scores_rating: -1 } // Sort by review_scores_rating in descending order
  }
])

```

### Result
```

{
    name: 'rental unit in newport · ★5.0 · 2 bedrooms · 3 beds · 1 bath',
    neighbourhood_group_cleansed: 'Newport',
    beds: 3,
    price: '',
    review_scores_rating: 5
  },
  {
    name: 'home in newport · ★5.0 · 3 bedrooms · 4 beds · 2.5 baths',
    neighbourhood_group_cleansed: 'Newport',
    beds: 4,
    price: '',
    review_scores_rating: 5
  },
  {
    name: 'rental unit in newport · ★5.0 · 2 bedrooms · 4 beds · 2 baths',
    neighbourhood_group_cleansed: 'Newport',
    beds: 4,
    price: '',
    review_scores_rating: 5
  },
```

### 6. Show the number of listings per host

### Code
```
db.listing.aggregate([
  {
    $group: {
      _id: "$host_id",
      count: { $sum: 1 }
    }
  }
])
```
### Result 
```
 {_id: 418031528, count: 2 },
  { _id: 55973720, count: 10 },
  { _id: 43445655, count: 2 },
  ```

### 7. Find the average `review_scores_rating` per neighborhood, and only show those that are `4` or above, sorted in descending order of rating 

### Code
```
db.listing.aggregate([
  {
    $match: {
      review_scores_rating: { $gte: 4 } 
    }
  },
  {
    $group: {
      _id: "$neighbourhood", 
      avg_rating: { $avg: "$review_scores_rating" } 
    }
  },
  {
    $match: {
      avg_rating: { $gte: 4 } 
    }
  },
  {
    $sort: { avg_rating: -1 } 
  }
])
```

### Result
```
[
  {
    _id: 'Westerly, Rhode Island, United States',
    avg_rating: 4.903693693693694
  },
  { _id: 'Exeter, Rhode Island, United States', avg_rating: 4.9 },
  {
    _id: 'Middletown, Rhode Island, United States',
    avg_rating: 4.896111111111111
  }
]```