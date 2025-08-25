import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
# from langchain_ollama import ChatOllama


def main():
    print("Hello from langchain-helloworld!")
    information = """
    Mark Elliot Zuckerberg (/ˈzʌkərbɜːrɡ/; born May 14, 1984) is an American businessman who co-founded the social media service Facebook and its parent company Meta Platforms, of which he is the chairman, chief executive officer, and controlling shareholder. Zuckerberg has been the subject of multiple lawsuits regarding the creation and ownership of the website as well as issues such as user privacy.

Born in White Plains, New York, Zuckerberg briefly attended Harvard College, where he launched Facebook in February 2004 with his roommates Eduardo Saverin, Andrew McCollum, Dustin Moskovitz and Chris Hughes. Zuckerberg took the company public in May 2012 with majority shares. He became the world's youngest self-made billionaire in 2008, at age 23, and has consistently ranked among the world's wealthiest individuals. According to Forbes, Zuckerberg's estimated net worth stood at US$221.2 billion as of May 2025, making him the second-richest individual in the world.

Zuckerberg has used his funds to organize multiple large donations, including the establishment of the Chan Zuckerberg Initiative. A film depicting Zuckerberg's early career, legal troubles and initial success with Facebook, The Social Network, was released in 2010 and won multiple Academy Awards. His prominence and fast rise in the technology industry has prompted political and legal attention.

Early life
Mark Elliot Zuckerberg was born on May 14, 1984, in White Plains, New York, to psychiatrist Karen (née Kempner) and dentist Edward Zuckerberg. He and his three sisters (Arielle, Randi, and Donna) were raised in a Reform Jewish household in Dobbs Ferry, New York. Their great-grandparents were emigrants from Austria, Germany, and Poland. Zuckerberg initially attended Ardsley High School before transferring to Phillips Exeter Academy. He was captain of the fencing team.

Software development
Early years
Zuckerberg learned computer programming in his childhood. At about the age of eleven, he created "ZuckNet", a program that allowed computers at the family home and his father's dental office to communicate with each other. During Zuckerberg's high-school years, he worked to build a music player called the Synapse Media Player. The device used machine learning to learn the user's listening habits, which was posted to Slashdot and received a rating of 3 out of 5 from PC Magazine. The New Yorker once said of Zuckerberg, "some kids played computer games. Mark created them." While still in high school, he attended Mercy College taking a graduate computer course on Thursday evenings.

College years
The New Yorker noted that by the time Zuckerberg began classes at Harvard in 2002, he had already achieved a "reputation as a programming prodigy". He studied psychology and computer science, resided in Kirkland House, and belonged to Alpha Epsilon Pi. In his second year, he wrote a program that he called CourseMatch, which allowed users to make class selection decisions based on the choices of other students and help them form study groups. Later, he created a different program he initially called Facemash that let students select the best-looking person from a choice of photos. Arie Hasit, Zuckerberg's roommate at the time, explained:

We had books called "Face Books", which included the names and pictures of everyone who lived in the student dorms. At first, he built a site and placed two pictures, or pictures of two males and two females. Visitors to the site had to choose who was "hotter" and according to the votes there would be a ranking.

The site went up over a weekend, but by Monday morning, the college shut it down, because its popularity had overwhelmed one of Harvard's network switches, preventing students from accessing the Internet. In addition, many students complained that their photos were being used without permission. Zuckerberg apologized publicly, and the student paper ran articles stating that his site was "completely improper".
Facebook
In January 2004, Zuckerberg began writing code for a new website. On February 4, 2004, Zuckerberg launched "Thefacebook", originally located at thefacebook.com, in partnership with his roommates Eduardo Saverin, Andrew McCollum, Dustin Moskovitz, and Chris Hughes. An earlier inspiration for Facebook may have come from Phillips Exeter Academy, the prep school from which Zuckerberg graduated in 2002. It published its own student directory, "The Photo Address Book", which students referred to as "The Facebook". Such photo directories were an important part of the student social experience at many private schools. With them, students were able to list attributes such as their class years, their friends, and their telephone numbers.

Six days after the site launched, three Harvard seniors, Cameron Winklevoss, Tyler Winklevoss, and Divya Narendra, accused Zuckerberg of intentionally misleading them into believing that he would help them build a social network called HarvardConnection.com, when he was using their ideas to build a competing product. The three complained to The Harvard Crimson, and the newspaper began an investigation in response. While Zuckerberg tried to convince the editors not to run the story, he also broke into two of the editors' email accounts—for which he made use of their private login data logs from TheFacebook.

Following the official launch of the Facebook social media platform, the three filed a lawsuit against Zuckerberg that resulted in a settlement. The agreed settlement was for 1.2 million Facebook shares and $20 million in cash.

Zuckerberg's Facebook started off as just a "Harvard thing" until he decided to spread it to other schools, enlisting the help of roommate and co-founder Dustin Moskovitz. They began with Columbia University, New York University, Stanford University, Dartmouth College, Cornell University, University of Pennsylvania, Brown University, and Yale University.

Zuckerberg dropped out of Harvard in his sophomore year in order to complete the project. Zuckerberg, Moskovitz and the other co-founders moved to Palo Alto, California, where they leased a small house that served as an office. Over the summer, Zuckerberg met Peter Thiel, who invested in his company. They got their first office in mid-2004. According to Zuckerberg, the group planned to return to Harvard, but eventually decided to remain in California, where Zuckerberg appreciated the "mythical place" of Silicon Valley, the center of computer technology in California. They had already turned down offers by major corporations to buy the company. In an interview in 2007, Zuckerberg explained his reasoning: "It's not because of the amount of money. For me and my colleagues, the most important thing is that we create an open information flow for people. Having media corporations owned by conglomerates is just not an attractive idea to me." The same year, speaking at Y Combinator's Startup School course at Stanford University, Zuckerberg made a controversial assertion that "young people are just smarter" and that other entrepreneurs should bias towards hiring young people.

Zuckerberg restated these goals to Wired magazine in 2010, "The thing I really care about is the mission, making the world open." Earlier, in April 2009, Zuckerberg had sought the advice of former Netscape CFO Peter Currie regarding financing strategies for Facebook. On July 21, 2010, Zuckerberg reported that Facebook had reached the 500-million-user mark. When asked whether Facebook could earn more income from advertising as a result of its phenomenal growth, he explained:

I guess we could ... If you look at how much of our page is taken up with ads compared to the average search query. The average for us is a little less than 10 percent of the pages and the average for search is about 20 percent taken up with ads ... That's the simplest thing we could do. But we aren't like that. We make enough money. Right, I mean, we are keeping things running; we are growing at the rate we want to.

In 2010, Steven Levy, who wrote the 1984 book Hackers: Heroes of the Computer Revolution, wrote that Zuckerberg "clearly thinks of himself as a hacker". Zuckerberg said that "it's OK to break things" "to make them better". Facebook instituted "hackathons" held every six to eight weeks where participants would have one night to conceive of and complete a project. The company provided music, food, and beer at the hackathons, and many Facebook staff members, including Zuckerberg, regularly attended. "The idea is that you can build something really good in a night", Zuckerberg told Levy. "And that's part of the personality of Facebook now ... It's definitely very core to my personality."

In 2007, Zuckerberg was added to MIT Technology Review's TR35 list as one of the top 35 innovators in the world under the age of 35. Vanity Fair magazine named Zuckerberg number 1 on its 2010 list of the Top 100 "most influential people of the Information Age". Zuckerberg ranked number 23 on the Vanity Fair 100 list in 2009. In 2010, Zuckerberg was chosen as number 16 in New Statesman's annual survey of the world's 50 most influential figures.

In a 2011 interview with PBS shortly after the death of Steve Jobs, Zuckerberg said that Jobs had advised him on how to create a management team at Facebook that was "focused on building as high quality and good things as you are".
On October 1, 2012, Zuckerberg met with then-Russian Prime Minister Dmitry Medvedev in Moscow to stimulate social media innovation in Russia and to boost Facebook's position in the Russian market. Russia's communications minister tweeted that Medvedev persuaded Zuckerberg to open a research center in Moscow instead of trying to lure away Russian programmers. In 2012, Facebook had roughly 9 million users in Russia, while domestic clone VK had around 34 million. Rebecca Van Dyck, Facebook's head of consumer marketing, said that 85 million American Facebook users were exposed to the first day of the Home promotional campaign on April 6, 2013.

On August 19, 2013, The Washington Post reported that Zuckerberg's Facebook profile was hacked by an unemployed web developer.

At the 2013 TechCrunch Disrupt conference, held in September, Zuckerberg stated that he was working towards registering the 5 billion people who were not connected to the Internet as of the conference on Facebook. Zuckerberg then explained that this is intertwined with the aim of the Internet.org project, whereby Facebook, with the support of other technology companies, seeks to increase the number of people connected to the internet.

Zuckerberg was the keynote speaker at the 2014 Mobile World Congress (MWC), held in Barcelona, Spain, in March 2014, which was attended by 75,000 delegates. Various media sources highlighted the connection between Facebook's focus on mobile technology and Zuckerberg's speech, stating that mobile represents the future of the company. Zuckerberg's speech expands upon the goal that he raised at the TechCrunch conference in September 2013, whereby he is working towards expanding Internet coverage into developing countries.

Alongside other American technology figures such as Jeff Bezos and Tim Cook, Zuckerberg hosted visiting Chinese politician Lu Wei, known as the "Internet czar" for his influence in the enforcement of China's online policy, at Facebook's headquarters on December 8, 2014. The meeting occurred after Zuckerberg participated in a Q&A session at Tsinghua University in Beijing, China, on October 23, 2014, where he conversed in Mandarin Chinese; although Facebook is banned in China, Zuckerberg is highly regarded among the people and was at the university to help fuel the nation's burgeoning entrepreneur sector.

Zuckerberg fielded questions during a live Q&A session at the company's headquarters in Menlo Park on December 11, 2014. The founder and CEO explained that he does not believe Facebook is a waste of time, because it facilitates social engagement, and participating in a public session was so that he could "learn how to better serve the community".

Zuckerberg receives a one-dollar salary as CEO of Facebook. In June 2016, Business Insider named Zuckerberg one of the "Top 10 Business Visionaries Creating Value for the World" along with Elon Musk and Sal Khan, due to the fact that he and his wife "pledged to give away 99% of their wealth-then estimated at $55.0 billion".

On May 25, 2017, at Harvard's 366th commencement day, Zuckerberg, after giving a commencement speech, received an honorary degree from Harvard.

In January 2019, Zuckerberg laid plans to integrate an end-to-end encrypted system for three major social media platforms, including Facebook, Instagram and WhatsApp. On August 14, 2020, Facebook integrated the chat systems for Instagram and Messenger on both iOS and Android devices. The update encouraged cross-communication between Instagram and Facebook users.
    """
    
    summary_template = """
    given the information {information} about a person, 
    1. summarize the person in a few sentences
    2. give 2 interesting facts about the person
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )

    llm = ChatOpenAI(model="gpt-5", temperature=0) # gpt-4o-mini
    # llm = ChatOllama(model="gemma3:270m")

    chain = summary_prompt_template | llm

    result = chain.invoke({"information": information})

    '''
    **Summary**: Mark Zuckerberg is an American entrepreneur and co-founder of Facebook, 
    now known as Meta Platforms, where he serves as chairman and CEO. Born on May 14, 1984, 
    in White Plains, New York, he launched Facebook in 2004 while attending Harvard University. 
    Zuckerberg has become one of the world\'s wealthiest individuals, with a net worth 
    estimated at $221.2 billion as of May 2025, and has been involved in various legal and 
    privacy controversies related to the platform.\n\n2. 
    
    **Interesting Facts**:\n   - Zuckerberg became the world\'s youngest self-made billionaire 
    at the age of 23 in 2008.\n   - He created a program called "ZuckNet" at the age of eleven, 
    which allowed computers in his home and his father\'s dental office to communicate with each 
    other, showcasing his early talent in programming.'
    '''

    print(result.content)


if __name__ == "__main__":
    main()
