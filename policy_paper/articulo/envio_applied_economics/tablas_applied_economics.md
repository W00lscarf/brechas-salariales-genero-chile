# Tables

*Same occupation, different pay: decomposing the gender wage gap within 4-digit occupations in Chile*


**Table 1**
*Adjusted Gender Gap by Granularity of the Occupational Control*

| Specification | Adjusted gap | 95% CI | SE (log) | R² |
|---|---|---|---|---|
| 1-digit occupation (~9 categories) | -20.9% | [-21.7, -20.0] | 0.0052 | .488 |
| 4-digit occupation (354 categories) | -15.3% | [-16.2, -14.4] | 0.0055 | .537 |
| Difference | +5.6 pp | | | |

*Note.* Weighted least squares with expansion factors; design-based standard errors (Taylor linearization with strata and clusters). *n* = 174,924. Source: authors' elaboration based on CASEN 2022 and 2024.

**Table 2**
*Oaxaca-Blinder Decomposition of the Total Wage Gap (Male Reference)*

| Factor | Without children/marital status | With children/marital status |
|---|---|---|
| Hours worked | +28.7% | +27.8% |
| Occupation (4 digits) | +17.0% | +14.2% |
| Marital status | — | +1.8% |
| Has children | — | -1.4% |
| Age | -1.1% | -2.0% |
| Education | -10.8% | -10.9% |
| Year | -0.4% | -0.4% |
| **Unexplained** | **66.6%** | **70.9%** |

*Note.* Percentages of the total log gap attributable to the composition of each factor; negative values indicate factors operating in women's favor. Under female and pooled reference vectors the unexplained component is 49.0% and 65.8% respectively, with an identical ordering of factors. Source: authors' elaboration based on CASEN 2022 and 2024.

**Table 3**
*Associations of Parenthood and Marital Status With Labor Income, by Sex*

| Term | Association with income | p value |
|---|---|---|
| Female (base gap) | -12.3% | < .001 |
| Has children (association for men) | +5.0% | < .001 |
| Female × has children | -7.8% | < .001 |
| Female × single (vs. married/cohabiting) | +5.3% | < .001 |

*Note.* Weighted least squares with interactions; marital status reference: married or cohabiting. Source: authors' elaboration based on CASEN 2022 and 2024.

**Table 4**
*Adjusted Gap by Household Socioeconomic Status and by Educational Level*

| Segment | Adjusted gap |
|---|---|
| Household SES: low | -21.2% |
| Household SES: lower-middle | -17.0% |
| Household SES: upper-middle | -15.6% |
| Household SES: high | -11.2% |
| Primary education | -21.2% |
| Secondary education | -19.1% |
| Technical tertiary | -16.9% |
| University | -8.4% |
| Postgraduate | -14.6% |

*Note.* SES measured through weighted quintiles of the per capita income of the rest of the household. All estimates control for 4-digit occupation, age, age squared, education, hours, and year. The official household income quintile shows the same gradient (from -22.3% in the first quintile to -10.5% in the fourth). Source: authors' elaboration based on CASEN 2022 and 2024.

**Table 5**
*Adjusted Gap Under Alternative Specifications*

| Specification | Adjusted gap | *n* |
|---|---|---|
| Reference: monthly income + hours control, all employed | -15.3% | 174,924 |
| Maximal specification (all controls; 375 parameters) | -15.6% | 174,719 |
| Maximal + region and urban/rural fixed effects | -15.7% | 174,719 |
| Maximal + geography + higher-ed institution type | -15.6% | 174,719 |
| University graduates only, with institution type | -10.6% | 46,532 |
| Prime age (25-59) | -14.9% | 135,471 |
| Income trimmed at percentiles 1-99 | -13.0% | 171,481 |
| Full-time only (40-45 weekly hours) | -12.9% | 110,716 |
| Formal employees only (pension contributors) | -12.0% | 110,098 |
| Employees with signed contract only | -11.9% | 110,721 |
| Formality as a control | -15.2% | 174,924 |
| Hourly wage | -11.1% | 174,924 |
| Public sector employees only | -9.8% | 27,222 |
| Private sector employees only | -12.7% | 98,163 |
| Self-employed only | -25.5% | 44,697 |

*Note.* Unless noted, all specifications include 4-digit occupation controls, expansion factors, and clustered standard errors. Source: authors' elaboration based on CASEN 2022 and 2024.

**Table 6**
*Unexplained Component (Δ0) of the Matching Decomposition*

| Exact matching on | Cells in support | % of women in support | Δ0 (% of female wage) | Regression-convention equivalent |
|---|---|---|---|---|
| Year + education + age band | 50 | 100.0 | 34.4% | -25.6% |
| + occupation (1 digit) | 433 | 100.0 | 32.6% | -24.6% |
| + occupation (4 digits) | 5,429 | 91.2 | 17.9% | -15.2% |
| + workweek band | 7,664 | 82.6 | 13.4% | -11.8% |

*Note.* Weighted decomposition; Δ0 compares men and women within the common support, reweighting the male cell distribution to the female one. Bootstrap 95% CI (500 replications) for Δ0 with 4-digit occupation: [15.3, 19.0]. Equivalence computed as −Δ0/(1+Δ0). Source: authors' elaboration based on CASEN 2022 and 2024.
