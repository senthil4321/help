# canoe
## capl
``` c
message * m;
int i, mx;
mx=elcount(aNet::aNode.Tx);
for (i = 0; i < mx; ++i)
{
 m.id=aNet::aNode.TX[i];
 write(DBLookup(m).Name);
}
```

https://kb.vector.com/upload_551/file/SN-IND-1-011_InteractionLayer(1).pdf
file:///hb_capl_programming.pdf

Signal level manupulation
on signal ( LightSwitch::OnOff | MotorSwitch::OnOff )
{
  putValue (yourEnvironmentVariable, this);      // Maybe phys, if applies
}
https://stackoverflow.com/questions/45417876/how-to-set-env-variable-in-capl-code-from-an-incoming-signal
https://stackoverflow.com/questions/36447154/how-to-access-can-signals-dynamically-by-string-in-capl?rq=1


Environment variables are data objects global to the CANoe environment, and are used to link the functions of a
CANoe panel to CAPL programs.
putValue
getValue
On envVar XXX
{

}

Canoe Pannel creation and sending value
https://kb.vector.com/upload_551/file/SN-IND-1-004_CANalyzer_Panel_with_SendFunctionality(1).pdf

IL Layer
https://stackoverflow.com/questions/48710863/disable-messages-and-nodes
https://kb.vector.com/upload_551/file/SN-IND-1-011_InteractionLayer.pdf --- Defines the procedure to enable continuous data sending
https://assets.vector.com/cms/content/know-how/_application-notes/AN-IND-1-011_Using_CANoe_NET_API.pdf
https://kb.vector.com/upload_551/file/SN-IND-1-011_InteractionLayer(1).pdf
https://stackoverflow.com/questions/40024879/continuous-signal-transmission-in-vector-canoe
GenMsgILSupport
GenMsgSendType
GenMsgSendType
GenSigSendType
ILUsed
NodeLayerModules


https://kb.vector.com/upload_551/file/SN-IND-1-021_GraphicalDefinitions_ExpectedCurves(1).pdf
### rs232
* https://www.fatalerrors.org/a/rs232-capl-functions-serial-port-configuration.html
### IL
* https://stackoverflow.com/questions/36447154/how-to-access-can-signals-dynamically-by-string-in-capl
### isotp
* https://stackoverflow.com/questions/35626632/transmitting-data-over-iso-tp-transport-protocol-in-canoe-using-capl
### value table
* https://kb.vector.com/entry/1443/
### diag request from canoe
* https://kb.vector.com/entry/982/

## canoe shortcut
### capl editor
F9 to compile capl code
### canoe
F9 to start the canoe 
Esc to stop the canoe
---
---
# can
## uds
### Ref.
* https://automotive.wiki/index.php/ISO_14229
* https://automotive.softing.com/fileadmin/sof-files/pdf/de/ae/poster/UDS_Faltposter_softing2016.pdf
