Set-Location -Path "c:\Users\Lyes\Documents\e-portfolio\pdf"
$ErrorActionPreference = "Continue"

function Move-Safe {
    param([string]$pattern, [string]$dest)
    if (Test-Path $dest) {
        $files = Get-ChildItem -Path . -Filter $pattern -File
        foreach ($f in $files) {
            Move-Item -Path $f.FullName -Destination $dest
            Write-Host "Moved $($f.Name) to $dest"
        }
    }
}

mkdir certifications, doc_technique, stages, officiels, e6, cours -Force | Out-Null

Move-Safe "*Certificate*.pdf" "certifications"
Move-Safe "Python Essentials 1.pdf" "certifications"
Move-Safe "pix_certification.pdf" "certifications"

Move-Safe "Documentation*.pdf" "doc_technique"
Move-Safe "Installation de Metasploitable*.pdf" "doc_technique"
Move-Safe "documentation instalation et utilisation Lynis *.pdf" "doc_technique"
Move-Safe "nouvelle doc.pdf" "doc_technique"
Move-Safe "pfsense.pdf" "doc_technique"
Move-Safe "proxmox instalation.pdf" "doc_technique"
Move-Safe "sauvegarde*.pdf" "doc_technique"

Move-Safe "Raportstage.pdf" "stages"
Move-Safe "rapport de stage 2eme annee.pdf" "stages"

Move-Safe "Lyes*.pdf" "officiels"
Move-Safe "Tableau*.pdf" "officiels"

Move-Safe "infra_reseau.pdf" "e6"
Move-Safe "situation_pro_*.pdf" "e6"

Move-Safe "introcyber.pdf" "cours"
Move-Safe "intropackettracer.pdf" "cours"
Move-Safe "notionsdebasesreseau.pdf" "cours"
