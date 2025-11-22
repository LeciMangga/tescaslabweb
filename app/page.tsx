"use client";
import { getAllTP, createTP } from "@/lib/api";
import React from "react";
import { useRouter } from "next/navigation";

export default function Home() {
  const [listTP, setlistTP]= React.useState<any[]>([]);
  
  const router = useRouter();
  const ambilAllTP = async () =>{
    const listtp = await getAllTP();
    setlistTP(listtp);
  }
  React.useEffect(()=>{
    ambilAllTP();
  });
  return (
    <div className="flex min-h-screen items-center justify-center bg-zinc-50 font-sans">
      <main className="flex min-h-screen w-full max-w-3xl flex-col items-center justify-between py-32 px-16 bg-white">
        <div className="width=[100px] bg-black" onClick={() =>router.push("/create")}>
          CreateTP
        </div>
        <div className="flex flex-row text-black width-[400px]">
          <div className="px-4">judul</div>
              <div className="px-4">subjudul</div>
              <div className="px-4">kategori</div>
              <div className="px-4">deskripsi</div>
              <div className="px-4">deadline</div>
        </div>
        {listTP.map((tp: any) => {
          return (
            <div className="flex flex-row text-black width-[400px]">
              <div className="px-4">{tp.judul}</div>
              <div className="px-4">{tp.subjudul}</div>
              <div className="px-4">{tp.kategori}</div>
              <div className="px-4">{tp.deskripsi}</div>
              <div className="px-4">{tp.deadline}</div>
              {/* <div>{tp.judul}</div> */}
            </div>
          )
        })}
      </main>
    </div>
  );
}
