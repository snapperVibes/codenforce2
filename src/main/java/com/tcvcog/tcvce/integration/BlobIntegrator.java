/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.tcvcog.tcvce.integration;

import com.tcvcog.tcvce.application.BackingBeanUtils;
import com.tcvcog.tcvce.domain.IntegrationException;
import com.tcvcog.tcvce.entities.Blob;
import com.tcvcog.tcvce.entities.BlobType;
import java.io.Serializable;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.time.ZoneId;

/**
 *
 * @author noah
 */
public class BlobIntegrator extends BackingBeanUtils implements Serializable{
    
    /**
     * 
     * @param blobID the blobID of the blob to be retrieved from db
     * @return the blob pulled from the db
     * @throws IntegrationException thrown instead of SCLException
     */
    public Blob getBlob(int blobID) throws IntegrationException{
        Blob blob = null;
        Connection con = getPostgresCon();
        ResultSet rs = null;
        String query = "SELECT photodocid, photodocdescription, photodocdate, photodoctype_typeid, \n" +
                        "       photodocblob\n" +
                        "       photodocuploadpersonid, photodocuploaddate \n" +
                        "  FROM public.photodoc WHERE photodocid = ?;";
        
        PreparedStatement stmt = null;
        
        try {
            
            stmt = con.prepareStatement(query);
            stmt.setInt(1, blobID);
            rs = stmt.executeQuery();
            while(rs.next()){
                blob = new Blob();
                System.out.println("BlobIntegrator.getBlob: | retrieving blobID "  + blobID);
                blob.setBlobID(rs.getInt("photodocid"));
                blob.setDescription(rs.getString("photodocdescription"));
                blob.setTimestamp(rs.getTimestamp("photodocdate").toLocalDateTime());
                blob.setType(BlobType.blobTypeFromInt(rs.getInt("photodoctype_typeid")));
                blob.setBytes(rs.getBytes("photodocblob"));
                blob.setUploadPersonID(rs.getInt("photodocuploadpersonid"));
            }
            
        } catch (SQLException ex) {
            //System.out.println(ex);
            throw new IntegrationException("Error retrieving blob. ", ex);
        } finally{
             if (stmt != null){ try { stmt.close(); } catch (SQLException ex) {/* ignored */ } }
             if (rs != null) { try { rs.close(); } catch (SQLException ex) { /* ignored */ } }
             if (con != null) { try { con.close(); } catch (SQLException e) { /* ignored */} }
        } // close finally
        
        return blob;
        
    }
    
    /**
     * stores this blob in the db with committed set to false
     * @param blob the blob to be stored
     * @return the blobID of the newly stored blob
     * @throws IntegrationException thrown in place of SQLException
     */
    public int storeBlob(Blob blob) throws IntegrationException{
        // do not call this directly.  Should call from BlobCoordinator to properly track upload time and person
        Connection con = getPostgresCon();
        String query =  " INSERT INTO public.photodoc(\n" +
                        "            photodocid, photodocdescription, photodocdate, photodoctype_typeid, photodocuploadpersonid, \n" +
                        "            photodocblob, photodoccommitted)\n" +
                        "    VALUES (DEFAULT, ?, ?, ?, \n" +
                        "            ?, ?);";
        
        PreparedStatement stmt = null;
        
        int lastID = 0;

        
        try {
            
            stmt = con.prepareStatement(query);
            stmt.setString(1, blob.getDescription());
            stmt.setTimestamp(2, java.sql.Timestamp.from(blob.getTimestamp()
                    .atZone(ZoneId.systemDefault()).toInstant()));
            stmt.setInt(3, blob.getType().getTypID());
            stmt.setInt(4, blob.getUploadPersonID());
            
            stmt.setBytes(5, blob.getBytes());
            stmt.setBoolean(6, false);
            
            System.out.println("BlobInegrator.storeBlob | Statement: " + stmt.toString());
            stmt.execute();
            
            String idNumQuery = "SELECT currval('photodoc_photodocid_seq');";
            Statement s = con.createStatement();
            ResultSet rs;
            rs = s.executeQuery(idNumQuery);
            rs.next();
            lastID = rs.getInt(1);
            blob.setBlobID(lastID);
            
        } catch (SQLException ex) {
            //System.out.println(ex);
            throw new IntegrationException("Error inserting blob. ", ex);
        } finally{
             if (stmt != null){ try { stmt.close(); } catch (SQLException ex) {/* ignored */ } }
             if (con != null) { try { con.close(); } catch (SQLException e) { /* ignored */} }
        } // close finally
        return lastID;
    }
    
