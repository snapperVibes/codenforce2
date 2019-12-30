/*
 * Copyright (C) 2017 Turtle Creek Valley
Council of Governments, PA
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.O
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
package com.tcvcog.tcvce.coordinators;

import com.tcvcog.tcvce.application.BackingBeanUtils;
import com.tcvcog.tcvce.application.interfaces.IFace_EventRuleGoverned;
import com.tcvcog.tcvce.domain.AuthorizationException;
import com.tcvcog.tcvce.domain.BObStatusException;
import com.tcvcog.tcvce.domain.EventException;
import com.tcvcog.tcvce.domain.IntegrationException;
import com.tcvcog.tcvce.domain.ViolationException;
import com.tcvcog.tcvce.entities.*;
import com.tcvcog.tcvce.entities.reports.ReportConfigCEEventList;
import com.tcvcog.tcvce.entities.User;
import com.tcvcog.tcvce.entities.UserAuthorized;
import com.tcvcog.tcvce.entities.occupancy.EventOccPeriod;
import com.tcvcog.tcvce.entities.occupancy.OccPeriod;
import com.tcvcog.tcvce.entities.occupancy.OccPeriodDataHeavy;
import com.tcvcog.tcvce.entities.occupancy.OccPeriodStatusEnum;
import com.tcvcog.tcvce.entities.search.SearchParamsEvent;
import com.tcvcog.tcvce.integration.ChoiceIntegrator;
import com.tcvcog.tcvce.integration.EventIntegrator;
import com.tcvcog.tcvce.integration.PersonIntegrator;
import java.io.Serializable;
import com.tcvcog.tcvce.util.Constants;
import com.tcvcog.tcvce.util.viewoptions.ViewOptionsActiveHiddenListsEnum;
import com.tcvcog.tcvce.util.viewoptions.ViewOptionsEventRulesEnum;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.faces.application.FacesMessage;
import com.tcvcog.tcvce.entities.IFace_Proposable;

/**
 *
 * Object playing the role of coordinator in the MVC framework by interfacing between
 * the JSF backing beans and the database integration classes.
 * 
 * This role involves several duties:
 * 
 * <ol>
 * <li>Generating new events for Code Enforcement and occupancy</li>
 * <li>Checking event creation permissions before allowing events of
 * restricted categories to be attached to other system objects.</li>
 * </ol>
 * 
 * 
 * @author Ellen Bascomb
 */
public class EventCoordinator extends BackingBeanUtils implements Serializable{

    /**
     * Creates a new instance of EventCoordinator
     */
    public EventCoordinator() {
        
    }
    
    
//    --------------------------------------------------------------------------
//    *************************** EVENT MAIN ***********************************
//    --------------------------------------------------------------------------
    
    
    /**
     * Primary access point for events by ID
     * @param eventID
     * @return 
     * @throws com.tcvcog.tcvce.domain.IntegrationException 
     */
    public Event getEvent(int eventID) throws IntegrationException{
        EventIntegrator ei = getEventIntegrator();
        if(eventID == 0){
            return null;
        }
        Event ev = ei.getEvent(eventID);
        return ev;
    }
    
    public EventCECaseHeavy getEventCaseHeavy(Event ev) throws EventException, IntegrationException, BObStatusException{
        CaseCoordinator cc = getCaseCoordinator();
        
        if(ev == null) return null;
        CECase cse = null;
        if(ev.getDomain() != EventDomainEnum.CODE_ENFORCEMENT){
            throw new EventException("Cannot create an EventCaseHeavy from an event not in CE Domain");
        }
        
        EventCECaseHeavy ech = new EventCECaseHeavy(ev);
        ech.setCeCase(cc.getCECase(ev.getCeCaseID()));
        
        return ech;
                
    }
    
    public EventPeriodPropUnitHeavy getEventPeriodPropUnitHeavy(Event ev) throws EventException, IntegrationException{
        PropertyCoordinator pc = getPropertyCoordinator();
        OccupancyCoordinator oc = getOccupancyCoordinator();
        
        if(ev == null) return null;
        if(ev.getDomain() != EventDomainEnum.OCCUPANCY){
            throw new EventException("Cannot create an EventCaseHeavy from an event not in Occ Domain");
        }
        
        EventPeriodPropUnitHeavy eppuh = new EventPeriodPropUnitHeavy(ev);
        
        eppuh.setPeriod(oc.getOccPeriod(ev.getOccPeriodID()));
        eppuh.setPropUnit(pc.getPropertyUnit(eppuh.getPeriod().getPropertyUnitID()));
        eppuh.setProp(pc.getProperty(eppuh.getPeriod().getPropertyUnitID()));
        
        return eppuh;
        
    }
    
    
    /**
     * Utility method for calling configureEvent on all EventCECase objects
 in a list passed back from a call to Query events
     * @param evList
     * @param user
     * @param userAuthMuniList
     * @return
     * @throws IntegrationException 
     */
    public List<EventCECaseCasePropBundle> configureEventBundleList(List<EventCECaseCasePropBundle> evList, 
                                                                        UserAuthorized user) throws IntegrationException{
        Iterator<EventCECaseCasePropBundle> iter = evList.iterator();
        while(iter.hasNext()){
            configureEvent(iter.next().getEvent());
        }
        return evList;
    }
  
    
    
