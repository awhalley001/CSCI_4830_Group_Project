import {Component, OnInit, TemplateRef, ViewChild} from '@angular/core';
import {ColumnMode, TableColumn} from "@swimlane/ngx-datatable";
import {YardControllerService} from "../services/yard-controller.service";
import {Track} from "../models/track";

@Component({
  selector: 'app-yard',
  templateUrl: './yard.component.html',
  styleUrls: ['./yard.component.scss']
})
export class YardComponent implements OnInit {
  @ViewChild('editTmpl', { static: true }) editTmpl: TemplateRef<any> | undefined;
  @ViewChild('hdrTpl', { static: true }) hdrTpl: TemplateRef<any> | undefined;

  cMode: any = ColumnMode;

  tracks: Object = [];
  columns: TableColumn[] = [];
  //
  // columnArray: TableColumn[] = [
  //   {name: 'id'},
  //   {name: 'SBDV_NAME'},
  //   {name: 'TRK_SYS_NBR'},
  //   {name: 'dist'},
  //   {name: 'car_capacity'}
  // ];
  constructor(private readonly yardControllerService: YardControllerService) {

  }

  async ngOnInit() {
    this.yardControllerService.get().subscribe({
      next: value => {
        console.log('value')
        console.log(value);

        this.tracks = value;
      }, error: err => {
        console.error(err);
      }});
    this.columns = [
      {
        cellTemplate: this.editTmpl,
        headerTemplate: this.hdrTpl,
        name: 'id'
      },
      {
        cellTemplate: this.editTmpl,
        headerTemplate: this.hdrTpl,
        name: 'SBDV_NAME',
        prop: 'SBDV_NAME'
      },
      {
        cellTemplate: this.editTmpl,
        headerTemplate: this.hdrTpl,
        name: 'TRK_SYS_NBR',
        prop: 'TRK_SYS_NBR'
      },
      {
        cellTemplate: this.editTmpl,
        headerTemplate: this.hdrTpl,
        name: 'dist'
      },
      {
        cellTemplate: this.editTmpl,
        headerTemplate: this.hdrTpl,
        name: 'car_capacity',
        prop: 'car_capacity'
      },
      {
        cellTemplate: this.editTmpl,
        headerTemplate: this.hdrTpl,
        name: 'actions',
        prop: 'actions'
      }
    ];
  }
}
