"""Arceus LV.X (DPP #DP53)."""
from spirit.game.data_utils import PokemonCardDef, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    arceus_multitype_passive,
    arceus_omniscient_passive,
)

card = PokemonCardDef(
    guid='e9fbf3bc-3447-5abf-b961-431bdd4569f9',
    key='DPP',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.ArceusLVX.Name',
    display_name='Arceus LV.X',
    searchable_by=['Arceus LV.X', 'Level-Up', 'ArceusLVX'],
    subtypes=['Level-Up'],
    collector_number=53,
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
            game_text="Arceus LV. X's type is the same type as its previous Level.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=arceus_multitype_passive(),
        ),
        Ability(
            title='Omniscient',
            game_text='Arceus can use the attacks of all Arceus you have in play as its own. (You still need the necessary Energy to use each attack.)',
            ability_type=AbilityTypes.POKE_BODY,
            passive=arceus_omniscient_passive(),
        ),
    ],
)
