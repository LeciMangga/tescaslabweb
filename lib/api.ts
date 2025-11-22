
const be_url = "http://127.0.0.1:8000" 
export async function getAllTP(){
    const result = await fetch(`${be_url}/api/v1/tp/readalltp`, {
        method: "GET",
        headers: { "Content-Type": "application/json" },
    });
    // console.log(result.json());
    return result.json();
}

export async function createTP(judul: string, subjudul: string, kategori: string, tanggalpost: Date, deadline: Date, deskripsi: string){
    const result = await fetch(`${be_url}/api/v1/tp/createtp`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            judul: judul,
            subjudul: subjudul,
            kategori: kategori,
            tanggalpost: tanggalpost,
            deadline: deadline,
            deskripsi: deskripsi
        })
    });
    if (result.ok){
        return result.json();
    }
}