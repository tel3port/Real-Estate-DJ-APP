// existence not justified
function setPageTitle(){
    heading_list = [
        'My wife told me to stop impersonating a flamingo. I had to put my foot down. ',
        'I went to buy some camo pants but couldn’t find any.',
        'I failed math so many times at school, I can’t even count.',
        'I used to have a handle on life, but then it broke.',
        'I was wondering why the frisbee kept getting bigger and bigger, but then it hit me.',
        'I heard there were a bunch of break-ins over at the car park. That is wrong on so many levels.',
        'I want to die peacefully in my sleep, like my grandfather… Not screaming and yelling like the passengers in his car.',
        'When life gives you melons, you might be dyslexic.',
        'Don’t you hate it when someone answers their own questions? I do.',
        'It takes a lot of balls to golf the way I do.',
        'I told him to be himself; that was pretty mean, I guess. ',
        'I know they say that money talks, but all mine says is ‘Goodbye.’',
        'My father has schizophrenia, but he’s good people.',
        'The problem with kleptomaniacs is that they always take things literally.',
        'I can’t believe I got fired from the calendar factory. All I did was take a day off.',
        'Most people are shocked when they find out how bad I am as an electrician.',
        'Never trust atoms; they make up everything.',
        'My wife just found out I replaced our bed with a trampoline. She hit the ceiling! ',
        'I was addicted to the hokey pokey, but then I turned myself around.',
        'I used to think I was indecisive. But now I’m not so sure.',
        'I just got kicked out of a secret cooking society. I spilled the beans.',
        'What’s a frog’s favorite type of shoes? Open toad sandals.',
        'Blunt pencils are really pointless.',
        '6:30 is the best time on a clock, hands down.',
        'Two wifi engineers got married. The reception was fantastic.',
        'Just got fired from my job as a set designer. I left without making a scene.',
        'What’s the difference between ignorance and apathy? I don’t know and I don’t care.',
        'One of the cows didn’t produce milk today. It was an udder failure.',
        'Adam & Eve were the first ones to ignore the Apple terms and conditions.',
        'Refusing to go to the gym is a form of resistance training.',
        'If attacked by a mob of clowns, go for the juggler.',
        'The man who invented Velcro has died. RIP.',
        'Despite the high cost of living, it remains popular.',
        'A dung beetle walks into a bar and asks, ‘Is this stool taken?’',
        'I can tell when people are being judgmental just by looking at them.',
        'The rotation of Earth really makes my day.',
        'Well, to be Frank with you, I’d have to change my name.',
        'My friend was explaining electricity to me, but I was like, ‘Watt?’',
        'What if there were no hypothetical questions?',

        ]
        random_title = heading_list[Math.floor(Math.random()*heading_list.length)]
        document.title = random_title;

        console.log(document.getElementById('anchor_heading'))
}
setPageTitle()
