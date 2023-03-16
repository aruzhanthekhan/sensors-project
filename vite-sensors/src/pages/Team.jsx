import '../App.css'
export function Team() {
    return (
        <div>
            <main>
                <h1 className="centered-header">Команда</h1>
                <div className='team-container'>
                    <div className='person-container'>
                        <img src="/person-1.jpg" className='team-member-picture'></img>
                        <p className='team-member-description'>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sollicitudin justo vel libero mollis semper. Donec varius justo id est ornare blandit. In interdum, felis eget hendrerit suscipit, justo dolor posuere est, et efficitur lacus lectus eget mauris. Phasellus elementum felis quis sem auctor, quis faucibus justo pellentesque.</p>
                    </div>
                    <div className='person-container'>
                        <img src="/person-2.jpg" className='team-member-picture'></img>
                        <p className='team-member-description'>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sollicitudin justo vel libero mollis semper. Donec varius justo id est ornare blandit. In interdum, felis eget hendrerit suscipit, justo dolor posuere est, et efficitur lacus lectus eget mauris. Phasellus elementum felis quis sem auctor, quis faucibus justo pellentesque.</p>
                    </div>
                    <div className='person-container'>
                        <img src="/person-3.jpg" className='team-member-picture'></img>
                        <p className='team-member-description'>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sollicitudin justo vel libero mollis semper. Donec varius justo id est ornare blandit. In interdum, felis eget hendrerit suscipit, justo dolor posuere est, et efficitur lacus lectus eget mauris. Phasellus elementum felis quis sem auctor, quis faucibus justo pellentesque.</p>
                    </div>
                </div>
            </main>
        </div>
    )
}