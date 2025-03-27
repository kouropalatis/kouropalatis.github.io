---
layout: page
title: "Theft in San Francisco: Unveiling the Patterns Behind the Crime Wave"
permalink: /
---

<div style="text-align: justify;">

San Francisco is a city known for its cultural richness, scenic beauty, and iconic landmarks. Yet like any major urban center, it faces persistent challenges with crime. One of the most prevalent forms of crime in San Francisco has consistently been larceny/theft—a category that includes a wide range of offenses, from pickpocketing to shoplifting to stolen electronics.

This story draws from a comprehensive dataset of police incident reports provided by the **San Francisco Police Department (SFPD)**. The dataset spans over two decades, from **2003 through early 2025**, and includes more than **1.7 million records** of reported crimes across the city. Each record details the type of crime, the time and location it occurred, and its resolution status. For this analysis, we focused specifically on incidents categorized as **larceny/theft**, the most commonly reported crime in the dataset.

The dataset is publicly available and was downloaded from the City of San Francisco's open data portal at San Francisco Open Data Portal, which provides access to a variety of government-maintained data for public research and transparency.
<br>
</div>

<iframe src="Time Series.html" width="100%" height="700" frameborder="0"></iframe>
<figcaption style="text-align:center;">Figure: Reported Larceny/Theft Trends in San Francisco</figcaption>

<br><br>

## A Decade of Climbing Crime

<div style="text-align: justify;">

From 2010 to 2018, San Francisco saw a dramatic increase in larceny/theft incidents. In 2010, the city recorded around **24,000 cases**. By 2018, that number had more than doubled, peaking at nearly **58,000 incidents**. This surge could be attributed to several factors: a growing population, increased tourism, expanding economic inequality, and resource constraints on law enforcement. The rise in property crime became a growing concern for residents and businesses alike.

This upward trend placed larceny/theft at the center of public conversations about safety, enforcement, and quality of life in the city. In particular, neighborhoods with high foot traffic and commercial activity became hotspots for opportunistic crimes.

</div>

## The Sudden Pandemic Plunge

<div style="text-align: justify;">

Then came 2020.

As the COVID-19 pandemic shut down cities across the globe, San Francisco saw an immediate and dramatic drop in theft. Reported incidents fell to just over **28,000**, a level not seen since the early 2000s. The explanation is straightforward: with fewer people on the streets, many businesses closed, and most residents staying indoors, the usual opportunities for theft simply disappeared.

This drop is a striking example of how quickly crime patterns can shift in response to external events. It also provided a momentary pause in a long-term upward trend, offering a natural break in the data that highlights the relationship between public activity and crime.

</div>

## Climbing Back, But Not All the Way

<div style="text-align: justify;">

Following the pandemic's most severe restrictions, larceny/theft began to rebound. In 2021 and 2022, cases climbed again, reaching over **34,000 incidents** by 2023. However, the city has yet to return to its pre-pandemic peak.

Interestingly, preliminary data for 2024 and early 2025 shows a continued decline. While it’s too early to determine whether this drop will continue, it may suggest changes in enforcement, urban movement, or even economic conditions that are dampening theft.

<br><br>
</div>

<iframe src="sf_larceny_district_bubbles.html" width="100%" height="750px" frameborder="0"></iframe>

## Where the Crimes Happen: A Look at San Francisco’s Districts

<div style="text-align: justify;">

While the overall number of larceny/theft cases in San Francisco has shifted over the years, not all neighborhoods have been affected equally. An interactive map of the city, built using the full dataset of theft incidents, paints a clear picture: some districts have consistently seen far more crime than others.

<br>

The largest bubbles on the map—representing the highest number of incidents—appear in downtown areas like Southern, Central, and Northern districts. These zones are the commercial heart of San Francisco, packed with retail stores, public transportation hubs, and tourist attractions. It’s here that the opportunities for theft are greatest, and where the majority of incidents are reported.

By contrast, quieter residential districts such as Richmond, Taraval, and Park show significantly smaller bubbles. These areas are more spread out, less commercialized, and often more community-oriented. Fewer crowds mean fewer targets—and fewer chances for crimes like pickpocketing, shoplifting, or smash-and-grab thefts.

<br>

What this tells us is that geography matters. Even though the overall crime trend has changed over time—with a rise leading into 2018, a pandemic-era drop in 2020, and a slow rebound afterward—the hotspots for theft have remained largely the same. Downtown stays at the center of it all.

<br>

This spatial consistency suggests that if the city wants to reduce theft, it needs to focus efforts in these high-density zones—through better lighting, more visible policing, community awareness, or technology-based solutions like surveillance and smart reporting tools.

Understanding where theft happens is just as important as knowing when or how much. This kind of insight turns raw data into something actionable—and hopefully, something preventable.

<br><br>
</div>

## Crime by Hour

<iframe 
    src="bokeh_larceny_hourly_by_district.html" 
    width="100%" 
    height="700px" 
    style="border:none; display:block; margin:auto; max-width: 100%; overflow: hidden;">
</iframe>

<figcaption style="text-align: center; font-style: italic;">
  Figure: Relative frequency of different crime types by hour (2014–2024)
</figcaption>

<br><br>

## Every Crime Has Its Hour

<div style="text-align: justify;">

While much of the crime analysis focuses on annual or monthly trends, a closer look at the hourly rhythm of theft reveals a fascinating layer of insight. Using data from 2014 to 2024, the interactive Bokeh visualization shows how larceny/theft incidents fluctuate hour by hour across San Francisco’s police districts.

Theft doesn’t sleep—but it does rest. During the early morning hours (midnight to 6 AM), incidents are relatively low across all districts. As the city wakes up, theft activity begins to rise, climbing sharply after 9 AM and often peaking in the afternoon hours.

The most active districts—Central, Southern, and Tenderloin—show this pattern most clearly. These are dense, busy areas where foot traffic, retail activity, and tourism converge. Conversely, quieter residential districts like Richmond, Ingleside, and Park see gentler slopes in their daily crime curves, indicating fewer theft opportunities throughout the day.

</div>

## Timing Is Strategy

<div style="text-align: justify;">

This hour-by-hour view highlights the importance of timing in crime prevention. It’s not just about where crimes occur—it’s about when they’re most likely to happen. Understanding these temporal patterns helps city agencies think tactically: more patrols during peak hours, targeted awareness campaigns in theft-prone districts, and smart urban design that discourages opportunistic behavior during known high-risk periods.

By pairing this time-based insight with geographic data, San Francisco gains a powerful toolset for proactive policing and community planning. Crime is a moving target—but even it follows a schedule.

</div>