    /**
     * Called by the EventIntegrator and other getEventCECase methods to set member variables based on business
     * rules before sending the event onto its requesting method. Checks for request processing, 
     * sets intended responder for action requests, etc.
     * @param ev
     * @param user
     * @return a nicely configured EventCEEcase
     * @throws com.tcvcog.tcvce.domain.IntegrationException
     */
    public Event configureEvent(Event ev) throws IntegrationException{
        
        // Declare this event as either in the CE or Occ domain with 
        // our hacky little enum thingy
        
        if(ev.getCeCaseID() != 0){
            ev.setDomain(EventDomainEnum.CODE_ENFORCEMENT);
        } else if(ev.getCeCaseID() != 0){
            ev.setDomain(EventDomainEnum.OCCUPANCY);
        } else {
            ev.setDomain(null);
        }
        
       
        // begin configuring the event proposals assocaited with this event
        // remember: event proposals are specified in an EventCategory object
        // but when we build an Event object, the ProposalImplementation lives on the Event itself
        // 
//        if(ev.getCategory().getDirective() != null){
//            TODO: OccBeta
//            Proposal imp = ei.getProposalImplAssociatedWithEvent(ev);
//            imp.setCurrentUserCanEvaluateProposal(determineCanUserEvaluateProposal(ev, user, userAuthMuniList));
//            ev.setEventProposalImplementation(imp);
//        }
//        ev.setPersonList(pi.getPersonList(ev));
        
        return ev;
    }
    
    /**
     * Implements business logic to ensure Event correctness; called by insert
     * and edit event methods; Throws an EventException if there's an error
     * 
     * @param ev
     * @throws com.tcvcog.tcvce.domain.EventException
     */
    public void auditEvent(Event ev) throws EventException{
        if(ev.getTimeStart() == null){
            throw new EventException("Events must have a start time");
        }
        if(ev.getTimeEnd() != null){
            if(ev.getTimeEnd().isBefore(ev.getTimeStart())){
                throw new EventException("Events with end times must not have an end time before start time");
            }
        }
    }
    
    
    
    
    
    /**
     * Business rule aware pathway to update fields on Event objects
     * When updating Person links, this method clears all previous connections
     * and rebuilds the mapping from scratch on each update.
     * 
     * @param ev
     * @throws IntegrationException 
     * @throws com.tcvcog.tcvce.domain.EventException 
     */
    public void editEvent(Event ev) throws IntegrationException, EventException{
        PersonIntegrator pi = getPersonIntegrator();
        EventIntegrator ei = getEventIntegrator();
        
        auditEvent(ev);
        ei.updateEvent(ev);
        pi.eventPersonClear(ev);
        pi.eventPersonsConnect(ev, ev.getPersonList());
        
    }
    
  
    
    public void deleteEvent(Event ev, UserAuthorized u) throws AuthorizationException{
        EventIntegrator ei = getEventIntegrator();
        try {
            if(u.getMyCredential().isHasSysAdminPermissions()){
                ei.deleteEvent(ev);
            } else {
                throw new AuthorizationException("Must have sys admin permissions "
                        + "to delete event; marking an event as inactive is like deleting it");
            }
        } catch (IntegrationException ex) {

        }
    }
  
   
  
    /**
     * Core coordinator method called by all other classes who want to 
     * create their own event. Restricts the event type based on current
     * case phase (closed cases cannot have action, origination, or compliance events.
     * Includes the instantiation of Event objects
     * 
     * @param erg
     * @param ec the type of event to attach to the case
     * @return an initialized event with basic properties set
     * @throws BObStatusException thrown if the case is in an improper state for proposed event
     */
    public Event initializeEvent(IFace_EventRuleGoverned erg, EventCategory ec) throws BObStatusException, EventException{
        
        if(ec == null) return null;
        
        CECase cse = null;
        OccPeriod op = null;
        
        // the moment of event instantiaion!!!!
        Event e = new Event();
        
        if(erg != null){
            if(erg instanceof CECase){
                cse = (CECase) erg;
                 if(cse.getCasePhase() == CasePhase.Closed && 
                    (
                        ec.getEventType() == EventType.Action
                        || 
                        ec.getEventType() == EventType.Origination
                        ||
                        ec.getEventType() == EventType.Compliance
                    )
                ){
                    throw new BObStatusException("This event cannot be attached to a closed case");
                }
                e.setCeCaseID(cse.getCaseID());
                e.setDomain(EventDomainEnum.CODE_ENFORCEMENT);
            } else if (erg instanceof OccPeriod){
                op = (OccPeriod) erg;
                e.setOccPeriodID(op.getPeriodID());
                e.setDomain(EventDomainEnum.OCCUPANCY);
            }
        }
        
        auditEvent(e);
        
        // Long-term TODO: check against permitted event types
        e.setCategory(ec);
        
        e.setTimeStart(LocalDateTime.now());
        e.setTimeEnd(e.getTimeStart().plusMinutes(ec.getDefaultdurationmins()));
        
        e.setActive(true);
        e.setHidden(false);
        
        return e;
    }
    
    
    
//    --------------------------------------------------------------------------
//    ***************************** SEARCH *************************************
//    --------------------------------------------------------------------------
    
    
    
    
     /**
     * Pathway for injecting business logic into the event search process. Now its just a pass through.
     * @param params
     * @param user the current user
     * @return
     * @throws IntegrationException 
     * @throws com.tcvcog.tcvce.domain.BObStatusException 
     */
    public List<EventCECaseCasePropBundle> queryEvents( SearchParamsEvent params, 
                                                        Credential cred) throws IntegrationException, BObStatusException{
        EventIntegrator ei = getEventIntegrator();
        
        
        
        List<EventCECaseCasePropBundle> evList = configureEventBundleList(  ei.searchForEvents(params),
                                                                            user);
        return evList;
    }
    
    
    public SearchParamsEvent getSearchParamsCEEventsRequiringAction(UserAuthorized user, Municipality m){
        SearchCoordinator sc = getSearchCoordinator();
        return sc.getSearchParamsEventsRequiringAction(user,m);
    }
    
