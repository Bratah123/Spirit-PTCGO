from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm9 import (
    dueling_saber,
    iron_rule_gx,
    metal_symbol_cure,
    metal_symbol_passive,
)

card = PokemonCardDef(
    guid="b88f6f49-9fb8-58c8-bd16-6691656072e9",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CobalionGX.Name",
    display_name="Cobalion-GX",
    searchable_by=["Cobalion-GX", "Basic", "GX", "CobalionGX"],
    subtypes=["Basic", "GX"],
    collector_number=168,
    set_code="SM9",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=638,
    abilities=[
        Ability(
            title="Metal Symbol",
            game_text="Each of your Pok\u00e9mon that has any Metal Energy attached to it can't be affected by any Special Conditions. Remove any Special Conditions affecting those Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=metal_symbol_cure,
            passive=metal_symbol_passive,
            trigger=Triggers.BETWEEN_TURNS,
        ),
        Attack(
            title="Dueling Saber",
            game_text="If there is any Stadium card in play, this attack does 60 more damage.",
            cost={PokemonTypes.METAL: 2},
            damage=50,
            damage_operator="+",
            effect=dueling_saber,
        ),
        Attack(
            title="Iron Rule-GX",
            game_text="During your opponent's next turn, their Pok\u00e9mon can't attack. (This includes Pok\u00e9mon that come into play on that turn.) (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=iron_rule_gx,
        ),
    ],
)