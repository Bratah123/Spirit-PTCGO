from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.sm10 import (
    flare_starter,
    high_heat_blast,
)

card = PokemonCardDef(
    guid="ecd53342-890c-5fca-9d11-a0ec65c47e3e",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Volcanion.Name",
    display_name="Volcanion",
    searchable_by=["Volcanion", "Basic", "Volcanion"],
    subtypes=["Basic"],
    collector_number=179,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=721,
    abilities=[
        Attack(
            title="Flare Starter",
            game_text="Search your deck for a Fire Energy card and attach it to 1 of your Pok\u00e9mon. If you go second and it's your first turn, instead search for up to 3 Fire Energy cards and attach them to your Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.FIRE: 1},
            effect=flare_starter
        ),
        Attack(
            title="High-Heat Blast",
            game_text="If you have at least 4 Fire Energy in play, this attack does 60 more damage.",
            cost={PokemonTypes.FIRE: 2},
            damage=50,
            damage_operator="+",
            effect=high_heat_blast
        ),
    ],
)