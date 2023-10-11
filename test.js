const assert = require('assert'); // Node.js'in dahili bir modülü olan assert kullanıyoruz.
const fetch = require('node-fetch').default;
 // HTTP istekleri yapmak için node-fetch modülünü kullanıyoruz.

// Test senaryosu için web sayfasının URL'sini belirtin.
const webPageURL = 'localhost:4000';

describe('Kullanıcı Ekleme ve Liste Testi', function () {
  it('Yeni bir kullanıcı ekler ve listeye eklenir', async function () {
    // Kullanıcı eklemek için bir POST isteği yapın.
    const response = await fetch(`${webPageURL}/add`, {
      method: 'POST',
      body: new URLSearchParams({
        name: 'TestUser',
        surname: 'TestSurname',
        email: 'testuser@example.com',
        password: 'testpassword',
      }),
    });

    // POST isteğinin başarılı bir şekilde tamamlandığını doğrulayın.
    assert.strictEqual(response.status, 200);

    // Kullanıcı listesini almak için bir GET isteği yapın.
    const userListResponse = await fetch(`${webPageURL}/all`);
    const userList = await userListResponse.json();

    // Kullanıcı listesinin alındığını ve en az bir kullanıcının listeye eklendiğini doğrulayın.
    assert.strictEqual(userListResponse.status, 200);
    assert(Array.isArray(userList));
    assert(userList.length > 0);

    // Eklenen kullanıcının listeye eklenip eklenmediğini kontrol edin.
    const addedUser = userList.find(user => user.name === 'TestUser' && user.surname === 'TestSurname');
    assert.ok(addedUser, 'Eklenen kullanıcı listeye eklenmedi.');
  });
});
