import { Component } from '@angular/core';
import { PasswordOptions } from './models/password-options.model';
import { PasswordGeneratorService } from './services/password-generator.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'app';
  model: PasswordOptions = {
    password_length: 12,
    uppers: 2,
    lowers: 2,
    digits: 4,
    symbols: 2
  };
  password: string;
  errors: any;

  public constructor(
    private passwordGeneratorService: PasswordGeneratorService
  ) { }

  public onSubmit() {
    this.passwordGeneratorService.generate(this.model)
      .subscribe(
        data => this.password = data,
        err => {
          console.log(err);
          this.password = null;
          this.errors = Object.entries(err);
        }
      );
  }
}
