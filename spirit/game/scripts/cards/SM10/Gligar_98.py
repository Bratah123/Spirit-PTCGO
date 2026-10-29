from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm10 import (
    free_flight_passive,
    shinobi_strike,
)

card = PokemonCardDef(
    guid="41dd81cd-a20b-5daf-aabc-87d1a0075647",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gligar.Name",
    display_name="Gligar",
    searchable_by=["Gligar", "Basic", "Gligar"],
    subtypes=["Basic"],
    collector_number=98,
    set_code="SM10",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=207,
    abilities=[
        Ability(
            title="Free Flight",
            game_text="If this Pok\u00e9mon has no Energy attached to it, it has no Retreat Cost.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=free_flight_passive
        ),
        Attack(
            title="Shinobi Strike",
            game_text="If you played Janine from your hand during this turn, this attack does 90 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            effect=shinobi_strike
        ),
    ],
)