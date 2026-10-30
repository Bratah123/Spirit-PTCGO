"""Arceus LV.X (DPP #DP56)."""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dpp_arceuslvx_dp56_meteor_blast,
    arceus_multitype_passive,
)

card = PokemonCardDef(
    guid='022dbcc8-d2db-5a93-a119-84bdf73d9dbb',
    key='DPP',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.ArceusLVX.Name',
    display_name='Arceus LV.X',
    searchable_by=['Arceus LV.X', 'Level-Up', 'ArceusLVX'],
    subtypes=['Level-Up'],
    collector_number=56,
    set_code='DPP',
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.LEVELUP,
    retreat_cost=1,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Arceus.Name',
    family_id=493,
    abilities=[
        Ability(
            title='Multitype',
            game_text="Arceus LV.X's type is the same as its previous Level.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=arceus_multitype_passive(),
        ),
        Attack(
            title='Meteor Blast',
            game_text="Flip a coin. If tails, this attack's base damage is 50 instead of 100.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=dpp_arceuslvx_dp56_meteor_blast(),
        ),
    ],
)
