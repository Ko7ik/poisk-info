import Skeleton from 'react-loading-skeleton'

const CardSkeleton = ({ cards }) => {
    return Array(cards)
        .fill(0)
        .map((item, i) => (
            <div className="card-skeleton" key={i}>
                <Skeleton height={450} className="item-skeleton" />
            </div>
        ))
}

const ResultsSkeleton = ({ cards }) => {
    return Array(cards)
        .fill(0)
        .map((item, i) => (
            <div className="card-skeleton" key={i}>
                <Skeleton height={270} />
            </div>
        ))
}

export { CardSkeleton, ResultsSkeleton }