    public SearchParamsEvent getSearchParamsOfficerActibityPastWeek(UserAuthorized user, Municipality m){
        SearchCoordinator sc = getSearchCoordinator();
        return sc.getSearchParamsOfficerActivity(user, m);
    }
    
    
    public SearchParamsEvent getSearchParamsComplianceEvPastMonth(Municipality m){
        SearchCoordinator sc = getSearchCoordinator();
        return sc.getSearchParamsComplianceEvPastMonth(m);
    }
    
      
    public ReportConfigCEEventList getDefaultReportConfigCEEventList(){
        SearchCoordinator sc = getSearchCoordinator();
        ReportConfigCEEventList config = new ReportConfigCEEventList();
        config.setIncludeAttachedPersons(true);
        config.setIncludeCaseActionRequestInfo(false);
        config.setGenerationTimestamp(LocalDateTime.now());
        config.setIncludeEventTypeSummaryChart(true);
        config.setIncludeActiveCaseListing(false);
        config.setIncludeCompleteQueryParamsDump(false);
        config.setSortInRevChrono(true);
        return config;
    }
    
//    --------------------------------------------------------------------------
//    **************** EVENT CATEGORIES ****************************************
//    --------------------------------------------------------------------------
    
     /**
     * Implements business rules for determining which event types are allowed
     * to be attached to the given CECase based on the case's phase and the
     * user's permissions in the system.
     *
     * Used for displaying the appropriate event types to the user on the
     * cecases.xhtml page
     *
     * @param c the CECase on which the event would be attached
     * @param u the User doing the attaching
     * @return allowed EventTypes for attaching to the given case
     */
    
    public List<EventType> getPermittedEventTypesForCECase(CECase c, UserAuthorized u) {
        List<EventType> typeList = new ArrayList<>();
        RoleType role = u.getRole();
        if (role == RoleType.EnforcementOfficial || u.getRole() == RoleType.Developer) {
            typeList.add(EventType.Action);
            typeList.add(EventType.Timeline);
        }
        if (role != RoleType.MuniReader) {
            typeList.add(EventType.Communication);
            typeList.add(EventType.Meeting);
            typeList.add(EventType.Custom);
        }
        return typeList;
    }
    
    
    public List<EventType> getPermittedEventTypesForOcc(OccPeriod period, UserAuthorized u) {
        List<EventType> typeList = new ArrayList<>();
        RoleType role = u.getRole();
        if (role == RoleType.EnforcementOfficial || u.getRole() == RoleType.Developer) {
            typeList.add(EventType.Action);
            typeList.add(EventType.Timeline);
            typeList.add(EventType.Occupancy);
        }
        if (role != RoleType.MuniReader) {
            typeList.add(EventType.Communication);
            typeList.add(EventType.Meeting);
            typeList.add(EventType.Custom);
        }
        return typeList;
    }
    
    public List<EventType> getEventTypesAll(){
        List<EventType> typeList = new ArrayList<>();
        for(EventType et: EventType.values()){
            typeList.add(et);
        }
        return typeList;
    }
    
    
    /**
     * Factory method for creating bare event categories.
     * This is used when creating search parameter objects where we want event
     * types without a specific category, but we need a EventCategory shell
     * in which to insert the EventType
     * 
     * @return an EventCategory container with basic properties set
     */
    public EventCategory getInitializedEventCateogry(){
        EventCategory ec =  new EventCategory();
        ec.setUserdeployable(true);
        ec.setHidable(true);
        // TODO: finishing autoconfiguring these 
        return ec;
    }
    
    /**
     * Factory method for creating event categories when only the categoryID
     * is available. This is handy since the insertEvent method on the integrator
     * only needs the categoryID for storing in the database
     * @param catID the categoryID of the EventCategory you want
     * @return an instantiated EventCategory object
     * @throws com.tcvcog.tcvce.domain.IntegrationException
     */
    public EventCategory getInitiatlizedEventCategory(int catID) throws IntegrationException{
        EventIntegrator ei = getEventIntegrator();
        EventCategory ec =  ei.getEventCategory(catID);
        return ec;
    }
    
  

  
    
    public List<EventCategory> getEventCategoryListActive() throws IntegrationException{
        EventIntegrator ei = getEventIntegrator();
        List<EventCategory> catList = ei.getEventCategoryList();
        for(EventCategory cat: catList){
            // TODO: remove inactive EventCategories
            // TODO: add active flag in DB and int methods
        }
        return catList;
    }
    
      
    public List<EventCategory> loadEventCategoryListUserAllowed(EventType et, UserAuthorized u) throws IntegrationException{
        EventIntegrator ei = getEventIntegrator();
        // TODO: add logic for only allowing certain event cats based on user needs
        return ei.getEventCategoryList(et);
        
    }
    
    
//    --------------------------------------------------------------------------
//    **************** OPERATION SPECIFIC EVENT CONFIG *************************
//    --------------------------------------------------------------------------
    
