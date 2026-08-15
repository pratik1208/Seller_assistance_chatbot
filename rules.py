CATEGORY_RULES = {
  "Electronics > Audio > Headphones": {
    "required_fields": [
      "title",
      "description",
      "price",
      "images",
      "attributes.brand",
      "attributes.connectivity"
    ],
    "min_images": 3,
    "min_description_length": 50
  },
  "Electronics > Accessories > Cables": {
    "required_fields": [
      "title",
      "description",
      "price",
      "images",
      "attributes.brand"
    ],
    "min_images": 2,
    "min_description_length": 30
  },
  "Electronics > Smartphones": {
    "required_fields": [
      "title",
      "description",
      "price",
      "images",
      "attributes.brand",
      "attributes.storage",
      "attributes.warranty_months"
    ],
    "min_images": 3,
    "min_description_length": 100
  },
  "Clothing > Men > Casual": {
    "required_fields": [
      "title",
      "description",
      "price",
      "images",
      "attributes.brand",
      "attributes.size",
      "attributes.material"
    ],
    "min_images": 2,
    "min_description_length": 40
  },
  "Clothing > Men > Sportswear": {
    "required_fields": [
      "title",
      "description",
      "price",
      "images",
      "attributes.brand",
      "attributes.size",
      "attributes.material"
    ],
    "min_images": 2,
    "min_description_length": 40
  },
  "Home & Kitchen > Kitchen Tools > Knives": {
    "required_fields": [
      "title",
      "description",
      "price",
      "images",
      "attributes.brand",
      "attributes.material"
    ],
    "min_images": 2,
    "min_description_length": 40
  },
  "Electronics > Cameras > Action Cameras": {
    "required_fields": [
      "title",
      "description",
      "price",
      "images",
      "attributes.brand",
      "attributes.resolution"
    ],
    "min_images": 2,
    "min_description_length": 50
  }
}

PROHIBITION_RULES = {
  "prohibited_keywords": [
    "spy camera",
    "hidden camera",
    "surveillance",
    "secret recording",
    "counterfeit",
    "replica",
    "first copy",
    "master copy",
    "weapon",
    "firearm",
    "ammunition",
    "explosive",
    "drug",
    "narcotic",
    "steroid"
  ],
  "restricted_categories": [
    "surveillance equipment",
    "weapons",
    "pharmaceuticals"
  ],
  "protected_brands": [
    {
      "original": "Apple",
      "known_variants": [
        "Appel",
        "Aple",
        "Aplle",
        "A.P.P.L.E"
      ]
    },
    {
      "original": "Samsung",
      "known_variants": [
        "Samsuung",
        "Samsang",
        "Sumsung"
      ]
    },
    {
      "original": "Nike",
      "known_variants": [
        "Nikee",
        "Nikey",
        "N1ke"
      ]
    },
    {
      "original": "Sony",
      "known_variants": [
        "Sonny",
        "S0ny",
        "Soni"
      ]
    }
  ]
}
