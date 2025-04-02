function Quizzlet() {
    const cards = [
        {
            id: 0,
            question: 'What day is it?',
            answer: 'Today',
        },
        {
            id: 1,
            question: 'Is Millie a dog?',
            answer: 'Yup',
        },
        {
            id: 2,
            question: 'What color do red and yellow make?',
            answer: 'Orange',
        },
        {
            id: 3,
            question: 'If a tree falls in the woods, etc etc.?',
            answer: "Who's to say",
        },
        {
            id: 4,
            question: 'Are blueberries really blue?',
            answer: 'No',
        },
    ];

    // parent component that will track all of our state
    // here we split up our state so we can make updates independently, which gives React more flexibility to determine re-renders
    const [currentCardIdx, setCurrentCardIdx] = React.useState(0);
    const [correctCards, setCorrectCards] = React.useState([]);

    // Defining React callbacks in this way helps React track the memory location of this function
    // in the event that the parent component needs to re-render for any reason
    const onCorrect = React.useCallback(() => {
        setCorrectCards([...correctCards, cards[currentCardIdx]]); // React does not like it when we mutate arrays, so we create and update a copy
        setCurrentCardIdx(currentCardIdx + 1);
    }, [correctCards, currentCardIdx]); // these are dependencies React will check for changes to determine what must be re-rendered

    // TODO #1: define this callback (hint: you may need to define more state!)
    const onIncorrect = React.useCallback(() => {}, []);

    return (
        <div class="row">
            <div class="col-md">
                <div class="row">
                    <h3>Correct</h3>
                    <hr />
                    <div id="correct-div">
                        {/* TODO #3: Render a CardList with the correct cards*/}
                        {/* Hint: try rendering a single Card first */}
                    </div>
                </div>
                <div class="row">
                    <h3>Incorrect</h3>
                    <hr />
                    <div id="incorrect-div">
                        {/* TODO #4: Render a CardList with the incorrect cards*/}
                    </div>
                </div>
            </div>
            <div class="col-md">
                <div id="card-start-div">
                    {/* TODO #2: render a Prompter here, passing the appropriate props */}
                    {/* This pattern allows an event that is defined in the child to affect state in the parent. It is how a child can pass state back to a parent */}
                </div>
            </div>
        </div>
    );
}

function Card({ question, answer }) {
    const handleCardClick = React.useCallback((event) => {
        // currentTarget gets us the element to which the event is bound
        event.currentTarget.classList.add('card-flip');
        event.currentTarget.onanimationend = function () {
            // "this" is still the card div
            this.classList.remove('card-flip');
        };
    });

    return (
        <div onClick={handleCardClick} class="card-ab">
            <div class="front">{question}</div>
            <div class="back">{answer}</div>
        </div>
    );
}

function ShowMoreToggle() {
    // TODO #5: implement this checkbox toggle. You'll want an initial value for the input, and a function to handle
    // a value change
}

function CardList({ cards }) {
    // TODO #6: implement "show more" functionality

    const cardsToRender = cards.map((card) => (
        <Card question={card.question} answer={card.answer} />
    ));

    return (
        <div>
            {cards.length ? <ul>{cardsToRender}</ul> : <p>No cards to show</p>}
        </div>
    );
}

function Prompter({ cards, currentCardIdx, onCorrect, onIncorrect }) {
    return (
        <div>
            {!cards ? (
                <p>No cards to test</p>
            ) : currentCardIdx < 0 || currentCardIdx >= cards.length ? (
                <p>
                    Unable to render card #{currentCardIdx + 1} or no more cards
                    to render
                </p>
            ) : (
                <div>
                    Viewing card {currentCardIdx + 1} of {cards.length}
                    <Card
                        question={cards[currentCardIdx].question}
                        answer={cards[currentCardIdx].answer}
                    />
                    <button class="btn btn-success" onClick={onCorrect}>
                        Correct
                    </button>
                    <button class="btn btn-danger" onClick={onIncorrect}>
                        Incorrect
                    </button>
                </div>
            )}
        </div>
    );
}

if (document.readyState !== 'loading') {
    ReactDOM.render(<Quizzlet />, document.querySelector('.container'));
} else {
    document.addEventListener('DOMContentLoaded', () => {
        ReactDOM.render(<Quizzlet />, document.querySelector('.container'));
    });
}
