/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.tcvcog.tcvce.entities.search;

import com.tcvcog.tcvce.entities.EntityUtils;
import com.tcvcog.tcvce.entities.Municipality;
import com.tcvcog.tcvce.entities.RoleType;
import com.tcvcog.tcvce.entities.User;
import java.io.Serializable;
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.util.ArrayList;
import java.util.List;

/**
 * Encapsulates municipality restrictions and start/end
 * dates for searching. Types for all three commonly used date
 * formats system wide are included in the params object
 * and the conversions are made automatically based on the
 * LocalDateTime value, allowing objects on the front end and 
 * integration end to just grab the date Type they need and go!
 * @author Sylvia, no wait, Lauren
 */

public  class           SearchParams 
        implements      Serializable{

    
    private String searchName;
    private String searchDescription;
    
    private RoleType muni_rtMin;
    private boolean muni_ctl;
    private Municipality muni_val;
    protected List<Municipality> muniList_val;
    
    private RoleType date_rtMin;
    private boolean date_startEnd_ctl;
   private boolean date_null_ctl;
    private LocalDateTime date_start_val;
    private LocalDateTime date_end_val;

    private boolean date_relativeDates_ctl;
    private int date_relativeDates_start_val;
    private int date_realtiveDates_end_val;
    
   private boolean user_ctl;
   // subclasses must have a user_field enum member to make these work
   private User user_val;
    
    
    private boolean applyDateSearchToDateOfRecord;
    private boolean useEntryTimestamp;
    
    private RoleType bobID_rtMin;
    private boolean bobID_ctl;
    private int bobID_val;
    
    private RoleType limitResultCount_rtMin;
    private boolean limitResultCount_ctl;
    private int limitResultCount_val;
    
    private boolean active_ctl;
    private boolean active_val;
    
   public SearchParams(){
       muniList_val = new ArrayList<>();
       
   }
   
   
    @Override
   public String toString(){
       StringBuilder sb = new StringBuilder();
       sb.append("Muni: ");
       sb.append(muni_val.getMuniName());
       return sb.toString();
   }
   
    /**
     * @return the date_null_ctl
     */
    public boolean isDate_null_ctl() {
        return date_null_ctl;
    }

    /**
     * @param date_null_ctl the date_null_ctl to set
     */
    public void setDate_null_ctl(boolean date_null_ctl) {
        this.date_null_ctl = date_null_ctl;
    }

    /**
     * @return the muni_rtMin
     */
    public RoleType getMuni_rtMin() {
        return muni_rtMin;
    }

    /**
     * @param muni_rtMin the muni_rtMin to set
     */
    public void setMuni_rtMin(RoleType muni_rtMin) {
        this.muni_rtMin = muni_rtMin;
    }
   
   
    /**
     * Adds a given municipality to the Query's internal list of Municipalities
     * to query
     * @param muni a muni_val to search using the Query Object's parameter list
     * @return the size of the list after the inputed Muni is added
     */
    public int addMuni(Municipality muni){
        muniList_val.add(muni);
        return muniList_val.size();
        
    }
    
    /**
     * Utility method for calling clear() on the internal munilist
     */
    public void clearMuniList(){
        muniList_val.clear();
    }
    
    /**
     * Retrieves the internal list of Municipality objects held by this Query subclass
     * @return a reference to the internal muniList_val
     */
    public List<Municipality> getMuniList_val(){
        return muniList_val;
    }
  
    
    
    /**
     * @return the muni_val
     */
    public Municipality getMuni_val() {
        return muni_val;
    }

    /**
     * @param muni_val the muni_val to set
     */
    public void setMuni_val(Municipality muni_val) {
        this.muni_val = muni_val;
    }

    /**
     * @return the startDate_val_utilDate
     */
    public java.util.Date getStartDate_val_utilDate() {
        if(date_start_val != null){
            return java.util.Date.from(getDate_start_val().atZone(ZoneId.systemDefault()).toInstant());
        }
        return null;
    }

    /**
     * @param startDate_val_utilDate the startDate_val_utilDate to set
     */
    public void setStartDate_val_utilDate(java.util.Date startDate_val_utilDate) {
        if(startDate_val_utilDate != null){
            date_start_val = startDate_val_utilDate.toInstant().atZone(ZoneId.systemDefault()).toLocalDateTime();
        }
    }

    /**
     * @return the endDate_val_utilDate
     */
    public java.util.Date getEndDate_val_utilDate() {
        if(date_end_val != null){
            return java.util.Date.from(getDate_end_val().atZone(ZoneId.systemDefault()).toInstant());
        }
        return null;
    }

    /**
     * @param endDate_val_utilDate the endDate_val_utilDate to set
     */
    public void setEndDate_val_utilDate(java.util.Date endDate_val_utilDate) {
        if(endDate_val_utilDate != null){
            date_end_val = endDate_val_utilDate.toInstant().atZone(ZoneId.systemDefault()).toLocalDateTime();
        }
    }

    /**
     * @return the date_start_val
     */
    public LocalDateTime getDate_start_val() {
        return date_start_val;
    }

    /**
     * @return the date_end_val
     */
    public LocalDateTime getDate_end_val() {
        return date_end_val;
    }

    /**
     * @param date_start_val the date_start_val to set
     */
    public void setDate_start_val(LocalDateTime date_start_val) {
        this.date_start_val = date_start_val;
    }

    /**
     * @param date_end_val the date_end_val to set
     */
    public void setDate_end_val(LocalDateTime date_end_val) {
        this.date_end_val = date_end_val;
    }

    /**
     * @return the startDate_val_SQLDate
     */
    public java.sql.Timestamp getStartDate_val_SQLDate() {
        if(date_relativeDates_ctl){
            return java.sql.Timestamp.valueOf(LocalDateTime.now().plusDays(date_relativeDates_start_val));
        } else {
            if(date_start_val != null){
                return java.sql.Timestamp.valueOf(getDate_start_val());
            }
        }
        return null;
    }

    /**
     * @return the endDate_val_SQLDate
     */
    public java.sql.Timestamp getEndDate_val_SQLDate() {
        if(date_relativeDates_ctl){
            return java.sql.Timestamp.valueOf(LocalDateTime.now().plusDays(date_realtiveDates_end_val));
        } else {
            if(date_end_val != null){
                return java.sql.Timestamp.valueOf(getDate_end_val());
            }
        }
        return null;
    }

    /**
     * @return the date_startEnd_ctl
     */
    public boolean isDate_startEnd_ctl() {
        return date_startEnd_ctl;
    }

    /**
     * @param date_startEnd_ctl the date_startEnd_ctl to set
     */
    public void setDate_startEnd_ctl(boolean date_startEnd_ctl) {
        this.date_startEnd_ctl = date_startEnd_ctl;
    }

    /**
     * @return the limitResultCount_ctl
     */
    public boolean isLimitResultCount_ctl() {
        return limitResultCount_ctl;
    }

    /**
     * @param limitResultCount_ctl the limitResultCount_ctl to set
     */
    public void setLimitResultCount_ctl(boolean limitResultCount_ctl) {
        this.limitResultCount_ctl = limitResultCount_ctl;
    }

    /**
     * @return the bobID_val
     */
    public int getBobID_val() {
        return bobID_val;
    }

    /**
     * @param bobID_val the bobID_val to set
     */
    public void setBobID_val(int bobID_val) {
        this.bobID_val = bobID_val;
    }

    /**
     * @return the filterByObjectID
     */
    public boolean isBobID_ctl() {
        return bobID_ctl;
    }

    /**
     * @param bobID_ctl the filterByObjectID to set
     */
    public void setBobID_ctl(boolean bobID_ctl) {
        this.bobID_ctl = bobID_ctl;
    }

    /**
     * @return the searchName
     */
    public String getSearchName() {
        return searchName;
    }

    /**
     * @param searchName the searchName to set
     */
    public void setSearchName(String searchName) {
        this.searchName = searchName;
    }

    /**
     * @return the searchDescription
     */
    public String getSearchDescription() {
        return searchDescription;
    }

    /**
     * @param searchDescription the searchDescription to set
     */
    public void setSearchDescription(String searchDescription) {
        this.searchDescription = searchDescription;
    }

    /**
     * @return the muni_ctl
     */
    public boolean isMuni_ctl() {
        return muni_ctl;
    }

    /**
     * @param muni_ctl the muni_ctl to set
     */
    public void setMuni_ctl(boolean muni_ctl) {
        this.muni_ctl = muni_ctl;
    }

    /**
     * @return the date_relativeDates_ctl
     */
    public boolean isDate_relativeDates_ctl() {
        return date_relativeDates_ctl;
    }

    /**
     * @return the date_relativeDates_start_val
     */
    public int getDate_relativeDates_start_val() {
        return date_relativeDates_start_val;
    }

    /**
     * @return the date_realtiveDates_end_val
     */
    public int getDate_realtiveDates_end_val() {
        return date_realtiveDates_end_val;
    }

    /**
     * @param date_relativeDates_ctl the date_relativeDates_ctl to set
     */
    public void setDate_relativeDates_ctl(boolean date_relativeDates_ctl) {
        this.date_relativeDates_ctl = date_relativeDates_ctl;
    }

    /**
     * @param date_relativeDates_start_val the date_relativeDates_start_val to set
     */
    public void setDate_relativeDates_start_val(int date_relativeDates_start_val) {
        this.date_relativeDates_start_val = date_relativeDates_start_val;
    }

    /**
     * @param date_realtiveDates_end_val the date_realtiveDates_end_val to set
     */
    public void setDate_realtiveDates_end_val(int date_realtiveDates_end_val) {
        this.date_realtiveDates_end_val = date_realtiveDates_end_val;
    }

    /**
     * @return the useEntryTimestamp
     */
    public boolean isUseEntryTimestamp() {
        return useEntryTimestamp;
    }

    /**
     * @param useEntryTimestamp the useEntryTimestamp to set
     */
    public void setUseEntryTimestamp(boolean useEntryTimestamp) {
        this.useEntryTimestamp = useEntryTimestamp;
    }

    /**
     * @return the applyDateSearchToDateOfRecord
     */
    public boolean isApplyDateSearchToDateOfRecord() {
        return applyDateSearchToDateOfRecord;
    }

    /**
     * @param applyDateSearchToDateOfRecord the applyDateSearchToDateOfRecord to set
     */
    public void setApplyDateSearchToDateOfRecord(boolean applyDateSearchToDateOfRecord) {
        this.applyDateSearchToDateOfRecord = applyDateSearchToDateOfRecord;
    }

    /**
     * Used for printing search params on reports: since the correct SQL timestamp
     * is the relevant field that we draw from for building the actual SQL query
     * and those getters take into account relative date preferences, we need
     * to first convert the SQL-compatible date back to LocalDateTime and then
     * make it pretty for printing
     * @return the startDatePretty
     */
    public String getStartDatePretty() {
        if(date_start_val != null){
            return EntityUtils.getPrettyDate(date_start_val);
        }
        return null;
    }

    /**
     * @return the endDatePretty
     */
    public String getEndDatePretty() {
        if(date_end_val != null){
            return EntityUtils.getPrettyDate(date_end_val);
        }
        return null;
    }

    /**
     * @return the active_ctl
     */
    public boolean isActive_ctl() {
        return active_ctl;
    }

    /**
     * @return the active_val
     */
    public boolean isActive_val() {
        return active_val;
    }

    /**
     * @param active_ctl the active_ctl to set
     */
    public void setActive_ctl(boolean active_ctl) {
        this.active_ctl = active_ctl;
    }

    /**
     * @param active_val the active_val to set
     */
    public void setActive_val(boolean active_val) {
        this.active_val = active_val;
    }

    /**
     * @return the date_rtMin
     */
    public RoleType getDate_rtMin() {
        return date_rtMin;
    }

    /**
     * @param date_rtMin the date_rtMin to set
     */
    public void setDate_rtMin(RoleType date_rtMin) {
        this.date_rtMin = date_rtMin;
    }

    /**
     * @return the bobID_rtMin
     */
    public RoleType getBobID_rtMin() {
        return bobID_rtMin;
    }

    /**
     * @param bobID_rtMin the bobID_rtMin to set
     */
    public void setBobID_rtMin(RoleType bobID_rtMin) {
        this.bobID_rtMin = bobID_rtMin;
    }

    /**
     * @return the limitResultCount_val
     */
    public int getLimitResultCount_val() {
        return limitResultCount_val;
    }

    /**
     * @param limitResultCount_val the limitResultCount_val to set
     */
    public void setLimitResultCount_val(int limitResultCount_val) {
        this.limitResultCount_val = limitResultCount_val;
    }

    /**
     * @return the limitResultCount_rtMin
     */
    public RoleType getLimitResultCount_rtMin() {
        return limitResultCount_rtMin;
    }

    /**
     * @param limitResultCount_rtMin the limitResultCount_rtMin to set
     */
    public void setLimitResultCount_rtMin(RoleType limitResultCount_rtMin) {
        this.limitResultCount_rtMin = limitResultCount_rtMin;
    }

    /**
     * @return the user_ctl
     */
    public boolean isUser_ctl() {
        return user_ctl;
    }

    /**
     * @param user_ctl the user_ctl to set
     */
    public void setUser_ctl(boolean user_ctl) {
        this.user_ctl = user_ctl;
    }

    /**
     * @return the user_val
     */
    public User getUser_val() {
        return user_val;
    }

    /**
     * @param user_val the user_val to set
     */
    public void setUser_val(User user_val) {
        this.user_val = user_val;
    }

   
    
}
