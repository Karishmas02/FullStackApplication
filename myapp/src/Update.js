import React, { useState } from 'react';
import axios from 'axios';

const Update = () => {
    const [id, setId] = useState("");
    const [Fname, setFirstname] = useState("");
    const [Lname, setLastname] = useState("");
    const [Email, setEmail] = useState("");
    const [Phone, setPhone] = useState("");
    const [Password, setPassword] = useState("");
    const [message, setMessage] = useState("");

    const handlesubmit = (e) => {
        e.preventDefault();

        axios.put("http://localhost:8000/put/", {
            id, Fname, Lname, Email, Phone, Password
        })
        .then((res) => setMessage(res.data.message))
        .catch((err) => setMessage("Update Failed"));
    };

    return (
        <div>
            <h2>Update User</h2>
            <form onSubmit={handlesubmit}>

                <label>User ID:</label>
                <input value={id} onChange={(e)=>setId(e.target.value)} /><br/>

                <label>Firstname:</label>
                <input value={Fname} onChange={(e)=>setFirstname(e.target.value)} /><br/>

                <label>Lastname:</label>
                <input value={Lname} onChange={(e)=>setLastname(e.target.value)} /><br/>

                <label>Email:</label>
                <input value={Email} onChange={(e)=>setEmail(e.target.value)} /><br/>

                <label>Phone:</label>
                <input value={Phone} onChange={(e)=>setPhone(e.target.value)} /><br/>

                <label>Password:</label>
                <input value={Password} onChange={(e)=>setPassword(e.target.value)} /><br/>

                <button>Update</button>
            </form>

            <p>{message}</p>
        </div>
    );
};

export default Update;
