<h2>ECSE Lab2</h2>
This lab is meant to get students more accustomed to the technologies used in designing and implementing a RESTful API server.
<h2> Requirements</h2>
<ul>
<li>Design a RESTful API that allows each IoT enabled water tank to interface with your server so that the measure values can be represented visually on a web page.</li>
<li>Your server should be able to perform the actions of a simple HTTP web server. The server should be able to perform actions on a resource such as Create, Read, Update and Delete. </li>
</ul>

</br>
<h1><strong>Required Attributes</strong></h3>
<h2><strong>Profile Routes</strong></h2>
<ul>
<li> <strong>GET/Profile</strong>
 </br>
 Your server should allow a user to create only one user profile. Since you are not meant to store data in a database, this can be done in a global variable in your script. The get request should only ever return a singular JSON object.

<strong>POST/Profile</strong>
</br>
Your server should allow for an incoming post request that accepts a JSON body as described above. The structure of the JSON request should match the example illustrated by the "Example Request" in _fig.2._ The server response should be structured as the the "Expected Response" in _fig.2._ The `last_updated` attribute should be generated by he server and can be formatted any way you choose (it MUST include both date and time), as long as it reflects the time at the time of the request. The `last_updated` attribute should not be sent to the server by the requester.

</li>

<li><strong>PATCH/Profile</strong>
</br>
Your server should allow a user to alter the parts of the profile after it has been posted. The server should allow the requester to make a JSON body with any combination of the three attributes and update them as necessary. An example request and expected result can be seen in *fig.3.* The `last_updated` attribute should be updated by the server to reflect the time that the profile was updated.

</li>
</ul>
<h3><strong>Data Routes</strong></h3>
<ul>
<li> <strong>GET/data</strong>
 </br>
 This route should return an array of 0 or more objects. A newly deployed server should return an empty array.  If a POST request was successfully made to the /data route previously, the GET route should return the posted object in the array.

<strong>POST/data</strong>
</br>
This route should accepts a JSON structured as depicted in _fig.5._ On success, the server should respond the the same JSON that was posted with the addition of an `id` attribute. This `id` is to be generated by the server. It should assign an ID of 1 for the first posted object, 2 for the second object and so on. If there are n objects in storage and the nth object is deleted, the next posted object should have an ID of n+1.

Eg. If there were 3 successful POSTs made to the server in a row, the most recent object should have an ID of 3. If the object of ID 3 is deleted and a new object is POSTed immediately after, the newly posted object should have an ID of 4.

</li>

<li><strong>PATCH/data/:id</strong>
</br>
Your server should allow a user to alter the parts of one of the tanks after it has been posted. The server should allow the requester to make a JSON body with any combination of the four attributes and update them as necessary (The requester should NOT be allowed to edit the `id` attribute).

</li>
<li><strong>DELETE/data/:id</strong>
</br>
Your server should allow the requester to delete any previously POSTed object.

</li>
</ul>
