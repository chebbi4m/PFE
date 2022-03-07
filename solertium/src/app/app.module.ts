import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule} from '@angular/material/button';
import {MatCardModule} from '@angular/material/card';

import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NavbarComponent } from './navbar-main/navbar.component';
import { CoursesComponent } from './courses/courses.component';
import { HomeComponent } from './home/home.component';
import { HomeTopComponent } from './home-top/home-top.component';
import { DiamondHrComponent } from './diamond-hr/diamond-hr.component';
import { HomeAboutComponent } from './home-about/home-about.component';
import { CouponsComponent } from './coupons/coupons.component';
import { QuestionsComponent } from './questions/questions.component';
import { LoginComponent } from './login/login.component';
import { CoursesSearchComponent } from './courses-search/courses-search.component';
import {MatFormFieldModule} from '@angular/material/form-field';
import { CoursesMainComponent } from './courses-main/courses-main.component';
import { FooterComponent } from './footer/footer.component';



@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    CoursesComponent,
    HomeComponent,
    HomeTopComponent,
    DiamondHrComponent,
    HomeAboutComponent,
    CouponsComponent,
    QuestionsComponent,
    LoginComponent,
    CoursesSearchComponent,
    CoursesMainComponent,
    FooterComponent,
    


  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatToolbarModule,
    MatButtonModule,
    MatFormFieldModule,
    MatCardModule
  ],
  
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
