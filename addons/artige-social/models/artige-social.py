# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SocialConnector(models.Model):
    _name = 'artige-social.social-connector'
    name = fields.Char()
    type = fiels.Choices('r', 'w', 'rw')


class SocialAuthor(models.Model):
    _name = 'artige-social.social-author'

    name = fields.Char()
    pic = fields.Many2One(SocialMedia)


class SocialMedia(models.Model):
    _name = 'artige-social.social-media'

    _connector = fields.Many2One(SocialConnector)
    name = fields.Char()
    stream = fields.File()
    kind = fields.Choices(['img', 'mov', 'gif', 'aud'])
    owner = fields.Many2One(SocialAuthor)


class SocialPost(models.Model):
    _name = 'artige-social.social-topic'

    _connector = fields.Many2One(SocialConnector)
    name = fields.Char()
    text = fields.Text()
    media = Many2Many(SocialMedia)
    timestamp = fields.timestamp()
    update_date = fields.DateTime()
    create_date = fields.DateTime()
    publish_date = fields.DateTime()
    owner = fields.Many2One(SocialAuthor)


class SocialComment(models.Model):
    _name = 'artige-social.social-comment'

    _connector = fields.Many2One(SocialConnector)
    owner = fields.Many2One(SocialAuthor)
    text = fields.Text()
    post = fields.One2Many(SocialPost)
    pre_comment = fields.One2Many(SocialComment)


class SocialInteraction(models.Model):
    _name = 'artige-social.social-comment'

    _connector = fields.Many2One(SocialConnector)
    owner = fields.Many2One(SocialAuthor)
    kind = fields.Choices(['like'])
