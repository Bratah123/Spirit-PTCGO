from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import switch_self_attack
from spirit.game.card_effects.dm import (
    kingdra_hydro_pump,
    maelstrom_gx,
)

card = PokemonCardDef(
    guid="8acce9b4-cdc5-5333-a6e3-8f9e10410d48",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KingdraGX.Name",
    display_name="Kingdra-GX",
    searchable_by=["Kingdra-GX", "Stage 2", "GX", "KingdraGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=155,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=230,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name",
    family_id=116,
    abilities=[
        Attack(
            title="Hydro Pump",
            game_text="This attack does 50 more damage times the amount of Water Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=kingdra_hydro_pump,
        ),
        Attack(
            title="Reverse Thrust",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=switch_self_attack(),
        ),
        Attack(
            title="Maelstrom-GX",
            game_text="This attack does 40 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 1},
            effect=maelstrom_gx,
        ),
    ],
)