    /**
     * removes this blob from the db, as well as any rows associated with this blob in linker tables.
     * @param blobID the blobID of the blob to be removed
     * @throws IntegrationException thrown instead of a SQLException
     */
    public void deleteBlob(int blobID) throws IntegrationException{
        // TODO: delete from linker tables as they are added
        
        //actionrequest linker table
        Connection con = getPostgresCon();
        String query = "DELETE" +
                        "  FROM public.ceactionrequestphotodoc WHERE photodoc_photodocid = ?;";
        
        PreparedStatement stmt = null;
        
        try {
            stmt = con.prepareStatement(query);
            stmt.setInt(1, blobID);
            stmt.executeQuery();
        } catch (SQLException ex) {
            //System.out.println(ex);
            throw new IntegrationException("Error deleting blob. ", ex);
        } finally{
             if (stmt != null){ try { stmt.close(); } catch (SQLException ex) {/* ignored */ } }
             if (con != null) { try { con.close(); } catch (SQLException e) { /* ignored */} }
        } // close finally
        
        //violation linker table
        query = "DELETE FROM public.codeviolationphotodoc WHERE photodoc_photodocid = ?";
        stmt = null;
        
        try {
            stmt = con.prepareStatement(query);
            stmt.setInt(1, blobID);
            stmt.executeQuery();
        } catch (SQLException ex) {
            //System.out.println(ex);
            throw new IntegrationException("Error deleting blob. ", ex);
        } finally{
             if (stmt != null){ try { stmt.close(); } catch (SQLException ex) {/* ignored */ } }
             if (con != null) { try { con.close(); } catch (SQLException e) { /* ignored */} }
        } // close finally
        
        //delete the main photodoc entry
        query = "DELETE FROM public.photodoc WHERE photodocid = ?;";
        
        stmt = null;
        
        try {
            stmt = con.prepareStatement(query);
            stmt.setInt(1, blobID);
            stmt.executeQuery();
        } catch (SQLException ex) {
            //System.out.println(ex);
            throw new IntegrationException("Error deleting blob. ", ex);
        } finally{
             if (stmt != null){ try { stmt.close(); } catch (SQLException ex) {/* ignored */ } }
             if (con != null) { try { con.close(); } catch (SQLException e) { /* ignored */} }
        } // close finally
    }
    
    public void commitBlob(int blobID) throws IntegrationException{
        Connection con = getPostgresCon();
        String query =  " UPDATE public.photodoc\n" +
                        " SET photodoccommitted = true\n" +
                        " WHERE photodocid = ?;";
        
        PreparedStatement stmt = null;
        
        try {
            stmt = con.prepareStatement(query);
            stmt.setInt(1, blobID);
            
            stmt.execute();
            
        } catch (SQLException ex) {
            //System.out.println(ex);
            throw new IntegrationException("Error commiting blob. ", ex);
        } finally{
             if (stmt != null){ try { stmt.close(); } catch (SQLException ex) {/* ignored */ } }
             if (con != null) { try { con.close(); } catch (SQLException e) { /* ignored */} }
        } // close finally
    }
    
    public void linkBlobToActionRequest(int blobID, int requestID) throws IntegrationException{
        Connection con = getPostgresCon();
        String query =  " INSERT INTO public.ceactionrequestphotodoc(\n" +
                        "            photodoc_photodocid, ceactionrequest_requestid)\n" +
                        "    VALUES (?, ?);";
        
        PreparedStatement stmt = null;
        
        try {
            
            stmt = con.prepareStatement(query);
            stmt.setInt(1, blobID);
            stmt.setInt(2, requestID);
            
            stmt.execute();
            System.out.println("BlobIntegrator.linkBlobToActionRequest | link succesful. ");
            
        } catch (SQLException ex) {
            //System.out.println(ex);
            throw new IntegrationException("Error linking blob to action request", ex);
        } finally{
             if (stmt != null){ try { stmt.close(); } catch (SQLException ex) {/* ignored */ } }
             if (con != null) { try { con.close(); } catch (SQLException e) { /* ignored */} }
        } // close finally
    }
    
    public void linkBlobToCodeViolation(int blobID, int cvID) throws IntegrationException{
        Connection con = getPostgresCon();
        String query =  " INSERT INTO public.codeviolationphotodoc(\n" +
                        "            photodoc_photodocid, codeviolation_violationid)\n" +
                        "    VALUES (?, ?);";
        
        PreparedStatement stmt = null;
        try {
            
            stmt = con.prepareStatement(query);
            stmt.setInt(1, blobID);
            stmt.setInt(2, cvID);
            stmt.execute();
            System.out.println("BlobIntegrator.linkBlobToCodeViolation | link succesfull. ");
            
        } catch (SQLException ex) {
            //System.out.println(ex);
            throw new IntegrationException("Error linking photo to actionrequest", ex);
        } finally{
             if (stmt != null){ try { stmt.close(); } catch (SQLException ex) {/* ignored */ } }
             if (con != null) { try { con.close(); } catch (SQLException e) { /* ignored */} }
        } // close finally
    }
    
}
