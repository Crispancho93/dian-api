from lxml import etree

class TemplateXades:

    @classmethod
    def create_signature_template(
        cls,
        policy_url="https://facturaelectronica.dian.gov.co/politicadefirma/v1/politicadefirmav2.pdf",
        policy_digest="dMoMvtcG5aIzgYo0tIsSQeVJBDnUnfSOfBpxXrmor0Y="
    ):
        nsmap = {
            'ds': 'http://www.w3.org/2000/09/xmldsig#',
            'xades': 'http://uri.etsi.org/01903/v1.3.2#'
        }

        root = etree.Element("{http://www.w3.org/2000/09/xmldsig#}Signature", nsmap=nsmap, Id="xmldsig-d0322c4f-be87-495a-95d5-9244980495f4")

        signed_info = etree.SubElement(root, "{http://www.w3.org/2000/09/xmldsig#}SignedInfo")

        etree.SubElement(
            signed_info, 
            "{http://www.w3.org/2000/09/xmldsig#}CanonicalizationMethod", 
            Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315"
        )

        etree.SubElement(
            signed_info, 
            "{http://www.w3.org/2000/09/xmldsig#}SignatureMethod", 
            Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"
        )

        reference1 = etree.SubElement(
            signed_info, 
            "{http://www.w3.org/2000/09/xmldsig#}Reference", 
            Id="xmldsig-d0322c4f-be87-495a-95d5-9244980495f4-ref0", 
            URI=""
        )
        transforms = etree.SubElement(reference1, "{http://www.w3.org/2000/09/xmldsig#}Transforms")
        etree.SubElement(
            transforms, 
            "{http://www.w3.org/2000/09/xmldsig#}Transform", 
            Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"
        )
        etree.SubElement(
            reference1, 
            "{http://www.w3.org/2000/09/xmldsig#}DigestMethod", 
            Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"
        )
        etree.SubElement(reference1, "{http://www.w3.org/2000/09/xmldsig#}DigestValue")

        reference2 = etree.SubElement(
            signed_info, 
            "{http://www.w3.org/2000/09/xmldsig#}Reference", 
            URI="#xmldsig-d0322c4f-be87-495a-95d5-9244980495f4-keyinfo"
        )

        # transforms = etree.SubElement(reference2, "{http://www.w3.org/2000/09/xmldsig#}Transforms")
        # etree.SubElement(
        #     transforms, 
        #     "{http://www.w3.org/2000/09/xmldsig#}Transform", 
        #     Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315"
        # )
        
        etree.SubElement(
            reference2, 
            "{http://www.w3.org/2000/09/xmldsig#}DigestMethod", 
            Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"
        )
        etree.SubElement(reference2, "{http://www.w3.org/2000/09/xmldsig#}DigestValue")

        reference3 = etree.SubElement(
            signed_info, 
            "{http://www.w3.org/2000/09/xmldsig#}Reference", 
            Type="http://uri.etsi.org/01903#SignedProperties", 
            URI="#xmldsig-d0322c4f-be87-495a-95d5-9244980495f4-signedprops"
        )
        # transforms = etree.SubElement(reference3, "{http://www.w3.org/2000/09/xmldsig#}Transforms")
        # etree.SubElement(
        #     transforms, 
        #     "{http://www.w3.org/2000/09/xmldsig#}Transform", 
        #     Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315"
        # )
        etree.SubElement(
            reference3, 
            "{http://www.w3.org/2000/09/xmldsig#}DigestMethod", 
            Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"
        )
        etree.SubElement(reference3, "{http://www.w3.org/2000/09/xmldsig#}DigestValue")

        etree.SubElement(
            root, 
            "{http://www.w3.org/2000/09/xmldsig#}SignatureValue", 
            Id="xmldsig-d0322c4f-be87-495a-95d5-9244980495f4-sigvalue"
        )

        key_info = etree.SubElement(
            root, 
            "{http://www.w3.org/2000/09/xmldsig#}KeyInfo", 
            Id="xmldsig-d0322c4f-be87-495a-95d5-9244980495f4-keyinfo"
        )
        x509_data = etree.SubElement(key_info, "{http://www.w3.org/2000/09/xmldsig#}X509Data")
        etree.SubElement(x509_data, "{http://www.w3.org/2000/09/xmldsig#}X509Certificate")

        ds_object = etree.SubElement(root, "{http://www.w3.org/2000/09/xmldsig#}Object")
        qualifying_properties = etree.SubElement(
            ds_object, 
            "{http://uri.etsi.org/01903/v1.3.2#}QualifyingProperties", 
            Target="#xmldsig-d0322c4f-be87-495a-95d5-9244980495f4"
        )
        signed_properties = etree.SubElement(
            qualifying_properties, 
            "{http://uri.etsi.org/01903/v1.3.2#}SignedProperties", 
            Id="xmldsig-d0322c4f-be87-495a-95d5-9244980495f4-signedprops"
        )
        signed_signature_properties = etree.SubElement(
            signed_properties, 
            "{http://uri.etsi.org/01903/v1.3.2#}SignedSignatureProperties"
        )
        etree.SubElement(
            signed_signature_properties, 
            "{http://uri.etsi.org/01903/v1.3.2#}SigningTime"
        )

        signing_certificate = etree.SubElement(
            signed_signature_properties, 
            "{http://uri.etsi.org/01903/v1.3.2#}SigningCertificate"
        )
        
        for _ in range(3):
            cert = etree.SubElement(signing_certificate, "{http://uri.etsi.org/01903/v1.3.2#}Cert")
            cert_digest = etree.SubElement(cert, "{http://uri.etsi.org/01903/v1.3.2#}CertDigest")
            etree.SubElement(
                cert_digest, 
                "{http://www.w3.org/2000/09/xmldsig#}DigestMethod", 
                Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"
            )
            etree.SubElement(cert_digest, "{http://www.w3.org/2000/09/xmldsig#}DigestValue")

            issuer_serial = etree.SubElement(cert, "{http://uri.etsi.org/01903/v1.3.2#}IssuerSerial")
            etree.SubElement(issuer_serial, "{http://www.w3.org/2000/09/xmldsig#}X509IssuerName")
            etree.SubElement(issuer_serial, "{http://www.w3.org/2000/09/xmldsig#}X509SerialNumber")

        # Añadir SignaturePolicyIdentifier
        signature_policy_identifier = etree.SubElement(
            signed_signature_properties,
            "{http://uri.etsi.org/01903/v1.3.2#}SignaturePolicyIdentifier"
        )
        signature_policy_id = etree.SubElement(
            signature_policy_identifier,
            "{http://uri.etsi.org/01903/v1.3.2#}SignaturePolicyId"
        )
        sig_policy_id = etree.SubElement(
            signature_policy_id,
            "{http://uri.etsi.org/01903/v1.3.2#}SigPolicyId"
        )
        etree.SubElement(
            sig_policy_id,
            "{http://uri.etsi.org/01903/v1.3.2#}Identifier"
        ).text = policy_url

        sig_policy_hash = etree.SubElement(
            signature_policy_id,
            "{http://uri.etsi.org/01903/v1.3.2#}SigPolicyHash"
        )
        etree.SubElement(
            sig_policy_hash,
            "{http://www.w3.org/2000/09/xmldsig#}DigestMethod",
            Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"
        )
        etree.SubElement(
            sig_policy_hash,
            "{http://www.w3.org/2000/09/xmldsig#}DigestValue"
        ).text = policy_digest

        # Añadir SignerRole
        signer_role = etree.SubElement(
            signed_signature_properties,
            "{http://uri.etsi.org/01903/v1.3.2#}SignerRole"
        )
        claimed_roles = etree.SubElement(
            signer_role,
            "{http://uri.etsi.org/01903/v1.3.2#}ClaimedRoles"
        )
        etree.SubElement(
            claimed_roles,
            "{http://uri.etsi.org/01903/v1.3.2#}ClaimedRole"
        ).text = "supplier"

        return root