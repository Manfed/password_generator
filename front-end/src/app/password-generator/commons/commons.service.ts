import { Injectable } from '@angular/core';
import { Mapping } from './mapping';

@Injectable()
export class CommonsService {

  constructor() {}

  public static readonly MEDIUM_PASSWORD_ENTROPY = 80;
  public static readonly STRONG_PASSWORD_ENTROPY = 120;

  public static readonly RW_COOKIE_NAME = 'rw_character_mappings';
  public static readonly RWFS_COOKIE_NAME = 'rwfs_character_groups';

  public static readonly DEFAULT_MAPPINGS = [
    new Mapping('a', '@', 50),
    new Mapping('s', '5T', 50),
    new Mapping('o', '0', 50),
    new Mapping('b', '8', 50)
  ];
}