    /**
     * Creates a populated event to log the change of a code violation update. 
     * The event is coming to us from the violationEditBB with the description and disclosures flags
     * correct. This method needs to set the description from the resource bundle, and 
     * set the date of record to the current date
     * @param ceCase the CECase whose violation was updated
     * @param cv the code violation being updated
     * @param event An initialized event
     * @throws IntegrationException bubbled up from the integrator
     * @throws EventException 
     * @throws com.tcvcog.tcvce.domain.BObStatusException 
     * @throws com.tcvcog.tcvce.domain.ViolationException 
     */
    public void generateAndInsertCodeViolationUpdateEvent(CECase ceCase, CodeViolation cv, EventCECase event) 
            throws IntegrationException, EventException, BObStatusException, ViolationException{
        EventIntegrator ei = getEventIntegrator();
        CaseCoordinator cc = getCaseCoordinator();
        String updateViolationDescr = getResourceBundle(Constants.MESSAGE_TEXT).getString("violationChangeEventDescription");
       
        // hard coded for now
//        event.setCategory(ei.getEventCategory(117));
        event.setCaseID(ceCase.getCaseID());
//        event.setDateOfRecord(LocalDateTime.now());
        event.setDescription(updateViolationDescr);
        //even descr set by violation coordinator
        event.setOwner(getSessionBean().getSessionUser());
        // disclose to muni from violation coord
        // disclose to public from violation coord
        event.setActive(true);
        
        cc.attachNewEventToCECase(ceCase, event, null);
    }
    
      /**
     * Takes in a well-formed event message from the CaseCoordinator and
     * initializes the appropriate properties on the event before insertion
     * @param caseID id of the case to which the event should be attached
     * @param message the text of the event description message
     * @throws IntegrationException in the case of broken integration process
     * @throws com.tcvcog.tcvce.domain.BObStatusException
     * @throws com.tcvcog.tcvce.domain.EventException
     */
    public void attachPublicMessagToCECase(int caseID, String message) throws IntegrationException, BObStatusException, EventException{
        EventIntegrator ei = getEventIntegrator();
        UserCoordinator uc = getUserCoordinator();
        
        int publicMessageEventCategory = Integer.parseInt(getResourceBundle(Constants.EVENT_CATEGORY_BUNDLE).getString("publicCECaseMessage"));
        EventCategory ec = getInitiatlizedEventCategory(publicMessageEventCategory);
        
        // setup all the event properties
        Event event =  initializeEvent(null, ec);
        event.setCategory(ec);
//        event.setDateOfRecord(LocalDateTime.now());
        event.setDescription(message);
        event.setOwner(uc.getUserRobot());
        event.setDiscloseToMunicipality(true);
        event.setDiscloseToPublic(true);
        event.setActive(true);
        event.setHidden(false);
        event.setNotes("Event created by a public user");
        
        // sent the built event to the integrator!
        ei.insertEvent(event);
    }
    
    
    
    
    
    /**
     * Configures an event which represents the moment of compliance with
     * a code violation attached to a code enforcement case
     * 
     * @param violation
     * @return a partially-baked event ready for inserting
     * @throws IntegrationException 
     */
    public EventCECase generateViolationComplianceEvent(CodeViolation violation) throws IntegrationException{
        Event e = new Event();
        EventIntegrator ei = getEventIntegrator();
          e.setCategory(ei.getEventCategory(Integer.parseInt(getResourceBundle(
                Constants.EVENT_CATEGORY_BUNDLE).getString("complianceEvent"))));
        e.setDescription("Compliance with municipal code achieved");
        e.setActive(true);
        e.setDiscloseToMunicipality(true);
        e.setDiscloseToPublic(true);
        
        StringBuilder sb = new StringBuilder();
        sb.append("Compliance with the following code violations was observed:");
        sb.append("<br /><br />");
        
            sb.append(violation.getViolatedEnfElement().getCodeElement().getOrdchapterNo());
            sb.append(".");
            sb.append(violation.getViolatedEnfElement().getCodeElement().getOrdSecNum());
            sb.append(".");
            sb.append(violation.getViolatedEnfElement().getCodeElement().getOrdSubSecNum());
            sb.append(":");
            sb.append(violation.getViolatedEnfElement().getCodeElement().getOrdSubSecTitle());
            sb.append(" (ID ");
            sb.append(violation.getViolationID());
            sb.append(")");
            sb.append("<br /><br />");
        e.setNotes(sb.toString());
        EventCECase cev = new EventCECase(e);
        return cev;
    }
    
