import os
from langchain_ollama import ChatOllama
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate


load_dotenv()


def main():
    print("Hello from langchain-course!")
    information = """A group of Indian Army Soldiers cordons off a village as a part of Counter-Insurgency Operation, in the Punj Area of Pulwama Dist in Kashmir Valley. After numerous chase sequences, the shot ends with an army officer being shot by his colleague. The offending officer instead of escaping promptly surrenders and is then taken into custody by his colleagues.

                    In New Delhi, best friends and army lawyers Major Siddhant Chaudhary and Major Akash Kapoor display contrasting personalities, with Akash being a dedicated army lawyer and Siddhant being an immature and care-free army officer. Siddhant (fondly called "Sid"), being the son of a highly decorated army officer, often feels compelled to live up to his father's legacy and therefore he reluctantly chooses to join the army. However, he himself has no plans for an army career and is therefore on the lookout for any chance to quit the army for an adventurous life.

                    In the present day, Akash is getting engaged to his fiancée Nandini, with Siddhant as his best man. Akash informs Siddhant that their postings are now due, with Akash himself expecting to get posted in Srinagar. A rather excited Siddhant asks Akash to swing his posting too so that they both could be posted together. Akash, despite his misgivings, agrees to Siddhant's demands and thus makes an official request to the Army HQ, thus ensuring the same posting for Siddhant.

                    A week prior to departure, Siddhant becomes aware of him being appointed as a defence lawyer and Akash being appointed the prosecuting lawyer, in a murder case involving two army officers, both belonging to the elite Rashtriya Rifles. On being aware about the nature of his new posting, Siddhant, who had the hopes of a tension-free tenure, throws a childish fit, but ends up getting shut up by an annoyed Akash.

                    Meanwhile, a young aspiring Srinagar-based journalist Kavya Shastri, in the hopes of a big story, chances upon the murder case involving two army officers. On further research, Kavya gathers that their names were Captain. Javed Khan and Major Virendra Singh Rathore, who, when deployed for a Counter-Insurgency operation, got into an argument, which ended with Javed fatally shooting Rathore. An army inquiry deems Javed guilty of insubordination and murder and is then to be subjected to a General Court Martial after a show trial.

                    An enthusiastic Kavya attempts to approach Javed, to get his side of story, but her efforts fail as the army authorities flatly refuse her request. Meanwhile, both Akash and Siddhant arrive in Srinagar, post which the duo get briefed by their CO, about the case. After the briefing, Siddhant heads out to meet Javed, for a better understanding of the case.

                    Javed and Siddhant meet at the barracks, where Siddhant makes a poor attempt at interrogation. Javed, unimpressed with Siddhant's immaturity, refuses to acknowledge him and continues maintaining a stoic silence. Javed's behavior angers and frustrates Siddhant, who ends up leaving in a huff.

                    Siddhant later confides his fears and doubts about the case to Akash, who is understanding of Siddhant's dilemma. Akash advises Siddhant to just plead guilty on Javed's behalf, while he promises to take care of all the prosecution work. To cheer up Siddhant, Akash points out the absurdity of the case, terming it open and shut. According to Akash, Javed is the guilty party and the case itself is unsubstantiated, thus making prosecution a cakewalk.

                    Meanwhile, Kavya, on hearing about the trial, tries to reach out to Siddhant. Siddhant, on meeting Kavya, gets attracted to her and relentlessly tries to flirt with her. He even attempts to bluff his way through the case, despite not having any idea himself, just to impress her.

                    His efforts however miserably fail as the unimpressed Kavya calls out Siddhant and exposes his lies about the case. She further points out that as the defence lawyer it is Siddhant's responsibility to properly analyze the case and present the facts. Before leaving she further tries to make Siddhant realize the consequences of his decisions and their impact on his life. However while flirting, Siddhant accidentally mentions a senior army officer Brigadier Pratap, who happens to be Javed's and Rathore's commanding officer. Kavya gets intrigued and presses for more information but Siddhant hastily covers up, thus prompting a disappointed Kavya to leave.

                    After the meeting, however, Kavya heads to her office where she writes and later publishes a slanderous article about Brigadier Pratap in a local daily, naming Siddhant as the source of information. The article spreads like wildfire and ends up causing huge embarrassment to the Army, thus leading Siddhant to get hauled up by his superiors.

                    A furious Siddhant later confronts Kavya and accuses her of betrayal and cheap sensationalism, at the cost of his reputation. Kavya instead hits back and accuses Siddhant of negligence and immaturity. She further tells him to focus on his job rather than worrying about a silly article.

                    Siddhant's superiors reprimand him for his actions as Brigadier Pratap is later revealed to be a highly decorated officer with a spotless reputation. Siddhant wishes for a meeting with Brigadier Pratap so as to apologize to him in person. The authorities grant him the permission and Siddhant heads out to meet Pratap, who is deployed at a forward area near the LOC.

                    Siddhant, on meeting Pratap, gets intimidated. He profusely apologizes for his actions but Pratap simply brushes the incident away. Seeing Pratap's jovial mood, Siddhant tries to press Pratap for more information regarding the Rathore murder case, but a dismissive Pratap coldly rebuffs him. Siddhant then tries to get access to the scene of the crime and to his relief Pratap accepts his request. Siddhant analyzes the scene of the crime and suspects something amiss. He tries to reach out to the local populace but he encounters their towards Vowing to get to the bottom of the case, Siddhant heads back to Srinagar. He then meets up with Javed, informing him of his meeting with Brigadier Pratap. Javed, for the first time, speaks, and asks Siddhant whether he thinks Javed is innocent or guilty. A baffled Siddhant tells Javed that he will inform his decision to the court along with presenting all the necessary facts.

                    Later in the evening Siddhant and Kavya run into each other. Despite a rocky start Siddhant becomes warm towards Kavya, who herself starts appreciating Siddhant's honesty and commitment. Kavya informs Siddhant about a major cover-up regarding the Rathore murder case, involving Brigadier Pratap and cautions him to be careful. Siddhant privately agrees and tells her about his meeting with Pratap, with Kavya promising to help Siddhant in every way possible. She later hands him several documents crucial for the case. A grateful Siddhant thanks her and heads back to further analyze the case. After spending the whole night studying the case, Siddhant concludes that Javed may actually be innocent and instead be a victim of a cover-up.

                    A now-mature Siddhant decides to take the case head-on. On the day of the prosecution, Siddhant blatantly goes against Akash's advice and to the surprise of many (including Javed himself), declares Javed not guilty. His actions earn Akash's ire who calls him irresponsible. Siddhant however maintains his decision and vows to prove Javed's innocence. This causes a frosty relationship between the two best friends for temporary. Despite this, they reconcile and Siddhant helps Akash get married in an impromptu ceremony.

                    Meanwhile, Javed, after witnessing Siddhant's genuine efforts, decides to completely open up. He not only answers all of Siddhant's questions but also provides him with documents that prove Javed's innocence, thus helping him prepare a strong defence. Kavya, meanwhile, pays a visit to Javed's ancestral village, where she meets Javed's mother. Kavya gathers the necessary information and heads back to Srinagar. She then meets up with Siddhant and the duo chalk out a plan to prove Javed's innocence.

                    On the day of the trial, Siddhant presents a credible defense that effectively counters Akash's narrative. While questioning the witnesses who were present at the time of the incident, Siddhant finds one witness, Captain R. P. Singh, to be suspiciously evasive. However, before he could probe any further, the session ends in a stalemate. Siddhant later meets up with Kavya and informs her about the day's trial.

                    Kavya then suggests paying Major Rathore's family a visit. The next day both Siddhant and Kavya visit Rathore's home and meet his widow Neerja and her son Kshitij. Kavya attempts to press Neerja for valuable information, while Siddhant snoops around the house for clues, but both end up empty-handed. Siddhant remarks that it was indeed odd that both Neerja and Kshitij failed to turn up for Major Rathore's funeral, but Kavya reveals that their marriage was an abusive one and Rathore's death seems to have sort of liberated her from some sort of bondage. While heading back, Siddhant comes to startling conclusion that not only proves Javed's innocence all along but also proves Major Rathore's guilt.

                    Kavya comes across evidence of the Indian Army's human rights violations in Jammu and Kashmir. She, on further analysis, concludes that both Brigadier Pratap and Major Rathore, who were known to be very close, also have numerous complaints of human rights abuses against them. Kavya sends the necessary proofs to Siddhant but is arrested for trespassing on army area and trying to access sensitive information without due authorization. Siddhant tries to bail out Kavya but fails. Kavya conveys her suspicions to Siddhant and tells him to focus completely on the case.

                    One night Javed's mother pays Siddhant a visit. She pleads Siddhant to fairly judge her son, whereupon Siddhant promises a fair trial for Javed. Meanwhile, Neerja posts several documents to Siddhant, after getting his address in a gift he sent to Neerja's son, that were important for the case. Siddhant on further probing finds a strong connection of the murder case with Brigadier Pratap. He then meets Pratap at his official residence. Pratap reveals that he was friends with Brigadier Shashank Chaudhary, Siddhant's father, for a long time. He further tells Siddhant not to spoil Brigadier Chaudhary's legacy. It is there when Siddhant becomes aware of his father's valor.

                    However, Siddhant's troubles increase when an important witness, Captain R. P. Singh mysteriously vanishes without a trace. Siddhant concludes that R. P. Singh is a prime witness as he was the one to arrest Javed, thus it was important that R. P. Singh be found. A few days later, Siddhant gets carjacked by a masked individual, who later reveals himself to be R. P. Singh. He informs Siddhant that it was actually Major Rathore who was the guilty one while Javed was actually innocent. On further coaxing, R. P. Singh reveals the actual sequence of events of that night of the operation.

                    According to R.P. Singh, during the operation, Major Rathore brutalized several villagers and charged them with supporting Pakistan and being terrorist sympathizers. He further tortured a young boy in falsely accepting the charge of hoarding weapons. The sadistic Rathore, still not satisfied, shot the boy in cold blood, terrifying the villagers and horrifying the soldiers. Javed, on witnessing the killing, tried to appease an enraged Rathore and even attempted to relieve him from command, who instead accused Javed of treason and tried to brutalize a young girl. A fed-up Javed promptly shot down Rathore, thus saving the girl and the villagers. Furthermore, R. P. Singh points out that despite a golden chance of escaping undetected and fully evading capture, Javed instead chose to surrender and accept his punishment.

                    Siddhant, satisfied with R. P. Singh's explanation, asks him to give his confession in the court, but to his great dismay, R. P. Singh refuses and instead runs into hiding, where he then kills himself. Thus with no credible witnesses available, Siddhant decides to take Brigadier Pratap to court. His decision shocks Akash and Kavya, both of whom caution Siddhant about the consequences of his actions.

                    Siddhant stands by his decision and on the day of the trial, Pratap makes an entry and heads towards the witness box. The trial begins poorly with Siddhant fumbling and Pratap getting the upper hand, and Akash objecting to Siddhant's questioning. A frustrated Siddhant decides to beat Pratap at his own game.

                    In the guise of a memory quiz, Siddhant reveals to everybody attending the trial that Brigadier Pratap's eight-year-old daughter and his wife were raped and murdered and his elderly mother burnt alive by their Muslim servant during a communal riot in 1993 and coaxes Pratap into revealing his involvement in the Rathore murder case.

                    Pratap justifies his actions in the name of nationalism and patriotism, but Siddhant calls out his bluff, thus exposing Pratap's lie and his bigotry. As Pratap attempts to leave, the panel of judges at the Army Court order an inquiry against him and charges are announced by Akash, while declaring Javed innocent, clearing him of all charges and restoring his rank and honours. As Pratap is taken into custody, a cleared Javed salutes Siddhant, who leaves the courtroom in relief.

                    Cast"""
    
    summary_template = """
    Given the information {information} about a movie, create:
    1. A short summary.
    2. Two interesting facts.
    """

    summary_prompt_template = PromptTemplate.from_template(summary_template)

    # # With Grok API
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0
    )


    # # With Local LLM with Ollama
    # llm = ChatOllama(
    #     model="qwen3:1.7b",
    #     temperature=0
    # )

    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information": information})
    print(response.content)


if __name__ == "__main__":
    main()
