/*
 * Copyright (C) 2019 Technology Rediscovery LLC
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
package com.tcvcog.tcvce.entities;

import com.tcvcog.tcvce.entities.occupancy.OccPeriod;

/**
 *
 * @author Ellen Bascomb
 */
public  class   EventOccPeriodPropUnitHeavy 
        extends Event{
    
    protected Property prop;
    protected PropertyUnit propUnit;
    protected OccPeriod period;
    
    public EventOccPeriodPropUnitHeavy(Event ev){
        this.eventID = ev.getEventID();
        this.category = ev.getCategory();
        
        this.domain = ev.getDomain();
        this.ceCaseID = ev.getCeCaseID();
        this.occPeriodID = ev.getOccPeriodID();

        this.dateOfRecord = ev.getDateOfRecord();
        this.timestamp = ev.getTimestamp();
        this.description = ev.getDescription();
        
        this.owner = ev.getOwner();
        this.discloseToMunicipality = ev.isDiscloseToMunicipality(); 
        this.discloseToPublic = ev.isDiscloseToPublic();
        this.active = ev.isActive();
        
        this.hidden = ev.isHidden();
        this.notes = ev.getNotes();
        this.personList = ev.getPersonList();
    }

    /**
     * @return the prop
     */
    public Property getProp() {
        return prop;
    }

    /**
     * @param prop the prop to set
     */
    public void setProp(Property prop) {
        this.prop = prop;
    }

    /**
     * @return the propUnit
     */
    public PropertyUnit getPropUnit() {
        return propUnit;
    }

    /**
     * @return the period
     */
    public OccPeriod getPeriod() {
        return period;
    }

    /**
     * @param propUnit the propUnit to set
     */
    public void setPropUnit(PropertyUnit propUnit) {
        this.propUnit = propUnit;
    }

    /**
     * @param period the period to set
     */
    public void setPeriod(OccPeriod period) {
        this.period = period;
    }
    
}
