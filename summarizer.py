import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
model = AutoModelForSeq2SeqLM.from_pretrained('t5-base')
tokenizer = AutoTokenizer.from_pretrained('t5-base', model_max_length=3000)

o = {'Introduction and Scope': """1. This  Standard  discusses  the  key  principles  of  supervisory  review,  with  respect  to 
banking risks, including guidance relating to, among other things, the treatment of interest 
rate risk in the banking book, credit risk (stress testing, residual risk, and credit concentration 
risk), operational risk, enhanced cross-border communication and cooperation, and 
securitisation. 
2. Banks are only permitted to perform a Pillar I Plus approach. Internal models are not 
allowed in ICAAP for estimating capital requirements for credit, market or operational risk. 
For risk management purposes, banks may use internal models, but figures reported to the 
Central Bank should be based on the Standardised Approach. 
3. All  buffers  are  to  be  in  addition  to  existing  requirements.  An  off-setting  of  certain 
requirements is not permitted i.e. lower Pillar 2 for Pillar 1 risks are not allowed. 
4. The type of capital which the Central Bank will require banks to provide  for pillar 2 
risks  will  be  solely  at  the  discretion  of the  Central  Bank;  this may  be  CET1  only,  or  a  mix 
between CET1 , AT1 and Tier 2. 
5. It should be noted that given a normal business model the capital risk charge for Pillar 
2 should always be positive if the risk exists (in particular for the IRRBB and Concentration 
risk)"""}

n= {'Introduction and Purpose': """I. Introduction and Purpose 
1. All  banks  licensed  by  the  Central  Bank  of  the  UAE  must  ensure  that  Pillar  1  risks  - 
credit, market, and operational risk  - are mitigated by capital, in compliance with the capital 
adequacy  framework  articulated  in  the  document  Central  Bank  “Regulations  re  Capital 
Adequacy” issued under Notice 60/2017 and the supporting capital standards and guidance, 
articulated in the document Central Bank “Standards and Guidance re Capital Adequacy of 
Banks in the UAE”. Incompliance with the Standards, each bank is required to quantify all risks 
that are not covered, or not sufficiently covered by Pillar 1 capital, and determine the additional 
capital required to mitigate these risks. The capital required to cover these risks is referred to 
as Pillar 2 capital. 
2. Each bank is required to have a process to assess its overall capital adequacy as a 
function of its risk profile and its strategy. Each bank is required to maintain appropriate capital 
levels in accordance with the Central Bank Standards on Pillar 2 capital. This process is termed 
the Internal Capital Adequacy Assessment Process (ICAAP). 
3. As part of the Supervisory Review and Evaluation Process (SREP), the Central Bank 
analyses the capitalisation levels of banks among other information, referring to the results of 
the ICAAP with regard to the internal view of capital adequacy. If the evaluation concludes that 
the capital levels of the individual bank are not satisfactory, the Central Bank may require a 
bank to meet an adjusted Minimum Capital Adequacy ratio accordingly. 
4. Consequently, Pillar 2 is both a bank internal process reported under the ICAAP, and 
the evaluation of each bank’s compete capital adequacy includes the ICAAP in its regulatory 
process  -  the  SREP.  First,  it  is  the  responsibility  of  each  bank  to  ensure  that  its  ICAAP  is 
comprehensive and proportionate to the nature, scale, and complexity of its activities. Each 
bank  bears  the  responsibility  for  the  appropriate  identification,  estimation,  and  reporting  of 
risks,  and  the  corresponding  the  calibration  of  capital  necessary  to  mitigate  these  risks. 
Second,  the  ICAAP  is  a  critical  reference  for  supervision  and  for  the  supervisory  dialogue 
between banks and Central Bank. 
Purpose 
5. This Guidance presents minimum expected practices to be considered by each bank 
in  order  to  undertake  their  ICAAP,  covering  the  process,  content,  outcome,  and  usage.  It 
clarifies the application of the Central Bank’s expectations regarding the requirements of the 
Central Bank ICAAP Standards.  Note, that the Central Bank plans to issue separately detailed 
requirements relating to the Internal Liquidity Adequacy Assessment Process (ILAAP). 
6. It also intends to support each bank in the identification, measurement, reporting, and 
mitigation of Pillar 2 risks. This Guidance does not prescribe specific methodologies but rather, 
it  provides  a framework,  within  which  a  bank should  elaborate  research,  analyse,  and  draw 
conclusions relevant to the risk profiles of their books. Each bank remains fully responsible for 
the methodology and process supporting the ICAAP. 
7. All methodologies employed by a bank for its ICAAP should be relevant to its business 
model, risk profile, to the geographies of its exposures, and, in particular, to the features of the 
UAE economy.  The methodologies and processes employed by the bank in its ICAAP should 
be fully documented, transparent and replicable. Each bank should be in a position to justify 
their decisions and modelling choices with historical data and benchmarking across a range of 
practices, which will be subject to supervisory scrutiny. Models employed for the measurement 
 
151  
CBUAE Classification: Public 
of  Pillar  2  risks  should  comply  with  the  Central  Bank  Model  Management  Standards  and 
Guidance. 
8. The Central Bank may apply proportionality for smaller and less complex banks when 
evaluating the ICAAP. This does not mean that smaller or less complex banks are exempted 
from the reporting requirements or from undertaking a comprehensive assessment of the risks 
they  face.  Smaller  banks  have  to  perform  the  whole  ICAAP  and  address  the  full  reporting 
scope. In cases where a bank’s capabilities lead them to use simpler methodologies, a more 
conservative capital treatment may be appropriate. However, the Central Bank expects a more 
sophisticated  risk  management  approach from  large  banks  and/  or  banks  with  complex  risk 
profiles in the assessment of their Pillar 2 risks. 
9. For the licensed operations of foreign banks in the UAE, when this document refers to 
the bank’s Board, it should be comprehended as the Managing Director and/ or the highest 
committee in the UAE operations of the bank in which the Managing Director has to be the 
Chairman. 
10. This Guidance serves several purposes. It 
(i) Explains  in  more  detail  the  Central  Bank’s  expectations  on  fulfilling  the 
requirements of the ICAAP Capital Standards, in particular, related to the ICAAP 
(process) at each bank and certain aspects of the content of the ICAAP report; 
(ii) Covers  expectations  on some  processual  elements  of the  ICAAP,  such as  an 
appropriate approval process of the ICAAP report and its submission timelines; 
and 
(iii) Formulates  expectations  about  additional  sections  of  the  ICAAP  report  (e.g. 
related to internal audit findings and changes compared to the previous ICAAP 
report)"""}
# tokens_input = tokenizer.encode(f"summarize changes between old document : {o} and  new document : {n} in a few points and please write it a more understandable way",
#                               return_tensors='pt',
#                               max_length=tokenizer.model_max_length,
#                               truncation=True)

tokens_input = tokenizer.encode(f"summarize changes between old document : {o} and  new document : {n} in a few points and please write it a more understandable way", return_tensors='pt', max_length=1024, truncation=True)

summary_ids = model.generate(tokens_input, min_length=1000, max_length=3000, length_penalty=2.0, num_beams=4, early_stopping=True)
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

print(summary)

print(summary)