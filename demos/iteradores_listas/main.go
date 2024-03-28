package main

import (
	"fmt"
	TDALista "tdas/lista"
)

/*
*
Si en cualquier momento de este seguimiento se ponen a pensar como Alan en vez de Bárbara, recuerdenlo a él:


                    ..        .
                ..            ....
           ..                   ....
         ..
       ..
    .....
    ...             .
    ..         ..','''.           ....
       ....,;:::ccllll;..... .......''..
      ,oolddooollloooc,....'''''',,;;:;'..
      ,dddddoooooolllc,'..',;;:;,,,,;cc;;,'.
      ;xxddddollooooooolccc::ccllc::c;;;,:o;.
      ,dxxxoc;;;;;;;coxkxddddxxdddoc:;cdl:c;.
      .;:cc'..    ...';lddxxxxxkkxoc;',:llc:.
      .. .,'       .';::lddxxddxkocl;;cllooc.                .........
         .od:;,'''',:loooodddddxxl;:coolldxd:.               ............
        .lkdlllodxxdollcccllol::lc,,;:codkOkx:.        ......''''',,,,'.....
        ,kOxol::ldoc:,'',;ccc:;;;:cc:;cdxkkOOk:.     .,:cclllooooooooolc;'....
        cxdolc:;:c:;,'...',,;;;,;:lxdccoxxkkOOkc.   .cdxkkkkkkkkkkOOOOOxoc,.....
       ..'.. ..,clc:;;,.......',;::ldl:lddxxOOOkd:;;lxOO0OOkOOOOOO00KK0Oxo:'....
     ........,:cc:;;;,,...   ....';:ll;:ldddxkkkkkxoco0XKOxxxxxxxxkO0K0Oxoc;'...
    ......':;;:::'....'....      .';:;,,:loodddxxxxo:;kWNNK0OkxocccoxkOOkdol:;'..
     ........  ..... .............''...,:cllooolodddllONNNNNNNNXKOkxxkkkkxdolc;'.
       ....             ............ ..',;:clolcclllcdKXXXXNXXXXXNNNNXKK0Okxdlc;..
               .    ...    .  .....  ..'',;:clllcclclOXKKKXXXXXXXXNNNNNNNNXXKOko;.
                ....'...      ....   ...',;;:ccclollkKKKKKKKKXXXXXXXXNNNNNNNXXXX0x,
                .,:l;.        ..  .  ...''',;::;;;:xKKKKKKKKKXXXXXXXXXXNNNNNNXXNNNXd'
                 .','.       ..   .  ...''..',;,,;d0KKKKKKKKKXXXXXXXXXXXNNNNNNNNNNNNKx;.
                  'l:.    .;l;..     ...''....,;cx0KKKKKKXXXXXXXXXXXXXXXXXXNNNNNNNNNNNXOl'
                .o0XKkdoooxKKk;.    ..........,oO0KKKKXXXXKKKKKKKKXXXXXXXXXNXXXNNNNNNNNNNKd;.
               ;OXXXKKKKK000KKkc.    ......';lxO0KKKKKKKKKKKKKKKKKKKKXXXXXXXXKXXXNNNNNNNNNNNOl;.
              cKXXKK00000KKKKK0kl,...',;:cloxOO0000KKKKKKKXXXXXXXKKKKKKKXKXXXKKXXXXXXXNXNNNNNNXk,
             cKXKKKKKKKXXXXK000OkdlcccllodxxkO0000KKKKKKKKKKKXXXXXXXXKKK000KKKKKKKXXXXXXXNNNNNXXO:.
            :KXKKKXXXXXXXXKK000OOkdddxxkOO000000KKKK000KK00000OOOOkkkkOOOkkOOO000KKKXXXXXXXXXNNXXXx.
           'OXXXXXXXXXK00OO000OOOOOOOOO00000000KKKKKKKKKKKKKK000OOOkkkkkkkkkkkkOO000KKKKXXXXXXXNNNKl.
           :KXKXXKOkxxxxkO00KKKK000OOOO000KKKXKKKKKKKKKKXXXKKKKK0000OOOkxxkkxxxxxxkkO00KKKKXXXXXNX0Ox.
           :KK0kxddxkO0XXXKK0KKKK000000KKXXXXXKKKKKKKKKKKKKKKKKKKK00OkxxxxxxdoodooddxkOO00K0O0K0xxdO0d'
           ,O0kxkOKKKKK0000KKKKKXXXXXXXXXXXXXKKXXKKKKKKKKKKKK0000OkkkkOOOkddxocccloxxxxkOO0OddxclOkkOX0c.
           .xK0OOkkO0KKKKKXXXXXXKXXXXXXXXXKKKXXXXXXXKKXXKKKK000OOOOxoool:llccoc;::codllokOxldl:',oddOKNKc
            :00xdxOKKXXXKKKXXXXXXXXXXXXXXXXXXXXXXXXXOx0XXKKK000OOkkkxxdl:;,,';:,,;;:oc:lxc,ckOoldkOO00XNKl.
            .o0kOOKKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxlkKkx0KKKK0000Okxdoc;,'..''''';c::lo;.;:cd0KK00KXNNNKc.
             .oOkkOKXXXXXXXXXXXXXXKKKKXXXXXXXXXXXXXKc.;c,:OKKKKK0000OOkdoc,'...''',;;;clol:,:kKK0KKKKKXX0ocl,.
            . .oxldKXXXXXXXXXXXXXKKKKKKXXXXXXXXXXXXX0o,,xKKKKKK000Okkkxxdc:,....'',,,:lccloook0K0O00K0xc,.,od:.
               'dock00KKKOOKXXXXXXXXXXXXXXXXXXXXKKKKKXklkK000000Okkxxdddol:;'.....,,;cccldxkkkkOOOOdc'....:xOko,.
               .,ddxkkkddk0XXXXXXXXXXXKKKKKKKKKKKKKK0x:,lkOOOOkkxxxdoolc;,',,,.....';::coxkkkO00kl'.    .;oxkOKOd;.
                .;dxxc:xKXKKKKKKKKKKKKKKKKKKKKKK0000x, ..:xkkkxddddooodxxxxkkxo:,...';;:lodxkko;.       .,cldx0KKkc.
                 .;xkdkKKK000000KK00000000000000OOOkxc'.'coooodddxdddxkkxdolcc:::;,...,cllol;.        ....,;ldxOOdc,.
                  .,xkk0KK00OOOOOOOOkkkkkkkkkkOOOkkxddocccc:::::ccc::;;::codxxdol:,........       .......'';:odddolc;'.
                    ,xxxkxxxxxxxxxkkkxxxxxxxxxxxxxddddooollcccllllodxkkOOkxolllcllc;,..           ......''',,:lodxxxdl,.
                     ;xxodkOkkkxddooooddxxxkkOOOkxdollooooollllllloddolloddxkOOkxdolccc;.....     .......'''',;coodkkxo;.
                      .,;:ldkkxxdddxkOOOkxxxdolcccllc:;:::cc:c::;;;:ldxk0000kxxxddxkOkd;....''.....  ....',',;:cllcdkOkdc'.
                           ;xolodddolcc:'...;clooddl,.....,cooddxkOO000OkxxkkkO00000x:'.....;:;'..   .......':cloolodk0Oxl,.
                        .. .,'..',:lloxxc'''ckkkxxxc..'cc'..;oxxxxxxkkkkkO0KK000K0xl:;;,....,,cd:'..       ..,:lodddxdk0Oko;.
                        ... .:;cd::x0000x;,,:dOOOOk:.';odc,...,cddxxkO000OOO0KX0kxxxdddc,'.',,lOxlc,..     ..';:coxkxodk0Okd;.
                         .. .;::kd,:k000kc,,;oOOOOx:.';odoc'...,okO00OkxxkKXNKkdx00kdxdcc:,:::xKOddd:..     ..',:cldxdodkOOxl'.
*/

func Downsample(lista TDALista.Lista[any], k int) {
	i := 0
	for iter := lista.Iterador(); iter.HaySiguiente(); iter.Siguiente() {
		if i%k != 0 {
			iter.Borrar()
		}
		i++
	}
}

/*

func Downsample(lista *listaEnlazada[any], k int) {
	actual := lista.primero
	var anterior *nodoLista[any] = nil
	i := 0
	for actual != nil {
		if i%k != 0 {
			anterior.proximo = actual.proximo
			if actual == lista.ultimo {
				lista.ultimo = anterior
			}
			actual = actual.proximo
			lista.cantidad--
		} else {
			anterior = actual
			actual = actual.proximo
		}
		i++
	}
}
*/

func main() {
	lista := TDALista.CrearListaEnlazada[int]()
	lista.InsertarUltimo(18)
	lista.InsertarUltimo(12)
	lista.InsertarUltimo(22)
	lista.InsertarUltimo(3)

	iter := lista.Iterador()
	for iter.HaySiguiente() {
		valor := iter.VerActual()
		fmt.Println(valor)
		iter.Siguiente()
	}
}
