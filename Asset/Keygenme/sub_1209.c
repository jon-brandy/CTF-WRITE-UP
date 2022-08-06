__int64 __fastcall sub_1209(const char *a1)
{
  size_t v1; // rax
  size_t v2; // rax
  int v4; // [rsp+18h] [rbp-C8h]
  int v5; // [rsp+18h] [rbp-C8h]
  int i; // [rsp+1Ch] [rbp-C4h]
  int j; // [rsp+20h] [rbp-C0h]
  int k; // [rsp+24h] [rbp-BCh]
  int m; // [rsp+28h] [rbp-B8h]
  char v10[18]; // [rsp+2Eh] [rbp-B2h] BYREF
  char v11[16]; // [rsp+40h] [rbp-A0h] BYREF
  char s[32]; // [rsp+50h] [rbp-90h] BYREF
  char v13[18]; // [rsp+70h] [rbp-70h] BYREF
  char v14; // [rsp+82h] [rbp-5Eh]
  char v15; // [rsp+89h] [rbp-57h]
  char v16; // [rsp+8Ah] [rbp-56h]
  char v17[72]; // [rsp+90h] [rbp-50h] BYREF
  unsigned __int64 v18; // [rsp+D8h] [rbp-8h]

  v18 = __readfsqword(0x28u);
  strcpy(s, "picoCTF{br1ng_y0ur_0wn_k3y_");
  strcpy(v10, "}");
  v1 = strlen(s);
  MD5(s, v1, &v10[2]);
  v2 = strlen(v10);
  MD5(v10, v2, v11);
  v4 = 0;
  for ( i = 0; i <= 15; ++i )
  {
    sprintf(&v13[v4], "%02x", (unsigned __int8)v10[i + 2]);
    v4 += 2;
  }
  v5 = 0;
  for ( j = 0; j <= 15; ++j )
  {
    sprintf(&v17[v5], "%02x", (unsigned __int8)v11[j]);
    v5 += 2;
  }
  for ( k = 0; k <= 26; ++k )
    v17[k + 32] = s[k];
  v17[59] = v14;
  v17[60] = v16;
  v17[61] = v15;
  v17[62] = v13[0];
  v17[63] = v16;
  v17[64] = v14;
  v17[65] = v13[12];
  v17[66] = v16;
  v17[67] = v10[0];
  if ( strlen(a1) != 36 )
    return 0LL;
  for ( m = 0; m <= 35; ++m )
  {
    if ( a1[m] != v17[m + 32] )
      return 0LL;
  }
  return 1LL;
}
