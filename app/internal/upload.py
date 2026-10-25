from fastapi import APIRouter, UploadFile, File, HTTPException
import xml.etree.ElementTree as ET
router = APIRouter()

@router.post("/nfe_upload")
async def nfe_upload(file: UploadFile = File(...)):
    contents = await file.read()
    root = ET.fromstring(contents)
    
    get_nfe_data(root)
    return {
            "filename": file.filename,
            "root_tag": root.tag,
            "Root Attributes": root,
            "message": "XML file successfully parsed"
        }

def get_nfe_data(root):
        for el in root.findall('.//{*}det'):
            print(
                el.find('.//{*}prod').find('.//{*}cProd').text,
                el.find('.//{*}prod').find('.//{*}xProd').text,
                el.find('.//{*}prod').find('.//{*}qCom').text,
                "x",el.find('.//{*}prod').find('.//{*}vUnCom').text
            )
        for el in root.findall('.//{*}total'):
            print(el.find('.//{*}ICMSTot').find('.//{*}vProd').text)
        
        for el in root.findall('.//{*}emit'):
            print(el.find('.//{*}CNPJ').text,
                  el.find('.//{*}xNome').text)

        for el in root.findall('.//{*}dest'):
            print(el.find('.//{*}CNPJ').text,
                  el.find('.//{*}xNome').text)