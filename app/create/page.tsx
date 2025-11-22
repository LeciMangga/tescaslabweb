"use client";
import { getAllTP, createTP } from "@/lib/api";
import React from "react";
import { useRouter } from "next/navigation";
export default function createPage(){
    const [judul, setjudul] = React.useState<string>();
    const [subjudul, setsubjudul] = React.useState<string>();
    const [kategori, setkategori] = React.useState<string>();
    const [tanggalpost, settanggalpost] = React.useState<Date>();
    const [deadline, setdeadline] = React.useState<Date>();
    const [deskripsi, setdeskripsi] = React.useState<string>();
    const router = useRouter();
    const createTPBaru = async() =>{
        await createTP(judul!,subjudul!,kategori!,tanggalpost!,deadline!,deskripsi!)
        router.push("/")
    }
    return (
        <div>
            <form onSubmit={createTPBaru}>
                <input
                        type="text"
                        placeholder="judul"
                        value={judul}
                        onChange={(e) => setjudul(e.target.value)}
                        />
                <input
                        type="text"
                        placeholder="subjudul"
                        value={subjudul}
                        onChange={(e) => setsubjudul(e.target.value)}
                        />
                <input
                        type="text"
                        placeholder="kategori"
                        value={kategori}
                        onChange={(e) => setkategori(e.target.value)}
                        />
                <input
                        type="text"
                        placeholder="deskripsi"
                        value={deskripsi}
                        onChange={(e) => setdeskripsi(e.target.value)}
                        />
                <button
                type="submit"           
                >
                Submit
                </button>
            </form>
        </div>
    )
}