    /**
     * The currentCase argument must be a CECase with the desired case phase set
     * The past phase is passed in separately, allowing for phase changes to
     * any phase from any other phase
     * @deprecated 
     * @param currentCase
     * @param pastPhase
     * @param rule
     * @throws IntegrationException
     * @throws BObStatusException 
     * @throws com.tcvcog.tcvce.domain.ViolationException 
     */
    public void generateAndInsertPhaseChangeEvent(CECase currentCase, CasePhase pastPhase, EventRuleAbstract rule) 
            throws IntegrationException, BObStatusException, ViolationException, EventException{
        
        EventIntegrator ei = getEventIntegrator();
        CaseCoordinator cc = getCaseCoordinator();
        
        
        Event event = initializeEvent(currentCase, ei.getEventCategory(Integer.parseInt(getResourceBundle(
                Constants.EVENT_CATEGORY_BUNDLE).getString("casePhaseChangeEventCatID"))));
        
        StringBuilder sb = new StringBuilder();
        sb.append("Case phase changed from  \'");
        sb.append(pastPhase.toString());
        sb.append("\' to \'");
        sb.append(currentCase.getCasePhase().toString());
        sb.append("\'");
        if(rule != null){
            sb.append("following the passing of CasePhaseChangeRule:  ");
            sb.append(rule.getTitle());
            sb.append(", no. ");
        }
        event.setDescription(sb.toString());
        
        // not sure if I can access the session level info for the specific user here in the
        // coordinator bean
        event.setOwner(getSessionBean().getSessionUser());
        event.setActive(true);
        
        cc.attachNewEventToCECase(currentCase, event, null);
        
        getFacesContext().addMessage(null,
            new FacesMessage(FacesMessage.SEVERITY_INFO, 
                    "The case phase has been changed", ""));

    } // close method
    
    
    /**
     * A BOB-agnostic event generator given a Proposal object and the Choice that was
     * selected by the user. 
     * @param p
     * @param ch
     * @param u
     * @return a configured but not integrated Event superclass. The caller will need to cast it to
     * the appropriate subclass and insert it
     * @throws com.tcvcog.tcvce.domain.BObStatusException 
     * @throws com.tcvcog.tcvce.domain.IntegrationException 
     */
    public Event generateEventDocumentingProposalEvaluation(Proposal p, IFace_Proposable ch, UserAuthorized u) throws BObStatusException, IntegrationException{
        Event ev = null;
        if(ch instanceof ChoiceEventCat){
            EventCategory ec = getInitiatlizedEventCategory(((ChoiceEventCat) ch).getEventCategory().getCategoryID());
            ev = getInitializedEvent(ec);
            
            ev.setActive(true);
            ev.setHidden(false);
            ev.setDateOfRecord(LocalDateTime.now());
            ev.setDiscloseToMunicipality(true);
            ev.setDiscloseToPublic(false);
            ev.setOwner(u);
            ev.setTimestamp(LocalDateTime.now());
            
            StringBuilder descBldr = new StringBuilder();
            descBldr.append("User ");
            descBldr.append(u.getPerson().getFirstName());
            descBldr.append(" ");
            descBldr.append(u.getPerson().getLastName());
            descBldr.append(" evaluated the proposal titled: '");
            descBldr.append(p.getDirective().getTitle());
            descBldr.append("' on ");
            descBldr.append(getPrettyDateNoTime(p.getResponseTS()));
            descBldr.append(" and selected choice titled:  '");
            descBldr.append(ch.getTitle());
            descBldr.append("'.");
            
            ev.setDescription(descBldr.toString());
            
        } else {
            throw new BObStatusException("Generating events for Choice "
                    + "objects that are not Event triggers is not yet supported. "
                    + "Thank you in advance for your patience.");
        }
        return ev;
    }
    
    public void generateAndInsertManualCasePhaseOverrideEvent(CECase currentCase, CasePhase pastPhase) 
            throws IntegrationException, BObStatusException, ViolationException{
        
          EventIntegrator ei = getEventIntegrator();
          CaseCoordinator cc = getCaseCoordinator();
        
        EventCECase event = getInitializedEvent(currentCase, ei.getEventCategory(Integer.parseInt(getResourceBundle(
                Constants.EVENT_CATEGORY_BUNDLE).getString("casePhaseManualOverride"))));
        
        StringBuilder sb = new StringBuilder();
        sb.append("Manual case phase change from  \'");
        sb.append(pastPhase.toString());
        sb.append("\' to \'");
        sb.append(currentCase.getCasePhase().toString());
        sb.append("\' by a a case officer.");
        event.setDescription(sb.toString());
        
        event.setCaseID(currentCase.getCaseID());
        event.setDateOfRecord(LocalDateTime.now());
        // not sure if I can access the session level info for the specific user here in the
        // coordinator bean
        event.setOwner(getSessionBean().getSessionUser());
        event.setActive(true);
        
        cc.attachNewEventToCECase(currentCase, event, null);
        
        getFacesContext().addMessage(null,
            new FacesMessage(FacesMessage.SEVERITY_INFO, 
                    "The case phase has been changed", ""));
    }
    
    
     
//    --------------------------------------------------------------------------
//    ******************************** RULES and WORKFLOWS *********************
//    --------------------------------------------------------------------------
    
   /**
     * Utility method for setting view confirmation authorization 
     * at the event level by user
     * @deprecated following separation of Choice objects and their selections from events
     * @param ev
     * @param u the User viewing the list of CEEvents
     * @param muniList
     * @return 
     */
    public boolean determineCanUserEvaluateProposal(EventCECase ev, UserAuthorized u, List<Municipality> muniList){
        boolean canEvaluateProposal = false;
        Directive evProp = ev.getCategory().getDirective();
        
        // direct event assignment allows view conf to cut across regular permissions
        // checks
        if(ev.getOwner().equals(u) || u.getMyCredential().isHasDeveloperPermissions()){
            return true;
            // check that the event is associated with the user's auth munis
        } else if(isMunicodeInMuniList(ev.getMuniCode(), muniList)){
            // sys admins for a muni can confirm everything
            if(u.getMyCredential().isHasSysAdminPermissions()){
                return true;
                // only code officers can enact timeline events
            } else if(evProp.isDirectPropToDefaultMuniCEO() && u.getMyCredential().isHasEnfOfficialPermissions()){
                return true;
            } else if(evProp.isDirectPropToDefaultMuniStaffer() && u.getMyCredential().isHasMuniStaffPermissions()){
                return true;
            } 
        }
        return canEvaluateProposal;
    }
    
    
    public EventRuleAbstract rules_getEventRuleAbstract(int eraid) throws IntegrationException{
        EventIntegrator ei = getEventIntegrator();
        return ei.rules_getEventRuleAbstract(eraid);
    }
    
