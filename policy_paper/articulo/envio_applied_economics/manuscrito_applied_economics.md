# Same occupation, different pay: decomposing the gender wage gap within 4-digit occupations in Chile

@@AUTOR@@**Nicolás Guerrero Herrera**

@@AUTOR@@Independent researcher, Santiago, Chile

@@AUTOR@@n.icolashrra@gmail.com (corresponding author)

---

## Abstract

We estimate the gender wage gap in Chile using the most granular set of observable controls available in public microdata: 4-digit ISCO-08 occupation (354 categories), together with hours, education and type of institution, field of study, age, geography, formality, sector, and family structure (CASEN 2022-2024, *n* = 174,924). The adjusted gap ranges between -11% and -16% across fourteen specifications and does not shrink as controls are added. Results are robust to complex survey-design inference (Taylor linearization with strata and clusters), to a Heckman correction for selection into employment (corrected gap of -12.2%), and to an exact-matching decomposition within the common support in the spirit of Ñopo, which yields an unexplained component equivalent to -15.2% — virtually identical to the regression estimate. Parenthood is asymmetrically associated with income: having children is associated with a +5.0% premium among men and an additional -7.8% penalty among women within the same exact occupation. No occupation among the 227 examined shows a gap favouring women that survives correction for multiple comparisons, whereas 66 show significant gaps against them. The gap doubles in low-socioeconomic-status households and is U-shaped along the wage distribution.

**Keywords:** gender wage gap; occupational segregation; motherhood penalty; Oaxaca-Blinder decomposition; sample selection; Chile

**JEL codes:** J16, J31, J71

---

---

## 1. Introduction

Female labour force participation in Chile stands at around 53%, some 18 percentage points below the male rate, and women who do participate systematically earn less. The reported magnitude of the gap varies with its definition: the OECD indicator — median earnings of full-time employees — yields figures below 10% for Chile, while means over all employed persons place it above 20%, consistent with the factor-weighted global average of around 19% estimated by the ILO (2018).

For both economic analysis and policy design, the magnitude matters less than its **decomposition**: how much of the differential arises because men and women work in different occupations, sectors, and schedules (composition), and how much because identical observable characteristics are associated with different pay depending on sex (returns)? The dominant reading in the Chilean public debate attributes the gap to women's choices — of career, hours, sector, and family. That interpretation has remained largely untested because the occupational controls available in standard employment surveys are too coarse: within a 1-digit category such as "Professionals," physicians, lawyers, engineers, and journalists coexist, with very different pay levels and gender compositions.

This paper addresses the question that the Chilean literature has left open: **does the gender wage gap persist once the most granular set of observable compositional controls that public data allow — exact occupation, hours worked, education and its institutional quality, field of study, geography, formality regime, sector, and family structure — is accounted for? And, if it persists, in which population segments is it largest?**

We exploit a feature of the CASEN household survey that, to the best of our knowledge, has not been used for this purpose with statistical inference and openly accessible data: occupation coded at the 4-digit ISCO-08 level, which allows wages to be compared within 354 specific occupations. A scope clarification is indispensable from the outset: 4-digit occupation is not equivalent to "same job." We do not observe the firm, hierarchical position, performance, or the composition of pay (bonuses, commissions, overtime), so our title must be read strictly: same *occupation*, not same *job*, nor "work of equal value" in the legal sense of the term.

This paper makes four contributions. First, it provides the first estimate for Chile of the wage gap within 4-digit occupations with openly accessible data, occupation-level statistical inference, and correction for multiple comparisons. Second, it implements a design that systematically confronts the choice-based explanation: fourteen specifications that net out, successively and jointly, each observable dimension of choice — including a maximal specification with 375 parameters — complemented by a Heckman (1979) correction for selection into employment and an exact-matching decomposition within the common support (Ñopo, 2008). Third, it provides the first distributional characterization of the adjusted gap for Chile at this granularity: a socioeconomic gradient — the gap doubles in the lowest-status households — and a U-shape along the wage distribution, with sticky floor and glass ceiling operating simultaneously. Fourth, the entire empirical apparatus is reproducible with public data and open code.

