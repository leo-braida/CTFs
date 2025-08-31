Machine's link: [TryHackMe | Neighbour](https://tryhackme.com/room/neighbour)

We start with a simple scan that showed to us that the machine is running a web server and SSH.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdHDcZqzlllla69zQgmSKM5v1H909jJyxGbXTlnVFuV5LfzxEL_KIpMdTj252Gai0dT6sKgDk_JWj2QwhoJLYQskteSCYIr3gK9GWR0kRZwHyeChBPH8TJgju_o3FtNuFNrfra0Dw?key=UPkumu6H_w0m_R7m1nLzQw)

Now, lets explore the web page!

With the machine description we already know somethings: its a cloud service with probably a Broken Access Control (A01:2021), more specifically, an IDOR.  

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdeH7eNWILQldM7PmsI6Pyb54PqCcDk9W4YE21zxDq6cQksHXqH3lfiVqk6wTybDQsez9hQ0LeMRkI0vsd-V4twjZ8mgv2FbW-539mDKkTpsWufURNPjSUiBKk9xAMkK3_xt5VHbw?key=UPkumu6H_w0m_R7m1nLzQw)

Thats the login page (the first page we see when enters the site).

The login page says about an guest account and says to look into the source code of the page, so lets look it there.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcanCcfR52oAEgmE8d8-JJxIGqK5RkFq_1uojlakdGP1fdTJZfdnIT7mUmISYEpX2TF04xGbww1uJDkDmW7nC0QxE2azaTIR3KRuFa-nPy5MY6vZ8Sja6sXiUhbBmx0Vod_xnSh?key=UPkumu6H_w0m_R7m1nLzQw)

So, the “guest” account is guest:guest and theres and “admin” account.

Now, we can enter the system with the guest account!  

Inside the system, we already saw a curious URL:

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcIdZQpy8sKRjVOMnXk448J5va1M_xlk_E9CmqiCEeysaLzyxQ1MiyE_hmLM6fi2psnu-ToVr0VWSgg8WBT_NnXqwu8QsN7XFDF8OL9ycryg_knFABvLG-EQqDvEXR156Ml8NtcxA?key=UPkumu6H_w0m_R7m1nLzQw)

Can we change it?

The guest account is:

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcHgS6o6rBxVgm4BejMakyTJr9QxwbEvL1PRh1F3N41sKwJf7rDgcA68P8y4F0035aByPxllCyOfTdBhh7StFRJz8JIzeaddf58QKpDfiFrgc69iIWl7h1P-43OCL4hIzgkGJDD?key=UPkumu6H_w0m_R7m1nLzQw)

So, lets try to change the guest to admin. And we’re done!

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdVfKcH8N8YiIgvGqebbemMWWSlCZt2h2FwZWi6jjuNmz-a9pu1f21M5G2_QePVWfZVMrBUTA2hn42CJHJuNA6xAmrAgdQTlz7ADmNOro_lp1k_NlE5_rviM0AALuZF26ZaWWB4oQ?key=UPkumu6H_w0m_R7m1nLzQw)