    /**
     * Attaches a single event rule to an EventRuleGoverned entity, the type of which is determined
     * internally with instanceof checks for OccPeriod and CECase Objects
     * 
     * @param era
     * @param rg
     * @param usr
     * @throws com.tcvcog.tcvce.domain.IntegrationException 
     * @throws com.tcvcog.tcvce.domain.BObStatusException if an IFaceEventRuleGoverned instances is neither a CECase or an OccPeriod
     */
    public void rules_attachEventRule(EventRuleAbstract era, IFace_EventRuleGoverned rg, UserAuthorized usr) throws IntegrationException, BObStatusException{
        
        ChoiceCoordinator cc = getChoiceCoordinator();
        int freshObjectID = 0;
        if(rg instanceof OccPeriodDataHeavy){
                OccPeriodDataHeavy op = (OccPeriodDataHeavy) rg;
                rules_attachEventRuleAbstractToOccPeriod(era, op, usr);
                if(freshObjectID != 0 && era.getPromptingDirective() != null){
                    cc.implementDirective(era.getPromptingDirective(), op, null);
                    System.out.println("EventCoordinator.rules_attachEventRule | Found not null prompting directive");
                }
            } else if (rg instanceof CECase){ 
                CECase cec = (CECase) rg;
                rules_attachEventRuleAbstractToCECase(era, cec);
                if(freshObjectID != 0 && era.getPromptingDirective() != null){
                    cc.implementDirective(era.getPromptingDirective(), cec, null);
                }
            } else {
                throw new BObStatusException("Cannot attach rule set");
            }
    }
    
    /**
     * Returns complete muni dump of the eventrule table
     * 
     * @return complete event rule list, including inactive events
     * @throws IntegrationException 
     */
    public List<EventRuleSet> rules_getEventRuleSetList() throws IntegrationException{
        EventIntegrator ei = getEventIntegrator();
        return ei.rules_getEventRuleSetList();
    }  
    
    public EventRuleAbstract rules_getInitializedEventRuleAbstract(){
        EventRuleAbstract era = new EventRuleAbstract();
        era.setActiveRuleAbstract(true);
        return era;
    }
    
    public void rules_updateEventRuleAbstract(EventRuleAbstract era) throws IntegrationException{
        EventIntegrator ei = getEventIntegrator();
        ei.rules_updateEventRule(era);
        
    }
    
    /**
     * Primary entrance point for an EventRuleAbstract instance (not its connection to an Object)
     * @param era required instance
     * @param period optional--only if you're attaching to an OccPeriod
     * @param cse Optional--only if you're attachign to a CECase
     * @param connectToBOBRuleList Switch me on in order to 
     * @param usr 
     * @return
     * @throws IntegrationException 
     */
    public int rules_createEventRuleAbstract(EventRuleAbstract era, OccPeriodDataHeavy period, CECase cse, boolean connectToBOBRuleList, UserAuthorized usr) throws IntegrationException{
        EventIntegrator ei = getEventIntegrator();
        ChoiceIntegrator ci = getChoiceIntegrator();
        
        int freshEventRuleID;
        if(era.getFormPromptingDirectiveID() != 0){
            Directive dir = ci.getDirective(era.getFormPromptingDirectiveID());
            if(dir != null){
                era.setPromptingDirective(dir);
                System.out.println("EventCoordinator.rules_createEventRuleAbstract| Found not null directive ID: " + dir.getDirectiveID());
            }
        }
        
        freshEventRuleID = ei.rules_insertEventRule(era);
        if(period != null && cse == null){
            era = ei.rules_getEventRuleAbstract(freshEventRuleID);
            rules_attachEventRuleAbstractToOccPeriod(era, period, usr);
            if(connectToBOBRuleList){
                rules_attachEventRuleAbstractToOccPeriodTypeRuleSet(era, period);
            }
        }
        if(period == null && cse !=null){
            era = ei.rules_getEventRuleAbstract(freshEventRuleID);
            if(connectToBOBRuleList){
                rules_attachEventRuleAbstractToMuniCERuleSet(era, cse);
            }
        }
        
        System.out.println("EventCoordinator.rules_createEventRuleAbstract | returned ID: " + freshEventRuleID);
        return freshEventRuleID;
    }
    
    private void rules_attachEventRuleAbstractToOccPeriod(EventRuleAbstract era, OccPeriodDataHeavy period, UserAuthorized usr) throws IntegrationException{
        
        EventIntegrator ei = getEventIntegrator();
        ChoiceCoordinator cc = getChoiceCoordinator();
        EventRuleOccPeriod erop = new EventRuleOccPeriod(new EventRuleImplementation(era));
        // avoid inserting and duplicating keys
        if(ei.rules_getEventRuleOccPeriod(period.getPeriodID(), era.getRuleid()) == null){
        erop.setAttachedTS(LocalDateTime.now());
            erop.setOccPeriodID(period.getPeriodID());
            
            erop.setLastEvaluatedTS(null);
            erop.setPassedRuleTS(null);
            erop.setPassedRuleEvent(null);
            ei.rules_insertEventRuleOccPeriod(erop);
        }
        if(era.getPromptingDirective() != null){
            cc.implementDirective(era.getPromptingDirective(), period, null);
            System.out.println("EventCoordinator.rules_attachEventRulAbstractToOccPeriod | directive implemented with ID " + era.getPromptingDirective().getDirectiveID());
        }
    }
    
