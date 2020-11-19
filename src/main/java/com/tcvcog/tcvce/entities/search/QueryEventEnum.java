/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.tcvcog.tcvce.entities.search;

import com.tcvcog.tcvce.entities.RoleType;

/**
 *
 * @author sylvia
 */
public  enum            QueryEventEnum 
        implements      IFace_RankLowerBounded{
    
    REQUESTED_ACTIONS(                  "Requested violation follow-up actions", 
                                        "System-generated events dated at the expiration of code violation compliance timeframes", 
                                        RoleType.MuniReader, 
                                        true),
    
    MUNI_MONTHYACTIVITY                 ("All system activity by Muni in the past 30 days", 
                                        "Events generated by the current municipality's default code officer in the past 30 days", 
                                        RoleType.MuniReader, 
                                        true),
    
    COMPLIANCE_EVENTS(                  "Violation compliance events: Past 30 days", 
                                        "Events detailing any code violation marked with compliance in the past 30 days", 
                                        RoleType.MuniReader, 
                                        true),
    
    OCCPERIOD(                          "Events by occ period",
                                        "All events by period",
                                        RoleType.MuniReader,
                                        false),
    
    CECASE  (                          "Events by Code Enforcement case",
                                        "All events by case",
                                        RoleType.MuniReader,
                                        false),
    
    PERSONS(                           "Events associated with a given Person",
                                       "in any way or capacity",
                                        RoleType.MuniReader,
                                        false),
    
    CUSTOM(                             "Custom", 
                                        "Custom", 
                                        RoleType.MuniReader,
                                        true);
    
    private final String title;
    private final String desc;
    private final RoleType requiredRoleMin;
    private final boolean log;
    
    private QueryEventEnum(String t, String l, RoleType minRoleType, boolean lg){
        this.desc = l;
        this.title = t;
        if(minRoleType != null){
            this.requiredRoleMin = minRoleType;
        } else {
            this.requiredRoleMin = RoleType.MuniStaff;
        }
        this.log = lg;
    }
    
    public String getDesc(){
        return desc;
    }
    
    public String getTitle(){
        return title;
    }

    
    public boolean logQueryRun(){
        return log;
    }

    @Override
    public RoleType getRequiredRoleMin() {
        return requiredRoleMin;
    }
    
    
}
