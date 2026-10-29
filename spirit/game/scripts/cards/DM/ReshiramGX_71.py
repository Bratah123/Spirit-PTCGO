from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.dm import (
    flame_charge,
    vermilion_gx,
)

card = PokemonCardDef(
    guid="7ffb673c-bb08-5b80-9ea1-75fc8d33f6f6",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ReshiramGX.Name",
    display_name="Reshiram-GX",
    searchable_by=["Reshiram-GX", "Basic", "GX", "ReshiramGX"],
    subtypes=["Basic", "GX"],
    collector_number=71,
    set_code="DM",
    rarity=Rarities.RareRainbow,
    hp=180,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=643,
    abilities=[
        Attack(
            title="Flame Charge",
            game_text="Search your deck for up to 2 Fire Energy cards and attach them to this Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=flame_charge,
        ),
        Attack(
            title="Scorching Column",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 1},
            damage=110,
            effect=condition_attack(SpecialConditions.BURNED),
        ),
        Attack(
            title="Vermilion-GX",
            game_text="You may attach up to 5 Fire Energy cards from your hand to your Pok\u00e9mon in any way you like. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=vermilion_gx,
        ),
    ],
)