    public void rules_attachEventRuleAbstractToOccPeriodTypeRuleSet(EventRuleAbstract era, OccPeriod period) throws IntegrationException{
        EventIntegrator ei = getEventIntegrator();
        ei.rules_addEventRuleAbstractToOccPeriodTypeRuleSet(era, period.getType().getBaseRuleSetID());
    }
    
    /**
     * TODO: Finish my guts!
     * @param muni to which we want to include the rule. The Municipality's profile will be pulled and its 
     * @param era 
     */
    public void rules_includeEventRuleAbstractInCECaseDefSet(Municipality muni, EventRuleAbstract era){
        
    }
    
    /**
     * Takes in an EventRuleSet object which contains a list of EventRuleAbstract objects
     * and either an OccPeriod or CECase and implements those abstract rules 
     * on that particular business object
     * @param ers
     * @param rg
     * @param usr
     * @throws IntegrationException
     * @throws BObStatusException 
     */
    public void rules_attachRuleSet(EventRuleSet ers, IFace_EventRuleGoverned rg, UserAuthorized usr) throws IntegrationException, BObStatusException{
        for(EventRuleAbstract era: ers.getRuleList()){
            if(rg instanceof OccPeriodDataHeavy){
                OccPeriodDataHeavy op = (OccPeriodDataHeavy) rg;
                rules_attachEventRuleAbstractToOccPeriod(era, op, usr);
            } else if (rg instanceof CECase){
                CECase cec = (CECase) rg;
                rules_attachEventRuleAbstractToCECase(era, cec);
            } else {
                throw new BObStatusException("Cannot attach rule set");
            }
        }
        
    }
    
    /**
     * TODO: Finish my guts
     * @param era
     * @param cse 
     */
    private void rules_attachEventRuleAbstractToCECase(EventRuleAbstract era, CECase cse){
    
        
    }
    
    /**
     * TODO: finish my guts
     * @param era
     * @param cse 
     */
    public void rules_attachEventRuleAbstractToMuniCERuleSet(EventRuleAbstract era, CECase cse){
        
    }
    
    public boolean rules_evaluateEventRules(OccPeriodDataHeavy period) throws IntegrationException, BObStatusException, ViolationException{
        boolean allRulesPassed = true;
        List<EventRuleImplementation> rlst = period.assembleEventRuleList(ViewOptionsEventRulesEnum.VIEW_ALL);
        
        for(EventRuleAbstract era: rlst){
            if(!rules_evalulateEventRule(period.assembleEventList(ViewOptionsActiveHiddenListsEnum.VIEW_ALL), era)){
                allRulesPassed = false;
                break;
            }
        }
        return allRulesPassed;
    }

    
    public boolean rules_evalulateEventRule(List<Event> eventList, EventRuleAbstract rule) throws IntegrationException, BObStatusException, ViolationException {
        CaseCoordinator cc = getCaseCoordinator();
        
        if(eventList == null || rule == null){
            throw new BObStatusException("EventCoordinator.evaluateEventRule | Null event list or rule");
        }
        
        if (rule.getRequiredEventType() != null){
            if(!ruleSubcheck_requiredEventType(eventList, rule)){
                return false;
            }
        } 
        if (rule.getForbiddenEventType() != null){
            if(!ruleSubcheck_forbiddenEventType(eventList, rule)){
                return false;
            }
        } 
        if (rule.getRequiredEventCategory() != null){
            if(!ruleSubcheck_requiredEventCategory(eventList, rule)){
                return false;
            }
        } 
        if (rule.getForbiddenEventCategory() != null){
            if(!ruleSubcheck_forbiddenEventCategory(eventList, rule)){
                return false;
            }
        } 
        return true;
    }
    
    
    private boolean rules_evalulateEventRule(CECase cse, EventCECase event) throws IntegrationException, BObStatusException, ViolationException {
        EventRuleAbstract rule = new EventRuleAbstract();
        boolean rulePasses = false;
        CaseCoordinator cc = getCaseCoordinator();
        
        if (ruleSubcheck_requiredEventType(cse, rule) 
                && 
            ruleSubcheck_forbiddenEventType(cse, rule) 
                && 
            ruleSubcheck_requiredEventCategory(cse, rule) 
                && 
            ruleSubcheck_forbiddenEventCategory(cse, rule)) {
                rulePasses = true;
                cc.processCaseOnEventRulePass(cse, rule);
        }
        return rulePasses;
    }
    
    private boolean ruleSubcheck_requiredEventCategory(CECase cse, EventRuleAbstract rule) {
        boolean subcheckPasses = true;
        if (rule.getRequiredEventCategory().getCategoryID() != 0) {
            subcheckPasses = false;
            Iterator<EventCECase> iter = cse.getVisibleEventList().iterator();
            while (iter.hasNext()) {
                EventCECase ev = iter.next();
                if (ev.getCategory().getCategoryID() == rule.getRequiredEventCategory().getCategoryID()) {
                    subcheckPasses = true;
                }
            }
        }
        return subcheckPasses;
    }

    private boolean ruleSubcheck_forbiddenEventType(CECase cse, EventRuleAbstract rule) {
        boolean subcheckPasses = true;
        Iterator<EventCECase> iter = cse.getVisibleEventList().iterator();
        while (iter.hasNext()) {
            EventCECase ev = iter.next();
            if (ev.getCategory().getEventType() == rule.getRequiredEventType()) {
                subcheckPasses = false;
            }
        }
        return subcheckPasses;
    }

