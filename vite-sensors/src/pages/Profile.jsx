import '../App.css'

export function Profile(props) {

    const [profileData, setProfileData] = useState(null)
    useEffect(() => {
        fetch('http://localhost:5000/profile', {
            method: 'GET',
            headers: {
                Authorization: 'Bearer ' + props.token
            }
        })
            .then(data => {
                const res = data;
                res.access_token && props.setToken(res.access_token);
                setProfileData({
                    profile_name: res.name,
                    about_me: res.about
                });
            })
            .catch(err => console.log(err))
    }, []);


    return (
        <div className="centered-header">
            <h1>Личный кабинет</h1>
            {profileData && <div>
                <p>Profile name: {profileData.profile_name}</p>
                <p>About me: {profileData.about_me}</p>
            </div>}
        </div>
    )
}