

Recon(Footprinting) -> Gather info -> Passive = Public 

https://ahrefs.com/blog/google-advanced-search-operators/
https://www.exploit-db.com/google-hacking-database
## Google search operators: the complete list

Below is a brief description of what every Google search operator does.

I’ve grouped them into three categories:

- **Working** – Works as intended.
- **Unreliable** – Not officially deprecated by Google, but results are hit-and-miss. 
- **Not working** – Officially deprecated by Google. 

Here’s the full list:

### Working

|Search operator|What it does|Example|
|---|---|---|
|`“ ”`|Search for results that mention a word or phrase.|[“steve jobs”](https://www.google.com/search?q=%22steve+jobs%22)|
|`OR`|Search for results related to X or Y.|[jobs OR gates](https://www.google.com/search?&q=jobs+OR+gates)|
|`\|`|Same as `OR:`|[jobs \| gates](https://www.google.com/search?q=jobs%7Cgates)|
|`AND`|Search for results related to X and Y.|[jobs AND gates](https://www.google.com/search?&q=jobs+AND+gates)|
|`-`|Search for results that don’t mention a word or phrase.|[jobs -apple](https://www.google.com/search?q=jobs+-apple)|
|`*`|Wildcard matching any word or phrase.|[steve * apple](https://www.google.com/search?q=%22steve+*+apple%22)|
|`( )`|Group multiple searches.|[(ipad OR iphone) apple](https://www.google.com/search?q=%28ipad+OR+iphone%29+apple)|
|`define:`|Search for the definition of a word or phrase.|[define:entrepreneur](https://www.google.com/search?q=define%3Aentrepreneur)|
|`cache:`|Find the most recent cache of a webpage.|[cache:apple.com](https://webcache.googleusercontent.com/search?q=cache%3Aapple.com)|
|`filetype:`|Search for particular types of files (e.g., PDF).|[apple filetype:pdf](https://www.google.com/search?q=apple+filetype%3Apdf)|
|`ext:`|Same as `filetype:`|[apple ext:pdf](https://www.google.com/search?q=apple+ext%3Apdf)|
|`site:`|Search for results from a particular website.|[site:apple.com](https://www.google.com/search?q=site%3Aapple.com)|
|`related:`|Search for sites related to a given domain.|[related:apple.com](https://www.google.com/search?q=related%3Aapple.com)|
|`intitle:`|Search for pages with a particular word in the title tag.|[intitle:apple](https://www.google.com/search?q=intitle%3Aapple)|
|`allintitle:`|Search for pages with multiple words in the title tag.|[allintitle:apple iphone](https://www.google.com/search?q=allintitle%3Aapple+iphone)|
|`inurl:`|Search for pages with a particular word in the URL.|[inurl:apple](https://www.google.com/search?q=inurl%3Aapple)|
|`allinurl:`|Search for pages with multiple words in the URL.|[allinurl:apple iphone](https://www.google.com/search?q=allinurl%3Aapple+iphone)|
|`intext:`|Search for pages with a particular word in their content.|[intext:apple iphone](https://www.google.com/search?q=intext%3Aapple)|
|`allintext:`|Search for pages with multiple words in their content.|[allintext:apple iphone](https://www.google.com/search?q=allintext%3Aapple+iphone)|
|`weather:`|Search for the weather in a location.|[weather:san francisco](https://www.google.com/search?q=weather%3Asan+francisco)|
|`stocks:`|Search for stock information for a ticker.|[stocks:aapl](https://www.google.com/search?q=stocks%3Aaapl)|
|`map:`|Force Google to show map results.|[map:silicon valley](https://www.google.com/search?q=map%3Asilicon+valley)|
|`movie:`|Search for information about a movie.|[movie:steve jobs](https://www.google.com/search?q=movie%3Asteve+jobs)|
|`in`|Convert one unit to another.|[$329 in GBP](https://www.google.com/search?q=$329+in+GBP)|
|`source:`|Search for results from a particular source in Google News.|[apple source:the_verge](https://www.google.com/search?q=apple+source%3Athe_verge&tbm=nws)|
|`before:`|Search for results from before a particular date.|[apple before:2007-06-29](https://www.google.com/search?q=apple+before%3A2007-06-29)|
|`after:`|Search for results from after a particular date.|[apple after:2007-06-29](https://www.google.com/search?q=apple+after%3A2007-06-29)|

Sidenote.

You can also use the _ operator, which acts as a wildcard in Google Autocomplete.

### Unreliable

|Search operator|What it does|Example|
|---|---|---|
|`#..#`|Search within a range of numbers.|[iphone case $50..$60](https://www.google.com/search?q=iphone+case+%2450..%2460)|
|`inanchor:`|Search for pages with backlinks containing specific anchor text.|[inanchor:apple](https://www.google.com/search?q=inanchor%3Aapple)|
|`allinanchor:`|Search for pages with backlinks containing multiple words in their anchor text.|[allinanchor:apple iphone](https://www.google.com/search?q=allinanchor%3Aapple+iphone)|
|`AROUND(X)`|Search for pages with two words or phrases within X words of one another.|[apple AROUND(4) iphone](https://www.google.com/search?q=apple+AROUND(4))|
|`loc:`|Find results from a given area.|loc:”san francisco” apple|
|`location:`|Find news from a certain location in Google News.|[location:”san francisco” apple](https://www.google.com/search?q=loc:%22san+francisco%22+apple)|
|`daterange:`|Search for results from a particular date range.|[daterange:11278-13278](https://www.google.com/search?q=steve+jobs+daterange%3A11278-13278)|

### Not working (officially dropped by Google)

|Search operator|What it does|Example|
|---|---|---|
|`~`|Include synonyms in the search. [Dropped in 2013](https://searchengineland.com/google-drops-another-search-operator-tilde-for-synonyms-164403).|~apple|
|`"+"`|Search for results mentioning an exact word or phrase. [Dropped in 2011.](https://searchengineland.com/google-sunsets-search-operator-98189)|jobs +apple|
|`inpostauthor:`|Search for posts by a specific author in the [discontinued](https://searchengineland.com/google-blog-search-now-within-google-news-search-202202) Google Blog Search.|inpostauthor:”steve jobs”|
|`allinpostauthor:`|Same as `inpostauthor:`, but removes the need for quotes.|allinpostauthor:steve jobs|
|`inposttitle:`|Search for posts with certain words in the title in Google’s discontinued Blog Search.|inposttitle:apple iphone|
|`link:`|Search for pages linking to a particular domain or URL. [Dropped in 2017](https://searchengineland.com/google-officially-killed-off-link-command-267454).|link:apple.com|
|`info:`|Search for information about a specific page or website. [Dropped in 2017](https://searchengineland.com/google-changes-info-command-search-operator-dropping-useful-links-286422).|info:apple.com|
|`id:`|Same as `info:`|id:apple.com|
|`phonebook:`|Search for someone’s phone number. [Dropped in 2010](https://searchengineland.com/google-drops-phonebook-search-operator-56173).|phonebook:tim cook|
|`#`|Search for hashtags on Google+. Dropped in 2019 [when Google+ shut down](https://support.google.com/googlecurrents/answer/9195133).|#apple|


## 11 ways to use Google search operators

Let’s tackle a few ways to put these operators into action.

My aim here is to show that you can achieve almost anything with Google advanced operators if you know how to use and combine them. So don’t be afraid to play around and deviate from the examples below. You may just discover something new.

### 1. Find possible indexing issues

Eyeballing the results of a `site:` search for your website can uncover potential indexing issues. 

For example, if we combine it with the `filetype:` operator, we see that this 3D printing company has quite a few PDFs indexed: 

![[image38-768x580.webp]]

This isn’t a bad thing if it’s intentional, but I have a feeling it isn’t for some of these. 

For instance, its site has a lead-generation landing page for a white paper about the total cost of ownership for 3D printers:

![[image8-10.webp]]

But this PDF is indexed, so you can easily access it without filling in your details:

![[image23-5.webp]]

The site owners should probably add an [x-robots noindex tag](https://ahrefs.com/blog/meta-robots/) to solve this.

### 2. Find and analyze your competitors

Use the `related:` operator to find websites related to yours, which are often competitors.

![The related: operator shows related sites](https://ahrefs.com/blog/wp-content/uploads/2023/04/image19-6.png)

You can then use other search operators to investigate these sites further.

For example, if we search for `site:moz.com`, we can quickly see that it has published a lot of content on its blog, help section, and “SEO Learning Center.”

![[image19-6.webp]]

If we adjust our `site:` operator to focus on its Learning Center, we can start to get a sense of the type of content published and what it’s about.

![[image40-1.webp]]
In this case, it looks like there are lots of definition-type posts. 

In fact, if we add `intitle:("what is"|"what are")` to our search, we see 86 matching pages.

![[image29-1.webp]]

However, what Google can’t tell us is whether these pages get any organic traffic. To find that out, we’ll need to use a third-party tool.

If you’re an Ahrefs user:

1. Go to [Site Explorer](https://ahrefs.com/site-explorer)
2. Enter the competitor’s domain or subsection
3. Check the **Top pages** report

![[image5-13.webp]]

If you’re not an Ahrefs user, you can use [our free traffic checker](https://ahrefs.com/traffic-checker) to check pages one by one:

![[image34.webp]]
Both of these methods show that many of its definition-type posts are getting in excess of 20K estimated monthly organic visits. So this could be a good type of content to create if you wanted to attract search traffic in this niche. 

In fact, that’s exactly what we did with [our SEO glossary](https://ahrefs.com/seo/glossary).

Here’s its organic traffic growth over the last few months:

![[image4-11.webp]]
### 3. Find guest post opportunities

Most people find guest posting opportunities by searching for “write for us” pages in their niche. 

For example, if you have a website about coffee, you can search for something like `coffee intitle:"write for us" inurl:write-for-us`:

![[image17-6-768x612.png]]

However, as lots of people are using this method, you’ll often end up pitching the same sites as everyone else. For that reason, a better method is to find a serial guest blogger in your niche and look for sites they’ve written for.

You can do this by searching for `[topic] inurl:author/[firstname-lastname]`.

For example, this search finds websites Ryan Stewart has written for:
![[image39.webp]]

You can also do this in Ahrefs’ [Content Explorer](https://ahrefs.com/content-explorer) by searching for `[topic] author:[firstname lastname"]`.

![Searching for posts by a particular author using the author: operator in Ahrefs' Content Explorer](https://ahrefs.com/blog/wp-content/uploads/2023/04/image13-7.png)

The benefit of using Content Explorer over Google is that you can filter the results to focus on high-quality websites. Plus, not every site will use the `/author/firstname-lastname/` footprint. 

For example, we can easily filter for posts from websites with a Domain Rating (DR) above 30 and an estimated website traffic of at least 5K per month.
![[image13-7.webp]]

Sidenote.

This can sometimes generate a few false positives, depending on how common the person’s name is.

You can even highlight results from domains that haven’t linked to you so you can prioritize getting backlinks from more websites. 
![[image35.webp]]

### 4. Find resource page opportunities

Resource pages curate and link to the best resources on a topic. This makes them great link prospects if you have a fitting resource.

To find them in Google, search for: `[topic] intitle:resources inurl:resources`.

For example, if you want to build links to a coffee resource, you can search for this:
![[image18-5.webp]]

However, not all of these pages will be worth pitching. You’ll find that some just link to their own resources, so you’ll need to sift through them and pitch the relevant ones.

If you want an even easier way to find resource pages, try this: 

1. Go to Ahrefs’ [Site Explorer](https://ahrefs.com/site-explorer)
2. Enter the domain of a big competitor
3. Go to the **Backlinks** report
4. Filter for backlinks with “resources” in the Ref. page URL
![[image22-4.png]]

### 5. Find files you don’t want in Google’s index

You probably don’t want Google to index every file you upload to your website.

For example, if you have PDFs behind lead magnets or content upgrades, you probably want to protect those files to prevent people from finding them on Google.

Let’s use the `filetype:` operator to check for these on ahrefs.com.
![[image6-10.webp]]

It looks like there’s one PDF indexed, which is an old resource from 2017.

If we were bothered about people finding this (we’re not), we’d want to set this file to noindex with an [x-robots header response](https://ahrefs.com/blog/meta-robots/). 

### 6. Find the email address of the person you want to reach out to

People often share their email addresses on Twitter, so you can use search operators to find those tweets.

For example, if you wanted to find Tim Soulo’s email address, you could search for any of his tweets that mention the word “email” and “gmail.com” or “ahrefs.com” (as his email address is almost certainly at one of those domains).

If you do this, his email address pops up right away: 
![[image37.webp]]

Further reading

- [6 Ways to Find Anyone’s Email Address (Tried & Tested)](https://ahrefs.com/blog/find-email-address/)

### 7. Find opportunities to add internal links

Internally linking to important content from other relevant pages on your website can send it more traffic and potentially help it to rank higher in organic search.

For example, let’s say we wanted to add some internal links to [our list of SEO tips](https://ahrefs.com/blog/seo-tips/). 

If we search in Google for `site:ahrefs.com/blog "SEO tips"`, we’ll find blog posts mentioning the phrase “SEO tips” somewhere in their content. 
![[image2-11.webp]]

In this case, we can ignore the first result, as this is the post we want to build internal links to. But there are 99 other results mentioning SEO tips, and many of them are perfect contextual internal link opportunities.

For instance, [our guide to creating SEO content](https://ahrefs.com/blog/seo-content/) has an unlinked mention of “SEO tips,” so this is the perfect opportunity to add an internal link. 

![[image43-1.png]]

That said, the one downside of using search operators to find internal link opportunities is that they don’t distinguish between linked and unlinked mentions. In other words, they often find opportunities you’ve already taken advantage of.

For example, our search found a mention of “SEO tips” in [our list of SEO techniques](https://ahrefs.com/blog/seo-techniques/):
![[image41-1.png]]

But if we find that mention on the page, we see that it’s already internally linked:
![[image42.png]]

If this happens a lot and you find it frustrating, sign up for a free [Ahrefs Webmaster Tools](https://ahrefs.com/webmaster-tools) account and try this instead:

1. Crawl your website with [Site Audit](https://ahrefs.com/site-audit)
2. Go to the **Internal Link Opportunities** tool in Site Audit
3. Add your target page’s URL to the search field
4. Select “Target page” from the dropdown next to the search field
5. Hit the return key
![[image26-3.webp]]

You should see a list of opportunities like this: 
![[image24-3.webp]]

It tells you:

- Where to link from (Source page).
- Where to add the link (Keyword context).
- Where to link to (Target page).

Further reading

- [Internal Links for SEO: An Actionable Guide](https://ahrefs.com/blog/internal-links-for-seo/)

### 8. Find “best” listicles that don’t mention your brand

Let’s say you run an email marketing tool like ConvertKit. 

If you search Google for “best email marketing tools,” you’ll find thousands of results listing top picks:
![[image11-7.webp]]

Given that you probably want to be featured on these lists, it’ll be helpful to see which ones do and don’t mention you already, right? That way, you can reach out to the authors of lists not mentioning your tool and see if you can get them to add you.

Luckily, you can do that by appending your search with `-[your business name]`:

![[image33.webp]]

Alternatively, if you want an even quicker method, you can use Ahrefs’ [Content Explorer](https://ahrefs.com/content-explorer). 

If you’re not familiar with Content Explorer, it’s a search engine for marketers with an index of over 11 billion pages. You can use this search to find listicles that don’t mention your brand: `title:"best [whatever]" -[yourbrand]`.

For example, if we look for lists of the best email marketing tools that don’t mention ConvertKit, we get 3,182 results:
![[image27-2.webp]]

What makes [Content Explorer](https://ahrefs.com/content-explorer) more convenient than Google is that you can filter the results by things like DR, estimated website and page traffic, and more. Then you can export them in a few clicks.

For example, if we restrict the results to one page per domain and filter for websites with a DR of 30 or more, we narrow things down from 3,182 to 156 pages.

![[image31-2.png]]

This is a much more manageable number of websites to review and potentially reach out to.

### 9. Find websites that have reviewed competitors

If a website posts a review of a competitor, chances are it may also be willing to review you.

Here’s how to find competitor reviews: `allintitle:review ([competitor 1] OR [competitor 2])`.

For example, if we wanted to find reviews of ConvertKit competitors, we could search for this: 
![[image9-8.webp]]

If you like, you can add the `after:` operator into the mix to find recently published posts. This way, you can focus on pitching websites that you know are still active.
![[image44-1.webp]]

Sidenote.

You can use Ahrefs’ [SEO Toolbar](https://ahrefs.com/seo-toolbar) to download search results.

However, all of this is once again easier in [Content Explorer](https://ahrefs.com/content-explorer) because you can filter and export the results more easily. 

Here’s how to run the same search there:

1. Choose “In title” as the search mode
2. Search for `review (mailchimp OR aweber)`
3. Filter for one page per domain
![[image16-8.webp]]

This gives us 2,948 results, which is a lot. So let’s prioritize our list by filtering for pages published in the last 12 months on websites that get at least 1K monthly search visits:
![[image12-8.webp]]

Get alerts for new competitor reviews

Just set up a new “Mentions” alert in [Ahrefs Alerts](https://ahrefs.com/alerts). You can use the same search from [Content Explorer](https://ahrefs.com/content-explorer) and filters for DR and domain traffic too. 
![[image36.webp]]

### 10. Find relevant Quora questions to answer

Quora is a website where people ask questions, contributors post answers, and the best ones get upvoted to the top.

As my colleague, Si Quan Ong, has proven, it’s a great place to build brand awareness. He’s had over 2 million views on his answers and continues to get over 25K views every month despite his recent inactivity:
![[image14-9.webp]]

When it comes to finding questions to answer, Quora’s search function works well. The downside is that you can only search for one topic at once.

As Quora uses the question itself as the URL, you can overcome this problem with this search operator: `site:quora.com inurl:([topic 1] | topic 2)`.

For example, if you have a health and fitness website, you can search for something like this:
![[image20-8.webp]]

If you’re an Ahrefs user, you can even combine this with the [SEO Toolbar](https://ahrefs.com/seo-toolbar) to overlay traffic estimates on the SERP. That way, you can focus on answering questions that already get organic traffic.
![[image3-13.webp]]

Or if you want an even faster method, try this:

1. Go to Ahrefs’ [Site Explorer](https://ahrefs.com/site-explorer)
2. Enter quora.com
3. Go to the **Top pages** report
4. Filter for results with URLs that contain particular words

This will give you a list of relevant Quora answers, sorted by their estimated monthly search traffic from high to low.

![[image25-3.webp]]

For example, one of the questions above asks whether it’s better to make a protein shake with milk or water and gets an estimated 792 monthly visits. If you can answer this question well and get upvoted, chances are hundreds of people will see your answer every month.

Even better, as you can include links in your answers, these answers can send some nice referral traffic your way.

### 11. Find how fast your competitors are publishing new content

Combine the `site:` operator with `before:` and/or `after:` operators to find out how much content any competitor has published in a given time period.

For example, here’s how many posts another SEO blog published in December 2022: 

![[image28-2.webp]]

And here’s how many it published in the whole of 2022:

![[image15-8.webp]]

Just be aware that this operator isn’t always 100% accurate, as it includes updated pages.

For example, the search below returns a post with January 25, 2022, attached to it:
![[image30-1.webp]]

But if we plug that post’s URL into Ahrefs’ [Site Explorer](https://ahrefs.com/site-explorer), we see that it’s been attracting organic traffic since 2019. So it must have existed long before 2022.

![[image1-10.webp]]

If you’re an Ahrefs user and want a more accurate way to see a competitor’s publishing frequency, run a `site:` search in [Content Explorer](https://ahrefs.com/content-explorer) and filter for “Pages published once.” 

![[image21-4.webp]]

## Final thoughts

Google advanced search operators are super powerful. You just have to know how to use them.

But I have to admit that some are more useful than others, especially when it comes to SEO. I find myself using `site:`, `intitle:`, and `inurl:` often. Yet I rarely use `allintitle:` and many of the other more obscure operators.

I’d also add that many operators are borderline useless unless paired with another operator, or two, or three.

So do play around with them and let me know what you come up with. 

I’d be more than happy to add any useful combinations you discover to the post. 

Got questions? Ping me [on Twitter](https://twitter.com/joshuachardwick).