Our central findings are easily summarized. The adjusted gap moves from -20.9% under 1-digit occupational controls to -15.3% under 4-digit controls: fine occupational segregation is real, but explains a minority of the differential. The gap never approaches zero under any specification — the full range is -11% to -16% — and adding controls does not reduce it, because several controls (education, formality, public-sector employment) capture composition that favours women. Selection into employment is substantial (the participation gap is 21 percentage points in the 25-64 population) and statistically detectable, but correcting for it leaves a gap of -12.2%. A nonparametric matching decomposition within the common support delivers the same answer as the weighted regression to within one decimal point. And the residual is not distributed at random: it is concentrated precisely where choice-based explanations are least plausible — low-income households, married or cohabiting mothers, and the tails of the wage distribution.

The remainder of the paper is organized as follows. Section 2 reviews the related literature. Section 3 describes the data. Section 4 presents the empirical strategy. Section 5 reports the main results, Section 6 the robustness analysis, and Section 7 discusses mechanisms and policy implications. Section 8 concludes.

---

## 2. Related literature

### 2.1 International evidence

The canonical starting point is the Mincer (1974) earnings function; the decomposition of wage differentials into composition and returns components follows Oaxaca (1973) and Blinder (1973). Blau and Kahn (2017) document for the United States that conventional human capital ceased to explain the gender gap, with occupation, industry, and the unexplained component becoming dominant. Two interpretive caveats accompany this framework and apply throughout: the "unexplained" component is not synonymous with discrimination — it includes any omitted variable correlated with sex — and the "explained" component is not necessarily non-discriminatory, since occupational segregation may itself result from barriers and norms (Bertrand et al., 2010).

On the granularity question, Petersen and Morgan (1995) showed that comparing within occupation-establishment cells drastically reduces the U.S. gap, and Card et al. (2016) quantified the firm channel — sorting into low-premium firms and lower rent capture in bargaining — at about one fifth of the gap in Portugal. Goldin (2014) supplies the within-occupation mechanism: convex returns to hours in "greedy" jobs penalize the flexibility that women demand more, given the asymmetric allocation of care (Goldin, 2021; Bolotnyy & Emanuel, 2022). The child-penalty literature based on event studies shows that the first birth opens a persistent earnings gap between mothers and fathers — around 20% in the long run in Denmark (Kleven et al., 2019) and substantially larger in Latin America (Kleven et al., 2025) — and Cortés and Pan (2023) conclude that children are today the single most important factor behind remaining gender gaps. On distribution, Albrecht et al. (2003) documented the glass ceiling in Sweden and Arulampalam et al. (2007) glass ceilings and sticky floors across Europe.

### 2.2 Chilean evidence and this paper's position

Six strands define the local state of the art. Official statistics (INE/ESI) describe raw gaps by sex and broad occupation; we add multivariate adjustment with fine occupation and inference. Ñopo (2006), using CASEN 1992-2003 and comparisons restricted to the common support, documented an unexplained component of around 25% of average female wages, larger at top percentiles — fully consistent with the U-shape we report; we implement his decomposition with 4-digit matching in Section 6. Perticará and Bueno (2009), using the Social Protection Survey, controlled for actual labour market experience and intermittency — the critical variable our source does not observe; against that advantage, we contribute recency, sample scale, occupational granularity, and reproducibility. Sánchez et al. (2022) estimate, with unemployment-insurance administrative records and a dynamic monopsony model, that differences in firm-level labor supply elasticities can generate differentials of 19-28%; that channel is unobservable with our data and remains, by construction, inside our unexplained component. Berniell et al. (2023) document with event studies for Chile and other Latin American countries sharp and persistent declines in mothers' employment, hours, and earnings after the first birth, with essentially unaffected fathers; our cross-sectional parenthood coefficients are the static imprint of that process, consistent with — but not a substitute for — that causal evidence. Finally, Parada-Contzen and Jara (2025) document gaps of 17-25% before the pandemic among workers with higher education, with a growing unexplained component and heterogeneous effects across fields of study; we incorporate field of study directly in Section 6 and show that its contribution is largely absorbed by exact occupation.

