import {Component, ElementRef, Input, OnInit, ViewChild} from '@angular/core';
import { Observable } from 'rxjs';
import { HttpHeaders } from '@angular/common/http';
import { HttpRequest } from '@angular/common/http';
import { UploadService } from '../upload.service';

@Component({
  selector: 'app-upload-csv',
  templateUrl: './upload-csv.component.html',
  styleUrls: ['./upload-csv.component.scss']
})
export class UploadCsvComponent {
  file!: File;
  @ViewChild('fileInput', {static: false}) fileInput: ElementRef | undefined;

 constructor(
   private uploadService: UploadService
 ) { }

 onFilechange(event: any) {
   console.log(event.target.files[0])
   this.file = event.target.files[0]
 }

 upload() {
   if (this.file) {
     this.uploadService.uploadFile(this.file).subscribe((resp: any) => {
       console.log('done');
       if(this.fileInput)
         this.fileInput.nativeElement.value = '';
       alert("Uploaded");
     })
   } else {
     alert("Please select a file first")
   }
 }
}
