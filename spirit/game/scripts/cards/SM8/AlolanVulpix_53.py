from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm8 import (
    secret_alleyway_passive,
)

card = PokemonCardDef(
    guid="fd3ec7ae-2b73-5eaf-bdae-aec7330a082e",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanVulpix.Name",
    display_name="Alolan Vulpix",
    searchable_by=["Alolan Vulpix", "Basic", "AlolanVulpix"],
    subtypes=["Basic"],
    collector_number=53,
    set_code="SM8",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=37,
    abilities=[
        Ability(
            title="Secret Alleyway",
            game_text="If you have any Fairy Pok\u00e9mon in play, this Pok\u00e9mon has no Retreat Cost.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=secret_alleyway_passive
        ),
        Attack(
            title="Gnaw",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)