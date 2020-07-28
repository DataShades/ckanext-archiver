def cmd_init():
    import ckan.model as model
    from ckanext.archiver.model import init_tables
    init_tables(model.meta.engine)