---

## 3. Data

We use the two public microdata sources that jointly cover the requirements of the analysis. The primary source is the National Socioeconomic Characterization Survey (CASEN) waves 2022 and 2024, the only Chilean public survey coding occupation at the 4-digit ISCO-08 level and including a direct fertility question (`s5`) and marital status. The Supplementary Income Survey (ESI 2018-2024) is used for context on the aggregate gap. CASEN 2017 is excluded because it codes occupation under ISCO-88, which is not comparable with ISCO-08.

The analytical sample pools the 2022 and 2024 waves: employed persons with positive main-job labour income and valid occupation (176,542 individuals across 444 occupation codes). Records with invalid weekly hours (code -88, "does not know," or above 112 hours) are excluded, leaving **174,924 individuals**; 354 occupation codes reach at least 30 observations. Occupation-specific analyses further require at least 20 men and 20 women per cell, leaving 227 occupations. The outcome is the logarithm of main-job labour income (`ytrabajocor`); hours are weekly hours in the main job.

CASEN has a complex sampling design. All estimates use the official expansion factors; inference uses standard errors clustered by primary sampling unit × wave in the main text, and Section 6.5 shows that fully design-based standard errors — Taylor linearization with strata (`varstrat`), clusters (`varunit`), and weights — are marginally *smaller*, so the reported inference is, if anything, conservative. In the pooled 25-64 population used for the selection analysis, the employment-sample participation rate is 82.5% for men and 61.6% for women (weighted), a 20.9-point gap that motivates the selection correction in Section 6.6.

---

## 4. Empirical strategy

### 4.1 Wage equations at two levels of occupational granularity

The baseline is a weighted least squares Mincer equation:

$$\ln w_i = \alpha + \delta F_i + x_i'\beta + \theta_{o(i)} + \varepsilon_i$$ (1)

where F_i is an indicator for women, x_i contains age, age squared, educational level (five categories), weekly hours, and wave fixed effects, and θ_o(i) denotes occupation fixed effects. We estimate (1) twice, holding everything constant except the occupational classification: 1-digit ISCO (roughly nine categories, the maximum available in standard employment surveys) versus 4-digit ISCO (354 categories). The difference between the two estimates of δ isolates the pure contribution of occupational granularity. The adjusted gap in percentage terms is 100·(exp(δ)−1).

### 4.2 Decomposition

We decompose the total log gap with the Oaxaca (1973)-Blinder (1973) procedure:

$$\Delta \equiv \overline{\ln w}_m - \overline{\ln w}_f = (\bar{x}_m - \bar{x}_f)'\hat{\beta}_m + \bar{x}_f'(\hat{\beta}_m - \hat{\beta}_f)$$ (2)

where the first term is the component explained by average characteristics and the second the unexplained component. We group detailed contributions into variable families (hours, occupation, education, age, family structure, formality, year) and, following Neumark (1988), report male, female, and pooled reference coefficient vectors to address the index number problem. Because high-dimensional categorical variables make detailed decompositions sensitive to the choice of base categories, family-level percentages should be read as orders of magnitude.

### 4.3 Occupation-specific gaps and multiple testing

To estimate a sex effect specific to each occupation without fitting 227 underpowered regressions, we estimate a single model interacting the female indicator with occupation dummies, with common controls estimated on the full sample:

$$\ln w_i = \alpha + \sum_{o} (\delta + \gamma_o) F_i D_{io} + x_i'\beta + \theta_{o(i)} + \varepsilon_i$$ (3)

