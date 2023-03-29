import requests

UserAgent = "9003's Python docs"
name = "9003"


r = requests.get('https://www.nationstates.net/cgi-bin/api.cgi/', headers={'User-Agent': UserAgent}, params={'nation':name})


# Most itmes you don't need this but its there!
#{'Date': 'Tue, 28 Mar 2023 20:24:50 GMT', 'Content-Type': 'text/html; charset=utf-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'X-Ratelimit-Requests-Seen': '29', 'Access-Control-Allow-Headers': 'X-Pin, X-Password, X-Autologin, User-Agent', 'Access-Control-Expose-Headers': 'X-Pin, X-Autologin', 'CF-Cache-Status': 'DYNAMIC', 'Report-To': '{"endpoints":[{"url":"https:\\/\\/a.nel.cloudflare.com\\/report\\/v3?s=Ob%2FSFTsu8AwXtO2mjU8mHC1Asx2paDlmZKSl%2B8RCYRyoxGHOFNS8fo6gYQPcHaw1EKsSeiDvzItE6c9IuThGCi8H01UQcC9mAinOgVzGuMVNjWcOp4AYtI9AlWkkvoaOAL6XOKyD"}],"group":"cf-nel","max_age":604800}', 'NEL': '{"success_fraction":0,"report_to":"cf-nel","max_age":604800}', 'Server': 'cloudflare', 'CF-RAY': '7af29953aca12321-ORD', 'alt-svc': 'h3=":443"; ma=86400, h3-29=":443"; ma=86400'}
print(r.headers)

#The Most common used header part is how many requests you've made in this bucket if it hits 51 you get locked out for 15 minutes
print(r.headers["X-Ratelimit-Requests-Seen"])


print(r.text)
"""
<NATION>
<NAME>9003</NAME>
<TYPE>⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜</TYPE>
<FULLNAME>The ⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜ of 9003</FULLNAME>
<MOTTO>ლ(ಠ益ಠ)ლ ♪ ♫ |̲̅̅●̲̅̅|̲̅̅=̲̅̅|̲̅̅●̲̅̅| ♫ ♪ ლ(ಠ益ಠ)ლ</MOTTO>
<CATEGORY>Corporate Police State</CATEGORY>
<UNSTATUS>Non-member</UNSTATUS>
<ENDORSEMENTS></ENDORSEMENTS>
<ISSUES_ANSWERED>2567</ISSUES_ANSWERED>
<FREEDOM>
 <CIVILRIGHTS>Unheard Of</CIVILRIGHTS>
 <ECONOMY>Frightening</ECONOMY>
 <POLITICALFREEDOM>Rare</POLITICALFREEDOM>
</FREEDOM>
<REGION>The North Pacific</REGION>
<POPULATION>22747</POPULATION>
<TAX>2.8</TAX>
<ANIMAL>human</ANIMAL>
<CURRENCY>𓆏 𓆏 𓆏 𓆏𓆏𓆏𓆏𓆏𓆏</CURRENCY>
<DEMONYM>Slave to the man</DEMONYM>
<DEMONYM2>Slave</DEMONYM2>
<DEMONYM2PLURAL>public filth</DEMONYM2PLURAL>
<FLAG>https://www.nationstates.net/images/flags/uploads/9003__476524.gif</FLAG>
<MAJORINDUSTRY>Arms Manufacturing</MAJORINDUSTRY>
<GOVTPRIORITY>Defence</GOVTPRIORITY>
<GOVT>
 <ADMINISTRATION>11.6</ADMINISTRATION>
 <DEFENCE>61.6</DEFENCE>
 <EDUCATION>0.0</EDUCATION>
 <ENVIRONMENT>0.0</ENVIRONMENT>
 <HEALTHCARE>0.0</HEALTHCARE>
 <COMMERCE>25.3</COMMERCE>
 <INTERNATIONALAID>0.0</INTERNATIONALAID>
 <LAWANDORDER>0.0</LAWANDORDER>
 <PUBLICTRANSPORT>0.0</PUBLICTRANSPORT>
 <SOCIALEQUALITY>0.0</SOCIALEQUALITY>
 <SPIRITUALITY>1.5</SPIRITUALITY>
 <WELFARE>0.0</WELFARE>
</GOVT>
<FOUNDED>10 years 156 days ago</FOUNDED>
<FIRSTLOGIN>1351173133</FIRSTLOGIN>
<LASTLOGIN>1680046186</LASTLOGIN>
<LASTACTIVITY>92 minutes ago</LASTACTIVITY>
<INFLUENCE>Minnow</INFLUENCE>
<FREEDOMSCORES>
 <CIVILRIGHTS>16</CIVILRIGHTS>
 <ECONOMY>100</ECONOMY>
 <POLITICALFREEDOM>15</POLITICALFREEDOM>
</FREEDOMSCORES>
<PUBLICSECTOR>9.5</PUBLICSECTOR>
<DEATHS>
 <CAUSE type="Heart Disease">4.2</CAUSE>
 <CAUSE type="Accident">0.4</CAUSE>
 <CAUSE type="War">0.1</CAUSE>
 <CAUSE type="Work">0.6</CAUSE>
 <CAUSE type="Involuntary Euthanasia">1.0</CAUSE>
 <CAUSE type="Scurvy">0.9</CAUSE>
 <CAUSE type="Exposure">0.2</CAUSE>
 <CAUSE type="Disappearance">83.1</CAUSE>
 <CAUSE type="Cancer">9.1</CAUSE>
 <CAUSE type="Murder">0.2</CAUSE>
</DEATHS>
<LEADER>⬞⬞⬞</LEADER>
<CAPITAL>Angband</CAPITAL>
<RELIGION>9002ism</RELIGION>
<FACTBOOKS>1</FACTBOOKS>
<DISPATCHES>13</DISPATCHES>
<DBID>85949</DBID>
<WABADGES>
 <WABADGE type="commend">311</WABADGE>
</WABADGES>

</NATION> 
"""
