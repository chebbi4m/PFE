import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CoursesComponent } from './courses/courses.component';
import { HomeComponent } from './home/home.component';

const routes: Routes = [
  { path : 'Home',component : HomeComponent},
  { path : 'Courses',component : CoursesComponent},
  { path : 'Coupons',component : CoursesComponent},
  { path : 'Questions',component : CoursesComponent},
  { path : 'Login',component : CoursesComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