where D_io indicates occupation o. The occupation-specific gap δ + γ_o is recovered as a linear combination of coefficients, with variance from the cluster-robust covariance matrix. With 227 simultaneous tests, approximately 11 false positives are expected at p < .05; we therefore report Benjamini-Hochberg false-discovery-rate and Bonferroni corrections.

### 4.4 Matching decomposition with common support

Following Ñopo (2008), we decompose the gap by exact matching on characteristic cells:

$$\Delta = \Delta_0 + \Delta_X + \Delta_M + \Delta_F$$ (4)

where Δ0 is the unexplained difference between comparable men and women within the common support (reweighting the male cell distribution to the female one), ΔX captures distribution differences within the support, and ΔM, ΔF the parts attributable to individuals without an exact counterpart of the other sex. The method imposes no functional form and does not extrapolate outside the support; additivity is verified exactly. Inference uses a 500-replication bootstrap.

### 4.5 Selection into employment

Because wages are observed only for workers and participation differs sharply by sex, we implement the Heckman (1979) two-step correction. The first stage is a participation probit on the 25-64 population with exclusion restrictions that plausibly shift participation but not conditional wages: presence of children, marital status, non-labor household income per capita, and their interactions with sex. The second stage augments equation (1) with the inverse Mills ratio:

$$\ln w_i = \alpha + \delta F_i + x_i'\beta + \theta_{o(i)} + \rho \hat{\lambda}_i + \varepsilon_i, \quad \hat{\lambda}_i = \frac{\phi(z_i'\hat{\gamma})}{\Phi(z_i'\hat{\gamma})}$$ (5)

where z_i collects the participation determinants including the exclusion restrictions. Confidence intervals bootstrap both stages jointly (120 replications). As in any Heckman application, validity rests on the exclusion restrictions; we read the result as a robustness bound rather than causal identification.

---

## 5. Results

### 5.1 The granularity test

Table 1 presents the central comparison: same data, same specification, different occupational resolution.

[Table 1 near here]

Granularity matters: a real share of what coarse estimates report as "unexplained" is fine occupational segregation — within "Professionals," men concentrate in the better-paid specialties. But the gap does not vanish: -15.3% persists comparing the same exact occupation. Descriptively, within identical occupations: medical specialists -20%, nursing technicians -13%, nurses -3%.

### 5.2 Decomposition: what explains the gap, and how much

Table 2 reports the Oaxaca-Blinder decomposition of the total gap (22.6% of the female mean), with and without family-composition controls.

[Table 2 near here]

Three readings follow. Hours worked are the largest compositional factor (about 29%), followed by fine occupational segregation (about 17%); together they account for nearly all of the explained share. Education operates in reverse: employed women are more educated than employed men. And family variables contribute almost nothing to the explained share — men and women do not differ much in average family composition. Their effect operates through returns, as the next subsection shows.

### 5.3 Parenthood: a returns-side association

Table 3 presents the Female × children and Female × marital status interactions, controlling for exact occupation, education, age, hours, and year (*n* = 174,719).

[Table 3 near here]

The contrast is stark: fatherhood is associated with a wage premium; motherhood with an additional penalty on top of the gap affecting all women — the pattern documented causally by the event-study literature (Kleven et al., 2019; Berniell et al., 2023). These coefficients are conditional associations, not causal effects: motherhood is measured as a self-reported stock, not a dated event. Their evidentiary value lies in the coherence of the pattern — sex asymmetry in response to the same family event, within the same occupation — with the causal evidence. This also resolves the apparent paradox of Table 2: adding family variables *raises* the unexplained share because the motherhood penalty is a difference in returns (the same child is associated with different impacts depending on the parent's sex), not in composition.

### 5.4 Isolating the sex effect occupation by occupation

With the full interaction model, 90 of 227 occupations (39.6%) show a statistically significant adjusted gap at p < .05: 89 against women and one in favour (bus and trolleybus drivers, +15.1%, p = .029) — exactly what chance would produce given approximately 11 expected false positives. Correction for multiple comparisons purges the result: 66 occupations survive the FDR correction (q < .05) and 30 survive Bonferroni — all of them, without exception, against women. Apparent female advantages in raw comparisons dissolve under adjustment: jewelry moves from +58.6% raw to -5.5% adjusted (not significant); music (+37.9%) and translation (+47.5%) are likewise insignificant once adjusted. The correlation between raw and adjusted occupation-level gaps is .79, with the mean moderating from -17.8% to -14.8%.

### 5.5 For whom is the gap largest?

The average conceals policy-relevant heterogeneity. By household socioeconomic status — measured with the per capita income of the *rest* of the household, to avoid the mechanical bias whereby women's lower earnings push their own households down the ranking — the adjusted gap displays a clear gradient (Table 4).

[Table 4 near here]

The gap is twice as large in low-SES households as in high-SES ones — largest precisely where each percentage point of income matters most and where individual bargaining power is weakest. The rebound at the postgraduate level (-14.6% versus -8.4% for university graduates) is a glass-ceiling signal. Along the wage distribution, quantile regressions with the full control set yield a U-shape: around -15% at the bottom decile, -12% at the median, and -16% at the top decile — sticky floor and glass ceiling simultaneously, the pattern of Albrecht et al. (2003) and Arulampalam et al. (2007).

---

## 6. Robustness

### 6.1 Specification battery

Table 5 reports the adjusted gap under alternative specifications and subsamples.

[Table 5 near here]

The gap never approaches zero, and adding controls does not reduce it: the maximal specification yields -15.6%, *more* than the reference, because several controls capture composition that favours women. Formality composition barely differs by sex (employees: 74.6% of men versus 77.7% of women), so the gap is not an artifact of mixing labour market segments; the most severe gap is among the self-employed (-25.5%) and the smallest in the public sector (-9.8% versus -12.7% private; interaction p = .078), consistent with pay governed by public scales — which compress, but do not eliminate, the differential.

### 6.2 Field of study

Among workers with higher education (n = 69,956), field of study (CINE-F 2013, ten areas, full coverage) explains a real share of the gap — from -17.1% with neither field nor occupation to -13.7% with field only — consistent with Parada-Contzen and Jara (2025). But its contribution is largely redundant with exact occupation: occupation alone brings the gap to -11.5%, and adding field on top contributes only one additional point (-10.4%). Even comparing professionals with the same education level, same field of study, and same exact occupation, a gap of about 10% persists.

### 6.3 Matching decomposition with common support

Table 6 reports the Ñopo decomposition under increasingly demanding matching sets.

[Table 6 near here]

The convergence of methods is the salient finding: the nonparametric Δ0 with 4-digit matching is equivalent to -15.2%, virtually identical to the regression estimate of -15.3%, with a wide common support (80% of men, 91% of women, 5,429 matched cells). The gap does not arise from comparing incomparable individuals or from functional-form assumptions.

### 6.4 Selection into employment

The participation gap in the 25-64 population is 20.9 percentage points (82.5% versus 61.6%, weighted). In the first-stage probit, the exclusion restrictions behave as theory predicts, with a sharp sex asymmetry: children are associated with higher male participation (+0.260) and lower female participation (interaction -0.389), and non-labour income reduces participation (all p < .001). The inverse Mills ratio is highly significant in the wage equation (coefficient -0.129, p < .001): selection into employment is real. The selection-corrected gap is **-12.2%** (bootstrap 95% CI [-13.9, -10.8]), against -15.4% uncorrected in the same 25-64 subsample. Two lessons follow: the observed gap among workers is not an artifact of positive selection — correcting for selection reduces it by about three points but does not eliminate it — and the common conjecture that selection necessarily implies the observed gap *understates* the population differential is not supported in these data.

### 6.5 Survey-design inference

Replacing cluster-robust standard errors with fully design-based ones — Taylor linearization with 1,511 strata, 24,450 primary sampling units, and expansion factors — leaves point estimates unchanged and yields standard errors marginally *smaller* than cluster-only (ratio 0.997 for the granular specification; the single-stratum case reproduces the cluster-robust benchmark exactly). The inference reported throughout is therefore conservative.

### 6.6 Multiple-testing and functional form

The one-directional occupation-level pattern survives the hourly-wage specification: 41 occupations survive FDR (40 against women) and 16 survive Bonferroni (all against women); the only female-favourable exception under FDR (taxi drivers, +13.1% per hour) reflects the extreme schedules of male drivers, which dilute their hourly rate. In hourly wages the gap is smaller than in monthly income (-11.1% versus -15.3%), consistent with the weight of hours in the decomposition.

---

## 7. Discussion

### 7.1 What lies inside the unexplained component

The roughly two thirds of the gap that composition does not explain is not a black box. The international literature with experimental and administrative designs has named its components: the ask gap — women request 2.9% less for the same profile, and displaying market medians eliminates the difference (Roussille, 2024; Leibbrandt & List, 2015; Exley et al., 2020); overtime and schedule flexibility within occupations (Bolotnyy & Emanuel, 2022; Goldin, 2014), whose imprint appears in our data both in the weight of hours and in the taxi-driver exception; competitiveness and personality attributes, which explain a small-to-moderate share (Niederle & Vesterlund, 2007; Buser et al., 2014; Croson & Gneezy, 2009; Mueller & Plug, 2006; Heckman et al., 2006; Bertrand, 2011; Blau & Kahn, 2017); firm-level sorting and bargaining, about one fifth of the gap where measurable (Card et al., 2016) and invisible to our data; and the dynamics of motherhood (Cortés & Pan, 2023; Kleven et al., 2019; Berniell et al., 2023), whose static imprint we estimate at -7.8% within occupations. None of these mechanisms is measurable today with Chilean public data — household surveys include no modules on wage negotiation, actual work histories, or socioemotional attributes — which itself defines a data-infrastructure agenda.

### 7.2 Policy implications

The diagnosis — a gap that is mostly a returns phenomenon, concentrated among low-SES households and mothers, with sticky floors and glass ceilings — maps onto instruments in a specific way. Pay transparency with occupation-adjusted gap reporting attacks the returns component directly, with favourable causal evidence (Bennedsen et al., 2022; Baker et al., 2023; Cullen, 2024), and should include the negotiability and salary ranges of positions (Roussille, 2024); the compressed public-sector gap we document (-9.8% versus -12.7%) is local evidence consistent with rule-based pay, while its persistence indicates that transparency must cover total remuneration. Care policy attacks the motherhood mechanism: replacing Chile's employer-specific childcare mandate (Article 203 of the Labour Code, which taxes female hiring at the margin; Prada et al., 2015) with collective financing, non-transferable paternal leave quotas (Patnaik, 2019), and expanded public childcare (Martínez & Perticará, 2017). Occupational desegregation policies attack the second-largest compositional factor (~17%), but even eliminating fine segregation entirely would leave more than 80% of the gap in place. Finally, the distributional evidence indicates that enforcement, minimum-wage, and formalization instruments matter at the bottom of the distribution, where the gap is largest and least visible to transparency-based tools designed for professional labor markets.

---

## 8. Concluding remarks

Using the most granular occupational classification available in Chilean public microdata, this paper shows that the gender wage gap is not reducible to observable choices. The adjusted gap of -15.3% within 4-digit occupations survives a fourteen-specification battery, field-of-study controls, fully design-based inference, a Heckman selection correction (-12.2%), and an exact-matching decomposition within the common support that reproduces the regression estimate almost exactly. The associations of parenthood with income are sharply asymmetric by sex within identical occupations, and the gap is largest precisely where the scope for choice is smallest.

Three limitations bound the interpretation. The data are cross-sectional: all estimates are conditional associations, and the unexplained component bounds but does not identify discrimination. Age proxies potential, not actual, experience — the variable that Chilean panel evidence identifies as first-order (Perticará & Bueno, 2009) — so part of the residual may reflect actual-experience differences, themselves largely a consequence of the asymmetric allocation of care. And we do not observe the employer, so the firm channel quantified by Sánchez et al. (2022) remains inside our unexplained component. Linked administrative data — unemployment insurance, tax, and pension records — would allow the natural extensions: firm fixed effects, event studies of motherhood, and actual work histories. Opening those records to research under stable protocols is, in itself, one of the paper's implications.

---

## Declarations

**Declaration of generative AI use.** During the preparation of this work the author used a generative artificial intelligence assistant (Anthropic's Claude) to assist with data-processing and statistical code, with drafting and language editing of the manuscript, and with document formatting. All research design and analytical decisions, the verification of every result, and the interpretation and final content are the author's own. The author takes full responsibility for the integrity and accuracy of the work. No AI tool is listed or claimed as an author.

**Funding.** The author received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.

**Competing interests.** The author declares no competing interests.

**Data availability statement.** This study uses publicly available microdata from the National Socioeconomic Characterization Survey (CASEN 2022 and 2024; Ministry of Social Development and Family, Observatorio Social) and the Supplementary Income Survey (ESI 2018-2024; National Institute of Statistics), both freely downloadable from their official repositories without registration. The complete code that reproduces every result and table is openly available in a public repository (https://github.com/W00lscarf/brechas-salariales-genero-chile).

**Author contributions.** Nicolás Guerrero Herrera: conceptualization, data curation, formal analysis, methodology, software, visualization, and writing (original draft, review and editing).

## References

- Albrecht, J., Björklund, A., & Vroman, S. (2003). Is there a glass ceiling in Sweden? *Journal of Labor Economics*, *21*(1).
- Arulampalam, W., Booth, A., & Bryan, M. (2007). Is there a glass ceiling over Europe? Exploring the gender pay gap across the wage distribution. *ILR Review*, *60*(2).
- Baker, M., Halberstam, Y., Kroft, K., Mas, A., & Messacar, D. (2023). Pay transparency and the gender gap. *American Economic Journal: Applied Economics*, *15*(2).
- Bennedsen, M., Simintzi, E., Tsoutsoura, M., & Wolfenzon, D. (2022). Do firms respond to gender pay gap transparency? *Journal of Finance*, *77*(4).
- Berniell, I., Berniell, L., de la Mata, D., Edo, M., & Marchionni, M. (2023). Motherhood and flexible jobs: Evidence from Latin American countries. *World Development*, *167*.
- Bertrand, M. (2011). New perspectives on gender. In O. Ashenfelter & D. Card (Eds.), *Handbook of labor economics* (Vol. 4B). Elsevier.
- Bertrand, M., Goldin, C., & Katz, L. (2010). Dynamics of the gender gap for young professionals in the financial and corporate sectors. *American Economic Journal: Applied Economics*, *2*(3).
- Blau, F., & Kahn, L. (2017). The gender wage gap: Extent, trends, and explanations. *Journal of Economic Literature*, *55*(3), 789-865.
- Blinder, A. (1973). Wage discrimination: Reduced form and structural estimates. *Journal of Human Resources*, *8*(4), 436-455.
- Bolotnyy, V., & Emanuel, N. (2022). Why do women earn less than men? Evidence from bus and train operators. *Journal of Labor Economics*, *40*(2).
- Buser, T., Niederle, M., & Oosterbeek, H. (2014). Gender, competitiveness, and career choices. *Quarterly Journal of Economics*, *129*(3).
- Card, D., Cardoso, A. R., & Kline, P. (2016). Bargaining, sorting, and the gender wage gap: Quantifying the impact of firms on the relative pay of women. *Quarterly Journal of Economics*, *131*(2).
- Cortés, P., & Pan, J. (2023). Children and the remaining gender gaps in the labor market. *Journal of Economic Literature*, *61*(4).
- Croson, R., & Gneezy, U. (2009). Gender differences in preferences. *Journal of Economic Literature*, *47*(2), 448-474.
- Cullen, Z. (2024). Is pay transparency good? *Journal of Economic Perspectives*, *38*(1).
- Exley, C., Niederle, M., & Vesterlund, L. (2020). Knowing when to ask: The cost of leaning in. *Journal of Political Economy*, *128*(3).
- Goldin, C. (2014). A grand gender convergence: Its last chapter. *American Economic Review*, *104*(4), 1091-1119.
- Goldin, C. (2021). *Career and family: Women's century-long journey toward equity*. Princeton University Press.
- Heckman, J. (1979). Sample selection bias as a specification error. *Econometrica*, *47*(1), 153-161.
- Heckman, J., Stixrud, J., & Urzúa, S. (2006). The effects of cognitive and noncognitive abilities on labor market outcomes and social behavior. *Journal of Labor Economics*, *24*(3).
- Kleven, H., Landais, C., & Leite-Mariante, G. (2025). The child penalty atlas. *Review of Economic Studies*.
- Kleven, H., Landais, C., & Søgaard, J. E. (2019). Children and gender inequality: Evidence from Denmark. *American Economic Journal: Applied Economics*, *11*(4), 181-209.
- Leibbrandt, A., & List, J. (2015). Do women avoid salary negotiations? Evidence from a large-scale natural field experiment. *Management Science*, *61*(9).
- Martínez, C., & Perticará, M. (2017). Childcare effects on maternal employment: Evidence from Chile. *Journal of Development Economics*, *126*.
- Mincer, J. (1974). *Schooling, experience, and earnings*. National Bureau of Economic Research.
- Mueller, G., & Plug, E. (2006). Estimating the effect of personality on male and female earnings. *ILR Review*, *60*(1), 3-22.
- Neumark, D. (1988). Employers' discriminatory behavior and the estimation of wage discrimination. *Journal of Human Resources*, *23*(3), 279-295.
- Niederle, M., & Vesterlund, L. (2007). Do women shy away from competition? Do men compete too much? *Quarterly Journal of Economics*, *122*(3), 1067-1101.
- Ñopo, H. (2006). *The gender wage gap in Chile 1992-2003 from a matching comparisons perspective*. Inter-American Development Bank.
- Ñopo, H. (2008). Matching as a tool to decompose wage gaps. *Review of Economics and Statistics*, *90*(2), 290-299.
- Oaxaca, R. (1973). Male-female wage differentials in urban labor markets. *International Economic Review*, *14*(3), 693-709.
- Parada-Contzen, M., & Jara, F. (2025). Gender wage gap among the educated: Evidence from fields of study in Chile. *Humanities and Social Sciences Communications*, *12*, 961.
- Patnaik, A. (2019). Reserving time for daddy: The consequences of fathers' quotas. *Journal of Labor Economics*, *37*(4).
- Perticará, M., & Bueno, I. (2009). A new approach to gender wage gaps in Chile. *CEPAL Review*, *99*.
- Petersen, T., & Morgan, L. (1995). Separate and unequal: Occupation-establishment sex segregation and the gender wage gap. *American Journal of Sociology*, *101*(2), 329-365.
- Prada, M. F., Rucci, G., & Urzúa, S. (2015). *The effect of mandated child care on female wages in Chile* (NBER Working Paper No. 21080). National Bureau of Economic Research.
- Roussille, N. (2024). The role of the ask gap in gender pay inequality. *Quarterly Journal of Economics*, *139*(3), 1557-1610.
- Sánchez, R., Finot, J., & Villena, M. G. (2022). Gender wage gap and firm market power: Evidence from Chile. *Applied Economics*, *54*(18), 2109-2121.
