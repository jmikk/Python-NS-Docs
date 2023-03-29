import requests

UserAgent = "9003's Python docs"
name = "9003"


r = requests.get('https://www.nationstates.net/cgi-bin/api.cgi/', headers={'User-Agent': UserAgent}, params={'nation':name,'q':"wa+type"})


# Most itmes you don't need this but its there!
#{'Date': 'Tue, 28 Mar 2023 20:24:50 GMT', 'Content-Type': 'text/html; charset=utf-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'X-Ratelimit-Requests-Seen': '29', 'Access-Control-Allow-Headers': 'X-Pin, X-Password, X-Autologin, User-Agent', 'Access-Control-Expose-Headers': 'X-Pin, X-Autologin', 'CF-Cache-Status': 'DYNAMIC', 'Report-To': '{"endpoints":[{"url":"https:\\/\\/a.nel.cloudflare.com\\/report\\/v3?s=Ob%2FSFTsu8AwXtO2mjU8mHC1Asx2paDlmZKSl%2B8RCYRyoxGHOFNS8fo6gYQPcHaw1EKsSeiDvzItE6c9IuThGCi8H01UQcC9mAinOgVzGuMVNjWcOp4AYtI9AlWkkvoaOAL6XOKyD"}],"group":"cf-nel","max_age":604800}', 'NEL': '{"success_fraction":0,"report_to":"cf-nel","max_age":604800}', 'Server': 'cloudflare', 'CF-RAY': '7af29953aca12321-ORD', 'alt-svc': 'h3=":443"; ma=86400, h3-29=":443"; ma=86400'}
print(r.headers)

#The Most common used header part is how many requests you've made in this bucket if it hits 51 you get locked out for 15 minutes
print(r.headers["X-Ratelimit-Requests-Seen"])


print(r.text)
