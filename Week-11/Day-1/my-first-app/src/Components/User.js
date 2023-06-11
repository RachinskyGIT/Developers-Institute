const User = (props) => {
    // console.log(props);
    const {userinfo} = props;
    const {id, name, email, username, phone} = userinfo;
    return (
        <div>
            <img src={`https://robohash.org/${id}?size=150x150`} alt="logo" />
            <h2>Name: {userinfo.name}</h2>
            <p>Email: {userinfo.email}</p>
            <p>Phone: {userinfo.phone}</p>
            <hr></hr>
        </div>
    )
}

export default User