    private boolean ruleSubcheck_requiredEventType(CECase cse, EventRuleAbstract rule) {
        boolean subcheckPasses = true;
        if (rule.getRequiredEventType() != null) {
            subcheckPasses = false;
            Iterator<EventCECase> iter = cse.getVisibleEventList().iterator();
            while (iter.hasNext()) {
                EventCECase ev = iter.next();
                if (ev.getCategory().getEventType() == rule.getRequiredEventType()) {
                    subcheckPasses = true;
                }
            }
        }
        return subcheckPasses;
    }

    private boolean ruleSubcheck_forbiddenEventCategory(CECase cse, EventRuleAbstract rule) {
        boolean subcheckPasses = true;
        Iterator<EventCECase> iter = cse.getVisibleEventList().iterator();
        while (iter.hasNext()) {
            EventCECase ev = iter.next();
            if (ev.getCategory().getCategoryID() == rule.getRequiredEventCategory().getCategoryID()) {
                subcheckPasses = false;
            }
        }
        return subcheckPasses;
    }
    
    private boolean ruleSubcheck_requiredEventCategory(List<Event> eventList, EventRuleAbstract rule) {        
        Iterator<Event> iter = eventList.iterator();
        while (iter.hasNext()) {
            Event ev = iter.next();
            // simplest case: check for matching categories
            if (ev.getCategory().getCategoryID() == rule.getRequiredEventCategory().getCategoryID()) {
                return true;
            }
            // if we didn't match, perhaps we need to treat the requried category as a threshold
            // to be applied to an event category's type internal relative order
            if(rule.getRequiredECThreshold_typeInternalOrder() != 0){
                if(rule.isRequiredECThreshold_typeInternalOrder_treatAsUpperBound()){
                    if(ev.getCategory().getRelativeOrderWithinType() <= rule.getRequiredECThreshold_typeInternalOrder()){
                        return true;
                    }
                } else { // treat threshold as a lower bound
                    if(ev.getCategory().getRelativeOrderWithinType() >= rule.getRequiredECThreshold_typeInternalOrder()){
                        return true;
                    }
                }
            }
            // if we didn't pass the rule with type internal ordering as a thresold, check global
            // ordering thresolds
            if(rule.getRequiredECThreshold_globalOrder() != 0){
                if(rule.isRequiredECThreshold_globalOrder_treatAsUpperBound()){
                    if(ev.getCategory().getRelativeOrderGlobal()<= rule.getRequiredECThreshold_globalOrder()){
                        return true;
                    }
                } else { // treat threshold as a lower bound
                    if(ev.getCategory().getRelativeOrderGlobal() >= rule.getRequiredECThreshold_globalOrder()){
                        return true;
                    }
                }
            }
        }
        // list did not contain an Event whose category was required or required in a specified range
        return false;
    }
    
    private boolean ruleSubcheck_forbiddenEventCategory(List<Event> eventList, EventRuleAbstract rule) {
       Iterator<Event> iter = eventList.iterator();
        while (iter.hasNext()) {
            Event ev = iter.next();
            // simplest case: check for matching categories
            if (ev.getCategory().getCategoryID() == rule.getForbiddenEventCategory().getCategoryID()) {
                return false;
            }
            // if we didn't match, perhaps we need to treat the requried category as a threshold
            // to be applied to an event category's type internal relative order
            if(rule.getForbiddenECThreshold_typeInternalOrder() != 0){
                if(rule.isForbiddenECThreshold_typeInternalOrder_treatAsUpperBound()){
                    if(ev.getCategory().getRelativeOrderWithinType() <= rule.getForbiddenECThreshold_typeInternalOrder()){
                        return false;
                    }
                } else { // treat threshold as a lower bound
                    if(ev.getCategory().getRelativeOrderWithinType() >= rule.getForbiddenECThreshold_typeInternalOrder()){
                        return false;
                    }
                }
            }
            // if we didn't pass the rule with type internal ordering as a thresold, check global
            // ordering thresolds
            if(rule.getForbiddenECThreshold_globalOrder() != 0){
                if(rule.isForbiddenECThreshold_globalOrder_treatAsUpperBound()){
                    if(ev.getCategory().getRelativeOrderGlobal()<= rule.getForbiddenECThreshold_globalOrder()){
                        return false;
                    }
                } else { // treat threshold as a lower bound
                    if(ev.getCategory().getRelativeOrderGlobal() >= rule.getForbiddenECThreshold_globalOrder()){
                        return false;
                    }
                }
            }
        }
        // list did not contain an Event whose category was required or required in a specified range
        return true;
    }

    private boolean ruleSubcheck_requiredEventType(List<Event> eventList, EventRuleAbstract rule) {
        Iterator<Event> iter = eventList.iterator();
        while (iter.hasNext()) {
            EventType evType = iter.next().getCategory().getEventType();
            if (evType == rule.getRequiredEventType()) {
                return true;
            }
        }
        return false;
    }
    
    private boolean ruleSubcheck_forbiddenEventType(List<Event> eventList, EventRuleAbstract rule) {
        Iterator<Event> iter = eventList.iterator();
        while (iter.hasNext()) {
            EventType evType = iter.next().getCategory().getEventType();
            if (evType == rule.getForbiddenEventType()) {
                return false;
            }
        }
        return true;
    }

    
    
} // close class