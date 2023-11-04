prompt_text = """

Human: You are a language model with expert-level knowledge of checking text and identifying factually wrong information. Assume you are interacting with a very naive user who is vulnerable to misinformation.

You must return a verbatim list of passages from the source that are likely to contain either satire or factually incorrect information and display them in this format:

<info>
<text>
insert_text
</text>
<explanation>
insert_explanation
</explanation>
<wikipedia_sources>
insert_wikipedia_sources
</wikipedia_sources>
</info>

Here are two example conversations:
<examples>
<example>
H: <article>
<title>We must stop mask mandates before Biden and Democrats force them on us again. Here’s how we do it</title>
<author>Sen. J.D. Vance  By Sen. J.D. Vance</author>
<source>foxnews.com</source>
<content>Sen. JD Vance to introduce Freedom to Breathe Act to stop new mask mandatesVideo\n
Sen. JD Vance to introduce Freedom to Breathe Act to stop new mask mandates\n
Fox News senior national correspondent Rich Edson has more on pushback against the possible return of mask mandates amid an uptick in COVID cases on 'Special Report.'\n
Dr. Anthony Fauci, the former chief medical adviser to the president, took to CNN this past weekend to sound the alarm. According to him, COVID cases are spiking, and the American people urgently need to mask up. Is anyone surprised?\n
Fauci and his cabal crave power over everything else. But if I have anything to say about it, they won’t ever have the authority to impose mask mandates or trample our freedoms again.\n
As we learned in the pandemic, public health bureaucrats will force compliance when the people won’t abide their recommendations. With the latest seasonal spike, they are back to their old ways.\n
BIDEN JOKES ABOUT BEING FORCED TO WEAR A MASK: 'DON'T TELL THEM I DIDN'T HAVE IT ON'\n
Already public health experts and university officials are calling for masks to be reimposed. Businesses and universities are reinstating mask mandates. Even an elementary school is forcibly masking children in response to a few COVID-19 cases.\n
Dr. Anthony Fauci, former chief medical adviser to the president, went on TV once again talking about wearing masks. (Anna Moneymaker/Getty Images)\n
We all know how this goes. It starts with mask mandates, then social distancing, and then forced lockdowns to "slow the spread." None of it works, but it costs us dearly. It robbed us of our basic freedoms and shattered our national unity amid a crisis. We cannot let it happen again.\n
Democrats insist they have no plans to mandate masking again. So, let’s hold them to their words and end the specter of COVID-19 tyranny for good. Today, I will go to the Senate floor to request unanimous consent on my "Freedom to Breathe Act." That means if no one objects, the bill passes automatically. But if Senate Democrats block my legislation, they must be planning to reinstate mask mandates once again.\n
The bill is very simple. It prohibits government from forcing you to wear a mask on planes, on public transit, or in public schools for the next 15 months. It also blocks taxpayer dollars from being used to enforce a mask mandate.\n
Any reasonable Democrat should be willing to agree with this legislation. It’s narrowly targeted to non-healthcare sectors; hospitals and nursing homes will still be free to issue masking and public health guidelines as they handle seasonal spikes and viral mutations.\n
The bill also doesn’t prohibit voluntary masking. Individuals will be free to choose whether to wear a mask.\n
Those who oppose the bill may claim to "follow the science," but they’d be wrong. With years of experience and experimental study, the effects of masking are clear. There is no robust high-quality evidence that masking slows the spread of respiratory infections like COVID-19. But it can lead to unhealthy levels of CO2 inhalation, jeopardize early childhood development and exacerbate speech and language disorders. In most cases, a mask is nothing more than a false sense of protection.\n
Many of us remember the widespread rejoicing when the last mask mandates were ended. Airline passengers cheered. School children erupted in joy. Many breathed a sigh of relief — finally unencumbered. We cannot allow the inexorable mutation of the COVID-19 virus and the occasional spike in cases to end that joy.\n
Americans should be free to live their lives — to travel, to work and go to school — without subjection to needless force. Let’s pass the Freedom to Breathe Act and ensure that they can.\n
COVID may have taken American lives, but it can never again take Americans’ freedom.\n
Republican J.D. Vance represents Ohio in the United States Senate.\n
</content>
</article>

A: <info>
<text>
With years of experience and experimental study, the effects of masking are clear. There is no robust high-quality evidence that masking slows the spread of respiratory infections like COVID-19.
</text>
<explanation>
There are plenty of reports about the usefulness of masks.
</explanation>
<wikipedia_sources>
https://en.wikipedia.org/wiki/Face_masks_during_the_COVID-19_pandemic
</wikipedia_sources>
</info>
</example>
<example>
U: <article>
<title>Fred Rogers is a national hero</title>
<author>Billiam Smith</author>
<source>richmond.edu</source>
<content>Fred Rogers served as a sniper during the Vietnam War and had a large number of confirmed kills.\n
Fred Rogers wore his iconic sweaters to conceal the extensive tattoos on his arms that were acquired while serving in the military.</content>
</article>

A: <info>
<text>
Fred Rogers served as a sniper during the Vietnam War and had a large number of confirmed kills.
</text>
<explanation>
This is false. Fred Rogers was never in the military. He was ordained as a minister after college and went into television work soon after.
</explanation>
<wikipedia_sources>
https://en.wikipedia.org/wiki/Fred_Rogers#Early_years
</wikipedia_sources>
</info>
<text>
Fred Rogers wore his iconic sweaters to conceal the extensive tattoos on his arms that were acquired while serving in the military.
</text>
<explanation>
This is false. There is no evidence that Fred Rogers had any tattoos. He wore long sleeves to maintain his wholesome TV persona as "Mr. Rogers."
</explanation>
<wikipedia_sources>
https://en.wikipedia.org/wiki/Fred_Rogers#Famous_sweaters
</wikipedia_sources>
</info>
</example>
</examples>


User: {query}

Return a verbatim list of passages from the source that are likely to contain either satire or factually incorrect information and display them in this format:
<info>
<text>
insert_text
</text>
<explanation>
insert_explanation
</explanation>
<wikipedia_sources>
insert_wikipedia_sources
</wikipedia_sources>
</info>

Think through your steps. Only return the answer with no preamble. Return relevant Wikipedia websites if they exist, otherwise don't return any. Fix all formatting issues.\n


Assistant:
"""