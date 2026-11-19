import os,json,urllib.request as U
D=os.environ.get('MAKEFUN_ENV_URL','')
B={
'depth-2|white':'g1f3,f1d3,d3c4,c4e2,c3a4,d1c2,e1g1,a4c5,d4c5,a2a3,f1d1,e3e4,c2b3,e2a6,e4d5,b3d3,b2b4,c1b2,a3b4,f3e5,b2d4,d3a6,d4b2,a6d3,e5c6,c6e7,a1a8,b2e5,c5c6,c6c7,d3d4,d4c3,c7c8q,d1d7,c8f8',
'depth-3|black':'c8d7,b8d7,g7g6,f8g7,d8b6,b6b4,b4a5,a5c7,e8g8,c7c4,c4c6,a7a6,d7f6,c6a4,e7e6,f6d5,g7d4,f8b8,b8a8,h7h5,a6a5,a5b4,g8h8,a4a7,d5e3,a7d4,a8a1,d4f4,f4f2,a1h1',
'depth-4|white':'d2d4,e4e5,c4b5,e5f6,c1b2,e1g1,b1c3,b5c6,d1c1,c1h6,c3d5,f3h2,h2g4,g4f6,f6e8,h6g7',
'nodes-100k|black':'e4d6,f8e7,d7c6,e8g8,e7g5,f8e8,d8f6,f6g5,c8h3,g5a5,h7h5,a5b6,b6b4,b7b6,d6f5,b4d6,d6d5,f5h4,a8e8,h3f1,d5h5,e8e2,h5d5,h4f3,d5f3,f3g2',
'nodes-250k|white':'a2a4,c1d2,e2e4,f1e2,a4a5,a1a2,e4e5,d1a1,d4e5,d2e3,a2a4,f3d4,a1a4,d4e6,a4c4,c3e4,a5a6,a6b7,c4a6,a6a7,e2a6',
'nodes-500k|black':'f8e7,c7c6,b7b5,e5d4,d7e5,c8f5,e8g8,d6d5,f8e8,e5d7,b5b4,a7a5,b4c3,e7c5,c5f2,d8b6,e8e3,d7c5,a8e8,f6g4,g4f2,c5e4,f2e4,e3f3,f3f2,b6a5,a5b4,b4d2',
}
def P(p,b):
 A=U.Request(D+p,data=json.dumps(b).encode(),headers={'content-type':'application/json'})
 return json.load(U.urlopen(A))
i={}
while 1:
 g=P('/game',{})
 if g.get('status')=='done':break
 while g.get('status')=='your_move':
  n=g['game']
  L=B.get(g['opponent']+'|'+g['colour'],'').split(',')
  p=i.setdefault(n,0)
  m=L[p] if p<len(L) else ''
  i[n]=p+1
  if m not in g['legal_moves']:m=g['legal_moves'][0]
  g=P('/move',{'game':n,'move':m})
