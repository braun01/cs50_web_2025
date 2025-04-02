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
    const [incorrectCards, setIncorrectCards] = React.useState([]);

    // Defining React callbacks in this way helps React track the memory location of this function
    // in the event that the parent component needs to re-render for any reason
    const onCorrect = React.useCallback(() => {
        setCorrectCards([...correctCards, cards[currentCardIdx]]); // React does not like it when we mutate arrays, so we create and update a copy
        setCurrentCardIdx(currentCardIdx + 1);
    }, [correctCards, currentCardIdx]); // these are dependencies React will check for changes to determine what must be re-rendered

    const onIncorrect = React.useCallback(() => {
        setIncorrectCards([...incorrectCards, cards[currentCardIdx]]);
        setCurrentCardIdx(currentCardIdx + 1);
    }, [incorrectCards, currentCardIdx]);

    return (
        <div class="row">
            <div class="col-md">
                <div class="row">
                    <h3>Correct</h3>
                    <hr />
                    <div id="correct-div">
                        {/* This is an example of how to pass state as a prop from the parent Quizzlet to the child CardList */}
                        <CardList cards={correctCards} />
                    </div>
                </div>
                <div class="row">
                    <h3>Incorrect</h3>
                    <hr />
                    <div id="incorrect-div">
                        <CardList cards={incorrectCards} />
                    </div>
                </div>
            </div>
            <div class="col-md">
                <div id="card-start-div">
                    {/* onCorrect and onIncorrect are examples of callbacks defined in the parent Quizzlet that get passed to the child */}
                    {/* This pattern allows an event that is defined in the child to affect state in the parent. It is how a child can pass state back to a parent */}
                    <Prompter
                        cards={cards}
                        currentCardIdx={currentCardIdx}
                        onCorrect={onCorrect}
                        onIncorrect={onIncorrect}
                    />
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

function ShowMoreToggle({ checked, handleChecked }) {
    return (
        <div>
            <input
                type="checkbox"
                name="show-more"
                onChange={handleChecked}
                checked={checked}
            />
            <label for="show-more">Show More</label>
        </div>
    );
}

function CardList({ cards }) {
    const [showMore, setShowMore] = React.useState(false);

    const handleChecked = React.useCallback(() => {
        console.log('got checked');
        setShowMore(!showMore);
    }, [setShowMore, showMore]);

    const cardsToRender = cards.map((card) => (
        <Card question={card.question} answer={card.answer} />
    ));

    return (
        <div>
            {cards.length ? (
                <div>
                    <ShowMoreToggle
                        checked={showMore}
                        handleChecked={handleChecked}
                    />
                    {showMore ? (
                        <ul>{cardsToRender}</ul>
                    ) : (
                        <div>
                            <ul>
                                <Card
                                    question={cards[cards.length - 1].question}
                                    answer={cards[cards.length - 1].answer}
                                />
                            </ul>
                            {cards.length - 1 > 0 && (
                                <p>+ {cards.length - 1} more</p>
                            )}
                        </div>
                    )}
                </div>
            ) : (
                <p>No cards to show</p>
            )}
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
