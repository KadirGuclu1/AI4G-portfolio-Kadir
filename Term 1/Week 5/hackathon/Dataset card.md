** Dataset card

* Name: Adult / Census Income Data Set
* Source: US Census Bureau, 1994 Current Population Survey database
* Collected / donated by: Barry Becker and Ronny Kohavi (Silicon Graphics), donated 30 April 1996
* Link: https://archive.ics.uci.edu/dataset/2/adult
* Licence: Creative Commons Attribution 4.0 International (CC BY 4.0) — sharing and adaptation allowed with credit
* Extraction filter applied by the original donors: age > 16, adjusted gross income > $100, final weight > 1, hours worked > 0
* Size: 48,842 rows (32,561 + 16,281 original train/test files, combined and re-split below), 14 raw features
* Target: income, binary — >50K vs <=50K (annual income, USD, 1994)
* Class balance: approx. 76% <=50K / 24% >50K
* Known limitations: US population only, 1994 labour market, income reported/derived at individual level from a household survey, fnlwgt is a census sampling weight (not a trait of the person), 41 countries in native_country are very unevenly represented (approx. 90% United States).
