rule PE_7d700715fcbd: Suspicious_PE_Detection
{
    meta:
        Author = "Atharva Shinde, Kavish Shah"
        Incident = "VIRUSTOTAL_ANALYSIS"
        Date = "2025-04-04"
        Last_Modified = "2025-04-04_UTC"
        Description = "Detects suspicious PE file compiled with Microsoft Visual C++"
        SHA256 = "7d700715fcbd853f2cfaf555840e61a7c88238b61657bf72f11ff27dc9e93246"
        Compiler = "Microsoft Visual C++ (19.36.34436)"
        Linker = "Microsoft Linker (14.36.34436)"
        Tool = "Visual Studio 2022 Version 17.6"

    strings:
        $s1 = "Microsoft Visual C++"
        $s2 = "PE32+ executable" nocase
        $s3 = "Visual Studio 2022" nocase
        $s4 = { 4D 5A }  // MZ Header (indicates a PE file)
        $s5 = { 50 45 00 00 } // PE Header
        $s6 = "Rich" // Rich header, often found in Microsoft-compiled files

    condition:
        uint16(0) == 0x5A4D and // MZ signature
        uint32(0x3C) == 0x00004550 and // PE signature
        filesize > 7MB and
        all of them
}
