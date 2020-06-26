/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.tcvcog.tcvce.entities;

import java.io.Serializable;

/**
 * 
 * @author sylvia
 */
public class PublicInfoBundleCEActionRequest extends PublicInfoBundle implements Serializable {
    
    //************************************************
    //*******Action request case public data********
    //************************************************
    
    private CEActionRequest bundledRequest;
    private PublicInfoBundlePerson requestor;
    private PublicInfoBundleProperty requestProperty;
    

    public void setBundledRequest(CEActionRequest input) {
        
        setMuni(input.getMuni());
        setPacc(input.getRequestPublicCC());
        setAddressAssociated(!input.getNotAtAddress());
        if (input.getNotAtAddress() || 
                    input.getRequestProperty() == null || 
                    input.getRequestProperty().isNonAddressable()) {
                setAddressAssociated(false);
            } else {
                setAddressAssociated(true);
                setPropertyAddress(input.getRequestProperty().getAddress());
            }
        
        input.setRequestor(new Person());
        
        input.setRequestProperty(new Property());
        input.setMuniCode(0);
        input.setCaseAttachmentUser(new User());
        input.setCogInternalNotes("*****");
        input.setMuniNotes("*****");
        
        bundledRequest = input;
    }

    public CEActionRequest getBundledRequest() {
        return bundledRequest;
    }
    
    @Override
    public String toString() {
        return this.getClass().getName() + bundledRequest.getRequestID();
    }

    public PublicInfoBundlePerson getRequestor() {
        return requestor;
    }

    public void setRequestor(PublicInfoBundlePerson requestor) {
        this.requestor = requestor;
    }

    public PublicInfoBundleProperty getRequestProperty() {
        return requestProperty;
    }

    public void setRequestProperty(PublicInfoBundleProperty requestProperty) {
        this.requestProperty = requestProperty;
    }
    
}
