import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CouponsComponent } from './coupons/coupons.component';
import { CoursesComponent } from './courses/courses.component';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { QuestionsComponent } from './questions/questions.component';

const routes: Routes = [
  { path : '',redirectTo : 'Home', pathMatch : 'full'},
  { path : 'Home',component : HomeComponent},
  { path : 'Courses',component : CoursesComponent},
  { path : 'Coupons',component : CouponsComponent},
  { path : 'Questions',component : QuestionsComponent},
  { path : 'Login',component : LoginComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
