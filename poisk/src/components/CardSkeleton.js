import Skeleton from 'react-loading-skeleton'

const CardSkeleton = () => {
    return (
        <div className="card-skeleton">
            <Skeleton count={4} />
        </div>
    )
}

export default CardSkeleton
