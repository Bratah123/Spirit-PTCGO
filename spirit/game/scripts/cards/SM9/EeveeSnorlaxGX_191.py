from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.sm9 import (
    cheer_up,
    dump_truck_press,
    megaton_friends_gx,
)

card = PokemonCardDef(
    guid="d7655e93-5b9d-5224-bb17-7b642eb23835",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EeveeSnorlaxGX.Name",
    display_name="Eevee & Snorlax-GX",
    searchable_by=["Eevee & Snorlax-GX", "Basic", "TAG TEAM", "GX", "EeveeSnorlaxGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=191,
    set_code="SM9",
    rarity=Rarities.RareRainbow,
    hp=270,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=133,
    abilities=[
        Attack(
            title="Cheer Up",
            game_text="Attach an Energy card from your hand to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=cheer_up,
        ),
        Attack(
            title="Dump Truck Press",
            game_text="If your opponent's Active Pok\u00e9mon is an Evolution Pok\u00e9mon, this attack does 120 more damage.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=120,
            damage_operator="+",
            effect=dump_truck_press,
        ),
        Attack(
            title="Megaton Friends-GX",
            game_text="If this Pok\u00e9mon has at least 1 extra Energy attached to it (in addition to this attack's cost), draw cards until you have 10 cards in your hand. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 4},
            damage=210,
            effect=megaton_friends_gx,
        ),
    ],
)