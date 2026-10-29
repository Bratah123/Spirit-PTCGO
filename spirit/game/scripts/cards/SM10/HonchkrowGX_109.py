from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm10 import (
    feather_storm,
    ruler_of_the_night_passive,
    unfair_gx,
)

card = PokemonCardDef(
    guid="374cf16f-d16f-5072-bd06-be30aaa30c4e",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HonchkrowGX.Name",
    display_name="Honchkrow-GX",
    searchable_by=["Honchkrow-GX", "Stage 1", "GX", "HonchkrowGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=109,
    set_code="SM10",
    rarity=Rarities.RareHoloGX,
    hp=210,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Murkrow.Name",
    family_id=198,
    abilities=[
        Ability(
            title="Ruler of the Night",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, your opponent can't play any Pok\u00e9mon Tool, Special Energy, or Stadium cards from their hand.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=ruler_of_the_night_passive
        ),
        Attack(
            title="Feather Storm",
            game_text="This attack does 30 damage to 2 of your opponent's Benched Pok\u00e9mon-GX and Pok\u00e9mon-EX. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=feather_storm
        ),
        Attack(
            title="Unfair-GX",
            game_text="Your opponent reveals their hand. Discard 2 cards from it. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unfair_gx
        ),
    ],
)